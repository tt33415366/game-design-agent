# Constructed Design Exercise: Latchline Salvage

This is an authoring-time constructed exercise of `gameplay-design` and `system-design`. Every approval and result below is simulated; it is not a real user decision, player feedback, or implementation evidence. Canonical shared terminology is in `CONTEXT.md`; this document is the sole authoritative source for this fixture's rule semantics.

## Confirmed Input in This Constructed Exercise

| Topic | Value | Classification |
| --- | --- | --- |
| Target players | Desktop players who enjoy short deterministic planning puzzles | simulated user input |
| Core experience | Commit scarce hull integrity for visible salvage value, then escape or fail clearly | simulated user input |
| Platform and team | Local desktop browser prototype by one developer | simulated user input |
| Budget | Local-only, zero spending, two prototype iterations maximum | simulated user input |

## Simulated Checkpoints

| Checkpoint | State | Explicit approval reference | Scope |
| --- | --- | --- | --- |
| Design Brief | confirmed | `SIMULATED USER APPROVAL S1, 2026-09-30: "Approve the English Design Brief for this local browser prototype."` | Fixture only |
| Core gameplay and prototype scope | confirmed | `SIMULATED USER APPROVAL S2, 2026-09-30: "Approve Latchline Salvage, the three-turn local prototype, zero spend, and at most two iterations."` | Fixture only |
| Development Handoff Draft | pending | none | No simulated handoff approval supplied |

## Gameplay Proposal

### Core Loop

The player reads the current wreck section, selects one of its two actions, sees cargo and hull changes immediately, then moves to the next section. The final state is an explicit extraction or loss result. The loop is specified by `R-01` through `R-08` below.

### Alternatives and Experiments

| Alternative | Experiential benefit | Trade-off | Low-cost experiment | Status |
| --- | --- | --- | --- | --- |
| Fixed three-section order | Makes each consequence learnable in one session | Less replay variety | Play the three verification cases in a local browser | selected |
| Random section order | Could create surprise | Obscures whether failure comes from choice or draw order | Defer until deterministic loop is verified | rejected for scope |
| One use rescue token | Could soften failure | Adds a second resource and masks hull planning | Test only after a confirmed scope change | not in scope |

### Prototype Scope

- Validation question: `Can a player identify that retrieving cargo, stabilizing the relay, then retrieving the reactor is the safe winning plan from visible outcomes?`
- Minimum playable content: `One screen, the three sections and actions in R-02 to R-04, current hull/cargo display, action log, and terminal result.`
- Maximum iterations: `2`
- Time limit: `Not estimated; developer confirmation required before committing effort.`
- Spending limit: `$0; local execution only.`
- Tentative technology: `Plain browser UI and local Python-served files are acceptable; developer confirmation required.`
- Excluded: `accounts, network play, payments, procedural generation, AI, physics simulation, inventory, save/load, accessibility localization, final art, music, and player research.`
- Player feedback: `Hull, cargo, action result, next section, and terminal reason must be visible after each action.`

The intended tension is a Design Assumption. The fixture has no Player Validation and makes no balance or fun claim.

## Authoritative System Specification

### Authority

- Project: `Latchline Salvage`
- Document language: `English; simulated confirmation S1`
- Scope approval: `simulated confirmation S2`
- Status: `authoritative for this constructed fixture only`

### State and Initial Parameters

| State ID | Meaning | Type or range | Initial value | Observable feedback |
| --- | --- | --- | --- | --- |
| `S-01` | Current section | `1..3` | `1` | Section name and two action labels |
| `S-02` | Hull integrity | integer `0..4` | `4` | `Hull: n/4` after every action |
| `S-03` | Salvage cargo | integer `0..6` | `0` | `Cargo: n` after every action |
| `S-04` | Run status | `active | extracted | lost` | `active` | Action log and terminal panel |

### Rule Catalog

