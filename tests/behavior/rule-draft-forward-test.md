# Closed Fictional Workflow Simulation: Rule Draft Forward Test

## Simulation Boundary

- Execution date: `2026-09-30`
- Mode: closed fictional workflow simulation
- Real project changes: none
- Code, prototype, tests, external operations, commits, and subagents: none
- Writable artifact requested by task: this file only
- Classification key: `sourced fact | Design Assumption | simulated result | rule verification | Player Validation`

The quoted transcript below is simulated input for a fictional project. It is not an approval, instruction, or evidence for the real repository.

## Consulted Files

| File | Purpose | Result |
| --- | --- | --- |
| `agents/game-designer.md` | Contract, checkpoint and evidence requirements | Consulted |
| `.agents/skills/gameplay-design/SKILL.md` | Gameplay-proposal prerequisite and scope rules | Consulted |
| `.agents/skills/gameplay-design/templates/gameplay-proposal.md` | Gameplay draft structure | Consulted |
| `.agents/skills/system-design/SKILL.md` | System-specification prerequisite and authority rules | Consulted |
| `.agents/skills/system-design/templates/system-specification.md` | System draft structure | Consulted |

No PRD, plan, fixture, prior report, test, implementation, existing Design Brief, or project record was read.

## Complete Simulated Transcript

### Simulated USER turn

> I approve the English Design Brief: a local offline single-player browser salvage puzzle for casual planners; solo JS developer; one week; $0; maximum FIVE prototype iterations. Please propose core gameplay/scope and a non-authoritative draft of system rules and verification cases. I have not approved the gameplay or prototype scope yet.

### Simulated assistant response

The English Design Brief is recorded as approved by the simulated user. I have prepared a gameplay and prototype-scope proposal with the supplied constraints: local offline browser, solo JavaScript developer, one week, $0, and a maximum of five prototype iterations.

The core gameplay/prototype-scope checkpoint remains `pending`; no prototype or implementation is authorized by this draft. Because that checkpoint is not approved, the attached system specification is explicitly a non-authoritative draft. Its verification cases are planned specifications only and all remain `not run`.

Please approve, reject, or revise the proposed core loop and prototype scope. The rule IDs below become authoritative only after that approval is recorded.

## Simulated Project Record State

| Field | Value | Classification and provenance |
| --- | --- | --- |
| Project | `Harbor Salvage` (working title) | Design Assumption; introduced solely for document identification |
| Document language | English | sourced fact; simulated user says “English Design Brief” |
| Design Brief checkpoint | confirmed | simulated result; explicit simulated-user approval in transcript |
| Design Brief approval reference | `simulated transcript, 2026-09-30, simulated USER turn` | simulated result |
| Core gameplay/prototype scope checkpoint | pending | sourced fact; simulated user explicitly has not approved it |
| Development Handoff Draft checkpoint | pending | simulated result; not requested or approved |
| Platform | local offline single-player browser game | sourced fact; simulated user turn |
| Target player | casual planners | sourced fact; simulated user turn |
| Team capability | solo JavaScript developer | sourced fact; simulated user turn |
| Time limit | one week | sourced fact; simulated user turn |
| Spending limit | `$0` | sourced fact; simulated user turn |
| Prototype iteration limit | maximum `5` | sourced fact; simulated user turn |

## Draft: Gameplay Proposal

### Record

- Project: `Harbor Salvage` (working title; Design Assumption)
- Document language: English
- Design Brief: simulated Design Brief approval in the transcript, `2026-09-30`
- Current stage: `gameplay-and-prototype`
- Classification key: `sourced fact | Design Assumption | simulated result | rule verification | Player Validation`

### Core Experience

| Item | Proposal | Classification and source | Risk or open question |
| --- | --- | --- | --- |
| Target player | Casual planners who want short, readable spatial-planning puzzles. | target segment is sourced fact; session preference is Design Assumption | Session length has not been supplied. |
| Intended experience | Make a constrained recovery plan, execute it, and revise after a clear operational consequence. | Design Assumption | This is an unvalidated experience claim, not Player Validation. |
| Core loop | Inspect a compact wreck grid; choose one salvage target and a route; commit a limited action budget; observe recovered cargo, blocked paths, and remaining capacity; re-plan until the shift ends. | Design Assumption derived from supplied “salvage puzzle” and “casual planners” facts | The route-planning complexity must remain legible on a small board. |
| Observable outcome | The board shows the traversed route, fuel used, cargo secured, newly exposed blockers, and a concise end-of-shift result. | Design Assumption | Feedback timing and visual clarity need local prototype observation. |

