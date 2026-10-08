# Echo Caves: Prototype Rules

Authority: combined core gameplay/prototype scope confirmed 2026-10-08 06:55 UTC (Candidate B, 2h / 1 iteration / zero spend; stop 08:55:15 UTC). Version 1.0. Geometry source: `prototypes/echo-caves/world.js`; rendering and tests share it. All checks begin `not run`.

## State

- Compact top-down underwater cave. Player starts in an open surface lagoon at the cave mouth.
- Phases: `surface` (calm swim) and `cave` (pressure/darkness). Returning to the lagoon is voluntary and always possible.
- Player: buoyant swim with acceleration, drag, max speed 150 px/s; circular footprint radius 10.
- Three branches from the cave mouth. Each branch has a visible environmental cue, a pressure gradient, and either a reveal or an empty retreat. No numeric oxygen meter.
- Transient state: held keys, current branch, revealed flags, flavor line, pressure level, timing baseline; all cleared/reset on restart.

## Rule Catalog

| ID | Trigger | Required behavior |
| --- | --- | --- |
| R01 | Initial load/restart | Spawn at surface, phase=surface, clear branch/reveal/flavor/pressure/keys, reset camera and timing baseline. |
| R02 | Swim | WASD/arrows, opposing cancel, normalized diagonals, acceleration/drag/max speed; active elapsed capped at .25 s per frame in .05 s steps; discard stall excess; reset baseline on blur/hidden. |
| R03 | Cave entry | Entering the cave mouth sets phase=cave and records current branch when crossing a branch threshold. Branches remain spatially distinct; no automatic assignment. |
| R04 | Pressure gradient | Pressure is atmospheric rendering/audio-free semantics: cave darkness and current visual increase with depth in the current branch. No damage, fail state, oxygen meter, or forced retreat. |
| R05 | Return | Player can swim back to the surface mouth from every branch. Crossing the mouth sets phase=surface and clears active pressure presentation, but does not clear revealed flags until restart. |
| R06 | Reveal | First arrival at a branch reveal triggers one scenery/light change and at most one inline flavor line. No score, inventory, checklist, or assigned next branch. |
| R07 | Branch cues | Three branch mouths have distinct visible cues: warm glow, slow drifting particles, or a rhythmic shadow pulse. Cues are invitations, not answer markers. |
| R08 | Geometry | Drawn cave walls, branch bounds, and player blockers share one geometry source; decorative darkness must not cover walkable water. |
| R09 | Real loop | Runtime must pass page/console error smoke with actual keyboard movement through surface, branch, retreat, and second-branch paths. |

## Planned Verification

Swim inertia, diagonal speed, collision/substeps, reset/blur, branch reachability and retreat, pressure rendering bounds, reveal-once, visual-vs-collider probes, three cue distinction, real-loop/page-error smoke, desktop/mobile screenshots. Player Validation is unassisted first; ask whether the first cue invited entry, whether the first reveal/retreat invited a second branch, and whether pressure felt atmospheric rather than meter management.
