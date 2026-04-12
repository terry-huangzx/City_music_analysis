# Urban Music Pulse: Interactive Vinyl Map

`interaction_vinyl_map` contains the standalone interactive visualization for the City Music Analysis project. It transforms real concert activity into a music-themed map experience where each metro is rendered as a vinyl record and each concert appears as a glowing genre-colored dot.

The piece is built from more than 56,000 real concert records collected from `setlist.fm` and summarized into 13 North American metro areas.

> Drop the needle, hear the city.

## What This Folder Contains

[`hero-real-data.html`](/Users/fanyanting/City_music_analysis/interaction_vinyl_map/hero-real-data.html) is the main deliverable. It is a self-contained interactive HTML file with embedded data, styles, rendering logic, and audio behavior.

Supporting files:

- [`scripts/setlistfmAPI.py`](/Users/fanyanting/City_music_analysis/interaction_vinyl_map/scripts/setlistfmAPI.py): fetches raw concert data from `setlist.fm`
- [`scripts/process_hero_data_v2.py`](/Users/fanyanting/City_music_analysis/interaction_vinyl_map/scripts/process_hero_data_v2.py): cleans data, aggregates suburbs into metros, assigns genres, and prepares the compact JSON
- [`scripts/build_hero_v2.py`](/Users/fanyanting/City_music_analysis/interaction_vinyl_map/scripts/build_hero_v2.py): embeds the processed JSON into the final HTML
- [`data/hero_data_v2.json`](/Users/fanyanting/City_music_analysis/interaction_vinyl_map/data/hero_data_v2.json): processed data used by the visualization
- [`WRITEUP.md`](/Users/fanyanting/City_music_analysis/interaction_vinyl_map/WRITEUP.md): deeper design and technical writeup

## Quick Start

Open [`hero-real-data.html`](/Users/fanyanting/City_music_analysis/interaction_vinyl_map/hero-real-data.html) in a modern browser.

No local server or install step is required for basic viewing.

Once it opens, you can:

- click a concert dot to preview an event
- click a city marker to open its detail panel
- toggle the beat on or off for the audio-reactive experience

## Folder Structure

```text
interaction_vinyl_map/
├── README.md
├── WRITEUP.md
├── hero-real-data.html
├── data/
│   └── hero_data_v2.json
└── scripts/
    ├── build_hero_v2.py
    ├── process_hero_data_v2.py
    └── setlistfmAPI.py
```

Related raw source CSV files live in [`../spotify_and_ticketmaster_data/setfim_data/`](/Users/fanyanting/City_music_analysis/spotify_and_ticketmaster_data/setfim_data).

## Data Pipeline

The interactive was assembled in three broad steps:

1. Fetch raw concert records from `setlist.fm`
2. Clean and aggregate events into 13 metro areas, then assign representative genre labels
3. Embed the processed data into a single self-contained HTML file

Conceptually, the flow looks like this:

```text
setlist.fm API
    ->
raw CSV files
    ->
processed metro-level JSON
    ->
self-contained interactive HTML
```

## Key Stats

| Metric | Value |
| --- | --- |
| Raw concerts | 56,122 |
| Metro areas | 13 |
| Satellite cities aggregated | 360+ |
| Event dots rendered | 1,560 |
| Genres represented | 8 |
| Final output | Single self-contained HTML file |

## Reproducing the Pipeline

The current repo is optimized for viewing the final artifact, not for one-command reproducibility. The included scripts reflect an earlier local project layout, so you will likely need to update hard-coded paths before rerunning them.

If you want to regenerate the final output, the intended sequence is:

```bash
python scripts/setlistfmAPI.py
python scripts/process_hero_data_v2.py
python scripts/build_hero_v2.py
```

In practice, you may need to:

- point the scripts at the CSV files in `../spotify_and_ticketmaster_data/setfim_data/`
- adjust any legacy `api/` or older local absolute paths
- provide any needed API credentials or headers for `setlist.fm`

## Documentation Strategy

This folder keeps two levels of documentation:

- `README.md` is the fast overview for readers who want to understand and open the artifact quickly
- `WRITEUP.md` is the deeper explanation of the design motivation, interaction model, and implementation decisions
