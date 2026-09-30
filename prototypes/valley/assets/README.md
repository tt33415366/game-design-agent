# Valley prototype assets

This directory contains only the two source atlases and their bundled license
texts needed by the local browser exploration prototype.

## Sources and license

- `kenney-tiny-town-tilemap.png`: extracted unchanged from the official free
  [Kenney Tiny Town](https://kenney.nl/assets/tiny-town) archive, downloaded
  September 30, 2026. Use for grass, water, paths, trees, rocks, and buildings.
- `kenney-tiny-dungeon-tilemap.png`: extracted unchanged from the official free
  [Kenney Tiny Dungeon](https://kenney.nl/assets/tiny-dungeon) archive,
  downloaded September 30, 2026. Use for the player and ruined stone elements.

Both packs are Creative Commons Zero (CC0) 1.0. Their original bundled license
texts are retained verbatim in the corresponding `LICENSE-*` files. Attribution
is optional under the license; source attribution is retained here for
provenance.

## Atlas layout

Each PNG is 203 x 186 pixels: a 12 x 11 grid of 16 x 16 pixel tiles with a
1-pixel transparent gutter between adjacent tiles and no outer margin. For
zero-based grid coordinate `(column, row)`, use source rectangle:

`x = column * 17`, `y = row * 17`, `width = 16`, `height = 16`.

Render with image smoothing disabled and integer scaling to preserve pixel art.
