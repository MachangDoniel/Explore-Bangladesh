# Explore Bangladesh

A bilingual Bangladesh travel guide featuring 30 destinations across eight divisions, destination photographs, smart search, an interactive map, selected-place grids, detailed travel guides, and persistent light/dark mode.

Live website: https://explore-bangladesh-doniel.donieltripura1971.chatgpt.site

## Run locally

From this folder, run `python3 -m http.server 8000 --directory .` and open http://localhost:8000. No build step or API key is required.

## Files

- `index.html`: homepage
- `places.html`: destination directory and selected places
- `place.html`: individual destination guides
- `map.html`: interactive map
- `destinations.json`: bilingual guide content, photo credits and source links
- `theme.js` and `dark.css`: theme switch

Map tiles use OpenStreetMap. Leaflet is distributed under its BSD 2-Clause license. Destination photographs retain their individual licenses; see IMAGE_CREDITS.md and the attribution shown on the website.
