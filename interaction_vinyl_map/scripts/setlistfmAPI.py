# setlistfmAPI.py
# Usage (PowerShell):
#   $env:SETLISTFM_API_KEY="YOUR_API_KEY"
#   python api/setlistfmAPI.py --city Toronto --country CA --year 2025 --out api/setlistfm_toronto_2025.csv
#
# Get your API key at: https://www.setlist.fm/settings/api

import os
import time
import argparse
import calendar
from typing import List, Dict, Any

import requests
import pandas as pd

BASE_URL = "https://api.setlist.fm/rest/1.0"


def get_api_key() -> str:
    api_key = os.getenv("SETLISTFM_API_KEY", "").strip()
    if not api_key:
        raise RuntimeError(
            "SETLISTFM_API_KEY is not set.\n"
            "PowerShell:  $env:SETLISTFM_API_KEY=\"YOUR_API_KEY\"\n"
            "Get your key at: https://www.setlist.fm/settings/api"
        )
    return api_key


def request_with_retries(url: str, headers: Dict, params: Dict, max_retries: int = 5) -> requests.Response:
    backoff = 1.0
    for attempt in range(max_retries):
        r = requests.get(url, headers=headers, params=params, timeout=30)

        if r.status_code in (403, 429):
            wait = backoff * (2 ** attempt)
            print(f"[WARN] Rate limited ({r.status_code}), waiting {wait:.1f}s...")
            time.sleep(min(wait, 30))
            continue

        if r.status_code in (500, 502, 503, 504):
            time.sleep(backoff * (2 ** attempt))
            continue

        return r

    return r


def flatten_setlist(s: Dict[str, Any]) -> Dict[str, Any]:
    artist = s.get("artist") or {}
    venue = s.get("venue") or {}
    city = venue.get("city") or {}
    country = (city.get("country") or {})
    coords = city.get("coords") or {}

    # Count total songs in setlist
    sets = s.get("sets") or {}
    set_list = sets.get("set") or []
    song_count = sum(len(st.get("song") or []) for st in set_list)

    # Extract song names
    songs = []
    for st in set_list:
        for song in (st.get("song") or []):
            songs.append(song.get("name", ""))

    return {
        "event_id": s.get("id"),
        "event_date": s.get("eventDate"),  # dd-MM-yyyy
        "artist_name": artist.get("name"),
        "artist_mbid": artist.get("mbid"),
        "artist_sort_name": artist.get("sortName"),
        "tour_name": (s.get("tour") or {}).get("name"),
        "venue_name": venue.get("name"),
        "venue_id": venue.get("id"),
        "city_name": city.get("name"),
        "state": city.get("state"),
        "state_code": city.get("stateCode"),
        "country_name": country.get("name"),
        "country_code": country.get("code"),
        "lat": coords.get("lat"),
        "lng": coords.get("long"),
        "song_count": song_count,
        "songs": "; ".join(songs) if songs else None,
        "setlist_url": s.get("url"),
    }


def fetch_city_year(
    city: str,
    country_code: str,
    year: int,
    state_code: str = None,
    sleep_s: float = 1.5,
) -> pd.DataFrame:
    """Fetch all setlists for a city + year by paginating through year query.
    Uses year-level query with pagination. Each page = 1 request.
    ~930 events/month => ~11000/year => 500 pages max (20/page).
    For cities near 10000 limit, we accept the cap to save daily quota.
    13 cities × ~500 pages = ~6500 requests, but most cities are small.

    With 1440/day limit, we paginate conservatively.
    """
    api_key = get_api_key()

    headers = {
        "x-api-key": api_key,
        "Accept": "application/json",
    }

    params_base = {
        "cityName": city,
        "countryCode": country_code,
        "year": year,
    }
    if state_code:
        params_base["stateCode"] = state_code

    all_rows: List[Dict[str, Any]] = []
    page = 1
    total_pages = None

    while True:
        params = dict(params_base)
        params["p"] = page

        r = request_with_retries(f"{BASE_URL}/search/setlists", headers=headers, params=params)

        if r.status_code in (429, 403):
            print(f"[WARN] Rate limited on page {page}, waiting 60s...")
            time.sleep(60)
            r = requests.get(f"{BASE_URL}/search/setlists", headers=headers, params=params, timeout=30)

        if r.status_code != 200:
            print(f"[ERROR] HTTP {r.status_code} on page {page}, skipping...")
            time.sleep(sleep_s)
            page += 1
            if total_pages and page > total_pages:
                break
            continue

        data = r.json()

        total = int(data.get("total", 0))
        items_per_page = int(data.get("itemsPerPage", 20))
        if total_pages is None:
            total_pages = min((total + items_per_page - 1) // items_per_page, 500)
            print(f"[INFO] {city}, {country_code}, {year}: {total} setlists, fetching {total_pages} pages (~{total_pages} requests)")

        setlists = data.get("setlist") or []
        if not setlists:
            break

        for s in setlists:
            all_rows.append(flatten_setlist(s))

        if page % 50 == 0:
            print(f"[INFO]   page {page}/{total_pages}, {len(all_rows)} rows so far...")

        if page >= total_pages:
            break

        page += 1
        time.sleep(sleep_s)

    df = pd.DataFrame(all_rows)

    # Convert date from dd-MM-yyyy to yyyy-MM-dd
    if "event_date" in df.columns and not df.empty:
        df["event_date"] = pd.to_datetime(df["event_date"], format="%d-%m-%Y", errors="coerce").dt.strftime("%Y-%m-%d")

    # de-duplicate
    if "event_id" in df.columns and not df.empty:
        df = df.drop_duplicates(subset=["event_id"])

    return df


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--city", required=True)
    ap.add_argument("--country", default="CA")
    ap.add_argument("--state", default=None, help="State/province code, e.g. ON, NY, CA")
    ap.add_argument("--year", type=int, required=True)
    ap.add_argument("--out", default="setlistfm_events.csv")
    args = ap.parse_args()

    df = fetch_city_year(
        city=args.city,
        country_code=args.country,
        year=args.year,
        state_code=args.state,
    )

    df.to_csv(args.out, index=False, encoding="utf-8")
    print(f"[DONE] Saved {len(df)} rows to {args.out}")


if __name__ == "__main__":
    main()