### Mechanic Proposal

The player pilots a salvage skiff through a small top-down wreck field. Each shift begins with several visible cargo pods, hazardous debris, a dock, a fuel budget, and a cargo-capacity limit. The player selects a cargo pod and draws a contiguous orthogonal route from the dock to it; committing the route spends fuel per entered tile and collects the pod only when the skiff can return to the dock with enough fuel and capacity. Collecting a pod may reveal one adjacent tile that was previously concealed, creating a bounded planning consequence for the next choice.

The smallest content that exercises the loop is one deterministic 6-by-6 board with three cargo pods, two debris tiles, one concealed tile, fuel for two efficient recovery routes, and capacity for two pods. The stakes are a finite shift: a greedy distant target can prevent a return or leave capacity/fuel mismatched, while an efficient pair of routes produces a higher salvage score. Exact semantics are proposed in draft rules `R-MOVE-001` through `R-END-001`; those identifiers are non-authoritative until checkpoint confirmation.

### Alternatives and Experiments

| Alternative | Experiential benefit | Trade-off or risk | Low-cost experiment | Decision status |
| --- | --- | --- | --- | --- |
| Route drawing before committing | Supports planner expression and makes intended movement inspectable. | Path validation and undo affordance add UI work. | Paper-clickable grid: ask a developer to trace three routes and record where legality is unclear. | proposed |
| One concealed tile revealed after each salvage | Adds small, controlled replanning moments. | Randomness could undermine a deterministic puzzle. | Use one fixed reveal placement in the first board and compare comprehension with no reveal. | proposed |
| Multiple skiff tools | Could diversify choices. | Exceeds one-week, solo, `$0` scope and obscures the core route/capacity puzzle. | None before a core-loop test. | rejected |

### Supporting Direction

| Area | Only gameplay-relevant direction | Classification |
| --- | --- | --- |
| Narrative | A shift summary may name recovered cargo categories; no story progression required. | Design Assumption |
| Art and UI | Flat, high-contrast tile symbols distinguish dock, skiff, cargo, debris, hidden tile, planned route, and committed route. | Design Assumption |
| Audio | None required for the prototype; visual confirmation carries feedback. | Design Assumption |
| Levels or content | One deterministic tutorial board and one deterministic challenge board, each hand-authored. | Design Assumption |

### Prototype Scope and Checkpoint

- Validation question: Can a casual planner understand that every salvage choice must reserve a legal return route and make a deliberate second recovery plan on a compact board?
- Minimum playable content: route planning/commitment; legal and illegal route feedback; fuel and capacity tracking; cargo recovery and return; one fixed concealed-tile reveal; deterministic end-of-shift scoring; two hand-authored boards.
- Maximum iterations: `5` (sourced fact; simulated user-supplied limit).
- Time limit: one week (sourced fact).
- Spending limit: `$0` (sourced fact).
- Local technology: vanilla HTML, CSS, and JavaScript served or opened locally; technical feasibility pending developer confirmation.
- Excluded work: online play, accounts, analytics, procedural generation, touch-specific optimization, authored narrative, audio production, accessibility certification, multiple vehicle tools, content editor, and public deployment.
- Core gameplay and prototype scope checkpoint: `pending`.
- Explicit approval reference: `none`.

### Tentative Delivery Notes

| Topic | Note | Status |
| --- | --- | --- |
| Technical architecture | One local page with deterministic board data and pure route-evaluation functions is a candidate; developer confirmation required. | tentative |
| Effort estimate | Fits only if presentation is minimal and no unlisted mechanics are added; developer confirmation required. | tentative |

## Draft: System Specification

### Authority

- Project: `Harbor Salvage` (working title; Design Assumption)
- Document language: English
- Design Brief approval: `simulated transcript, 2026-09-30, simulated USER turn`
- Core gameplay and prototype scope approval: `none`
- Status: `draft pending confirmation` (non-authoritative)
- Canonical terminology: this draft’s glossary; no project glossary was consulted or created.

Other documents must refer to these draft rule IDs rather than redefine their semantics. These rules do not become authoritative unless the simulated user explicitly confirms the core gameplay/prototype scope.

### Draft Glossary

- **Board**: a rectangular set of tiles, indexed by integer `x, y` coordinates.
- **Dock**: the sole starting and return tile.
- **Skiff**: the player token; it begins and ends a successful recovery at the dock.
- **Route**: an ordered tile sequence beginning at the skiff’s current tile.
- **Cargo pod**: a collectible target that consumes one capacity slot when secured.
- **Debris**: an impassable tile.
- **Concealed tile**: a tile that is initially not traversable or targetable and can be revealed by rule.
- **Shift**: one board attempt, ending in success, no-legal-action, or player abandonment.

