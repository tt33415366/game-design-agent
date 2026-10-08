# Tidal Garden: Gameplay Proposal

Date: 2026-10-08. Brief: [brief.md](brief.md), confirmed 2026-10-08. Structure under test: build-then-traverse (B). All experience claims are Design Assumptions; no Player Validation exists for this structure.

## Experience Candidates

| Candidate | Hook | Player action | Primary creative priority | Intentional sacrifice | Largest uncertainty | Decision status |
| --- | --- | --- | --- | --- | --- | --- |
| A. Three Stones | At low tide, exactly three movable stones sit in a tide-flat maze. Open one channel by dragging each stone, then the tide rises and you swim the route you made to reach a stranded tide pool. | Drag stones (calm), swim the authored-by-you route (tide) | Player-authored path with minimal verbs | Only three moves; little replay within one cycle | Is "I made this path" satisfying when there are so few choices? | proposed |
| B. Current Sculptor | The tide flows; you place driftwood barriers to steer the current so it carries you (or a seed pod) to a target eddy. Calm phase is placement; action phase is riding the flow you created. | Place barriers, then ride/observe the outcome | Indirect authorship — you shape forces, not paths | No direct swimming control in action phase; you watch your design run | Is watching your design succeed engaging, or does it feel passive? | proposed |
| C. Shared Garden | The flat is a grid of tide gates you open or close before the tide; the action phase is a slow flood, and you rescue stranded creatures along routes your gate pattern made reachable. | Toggle gates (calm), swim rescue routes (tide) | Consequence reading — your pattern decides what is reachable | More systemic, less spatial; risk of puzzle-y "find the one pattern" | Does it become an optimization puzzle instead of personal expression? | proposed |

These are materially different: A is direct path authorship with three moves, B is indirect force-steering with a passive action phase, C is pattern-to-consequence with rescue stakes. B and C are not cosmetic variants of A.

## Recommendation

**A — Three Stones.** Rationale: it isolates B's core question most cheaply. If three meaningful moves produce "I made this" satisfaction, the structure holds and can be enriched later. B's passive action phase risks the very boredom the user punished in valley v1 (watching is not arriving), and C risks sliding into an optimization puzzle, which conflicts with the user's dislike of obvious sequences and grinding. A also reuses the proven swim from Sunlight Shelf for the action phase, so the only new mechanic under test is the calm-phase drag — the smallest honest test of build-then-traverse.

## Core Experience and Mechanic Proposal (recommended candidate only, provisional until selected)

| Item | Proposal | Classification | Risk / open question |
| --- | --- | --- | --- |
| Target player | User as first evaluator | sourced fact | Does not generalize |
| Intended experience | Calm, unhurried shaping, then the quiet pleasure of swimming a route that exists because you made it | Design Assumption | "Few moves" may read as "no agency" |
| Core loop | Survey the flat → drag each stone to open a channel → the tide rises → swim the route you opened to the stranded pool → reflect on whether the route felt yours | Design Assumption | **Return pull: single cycle, one payoff. Sustained interest rests entirely on whether self-authored routes feel meaningfully different. If swimming your own route feels the same as swimming any route, the structure fails honestly. Stated per F6.** |
| Observable outcome | The tide floods along the channel pattern the player opened; the pool is reachable only through a route the player created | Design Assumption | Must not read as "the one correct solution" |

## Prototype Scope and Checkpoint (pending)

- Validation question (F6): initial attraction — does the user engage the stones unprompted and understand the drag; sustained interest / structure test — during the swim, does the user recognize and value that the route is self-made (reported after unassisted play), and would they do a second cycle differently?
- Minimum playable content: one tide-flat map with a default-blocked channel network, exactly three draggable stones, a rising-tide transition (soft timer), swim phase to a stranded pool, restart.
- Maximum iterations: propose 1. Time limit: propose 2 hours. Spending: zero. (Conservative; user supplied no budget.)
- Excluded: multiple cycles, persistent gardens, build menus, fail states, enemies, checklist UI, touch controls.
- Checkpoint: `pending` — user selects candidate and confirms scope+budget before system-design or implementation.
