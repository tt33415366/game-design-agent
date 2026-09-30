# Latchline Salvage prototype

Open `index.html` directly in a modern desktop or mobile browser. Select one action in each visible wreck section, then use the restart control to begin a new run.

This is a local, dependency-free, non-production prototype for the constructed fixture in `tests/scenarios/01-new-game/design.md`. `salvage-rules.js` is the single implementation of rules `R-01` through `R-09`; `index.html` renders its state and supplies controls. It does not establish player comprehension, fun, balance, production readiness, or accessibility completeness.

Run deterministic browser tests with:

```sh
PLAYWRIGHT_BROWSERS_PATH=/tmp/game-designer-browsers /tmp/game-designer-tools/bin/python -m unittest prototypes/salvage/tests/test_salvage.py
```

Capture the reproducible desktop/mobile evidence and direct-interface checks with:

```sh
PLAYWRIGHT_BROWSERS_PATH=/tmp/game-designer-browsers /tmp/game-designer-tools/bin/python prototypes/salvage/tests/capture_evidence.py
```