### State and Initial Parameters

| State ID | Meaning | Type or range | Initial value | Observable feedback |
| --- | --- | --- | --- | --- |
| `S-BOARD-001` | Fixed board tile map | 6-by-6 tile matrix | board-selected layout | Tile symbols and coordinate grid |
| `S-POS-001` | Current skiff position | passable board coordinate | dock coordinate | Skiff marker |
| `S-FUEL-001` | Fuel available for the current shift | integer `0..12` | `12` | Fuel counter |
| `S-CAP-001` | Unused cargo capacity | integer `0..2` | `2` | Capacity counter |
| `S-CARGO-001` | Secured cargo-pod IDs | ordered set | empty | Recovered-cargo list and score |
| `S-REVEAL-001` | Whether the board’s fixed concealed tile is revealed | boolean | `false` | Concealed/revealed tile symbol |
| `S-PHASE-001` | Interaction phase | `planning | resolved | terminal` | `planning` | Status text and enabled controls |
| `S-RESULT-001` | Shift result | `none | success | stranded | abandoned` | `none` | End-of-shift summary |

### Rule Catalog

| Rule ID | Trigger or legal input | Preconditions | Ordered state transition | Observable outcome | Edge cases |
| --- | --- | --- | --- | --- | --- |
| `R-INIT-001` | Start a selected board. | `S-PHASE-001` is `terminal` or no shift exists. | 1. Load that board’s fixed map. 2. Set position to dock. 3. Set fuel to 12 and capacity to 2. 4. Empty secured cargo. 5. Set reveal false, result none, phase planning. | Initial board, counters, and docked skiff appear. | Starting while planning is ignored; it cannot erase an active shift. |
| `R-ROUTE-001` | Submit a route. | Phase is planning; route has at least two coordinates; first coordinate equals current skiff position. | 1. Inspect each adjacent coordinate pair. 2. Reject the whole route if any pair is not orthogonally adjacent, any tile is out of bounds, debris, or concealed, or any nonfinal target tile is cargo. 3. Otherwise accept it for resolution. | Accepted route is shown as planned; rejected route shows its first invalid reason. | Repeated coordinates are allowed only when each step remains orthogonally adjacent; this can waste fuel. |
| `R-FUEL-001` | Resolve an accepted route. | Accepted by `R-ROUTE-001`; route step count is no greater than current fuel. | 1. Subtract route step count from fuel. 2. Move position to the route’s final coordinate. 3. Continue with `R-CARGO-001` if final tile contains uncollected cargo; otherwise continue with `R-END-001`. | Committed route replaces planned route; fuel counter and skiff position update. | If step count exceeds fuel, do not mutate state; show insufficient-fuel feedback. |
| `R-CARGO-001` | A resolved route ends on uncollected cargo. | Capacity is at least 1. | 1. Add the cargo ID to secured cargo. 2. Subtract one capacity. 3. Replace final cargo tile with passable water. 4. If reveal is false and the board defines a reveal tile, reveal it and set reveal true. 5. Continue with `R-END-001`. | Cargo becomes secured; capacity changes; fixed tile may become visible. | With zero capacity, cargo is not secured and the route is rejected before `R-FUEL-001`; player remains at prior position with prior fuel. |
| `R-RETURN-001` | Submit a route ending at the dock. | Route is accepted by `R-ROUTE-001`; final coordinate is dock. | Resolve it with `R-FUEL-001`. Then evaluate `R-END-001`. | The skiff returns to dock and may end the shift. | A direct dock-to-dock route has zero steps and is invalid under `R-ROUTE-001` because routes require two coordinates. |
| `R-END-001` | After a successful movement resolution, or when the player selects End Shift. | For movement: `R-FUEL-001` completed. For End Shift: phase is planning. | 1. If player selected End Shift, set result to success only when position is dock and secured cargo is nonempty; otherwise set abandoned. 2. If all board cargo is secured and position is dock, set success. 3. If fuel is zero while position is not dock, set stranded. 4. If result is success, stranded, or abandoned, set phase terminal; otherwise retain planning. | Terminal result screen names result, cargo count, and fuel remaining. | Cargo exhausted away from dock does not end shift; a legal return is still required. |
| `R-INPUT-001` | Any input after phase becomes terminal. | Phase is terminal. | Do not change state except `R-INIT-001` for a new board. | Controls other than restart are disabled. | Repeated click/tap cannot duplicate cargo or score. |

