# Three Stones: Prototype Rules

Authority: combined core-gameplay/prototype-scope checkpoint confirmed 2026-10-08 03:04 UTC (Candidate A, 2h / 1 iteration / zero spend; absolute stop 05:04:57 UTC). Version: 1.0. Single geometry source: `prototypes/tidal/world.js`; tests and rendering share it. All verification starts `not run`.

## State and Parameters

- One fixed top-down tide flat, ~2048x1536 world pixels, authored. A rock-walled channel network crosses it; three channel segments start blocked by three movable stones.
- Phases: `calm` (low tide, walk) → `rising` (tide floods along opened channels, timed transition) → `swim` (high tide, swim to the stranded pool). Phase is part of state; restart returns to `calm`.
- Player: calm phase = valley-style direct walk (160 px/s); swim phase = Sunlight-Shelf buoyant swim (accel 700, drag 3.2, max 150 px/s). Phase switches movement model.
- Stones: three entities `{x, y, placed}`; each starts in a notch blocking one channel segment; drag moves it; when placed into an adjacent open notch, that channel segment becomes open.
- Tide timer: `rising` lasts ~20 seconds; flood front advances along opened channels only. No fail state: if the player is not in water-safe position when flood passes, they are gently carried with the front (no damage).
- Transient state: held keys, place feedback, `revealed` flags, reveal presentation, stone positions, phase, tide timer, timing baseline. All cleared/reset on restart (F2).

## Rule Catalog

| ID | Trigger | Required behavior and edge cases |
| --- | --- | --- |
| R01 | Initial load or Restart | Restore authored spawn, phase=calm, stones to notches, clear held keys/feedback/reveals/tide state, reset camera and timing baseline. |
| R02 | Calm-phase movement | Direct walk (valley R02/R03 semantics): WASD/arrows, diagonal normalized, ≤4 px collision substeps, wall sliding, circular footprint against drawn geometry (F1). Time integration explicit per F3 (≤0.25 s active/frame in ≤0.05 s steps, stall discard, baseline reset on blur/hidden/resume). |
| R03 | Stone drag | Adjacent + hold toward a stone drags it along the channel axis at walk speed, contact-preserving. A stone moves only between its home notch and the adjacent open notch; releasing leaves it. When it reaches the open notch it snaps placed and its channel segment opens; it cannot be pushed back into blocking (one-way, keeps the calm phase to three meaningful moves). |
| R04 | Tide transition | After all three stones are placed, or when the player steps onto the marked starting rock after ≥1 stone placed, `rising` begins. Flood front advances along opened channels only; blocked segments stay dry rock. After ~20 s the map is at high tide: `swim`. |
| R05 | Swim phase | Buoyant swim (Shelf R02 semantics) over flooded channels; dry rock and reef still block. The stranded pool is reachable only through at least one opened channel; if no channel was opened the pool is unreachable but the swim phase still occurs (no fail — the player simply cannot arrive, an authored dead end, not a punishment). |
| R06 | Sight proximity + reveal | Restrained place-name feedback; first entry to a reveal radius triggers its authored reveal (scenery change + ≤1 inline flavor line). No modal/score/checklist. Exactly two reveals (the pool at journey's end; a tide-swept arch mid-flat). |
| R07 | Soft pressure | During `rising`, being in a flooding channel gives a brief current push along the flood direction (atmospheric, non-lethal). No damage, no fail state anywhere. |
| R08 | Blur/hidden/focus | Clear held keys; no background integration on resume; tide timer pauses while hidden and resumes without catch-up jump. |
| R09 | Camera/render | Follow player, clamp to edges, DPR-aware, movement/collision invariant to viewport. Tide flood is rendered as advancing water over the exact channel geometry that blocks/blocks-not (F1/F4). |

## Geometry Consistency (F1/F4)

Drawn and collidable geometry share `world.js`. Stones drawn at footprint in notch and placed states. Channel walls and reef drawn at collision footprint. Flood water covers exactly the opened channel rectangles; the visual flood front never extends over unopened or blocked segments (affordance honesty). Connection integrity: the pool is reachable in `swim` iff ≥1 channel was opened in `calm`; topology check verifies both directions (opened → reachable, none opened → unreachable).

## Planned Verification (all `not run`)

Calm walk + collision; drag semantics (adjacency, axis, one-way snap); tide transition trigger; flood advances only on opened channels; swim physics; pool reachable iff opened; reset across all transient state (stones/phase/tide/reveals); blur/hidden key clear + tide pause; camera/DPR; rendered-vs-collider probes; affordance honesty (flood only on opened); connection integrity both directions; real game-loop smoke with page/console errors and actual input across both phases (F5); screenshots desktop/mobile. First Player Validation session unassisted (F8), with a post-play question on whether the route felt self-authored.

Mobile-sized rendering checked for clipping only; touch out of scope. Rule tests do not establish whether self-authored routes feel rewarding.
