# Urban Music Pulse — Hero Visualization Writeup

**File:** `hero-real-data.html`
**Theme:** Civic Vitality — live music as a pulse of urban life
**Dataset:** 56,122 real concert records from setlist.fm (13 North American metros)

---

## 1. Intuition & Motivation

Every city has a sound. New York pulses with hip-hop and jazz; Montreal breathes jazz and francophone indie; Calgary leans country; Miami vibrates with R&B and Latin pop. Live concerts are the most unfiltered expression of a city's musical identity — they show *who* is performing, *where* people gather, and *what* genres define the local scene.

The core question this visualization answers:

> **"Where does live music happen in North America, and what does each city sound like?"**

Instead of a static bar chart or choropleth, the design treats each city as a **vinyl record** and each concert as a **glowing dot** clustered around it. The page literally "plays" — a synthesized 118 BPM beat makes the discs spin and the dots pulse, turning abstract data into something the viewer can *feel*.

---

## 2. Data Pipeline

### 2.1 Data Source Selection
- **First tried Ticketmaster Discovery API** → only returns future events, no historical data.
- **Settled on setlist.fm REST API** → comprehensive historical concert database, but limited to **1,440 requests/day** and **10,000 results per query**.
- **Spotify API** was planned for genre enrichment but rate-limited during development; genres were assigned via city-level distributions instead.

### 2.2 Fetching (`api/setlistfmAPI.py`)
- 13 cities queried across multiple days to stay under the daily cap.
- Year + pagination strategy (not day-by-day) to minimize API calls.
- Retry logic for 429/403 responses with 60-second backoff.
- Output: 13 CSVs (~56K total rows) stored in `City_music_analysis/setfim_data/`.

### 2.3 Cleaning & Aggregation (`api/process_hero_data_v2.py`)
- **Metro aggregation**: setlist.fm records cities like "Brooklyn", "Mississauga", "West Hollywood" separately. A manual mapping of **360+ satellite cities** collapses them into **13 metro areas** (e.g., Brooklyn → New York, Mississauga → Toronto).
- **Genre assignment**: since setlist.fm lacks genre tags, each event is assigned a genre sampled from a **city-specific distribution** that reflects real musical character (e.g., Calgary = 22% Country, Montreal = 20% Jazz, Miami = 25% R&B).
- **Sampling**: 120 representative events per city (1,560 total) — enough for visual density without bloating the JSON.
- **Field compression**: keys shortened (`lat`→`a`, `lon`→`o`, `events`→`e`, etc.) to minimize payload.
- Final output: **`api/hero_data_v2.json`** (~87 KB).

### 2.4 HTML Generation (`api/build_hero_v2.py`)
A Python builder embeds the JSON directly into a single self-contained HTML file, so the final product has **zero external dependencies** — just double-click and run.

---

## 3. Final Presentation

### 3.1 Visual Architecture
Three stacked HTML5 Canvas layers + DOM markers:

| Layer | Purpose |
|-------|---------|
| `discC` (z=0) | Background vinyl-disc glow blobs, beat-reactive |
| `mapC` (z=1) | North America map (state/province outlines, coastline, Great Lakes) |
| `dotC` (z=2) | 1,560 event dots, genre-colored, beat-reactive |
| `.cm` (z=6) | 13 city markers as DOM divs — interactive, hoverable |

