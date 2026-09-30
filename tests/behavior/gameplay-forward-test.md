# Gameplay and System Forward Test

Date: 2026-09-30

## Purpose and Input

This is an independent forward execution of `gameplay-design` followed by `system-design`, using only the constructed facts supplied for the test. It is not a code review and does not grade the work.

Raw constructed project facts:

- A user approved an English Design Brief for a local, single-player browser salvage puzzle for casual planning-game players, handled here as simulated approval reference `B1`.
- Team: one developer familiar with browser JavaScript.
- Time limit: one week.
- Intended experience: readable risk/reward choices in a short run.
- Maximum prototype iterations: 5.
- Spending limit: $0.
- Network use: prohibited.
- Actual request: “Propose the core gameplay and prototype scope, and prepare the draft system rules needed to evaluate it. I have not approved a gameplay proposal yet.”

No further approval was invented. The Design Brief is treated as confirmed by `SIMULATED B1`; the core gameplay and prototype-scope checkpoint remains pending.

## Consulted Files

Only these files were read:

- `agents/game-designer.md`
- `.agents/skills/gameplay-design/SKILL.md`
- `.agents/skills/gameplay-design/templates/gameplay-proposal.md`
- `.agents/skills/system-design/SKILL.md`
- `.agents/skills/system-design/templates/system-specification.md`

No PRD, plan, fixture, or report was read.

## State and Scope

| Item | State |
| --- | --- |
| Document language | English, from simulated Design Brief approval `B1` |
| Design Brief checkpoint | confirmed; explicit reference `SIMULATED B1` |
| Core gameplay and prototype scope checkpoint | pending; no approval reference |
| System specification authority | draft pending confirmation; not authoritative |
| Prototype execution | not started |
| Prototype iteration budget | maximum 5; none used |
| Time budget | one developer-week; no effort estimate asserted |
| Spending budget | $0 |
| Network | prohibited |
| Technology assumption | local vanilla HTML, CSS, and browser JavaScript; pending developer confirmation |

## Draft Artifacts

The working artifacts were produced at:

- `/tmp/game-designer-gameplay-eval/gameplay-proposal.md`
- `/tmp/game-designer-gameplay-eval/system-specification-draft.md`

### Gameplay Proposal Draft

Project: `Wreckline Salvage` (working title). Classification key: sourced fact, Design Assumption, simulated result, rule verification, and Player Validation.

| Item | Proposal | Classification and source | Risk or open question |
| --- | --- | --- | --- |
| Target player | Casual planning-game player using a local single-player browser game. | sourced fact: constructed Design Brief | Accessibility and preferred session length have not received Player Validation. |
| Intended experience | Make understandable risk/reward choices during one short salvage run. | sourced fact: constructed Design Brief | “Readable” and satisfying tension are unvalidated experience claims. |
| Core loop | Inspect three labelled salvage options, compare their shown cargo, power, and hull effects, commit to one, read the updated ship state, then plan the next sector. | Design Assumption | Must show whether players understand the displayed consequences before choosing. |
| Observable outcome | Each choice updates cargo, power, hull, sector progress, and a concise event log; the sixth sector produces a clear extraction success or failure result. | Design Assumption | A six-sector run may be too short or too repetitive. |

The proposed loop is a fixed six-sector wreck run. Each sector displays a dependable low-cost salvage route, a richer route with higher power demand and hull damage, and a recovery/preparation route that restores power or hull at the cost of immediate cargo. The player chooses one route, observes all immediate consequences, and advances. The run ends after the sixth resolution or earlier when the skiff is disabled; extraction requires at least 9 cargo. Detailed behavior is represented by draft rule IDs `R-01` through `R-08` and is not authoritative.

The smallest playable content is one screen with a status strip, six fixed sectors, three choices per sector, visible target, event log, terminal result, and restart. It excludes inventory, procedural generation, dialogue trees, long-term progression, online services, accounts, analytics, asset purchases, save system, localization, audio production, accessibility certification, narrative campaign, and mobile packaging.

