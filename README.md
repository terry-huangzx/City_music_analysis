# City Music Pulse

**Where does live music happen in North America — and what does each city actually sound like?**

An interactive data visualization that transforms 56,000+ concert records and Spotify streaming data into a scrollytelling narrative, comparing the live music ecosystems of 13 North American cities.

Built for STA313 Data Visualization, University of Toronto, 2025.

<br>

## Quick Start

Everything runs in the browser. No installs, no server — just open the HTML file.

| | File | What it is |
|---|---|---|
| **Start here** | [`output/city_music_pulse.html`](output/city_music_pulse.html) | Full scrollytelling experience — interactive vinyl map hero, four analytical chapters, guided narrative |
| Standalone | [`output/hero_vinyl_map.html`](output/hero_vinyl_map.html) | The vinyl-record map as a self-contained exploratory tool |

> Both are single-file, self-contained HTML. All data, styles, and scripts are embedded — no external dependencies.

<br>

## What You'll See

### The Hero — Interactive Vinyl Map

A dark-themed map of North America with 13 spinning vinyl-disc city markers. Each of the 56,000+ concert events appears as a color-coded dot orbiting its city, pulsing to a synthesized 118 BPM beat.

- **Click a city disc** — opens a detail panel with event count, genre distribution chart, top venues, and a scrollable concert list
- **Click any dot** — pops a card showing that specific concert's artist, venue, date, and genre
- **Toggle the beat** — turns the audio-reactive animation on/off
- Dots are sorted by genre frequency and scattered in an annular ring using `sqrt` distribution for uniform density

### Four Analytical Layers

Each chapter is a standalone interactive visualization, woven into the scroll narrative with story cards:

| Layer | Question | Visualization |
|---|---|---|
| **1 — Seasonal Volume** | When do cities come alive? | Heatmap grid (city x month), toggleable raw / per-capita, click to rank |
| **2 — Genre Diversity** | What does each city sound like? | Scatter plot (events vs. diversity index) + click-to-expand genre treemap |
| **3 — Venue Distribution** | Mega-venues or grassroots scenes? | Dual-city ranked bar chart with cumulative concentration curve |
| **4 — Demand Mismatch** | Where does listener demand outpace live supply? | Radial calendar (7 weekdays x 6 weeks), color-coded by gap severity |

<br>

## Repository Structure

```
.
├── output/                              # Final deliverables
│   ├── city_music_pulse.html            #   Scrollytelling narrative (hero + 4 layers)
│   └── hero_vinyl_map.html              #   Standalone interactive vinyl map
│
├── layers/                              # Analytical prototypes (one per chapter)
│   ├── layer1_seasonal_volume.html
│   ├── layer2_genre_diversity.html
│   ├── layer3_venue_distribution.html
│   └── layer4_demand_mismatch.html
│
├── scripts/                             # Data pipeline
│   ├── setlistfm_api.py                 #   API scraper for setlist.fm
│   ├── process_hero_data.py             #   Cleaning, geocoding, aggregation
│   └── build_hero.py                    #   Generates self-contained HTML output
│
├── data/                                # Source datasets
│   ├── setlistfm/                       #   13 city-level concert CSVs (56,000+ events)
│   └── spotify/                         #   Spotify weekly chart CSVs (13 cities)
│
└── docs/                                # Project documentation
    ├── writeup.md                       #   Design rationale and technical notes
    └── demo_script.md                   #   Video presentation storyboard
```

<br>

## Data Pipeline

```
setlist.fm API                          Spotify Weekly Charts
      │                                        │
      ▼                                        │
setlistfm_api.py                               │
      │                                        │
      ▼                                        │
  13 city CSVs ────────────┐                   │
   (56,000+ events)        │                   │
                           ▼                   ▼
                   process_hero_data.py ◄───────┘
                           │
                           ▼
                     hero_data.json
                           │
                           ▼
                     build_hero.py
                           │
                           ▼
                  hero_vinyl_map.html  ──►  embedded in city_music_pulse.html
```

<br>

## Technical Highlights

- **Zero dependencies** — no React, no D3, no build tools. Pure HTML/CSS/JS, each output is a single file
- **Layered HTML5 Canvas** — three stacked canvases (disc layer, map layer, dot layer) for smooth 60fps rendering of 56,000+ animated dots
- **DPR-aware rendering** — canvas backing store scaled by `devicePixelRatio` with explicit CSS sizing to prevent coordinate mismatch across different displays
- **Web Audio API** — procedural 118 BPM beat (kick, snare, hi-hat) that drives dot animation through amplitude coupling
- **Annular scatter** — `sqrt(random)` radial distribution ensures uniform dot density across the ring area, not clustered near the center
- **DOM-anchored positioning** — dot positions computed from live `getBoundingClientRect()` of marker elements, so canvas dots track DOM layout perfectly on resize
- **Proportional map projection** — longitude/latitude to pixel with `cos(lat)` correction for consistent city spacing

<br>

## Data Sources

| Source | What | Coverage |
|---|---|---|
| [setlist.fm](https://www.setlist.fm/) | Concert events — artist, venue, date, setlist | 13 cities, 56,000+ events, 2025 |
| [Spotify](https://www.spotify.com/) | Weekly streaming charts — top tracks, demand scores, genres | 13 cities, weekly, 2025 |

**Cities**: Calgary, Chicago, Detroit, Las Vegas, Los Angeles, Miami, Montreal, New York, Ottawa, San Francisco, Toronto, Vancouver, Washington DC

