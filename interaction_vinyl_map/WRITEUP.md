# Urban Music Pulse: Hero Visualization Writeup

**Primary file:** [`hero-real-data.html`](/Users/fanyanting/City_music_analysis/interaction_vinyl_map/hero-real-data.html)  
**Theme:** Civic vitality through live music  
**Dataset:** 56,122 concert records from `setlist.fm` across 13 North American metros

## 1. Intuition and Motivation

Every city has a sound. New York pulses with hip-hop and jazz, Montreal leans into jazz and indie scenes, Calgary carries a stronger country identity, and Miami suggests a different balance again. Live concerts provide one of the clearest public traces of those local identities because they reveal who performs, where audiences gather, and what genres dominate the scene.

The central question behind this piece is:

> Where does live music happen in North America, and what does each city sound like?

Instead of using a static bar chart or choropleth alone, the visualization treats each city as a vinyl record and each concert as a glowing dot orbiting around it. A synthesized 118 BPM beat makes the page pulse, so the viewer does not just read the data but feels the rhythm of the scene.

## 2. Data Pipeline

### 2.1 Source Selection

- Ticketmaster Discovery API was explored first, but it is oriented toward upcoming events rather than historical concert activity.
- `setlist.fm` became the main source because it provides a much stronger historical concert record.
- Spotify data was part of the broader project context, but this specific interactive ultimately relied on `setlist.fm` concert records plus city-level genre assignment logic.

### 2.2 Fetching

[`scripts/setlistfmAPI.py`](/Users/fanyanting/City_music_analysis/interaction_vinyl_map/scripts/setlistfmAPI.py) fetches raw event data from `setlist.fm`.

The data collection strategy was shaped by rate limits, pagination, and the need to cover multiple cities over time. The broader project stores the raw CSV exports in [`../spotify_and_ticketmaster_data/setfim_data/`](/Users/fanyanting/City_music_analysis/spotify_and_ticketmaster_data/setfim_data).

### 2.3 Cleaning and Aggregation

[`scripts/process_hero_data_v2.py`](/Users/fanyanting/City_music_analysis/interaction_vinyl_map/scripts/process_hero_data_v2.py) handles the main transformation work:

- aggregates 360+ suburb and satellite-city names into 13 metro areas
- assigns representative genres through city-level genre distributions
- samples a manageable set of events for display density
- compresses field names to keep the final payload small

The processed output is [`data/hero_data_v2.json`](/Users/fanyanting/City_music_analysis/interaction_vinyl_map/data/hero_data_v2.json).

### 2.4 Final Assembly

[`scripts/build_hero_v2.py`](/Users/fanyanting/City_music_analysis/interaction_vinyl_map/scripts/build_hero_v2.py) embeds the processed JSON directly into [`hero-real-data.html`](/Users/fanyanting/City_music_analysis/interaction_vinyl_map/hero-real-data.html), producing a single self-contained file with no data-loading dependency at runtime.

## 3. Final Presentation

### 3.1 Visual Architecture

The final interface combines layered canvases with DOM-based city markers:

| Layer | Purpose |
| --- | --- |
| `discC` | beat-reactive vinyl-disc glow layer |
| `mapC` | North America base map |
| `dotC` | concert dots, colored by genre |
| `.cm` markers | interactive city markers and hover targets |

### 3.2 Core Design Choices

- Each metro is represented as a vinyl record rather than a simple point marker.
- Concerts are arranged in an annular scatter around each city so the central marker remains clickable.
- Genre color helps viewers compare the musical character of cities at a glance.
- The layout is designed to stay aligned across different viewport sizes and high-DPI screens.

### 3.3 Audio-Reactive Motion

A Web Audio API beat pattern drives both sound and motion. On each pulse:

- vinyl records expand subtly
- event dots brighten and breathe
- the interface feels performative rather than static

This choice turns the map into an atmospheric experience, not just an analytical display.

## 4. Interaction Design

### 4.1 Home View

From the overview screen, users can:

- hover a dot to inspect it as an interactive target
- click a dot to preview a concert
- click a city marker to open a city-specific detail panel
- toggle the beat on or off

### 4.2 City Detail Panel

Opening a city reveals a deeper breakdown that includes:

- top-level stats
- genre composition
- leading venues
- a browsable event field for the sampled concerts

### 4.3 Event Detail Modal

Selecting an event inside the city detail view opens a focused card with artist, venue, date, and genre information.

## 5. Technical Challenges and Solutions

| Problem | Solution |
| --- | --- |
| API rate limits | batched collection strategy and careful query planning |
| messy city naming | manual metro aggregation logic |
| no direct genre field in source data | city-level genre assignment strategy |
| keeping the artifact lightweight | compressed fields and sampling |
| keeping interaction smooth | canvas rendering instead of thousands of DOM nodes |
| display alignment across screens | DPI-aware sizing and live layout anchoring |

## 6. Repo Notes

This writeup describes the logic of the visualization as preserved in the current repository, but some scripts still reflect an earlier local project structure. If you plan to rerun the pipeline, expect to adjust paths before execution.

For quick orientation:

- use [`README.md`](/Users/fanyanting/City_music_analysis/interaction_vinyl_map/README.md) for the short overview
- use [`hero-real-data.html`](/Users/fanyanting/City_music_analysis/interaction_vinyl_map/hero-real-data.html) for the final standalone artifact
- use the broader repo [`README.md`](/Users/fanyanting/City_music_analysis/README.md) for how this folder fits into the full project