| Alternative | Experiential benefit | Trade-off or risk | Low-cost experiment | Decision status |
| --- | --- | --- | --- | --- |
| Fixed six-sector route (baseline) | Makes consequences and player misunderstandings easy to inspect. | May feel solved after one run. | Ask players to narrate why they chose each option and compare chosen consequences to displayed values. | proposed |
| Randomize only the order of pre-authored sectors | Tests replay interest without adding new mechanics. | Makes failures harder to compare and can obscure balance defects. | After baseline feedback, run the same content in two orders and record target success and decision explanations. | pending |
| Add a one-use scan that previews the next sector | Adds a planning horizon. | Introduces a fourth resource and can weaken the short-run clarity goal. | Paper/UI mock: offer scan before sector 3; ask whether it changed the sector-2 choice. | pending |

Gameplay-relevant direction: one-line sector labels establish wreck context; UI uses distinct icons plus text and signed numeric deltas, without color-only danger cues; audio is not required; six pre-authored sector configurations exercise safe, risky, and recovery choices. These are Design Assumptions except the supported omission of audio under the zero-spend/one-week constraint.

Prototype scope submitted for confirmation:

- Validation question: Can a casual planning-game player accurately explain the visible trade-off in each of three options and intentionally plan enough cargo to extract within a six-sector run?
- Minimum playable content: local browser page with one fixed six-sector run, three fully labelled choices per sector, cargo/power/hull state, target display, event log, terminal success/failure, and restart.
- Maximum iterations: 5, supplied fact.
- Time limit: one developer-week, supplied fact.
- Spending limit: $0, supplied fact.
- Network: prohibited, supplied fact.
- Local technology: vanilla HTML, CSS, and browser JavaScript, a Design Assumption pending developer confirmation.
- Checkpoint: pending; explicit approval reference: none.

Tentative delivery notes: a local static page may keep run state in memory and use a fixed data array for sector options; developer confirmation is required. The supplied week is recorded but no implementation estimate is asserted.

### System Specification Draft

Authority: project `Wreckline Salvage`; document language English; Design Brief approval `SIMULATED B1`; core gameplay/prototype approval none; status `draft pending confirmation`; no supplied project glossary. It is evaluable only and not authoritative until the pending checkpoint is approved.

| State ID | Meaning | Type or range | Initial value | Observable feedback |
| --- | --- | --- | --- | --- |
| `S-01` | Run phase | `choice`, `terminal-success`, `terminal-failure` | `choice` | Current sector or result panel |
| `S-02` | Current sector | integer `1..6` | `1` | `Sector n of 6` |
| `S-03` | Cargo | integer `0..unbounded` | `0` | Cargo counter and target `9` |
| `S-04` | Power | integer `0..6` | `6` | Power counter |
| `S-05` | Hull | integer `0..3` | `3` | Hull counter |
| `S-06` | Extraction target | integer | `9` | Target label |
| `S-07` | Resolved sector count | integer `0..6` | `0` | Progress indicator |
| `S-08` | Event log | ordered list of strings | empty | Most recent result at top |

Fixed content uses signed deltas `[cargo, power, hull]`; positive power/hull recovery is capped at 6/3.

| Content ID | Sector | Options `[cargo, power, hull]` |
| --- | --- | --- |
| `C-01` | 1 | `A Quiet Berth [1,-1,0]`; `B Crushed Hold [3,-2,-1]`; `C Cell Rack [0,+2,0]` |
| `C-02` | 2 | `A Cable Run [2,-1,0]`; `B Sealed Vault [4,-3,-1]`; `C Patch Bay [0,-1,+1]` |
| `C-03` | 3 | `A Survey Deck [1,-1,0]`; `B Reactor Room [3,-2,-1]`; `C Capacitor Cache [1,+2,0]` |
| `C-04` | 4 | `A Tool Locker [2,-1,0]`; `B Collapsed Bay [4,-2,-1]`; `C Dry Dock [0,-1,+2]` |
| `C-05` | 5 | `A Crew Quarters [2,-1,0]`; `B Armored Store [3,-2,-1]`; `C Power Relay [0,+2,0]` |
| `C-06` | 6 | `A Escape Cache [1,-1,0]`; `B Command Safe [3,-2,-1]`; `C Stabilizer [0,-1,+1]` |

