# Latchline Salvage prototype

Open `index.html` directly in a modern desktop or mobile browser. Select one action in each visible wreck section, then use the restart control to begin a new run.

This is a local, dependency-free, non-production prototype for the constructed fixture in `tests/scenarios/01-new-game/design.md`. `salvage-rules.js` is the single implementation of rules `R-01` through `R-09`; `index.html` renders its state and supplies controls. It does not establish player comprehension, fun, balance, production readiness, or accessibility completeness.

## Legend Revision - 2026-09-30

The user reported that the artwork did not look like a ship, proposed a legend instead of a redesign, and explicitly approved the schematic label and key. This is actual user feedback and approval for one local presentation-only revision, separate from the fixture's simulated approvals. The broader gameplay explanation/redesign proposal was not approved by this decision.

The existing drawing now has a `Wreck schematic` caption and keys for its hull outline, internal structure, reactor, damage markers, and scan line. These are schematic annotations, not live gameplay indicators. Artwork and authoritative rules are unchanged; no spending, publishing, or handoff approval is implied.

Verification: the new legend test failed before implementation at all three viewport widths. After implementation, all 10 tests passed via the command below, including visible labels, no horizontal page overflow, and caption/drawing separation at 1280, 390, and 320 pixels. Screenshots were captured under `/tmp/salvage-legend-*.png`; visual inspection was unavailable in the current session. Earlier screenshots describe the pre-legend interface, not this revision. Whether the legend improves this user's recognition remains untested.

## Route And Outcome Revision - 2026-09-30

Actual user approval in this session: one local, zero-spend presentation-only iteration to make the current, completed, and upcoming sections clear; show each available action's cargo and hull effects before selection; and explain terminal success or failure with final resources and thresholds. This approval is distinct from the fixture's simulated approvals and the earlier actual legend approval. It does not authorize gameplay, rule, numeric, artwork, scope, spending, publishing, or handoff changes.

`index.html` now renders the route from the current state, and action previews call the existing pure `applyAction` function without assigning its returned state. Terminal text identifies the final cargo target (`5`), hull capacity (`4`), hull-breach priority even when cargo is sufficient, and the surviving-hull cargo-target failure. The original action names remain the button accessible names, with each preview associated through `aria-describedby`.

TDD evidence: the focused browser assertions were added first and failed before this implementation because `#route` and the new terminal explanation text were absent. The initial non-elevated run could not launch Chromium in the sandbox; the elevated local run then completed and reported the expected three UI assertion failures. A final focused assertion also failed when disabled terminal actions incorrectly showed `Cargo +0 / Hull +0`; it now reads `Run complete.`. After implementation, the command below passed all 12 tests, including desktop and 320px overflow checks, route state, non-mutating previews, accessibility associations, extraction, hull-breach priority, and surviving-hull cargo-target failure. This is rule/rendering verification only, not Player Validation or an accessibility-completeness claim.

Independent verification repeated the 12-test suite and exercised all eight legal action sequences: pre-click previews matched the rule function without mutating the live state. Desktop (1280x900), mobile (390x844), and narrow mobile (320x568) checks found no horizontal overflow or terminal overlap. The reviewer visually inspected `/tmp/salvage-clarity-{desktop,mobile-390,mobile-320,terminal-320}.png` without finding clipping or overlaps; these are temporary headless-browser screenshots, not player-comprehension evidence. Whether the revised presentation helps the user predict choices remains pending feedback.

Run deterministic browser tests with:

```sh
PLAYWRIGHT_BROWSERS_PATH=/tmp/game-designer-browsers /tmp/game-designer-tools/bin/python -m unittest prototypes/salvage/tests/test_salvage.py
```

Capture the reproducible desktop/mobile evidence and direct-interface checks with:

```sh
PLAYWRIGHT_BROWSERS_PATH=/tmp/game-designer-browsers /tmp/game-designer-tools/bin/python prototypes/salvage/tests/capture_evidence.py
```
