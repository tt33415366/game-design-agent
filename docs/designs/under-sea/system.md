# Sunlight Shelf: Prototype Rules

Authority: combined core-gameplay/prototype-scope checkpoint confirmed 2026-10-08 02:29 UTC (Candidate A, 2h / 1 iteration / zero spend; absolute stop 04:29:28 UTC). Version: 1.0. Single geometry source: `prototypes/undersea/world.js`; tests and rendering share it. All verification starts `not run`.

## State and Parameters

- One fixed top-down reef shelf, ~2048x1536 world pixels, authored (no generation).
- Player: continuous x/y, facing, swim velocity; initial position is an authored open-water spawn.
- Swim (buoyant, distinct from valley walk): acceleration toward input direction, water drag caps speed at ~150 px/s, inertia keeps the player drifting briefly after input stops; vertical movement (up/down) uses the same keys as horizontal (top-down, depth shown by tint, not a second axis).
- Camera: follows player, clamped to world edges; DPR-aware; movement/collision invariant to viewport.
- Transient state: held keys, place feedback, per-sight `revealed` flags, active reveal presentation, boulder state, timing baseline. All cleared/reset on restart (F2).

## Rule Catalog

| ID | Trigger | Required behavior and edge cases |
| --- | --- | --- |
| R01 | Initial load or Restart | Restore authored spawn/facing, clear held keys, place feedback, `revealed` flags, active reveal text/aura, boulder position, reset timing baseline and camera. |
| R02 | Keyboard swim | WASD/arrows map to cardinal swim. Opposing inputs cancel. Diagonal normalized (not faster). Acceleration/drag per swim parameters; no input decays velocity to 0. Time-based integration explicit: consume up to 0.25 s active elapsed per frame in ≤0.05 s physics steps; discard excess stall; reset baseline on blur/hidden/resume (F3). |
| R03 | Movement resolution | Subdivide displacement (≤4 px steps), test circular footprint against the same geometry that is drawn (F1). Coral/rock/reef walls and world boundary block; open water and swim-through gaps do not. Wall sliding via independent axis resolution. No invisible gates. |
| R04 | Blur/hidden/focus | Clear held keys on blur/hidden; no accumulated background integration on resume. |
| R05 | Camera/render | Render without changing simulation; DPR-aware resize; player visible at edges; route connectivity survives resize. |
| R06 | Sight proximity + reveal | Restrained place-name feedback near sights. First entry to a sight's reveal radius triggers its authored reveal (scenery/light change + at most one inline flavor line). No modal, score, inventory, assigned destination, or checklist UI. Once only; never blocks movement. Fern-equivalent (an empty sand flat) has no reveal, intentionally. |
| R07 | Pressure pocket | Exactly one dark crevice is a pressure pocket: its mouth is visible from open water (visual darkness gradient), entry is optional, and inside it the screen darkens (vignette) and the strongest reveal sits at its heart. Avoiding it must be possible without blocking any other content. No fail state, no damage — pressure is atmospheric, not lethal. |
| R08 | Push boulder | Exactly one pushable boulder. Player adjacent and pressing toward it moves it at swim speed in sync with the player (contact-preserving). It moves only into cells walkable for its footprint. The channel narrows gap is always swimmable; when the boulder fully spans the narrows it locks and becomes a wider swim-through arch — an optional convenience shortcut, not the sole crossing. |
| R09 | Reveal content | Exactly three reveals (reef arch, wreck exterior silhouette, anemone garden) plus the crevice-heart reveal inside the pocket. Wreck is exterior-only: no looting, no salvage interaction. |

## Geometry Consistency (F1/F4)

Drawn and collidable geometry share `world.js`. Coral/rock drawn at their collision footprint; decorative soft coral may overhang only above a visible hard base. Boulder drawn at footprint in both free and locked states. The crevice mouth's dark gradient must not extend over swimable open water (affordance honesty). The crevice and the shortcut arch participate in connection-integrity checks: the arch must be the only crossing of its channel, and the crevice interior must be reachable without crossing it.

## Planned Verification (all `not run`)

Swim inertia (accelerate, coast, stop); diagonal speed; low-fps speed consistency and stall cap; collision vs water/rock/coral with substep; reset (including revealed/boulder/transient UI); blur/hidden key clear; camera/viewport/DPR; BFS topology: all sights + crevice heart reachable, arch is sole channel crossing, crevice reachable without arch; rendered-vs-collider probes; affordance honesty (dark gradient only over crevice); connection integrity; real game-loop smoke with page/console errors and actual input (F5); reveal-once semantics; screenshot desktop/mobile. First Player Validation session unassisted, recorded before any explanation (F8).

Mobile-sized rendering is checked for clipping only; touch controls are not in scope. Rule tests do not establish fun, pressure feel, or accessibility.