| Rule ID | Trigger or legal input | Preconditions | Ordered state transition | Observable outcome | Edge cases |
| --- | --- | --- | --- | --- | --- |
| `R-01` | Start or restart | None | Reset phase, sector, cargo, power, hull, progress, and log to initial values; render `C-01`. | Fresh counters and sector-1 choices appear. | Restart replaces prior log. |
| `R-02` | Select displayed current-sector option | `S-01=choice` | Apply cargo, power, and hull deltas; clamp power `0..6` and hull `0..3`; append resulting values to log; increment resolved count. | Card locks; counters and log update together. | Non-current/fabricated option does nothing; capped recovery shows final value. |
| `R-03` | After `R-02` | Power or hull equals `0` | Set phase to terminal failure; do not advance sector. | Failure identifies depleted power or hull; recovered cargo is `0`. | If both are `0`, show both; this rule precedes `R-04`. |
| `R-04` | After `R-02` when `R-03` does not apply | Six sectors resolved | Cargo at least target sets terminal success; otherwise terminal failure. | Extraction result shows cargo and target. | Equality is success; no post-sector-6 action. |
| `R-05` | After `R-02` when `R-03`/`R-04` do not apply | Fewer than six sectors, positive power and hull | Increment sector and render next fixed content. | Next three options appear. | Sector never exceeds 6. |
| `R-06` | Choice click while resolving or terminal | Phase cannot accept a new choice | Ignore input. | No state change. | UI disables/hides unavailable choices. |
| `R-07` | Render available option | Current sector valid | Show name and exact signed cargo/power/hull deltas before input; negative hull also receives non-color warning. | Consequences are comparable. | Zero deltas may be visually omitted but remain zero. |
| `R-08` | Render terminal result | Terminal phase | Show result, final cargo, target, resolved count, and restart. Successful extraction equals cargo; failed extraction is zero. | Outcome is explicit. | Early failure reports fewer than six sectors. |

| Case | Initial state | Inputs in order | Expected rule IDs and final state | Evidence classification |
| --- | --- | --- | --- | --- |
| `V-01` | `R-01` initial state | `C-01 A` | `R-02`, `R-05`; cargo 1, power 5, hull 3, sector 2, phase choice. | rule verification |
| `V-02` | `R-01` initial state | `C-01 C` | `R-02`, `R-05`; cargo 0, capped power 6, hull 3, sector 2. | rule verification |
| `V-03` | `R-01` initial state | `C-01 B`, `C-02 B`, `C-03 B` | Cargo 10, power 0, hull 0; `R-03` terminates before sector 4. | rule verification |
| `V-04` | `R-01` initial state | `C-01 A`, `C-02 A`, `C-03 C`, `C-04 B`, `C-05 B`, `C-06 B` | Cargo 14, power 0, hull 0; `R-03` priority gives failure. | rule verification |
| `V-05` | `R-01` initial state | `C-01 A`, `C-02 A`, `C-03 A`, `C-04 A`, `C-05 A`, `C-06 A` | Cargo 9, power 0, hull 3; failure demonstrates power remains mandatory even at the target. | rule verification |
| `V-06` | Any terminal state | Old option, then restart | `R-06` is inert; `R-01` returns initial state. | rule verification |
| `V-07` | `R-01` initial state | `C-01 B`, `C-02 A`, `C-03 C`, `C-04 B`, `C-05 A`, `C-06 A` | `R-02`, `R-04`; cargo 13, power 1, hull 1, six sectors, terminal success. | rule verification |

Unvalidated claims and handoff notes:

- A six-sector run is short and satisfying: Design Assumption; requires Player Validation.
- Displayed deltas are readable to casual players: Design Assumption; evaluate comprehension, not completion alone.
- Fixed content supports a success route: Design Assumption; `V-07` verifies one deterministic sequence, but does not establish balance.
- Local vanilla browser implementation fits the week: Design Assumption; developer must confirm browser support, launch method, and effort.
- $0 spend, no network, and at most five iterations are sourced constraints.

## Actual Response

Prepared a core gameplay/prototype proposal and an evaluable, non-authoritative system-rule draft at `/tmp/game-designer-gameplay-eval/gameplay-proposal.md` and `/tmp/game-designer-gameplay-eval/system-specification-draft.md`. The Design Brief is recorded as `SIMULATED B1`, while the core gameplay and prototype-scope checkpoint remains pending, so no prototype work or iteration has started. The proposal retains the supplied limits of one developer-week, $0 spending, no network use, and no more than five prototype iterations.

## Limitations

- This execution relies entirely on constructed facts and a simulated Design Brief approval.
- No Player Validation, prototype implementation, implementation test, developer feasibility confirmation, spending, network use, or iteration occurred.
- The system document is intentionally a draft because the required core gameplay/prototype-scope approval was not supplied.
