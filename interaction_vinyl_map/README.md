# Urban Music Pulse — Interactive Hero Visualization

An interactive data visualization of **56,000+ live music concerts across 13 North American metro areas**, built from real [setlist.fm](https://www.setlist.fm) data. Each city is a vinyl record, each concert a glowing dot colored by genre, pulsing to a synthesized 118 BPM beat.

> *"Drop the Needle, Hear the City."*

---

## Quick Start

**Just double-click `hero-real-data.html`** — it opens in any modern browser with zero setup. The file is self-contained (all data, styles, and code embedded).

- Click any dot → preview a concert
- Click any city marker → dive into that city's detailed panel (genre DNA, top venues, all events)
- Click **BEAT ON/OFF** → toggle the audio-reactive beat

---

## Folder Structure

```
interaction_graph/
├── README.md                   ← you are here
├── WRITEUP.md                  ← full design intuition + technical writeup
├── hero-real-data.html         ← ★ the final self-contained visualization
│
├── scripts/                    ← the 3-step data pipeline
│   ├── setlistfmAPI.py         ← Step 1: fetch raw concert data from setlist.fm
│   ├── process_hero_data_v2.py ← Step 2: clean, aggregate into metros, assign genres
│   └── build_hero_v2.py        ← Step 3: embed JSON into self-contained HTML
│
├── data/
│   └── hero_data_v2.json       ← processed JSON (~87 KB, also embedded in HTML)
│
└── raw_data/                   ← the 13 raw CSVs from setlist.fm
    ├── setlistfm_toronto_2025.csv
    ├── setlistfm_montreal_2025.csv
    ├── setlistfm_vancouver_2025.csv
    ├── setlistfm_calgary_2025.csv
    ├── setlistfm_ottawa_2025.csv
    ├── setlistfm_newyork_2025.csv
    ├── setlistfm_losangeles_2025.csv
    ├── setlistfm_chicago_2025.csv
    ├── setlistfm_detroit_2025.csv
    ├── setlistfm_lasvegas_2025.csv
    ├── setlistfm_miami_2025.csv
    ├── setlistfm_sanfrancisco_2025.csv
    └── setlistfm_washington_2025.csv
```

---

## Data Pipeline

```
raw setlist.fm API
      │
      │  scripts/setlistfmAPI.py
      ▼
raw_data/setlistfm_*.csv      (13 files, ~56,000 total rows)
      │
      │  scripts/process_hero_data_v2.py
      │   - aggregate 360+ satellite cities into 13 metros
      │   - assign genre per city-level distribution
      │   - compress field names, sample 120 events/city
      ▼
data/hero_data_v2.json        (~87 KB)
      │
      │  scripts/build_hero_v2.py
      │   - embed JSON into HTML template
      │   - embed canvas rendering code + audio synthesis
      ▼
hero-real-data.html           (~128 KB, self-contained)
```

---

## Reproducing the Pipeline

The scripts were written to run from the original project root (`C:/uoft/sta313/project/`). They reference paths like `api/hero_data_v2.json` and `City_music_analysis/setfim_data/`. To re-run them:

1. Place `setlistfmAPI.py` in an `api/` folder, `raw_data/*.csv` in `City_music_analysis/setfim_data/`, etc.
2. Run in sequence:
   ```bash
   python api/setlistfmAPI.py        # Step 1 (takes ~2 days due to rate limits)
   python api/process_hero_data_v2.py # Step 2 (<1 min)
   python api/build_hero_v2.py        # Step 3 (<1 sec)
   ```

**You don't need to re-run anything to view the viz** — just open `hero-real-data.html`.

---

## Key Stats

| Metric | Value |
|--------|-------|
| Raw concerts | 56,122 |
| Metro areas | 13 |
| Satellite cities aggregated | 360+ |
| Event dots rendered | 1,560 (120 sampled per city) |
| Genres | 8 (Rock, Pop, Hip-Hop, Jazz, Classical, EDM, Country, R&B) |
| Data source | setlist.fm REST API |
| Final HTML size | ~128 KB (embeds 87 KB JSON) |
| External dependencies | None — pure HTML + Canvas + Web Audio |

---

## See Also

- **`WRITEUP.md`** — full design intuition, pipeline details, technical solutions, interactive feature list
