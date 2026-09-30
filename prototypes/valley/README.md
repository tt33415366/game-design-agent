# Unmarked Valley

Open [index.html](index.html) directly in a desktop browser. Move with `WASD` or arrow keys. The `Restart` button restores the authored starting point.

The game uses the single authored geometry source in [world.js](world.js) for drawing, collision, landmark feedback, and topology tests. Movement/collision rules live in [rules.js](rules.js). It is a small keyboard-only browser prototype; there is no touch control, saved progress, audio, or gameplay beyond exploration.

Local CC0 raster sheets are from Kenney's Tiny Town and Tiny Dungeon packs. Their license files remain in `assets/`; no network request is required at runtime.

Run checks with:

```bash
PLAYWRIGHT_BROWSERS_PATH=/tmp/game-designer-browsers /tmp/game-designer-tools/bin/python -m unittest prototypes/valley/tests/test_valley.py
```