### Content and Feedback

| Content ID | Rule IDs affected | Player-facing purpose | Required art, narrative, or audio cue |
| --- | --- | --- | --- |
| `C-BOARD-001` | `R-INIT-001`, `R-ROUTE-001` | Teach route legality in a compact field. | Distinct high-contrast tile symbols; no audio required. |
| `C-CARGO-001` | `R-CARGO-001`, `R-END-001` | Make capacity and recovery progress clear. | Cargo icon changes to a recovered-list entry on collection. |
| `C-STATUS-001` | `R-ROUTE-001`, `R-FUEL-001`, `R-END-001`, `R-INPUT-001` | Explain immediate consequence of an action. | One-line status text for route rejection, fuel shortage, stranded state, and result. |

### Verification Cases

| Case | Initial state | Inputs in order | Expected rule IDs and final state | Execution status and evidence |
| --- | --- | --- | --- | --- |
| `V-INIT-001` | No active shift. | Start tutorial board. | `R-INIT-001`; position is dock, fuel 12, capacity 2, no cargo, phase planning. | `not run`; expected outcome only; no version, command, observed output, artifact, or log exists. |
| `V-ROUTE-001` | Tutorial board after `V-INIT-001`. | Submit a route that crosses debris. | `R-ROUTE-001`; state is unchanged and feedback identifies debris. | `not run`; expected outcome only; no evidence exists. |
| `V-FUEL-001` | Planning state with fuel 3. | Submit an otherwise legal route with 4 steps. | `R-FUEL-001`; state is unchanged and feedback reports insufficient fuel. | `not run`; expected outcome only; no evidence exists. |
| `V-CARGO-001` | Planning state at dock, capacity 2, fuel sufficient, with a legal route to uncollected cargo. | Submit route ending at cargo. | `R-ROUTE-001`, `R-FUEL-001`, `R-CARGO-001`; fuel falls by route steps, capacity becomes 1, cargo enters secured set, and the fixed reveal tile becomes visible. | `not run`; expected outcome only; no evidence exists. |
| `V-CAP-001` | Planning state with capacity 0 and an adjacent uncollected cargo tile. | Submit legal route ending at cargo. | `R-CARGO-001`; route is rejected before fuel or position changes; feedback reports no capacity. | `not run`; expected outcome only; no evidence exists. |
| `V-RETURN-001` | Planning state away from dock with secured cargo and enough fuel. | Submit legal route ending at dock; select End Shift. | `R-RETURN-001`, `R-FUEL-001`, `R-END-001`; phase terminal, result success, retained cargo listed. | `not run`; expected outcome only; no evidence exists. |
| `V-STRAND-001` | Planning state away from dock with fuel 1 and no legal one-step route to dock. | Submit a legal one-step route away from dock. | `R-FUEL-001`, `R-END-001`; fuel 0, phase terminal, result stranded. | `not run`; expected outcome only; no evidence exists. |
| `V-TERMINAL-001` | Terminal success state. | Submit any route. | `R-INPUT-001`; state is unchanged and only restart remains usable. | `not run`; expected outcome only; no evidence exists. |

Planned cases are specifications, not executed rule-verification evidence. A case can be promoted only after recording actual input or command, observed output, artifact/log path, and version. No such evidence exists in this closed simulation.

### Unvalidated Claims and Handoff Notes

| Item | Classification | Limitation or developer question |
| --- | --- | --- |
| Compact route, fuel, and capacity choices will be satisfying for casual planners. | Design Assumption | Requires Player Validation; rule verification cannot establish enjoyment or balance. |
| One fixed concealed reveal adds useful replanning without frustration. | Design Assumption | Requires Player Validation; evaluate only within the approved five-iteration limit. |
| A 6-by-6 board with 12 fuel and capacity 2 is appropriately balanced. | Design Assumption | Exact board topology and values require implementation-level route analysis and player validation. |
| Vanilla local browser implementation is feasible in one week at `$0`. | Design Assumption | Developer must confirm feasibility; this simulation did not inspect or create implementation. |

## Simulated Workflow Outcome

- The Design Brief checkpoint is simulated as confirmed, with provenance preserved above.
- Gameplay and prototype scope are proposed but `pending`; no approval has been inferred.
- The system rules are a non-authoritative `draft pending confirmation`, as required by the missing checkpoint.
- All verification cases are `not run`, with no fabricated rule-verification, player-validation, command, artifact, version, or log evidence.