| Rule ID | Trigger or legal input | Preconditions | Ordered state transition | Observable outcome | Edge cases |
| --- | --- | --- | --- | --- | --- |
| `R-01` | Start run | None | Set `S-01=1`, `S-02=4`, `S-03=0`, `S-04=active`. | Show Cargo Hold actions. | A new run always discards prior state. |
| `R-02` | Cargo Hold: `Retrieve` or `Mark` | `S-04=active`, `S-01=1` | `Retrieve`: add `2` to `S-03`, subtract `1` from `S-02`; `Mark`: no cargo or hull change. Then apply `R-05`. | Log selected action and current totals. | All other inputs are ignored. |
| `R-03` | Relay: `Stabilize` or `Strip` | `S-04=active`, `S-01=2` | `Stabilize`: set `S-02` to `min(4, S-02+1)`; `Strip`: add `1` to `S-03`. Then apply `R-05`. | Log selected action and current totals. | Stabilize at `4` remains `4`; it does not create stored protection. |
| `R-04` | Reactor: `Retrieve` or `Mark` | `S-04=active`, `S-01=3` | `Retrieve`: add `3` to `S-03`, subtract `3` from `S-02`; `Mark`: no cargo or hull change. Then apply `R-05`. | Log selected action and current totals. | All other inputs are ignored. |
| `R-05` | Resolve a section action | An action in `R-02`, `R-03`, or `R-04` changed or retained state | If `S-02<=0`, set `S-02=0`, set `S-04=lost`, and do not advance. Otherwise, if `S-01<3`, add `1` to `S-01`; otherwise apply `R-06`. | On hull loss, show `Hull breach: run lost`; otherwise show next section or terminal result. | Hull loss has priority over extraction, including a reactor action that reaches cargo `5` at hull `0`. |
| `R-06` | Finish a surviving third section | `S-01=3`, `S-02>=1`, `S-04=active` | If `S-03>=5`, set `S-04=extracted`; otherwise set `S-04=lost`. | Show `Extraction successful` or `Cargo target missed: run lost`. | Cargo exactly `5` extracts; cargo below `5` loses. |
| `R-07` | Input after terminal status | `S-04=extracted` or `S-04=lost` | No state changes. | Keep terminal panel visible. | Restart is legal only through `R-01`. |
| `R-08` | Screen refresh while run is active | `S-04=active` | Render `S-01` section, `S-02`, `S-03`, legal actions, and latest action result without changing state. | Current state remains inspectable. | Rendering must not resolve an action or consume a turn. |

### Content and Feedback

| Content ID | Rule IDs affected | Player-facing purpose | Required cue |
| --- | --- | --- | --- |
| `C-01` | `R-02` | Cargo Hold introduces gain for hull cost | Cargo and hull delta in action log |
| `C-02` | `R-03` | Relay makes the recovery choice legible | Hull delta or capped-hull notice |
| `C-03` | `R-04` to `R-06` | Reactor makes final commitment and terminal reason legible | Cargo/hull delta and terminal panel |

### Verification Cases

| Case | Initial state | Inputs in order | Expected rule IDs and final state | Classification |
| --- | --- | --- | --- | --- |
| `V-01` | `R-01` state | `Retrieve`, `Stabilize`, `Retrieve` | `R-02,R-05,R-03,R-05,R-04,R-05,R-06`; `S-02=1`, `S-03=5`, `S-04=extracted` | simulated result |
| `V-02` | `R-01` state | `Retrieve`, `Strip`, `Retrieve` | `R-05` after reactor gives hull `0`; `S-03=6`, `S-04=lost`; `R-06` does not run | simulated result |
| `V-03` | `R-01` state | `Mark`, `Stabilize`, `Mark` | `R-06`; `S-02=4`, `S-03=0`, `S-04=lost` | simulated result |

## Unvalidated and Pending Items

| Item | Classification | Limitation |
| --- | --- | --- |
| Players understand the winning sequence | Design Assumption | Browser rule verification cannot establish comprehension. |
| Fixed order is suitably tense | Design Assumption | Requires Player Validation after a separately confirmed test plan. |
| Browser rendering approach and effort | tentative technical note | Developer confirmation required. |
| Development Handoff Draft | pending checkpoint | No implementation commitment is authorized by this fixture. |
