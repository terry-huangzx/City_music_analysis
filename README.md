# City Music Analysis

City Music Analysis is a multi-part data visualization project about how live music activity varies across major North American cities. The repository combines raw event data, exploratory visualization layers, and a polished final storytelling experience that turns concert activity into an interactive narrative.

At its core, the project asks a simple question: how can we compare the musical character of cities through the events they host, the genres they surface, and the venues that shape their scenes?

## Project Structure

The repo is organized into three main parts:

### 1. Data assets

[`spotify_and_ticketmaster_data/`](/Users/fanyanting/City_music_analysis/spotify_and_ticketmaster_data) stores the source CSV files used throughout the project.

- `setfim_data/` contains 13 city-level `setlist.fm` concert datasets for 2025
- `spotify_weekly_data_2025/` contains Spotify weekly chart exports used for comparison and enrichment

### 2. Exploratory visualization layers

[`layers/`](/Users/fanyanting/City_music_analysis/layers) contains four standalone HTML prototypes, each exploring a different analytical lens:

- [`layer1_seasonal_volume.html`](/Users/fanyanting/City_music_analysis/layers/layer1_seasonal_volume.html): monthly event volume across cities
- [`layer2_genre_diversity.html`](/Users/fanyanting/City_music_analysis/layers/layer2_genre_diversity.html): genre composition and diversity by city
- [`layer3_venue_distribution_comparison.html`](/Users/fanyanting/City_music_analysis/layers/layer3_venue_distribution_comparison.html): rank-based venue concentration comparisons
- [`layer4_radial_mismatch.html`](/Users/fanyanting/City_music_analysis/layers/layer4_radial_mismatch.html): temporal rhythm and supply-demand mismatch

These layers function as modular analysis views and also feed into the final storytelling direction of the project.

### 3. Final interactive outputs

The repo includes two polished presentation artifacts:

- [`final_product/city_music_pulse.html`](/Users/fanyanting/City_music_analysis/final_product/city_music_pulse.html): the long-form narrative experience that stitches together the project into a scrolling story
- [`interaction_vinyl_map/hero-real-data.html`](/Users/fanyanting/City_music_analysis/interaction_vinyl_map/hero-real-data.html): a self-contained interactive "vinyl map" showing live concert activity across 13 metros

The `interaction_vinyl_map` folder also includes the processing scripts, processed JSON, and project-specific documentation for that piece.

## Recommended Entry Points

If you are opening this repo for the first time, start here:

1. Open [`final_product/city_music_pulse.html`](/Users/fanyanting/City_music_analysis/final_product/city_music_pulse.html) for the full narrative experience.
2. Open [`interaction_vinyl_map/hero-real-data.html`](/Users/fanyanting/City_music_analysis/interaction_vinyl_map/hero-real-data.html) for the standalone interactive hero visualization.
3. Browse the files in [`layers/`](/Users/fanyanting/City_music_analysis/layers) if you want to see the intermediate analytical views.

All of these files are browser-ready HTML documents. In most cases, you can simply open them directly in a modern browser.

## Highlights

- Real concert data collected from `setlist.fm`
- Comparative analysis across 13 North American metros
- Multiple visualization forms, from exploratory analytical layers to a final narrative experience
- Self-contained HTML outputs that are easy to share and review

## Documentation

- [`interaction_vinyl_map/README.md`](/Users/fanyanting/City_music_analysis/interaction_vinyl_map/README.md): focused documentation for the vinyl map interactive
- [`interaction_vinyl_map/WRITEUP.md`](/Users/fanyanting/City_music_analysis/interaction_vinyl_map/WRITEUP.md): design rationale, data pipeline notes, and technical explanation

## Project Info

Course project for STA313 Data Visualization, University of Toronto, 2025.

Group 50: Yanting Fan, Zixiang Huang, Xiaoyao Wang, Jingyi Yang, Yuxin Yao

Data sources: `setlist.fm` and Spotify

## Notes

- Some processing scripts were originally written against an earlier local folder layout, so path adjustments may be needed if you want to rerun the full pipeline.
- The repo currently works best as a presentation and documentation artifact, with the HTML outputs serving as the easiest way to explore the project.
