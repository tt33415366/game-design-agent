# Unmarked Valley: Prototype Rules

Authority: actual approvals U1/U2 in [brief.md](brief.md). Version: 1.1, 2026-09-30. Experience claims remain Design Assumptions. Exact authored terrain, obstacle footprints, spawn, landmark approach points, and crossings have a single implementation source in `prototypes/valley/world.js`; test and rendering must use that same geometry.

## State and Parameters

- One fixed compact top-down world, approximately 2048x1536 world pixels; no generated levels.
- Player: continuous x/y coordinates, facing direction, movement state; initial position is the authored walkable spawn.
- Movement: 160 world pixels/second, radius 10 pixels, normalized diagonal input. Consume up to 0.25 seconds of active elapsed time per frame using physics steps no longer than 0.05 seconds, with collision movement subdivided into steps of at most 4 pixels. Discard excess stall time; reset the time baseline on blur/hidden/resume. This preserves ordinary low-frame-rate movement without background catch-up.
- Camera: follows the player, clamped to world edges; viewport scaling must not change world-space movement or collision.
- Temporary location feedback: the nearest landmark within its defined approach radius, otherwise none. No required visitation order, score, inventory, completion counter, or terminal win/loss state.

## Rule Catalog

| ID | Trigger | Required behavior and edge cases |
| --- | --- | --- |
| R01 | Initial load or Restart | Restore authored spawn/facing, clear held keys and transient location feedback, restore following camera. No prior movement survives restart. |
| R02 | Keyboard movement | WASD and arrow keys map to cardinal direction; opposing inputs cancel. Normalize nonzero direction so diagonals are not faster. Multiply by capped elapsed time. No input means no displacement. |
| R03 | Movement resolution | Subdivide displacement, test the player's circular footprint against the same terrain/obstacles that are drawn. Resolve horizontal and vertical movement independently for wall sliding. Water, tree trunks, rocks, ruin walls, and authored world boundary are blocked; bridges and walkable ground are not. No invisible puzzle gates. |
| R04 | Blur, tab hidden, or regained focus | Clear held keys on blur/hidden; do not integrate accumulated background time on resume. A paused/tabbed-out game must not walk on its own or jump across obstacles. |
| R05 | Camera/render | Render the world and player without changing simulation state. Respect pixel density and resize. Keep player visible at the edges; movement state and route connectivity survive resize. |
| R06 | Landmark proximity | Display restrained place-name feedback without awarding points, blocking movement, opening a modal, or assigning a next destination. Arrival can reveal scenery or a connection. Feedback is not a task list. |
| R07 | Exploration topology | All three landmark approaches and the optional detour are reachable from spawn. At least two physically distinct stream crossings connect the banks; neither crossing requires prior visitation elsewhere. No route order is prescribed. |

## Authored Content and Presentation

Three recognizable landmarks: a ruined stone tower, a stream crossing, and a secluded grove. Include a separate optional side path or nook, and interconnecting paths rather than one corridor visiting all three in sequence. At spawn, visual composition must suggest at least two plausible directions without instruction arrows. A small world boundary is visible terrain, not an unexplained barrier.

Use local raster art where suitable, with actual license/provenance retained; custom game-specific drawing may complete a missing landmark. Preserve asset readability and ground-level collision cues. Distinguish water, woodland, trails, stonework, and the player. The playable canvas is the main full-viewport experience, with restrained title/place feedback and a keyboard-accessible restart command, not a framed dashboard or landing page.

Tree collision follows the visible trunk/base, not decorative canopy overhang. Rock and wall footprints must likewise match their visible ground geometry. All rendered blocking objects participate in the shared geometry; decorative floor marks must not look like solid walls. Trails cross the stream at actual crossings, and the stream meets the visible world perimeter.

Version 1.1 is an implementation clarification following iteration-1 review: the former per-frame time cap caused slow movement below 20 fps, and decorative geometry did not consistently match collision. These corrections do not add gameplay or expand U2 scope.

## Planned Verification

These checks are not run until logged in validation.md: cardinal/diagonal speed; no-input stability; obstacle/water collision and substep protection; reset; focus-loss handling; camera and viewport bounds; keyboard movement; BFS or equivalent topology check for landmarks, detour, and both crossings; desktop/mobile-sized rendering checks; screenshots and console errors.

Mobile-sized rendering is checked for clipping; touch controls are not part of U2. Geometry/test correctness does not establish the feeling of freedom, interest, final-art quality, accessibility completeness, or production readiness.
