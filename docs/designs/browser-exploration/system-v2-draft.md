# Unmarked Valley v2: Prototype Rules (revision draft)

Authority: revised core gameplay/prototype scope confirmed 2026-09-30 09:25 UTC (user "Approved" to change-impact proposal). Supersedes v1.1 where in conflict; v1.1 retained in place as historical. Version: 2.0, 2026-09-30. Single geometry source remains `prototypes/valley/world.js` (v2 update); tests and rendering share it. All v1.1 verification is historical evidence for v1.1 only; every v2 rule below starts with `not run` verification.

## State and Parameters (delta from v1.1)

- All v1.1 state/parameters unchanged except: add per-landmark `revealed` flag (transient, cleared on restart); add log entity `{x, y, pushed}` (transient, reset on restart).
- Movement: unchanged (160 px/s, radius 10, fixed-step integration per v1.1 semantics).
- Push verb: player adjacent to the log and pressing toward it moves the log 8 px/frame if its target cell is walkable for the log's footprint; when the log's final position overlaps the ditch narrows, it becomes a walkable plank (bridge-like surface).

## Rule Catalog (v2)

v1.1 R01-R05, R07 carry over unchanged in semantics; reworded only where noted. New and revised rules:

| ID | Trigger | Required behavior and edge cases |
| --- | --- | --- |
| R01v2 | Initial load or Restart | Restore authored spawn/facing, clear held keys, clear all transient state including place feedback, `revealed` flags, reveal presentation, and log position; restore following camera. |
| R06v2 | Landmark proximity | Display restrained place-name feedback. On first entry to a landmark's reveal radius, trigger its authored reveal event (visual/camera/scenery change, at most one line of flavor text inline in the world, no modal, no score, no inventory, no assigned next destination, no checklist UI). Repeat entries do not re-trigger. Feedback and reveals never block movement. |
| R08 | Push interaction | The log is pushable when the player is adjacent and pressing toward it. The log moves only into cells walkable for its own footprint; it cannot be pushed through water except into the designated narrows, through trees/rocks/ruins, or off-world. When its final position overlaps the narrows, it locks and becomes a walkable plank. No push animation may displace the player. |
| R09 | Reveal content | Exactly three reveals exist (tower, crossing, grove). Fern Nook has no reveal. Reveals are scenery/light/camera changes plus at most one inline flavor line; they award nothing countable. |

## Reset Transient-State Enumeration (F2)

`heldKeys`, `place` text, `revealed[]`, active reveal presentation (light overlays, flavor text), log position/state, `last` timing baseline, camera. All cleared/restored in R01v2.

## Time Integration (F3)

Unchanged from v1.1: consume up to 0.25 s active elapsed per frame in ≤0.05 s physics steps; discard excess stall time; reset baseline on blur/hidden/resume.

## Geometry Consistency (F1/F4)

Drawn and collidable geometry share `world.js`. Decorative overhang permitted only for tree canopy above trunk bases. The log's pushed and plank states must both be drawn at their collidable footprint. The plank, once locked, participates in `blockedAt` as walkable surface, and the connection-integrity check must verify the shortcut connects where the narrows otherwise block.

## Planned Verification (all `not run`)

Carry over v1.1 planned checks (movement, collision, reset, focus, camera, topology, rendering sizes, screenshots, console errors) plus: rendered-vs-collider probes for log in both states; affordance honesty for the narrows before/after plank; connection integrity with the plank as the only crossing of the narrows; real game-loop smoke check collecting page/console errors with actual input (F5); three reveals trigger once and only once; reveals and log state reset under R01v2. First Player Validation session must be unassisted and recorded before any designer explanation (F8).