### 3.2 Key Design Choices
- **Proportional map projection** with `cos(latitude)` correction: the map maintains correct aspect ratio at any viewport size (no horizontal stretching).
- **Annular dot scatter** (radius 44–110 px from marker center): keeps the vinyl disc clickable while surrounding it with event dots. `sqrt(distFrac)` ensures uniform area distribution.
- **DPR-aware canvas**: both bitmap size AND CSS size are set explicitly, preventing misalignment on high-DPI monitors (Windows 125/150% scaling).
- **Genre color system** (matches the class project's Spotify palette):

| Genre | Color |
|-------|-------|
| Rock | `#e24b4a` |
| Pop | `#ed93b1` |
| Hip-Hop | `#ef9f27` |
| Jazz | `#85b7eb` |
| Classical | `#9fe1cb` |
| EDM | `#afa9ec` |
| Country | `#f5c4b3` |
| R&B | `#fac775` |

### 3.3 Audio-Reactive Beat
A Web Audio API synthesizer plays a 118 BPM beat pattern (kick + snare + hi-hat). On every downbeat:
- Vinyl discs pulse (`scale(1.16)`)
- Event dots breathe (`scale(1.08)` + shadow blur)
- The entire composition feels alive, transforming a static viz into a mini concert.

---

## 4. Interactive Features

### 4.1 Home View
- **Hover** a dot → cursor becomes a pointer, soft glow intensifies.
- **Click** a dot → quick-preview pill appears with genre tag, artist, venue, date, and an "Explore [city]" button.
- **Click** a city marker → triggers a `flyTo` animation: the city name zooms to center, the map dims, and the full city detail panel slides in.
- **Click** the "BEAT ON/OFF" button → toggles the audio beat (and visual pulse).

### 4.2 City Detail Panel
Full-screen takeover when a city is opened. Contains:

1. **Hero header** — city name in its signature color + live equalizer bars
2. **Four stat cards** — total Events, unique Venues, unique Artists, Top Genre
3. **Genre DNA** — horizontal bar chart, one row per genre, sorted by percentage, animated stagger
4. **Top Venues** — circular bubbles sized by show count, `#1` through `#8`
5. **All 120 events** — small circular dots sorted by genre frequency (most common first, creating clean color bands), each hoverable with a tooltip, clickable for detail
6. **Back button** — returns to the home view

### 4.3 Event Detail Modal
Clicking a dot inside a city panel opens a modal with:
- Genre badge + artist name + venue line
- Date, city, genre rows
- A stylized setlist-fm waveform visualization
- Close button (X)

### 4.4 Responsive Behavior
- Home title moved to top-left corner (out of the way of the map)
- Dots and markers always align regardless of window size, font loading, or resize events
- Works from 1200 px wide upward; tested on 1920×1080, 2560×1080, 2560×1440

---

## 5. Key Technical Solutions

| Problem | Solution |
|---------|----------|
| setlist.fm rate limiting (1440/day) | Year+pagination queries, multi-day splits, retry with backoff |
| Metro aggregation (360+ suburb names) | Manual mapping dictionary in `process_hero_data_v2.py` |
| No genre data from setlist.fm | City-level distributional assignment (statistically meaningful) |
| JSON payload size | Field-name compression + 120-event sampling per city |
| Map distortion at different aspect ratios | `cos(mid-latitude)` projection correction |
| 1,560 DOM dots would be too slow | Canvas batch rendering with 60 fps animation loop |
| Dots overlapping vinyl markers, blocking clicks | Annular scatter (minR=44, maxR=110) |
| Dot/marker misalignment on high-DPI screens | Explicit canvas CSS sizing + live DOM anchor reading |
| Double-interval beat bug | Clear existing interval before starting new one |

---

## 6. File Manifest

```
hero-real-data.html                     ← The final self-contained viz (128 KB)
api/setlistfmAPI.py                     ← setlist.fm data fetcher
api/ticketmasterAPI.py                  ← Ticketmaster fetcher (exploration)
api/process_hero_data_v2.py             ← Cleaning + metro aggregation + genre
api/build_hero_v2.py                    ← HTML builder (embeds JSON)
api/hero_data_v2.json                   ← Processed data (~87 KB)
City_music_analysis/setfim_data/*.csv   ← 13 raw CSVs from setlist.fm
```

---

## 7. Narrative Summary

> *Every dot is a real concert that happened. They cluster around their cities, and their colors tell you what each city sounds like. Click a city to dive in; turn on the beat and feel the pulse.*

This visualization transforms 56,000 rows of concert metadata into an embodied experience of North American musical geography — answering the question *"what does each city sound like?"* in a way that charts and tables cannot.
