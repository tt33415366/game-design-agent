# Valley Prototype Review

## Findings

- **P1 - R03 collision does not match the visible obstacle geometry.** `prototypes/valley/world.js:52-59` treats every listed obstacle as an axis-aligned rectangle expanded by the player radius, while `prototypes/valley/game.js:39-43,79,81-82` draws trees as overlapping circles and rocks as ellipses. More importantly, `world.js:49` terrain trees are drawn but are not included in `world.js:58` collision at all. Concrete checks: the visibly drawn trunk point `(118.6, 141.25)` for terrain tree `[90,100]` is walkable, while `(1442,322)`, a visible-grass corner outside the rock ellipse at `(1450,330,42,42)`, is blocked. This violates the required circular footprint against the same terrain/obstacles that are drawn and creates both pass-through and invisible blocking.

- **P2 - Restart does not clear transient landmark feedback synchronously.** `prototypes/valley/game.js:20` resets keys, player, timing, and camera but never clears `#place`; it is only rewritten in the next `requestAnimationFrame` at line 85. Restarting while a landmark name is visible therefore leaves stale location feedback until a later frame, contrary to R01's reset requirement.

- **P2 - Movement speed is frame-rate dependent below 20 fps.** `prototypes/valley/rules.js:19` discards every active-frame delta above `0.05` seconds. A one-second held-east simulation travels 160 px at 60/30/20 fps, but only 120 px at 15 fps and 80 px at 10 fps. The cap prevents a resume jump, but it also makes ordinary low-frame-rate active play slower than the specified 160 world px/s. This needs an active-time/fixed-step approach or an explicitly accepted lower-frame-rate exception.

## Confirmed Checks

- The direct `file://` page uses local scripts and raster assets only. The retained licenses/provenance are present.
- The supplied Playwright suite passes: 4 tests, 0 failures, when Chromium is run outside the sandbox.
- The authored water gaps and bridges provide two distinct horizontal crossings; all landmark and detour targets are reachable by the existing coarse BFS. No prescribed order, score, inventory, terminal state, or modal was found.
- Blur/hidden handlers clear held keys and reset the frame timestamp; DPR sizing and camera clamping are implemented.

## Test Gaps / Residual Risk

- The topology test establishes only that bridge-center cells are reachable/open. It does not prove each crossing connects opposite banks, nor that the player cannot bypass the stream around its open north/south endpoints.
- No test covers R01's visible feedback clear, hidden-to-visible resume timing, camera/player visibility after resize, DPR scaling, actual rendered-vs-collider correspondence, or frame-rate speed at less than 20 fps.
- The coarse 12 px BFS is not a substitute for the runtime circular collision path and cannot detect the rendered geometry mismatch above.
