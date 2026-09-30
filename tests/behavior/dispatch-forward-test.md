# Independent Forward Test: Beacon Charge Extension

## Input Reference

- Fixture input: `tests/scenarios/02-system-extension/input.md`
- Review date and source: `2026-09-30; independent closed fictional forward test of the fixture input`
- Scope: Review the fictional `Beacon Ledger` request to add `Overload` and prepare a Development Handoff Draft.

## Consulted Files

1. `agents/game-designer.md`
2. `.agents/skills/design-review/SKILL.md`
3. `.agents/skills/design-review/templates/design-review.md`
4. `.agents/skills/design-review/templates/development-handoff.md`
5. `tests/scenarios/02-system-extension/input.md`

## Design Review Record

### Authority and Scope

- Project: `Beacon Ledger` (fictional fixture project)
- Review date and source: `2026-09-30; tests/scenarios/02-system-extension/input.md`
- Project record: `tests/scenarios/02-system-extension/input.md`, section `Existing Project Record`
- Design Brief approval: `SIMULATED USER APPROVAL E1, 2026-09-30` (valid only as a fictional fixture approval)
- Core gameplay and prototype scope approval: `SIMULATED USER APPROVAL E2, 2026-09-30` (valid only as a fictional fixture approval)
- Authoritative system specification: `tests/scenarios/02-system-extension/input.md`, section `Existing Authoritative System Specification`; fixture revision supplied by input
- Canonical terminology: the same specification: `Charge`, `Score`, `Gather`, `Release`, and proposed `Overload`
- Requested change or handoff scope: local, zero-spend addition of `Overload`; retain the existing `Gather` and `Release` semantics
- Input classification: `simulated input` and `simulated approval`

### Review Outcome

- Readiness: `ready for confirmation`
- Blocking findings: `F-01`, `F-02`, `F-03`, and `F-04` are resolved by the proposed canonical deltas below, but none is authoritative until the fictional user confirms the Development Handoff Draft.
- Player Validation: `not performed`; no comprehension, fun, balance, accessibility, or feasibility claim is established. Conduct Player Validation after implementation if those claims are needed.
- Development Handoff Draft checkpoint: `pending`; no explicit handoff approval is supplied.

### Consistency and Actionability Checks

| Finding ID | Check | Sources reviewed | Observation | Severity | Required resolution or follow-up | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `F-01` | state/rule/transition | `S-01`, `R-01`, proposed `R-03` | `S-01` has range `0..2` and `R-01` caps `Gather` at `2`; therefore the proposed `R-03` precondition `S-01>=3` is unreachable. | critical | Apply `D-01` and `D-02` so Charge can reach and visibly report `3`. | resolved |
| `F-02` | input/dispatch | `R-02`, proposed `R-03` | `R-02` states that every input other than `Gather` or `Release` is ignored with no state or feedback change. That catch-all would consume `Overload`. | critical | Apply `D-03` to exclude `Overload` from the ignored-input rule. | resolved |
| `F-03` | feedback/edge case | proposed `R-03`, `S-01` | The proposal defines the successful `Overload` feedback and says a below-three attempt retains state, but it provides no visible outcome for the failed accepted action and no `A run is active` precondition. | high | Apply `D-04`: state the active-run precondition and `Need 3 charge` feedback for an insufficient-charge attempt. | resolved |
| `F-04` | prior-input behavior/edge case | `R-02`, requested extension | Raising Charge capacity permits `Release` at Charge `3`. `R-02`'s ordered transition already specifies subtracting `2`, but the newly reachable result must be explicit to preserve actionability. | medium | Apply `D-03`: retain `R-02`'s `S-01>=2` transition and state that Charge `3` becomes Charge `1`, Score increases by `1`, and `Beacon scored` is shown. | resolved |
| `F-05` | evidence | `V-01`, requested extension | `V-01` is planned only. No actual command or observed run exists for either the existing rules or the extension. | medium | Run the proposed verification cases and record command/input, observed output, artifact or log path, and version before claiming rule verification. | open |
| `F-06` | scope/approval | project record, requested extension | The local, zero-spend scope is bounded in the fictional input. The Development Handoff Draft has no approval reference. | high | Obtain an explicit fictional user confirmation of this corrected draft before treating it as authorized for implementation. | open |

### Requested and Corrected Deltas

| Delta ID | Canonical source | Requested or corrected change | Rules/state/feedback affected | Scope effect | Approval needed |
| --- | --- | --- | --- | --- | --- |
| `D-01` | `S-01` in `Existing Authoritative System Specification` | Change `Charge stored in the beacon` range from integer `0..2` to integer `0..3`; change feedback from `Charge: n/2` to `Charge: n/3` after every accepted action. Initial value remains `0`. | `S-01`, charge display | Enables the requested threshold only; remains local and zero-spend. | Development Handoff Draft confirmation pending |
| `D-02` | `R-01` | Replace `If S-01<2, add 1 ... otherwise retain all state` with `If S-01<3, add 1 to S-01; otherwise retain all state.` Replace the full-charge feedback/edge case at `2` with the same behavior at `3`: `Gather` at `3` is an accepted no-op, does not change `S-02`, and shows `Charge full`. | `R-01`, `S-01`, feedback | Retains Gather's increment-or-accepted-no-op pattern while making `Overload` reachable. | Development Handoff Draft confirmation pending |
| `D-03` | `R-02` | Retain the legal input, active-run precondition, and transition `if S-01>=2, subtract 2 from S-01 and add 1 to S-02`. Add the explicit edge case: `Release` at Charge exactly `3` is accepted, ends with Charge `1`, increases Score by `1`, and shows `Beacon scored`. Replace the catch-all with: `Inputs other than Gather, Release, or Overload are ignored with no state or feedback change.` | `R-02`, `S-01`, `S-02`, dispatch | Preserves Release semantics and leaves unknown inputs ignored. | Development Handoff Draft confirmation pending |
| `D-04` | new `R-03` in the authoritative rule catalog | Add: trigger `Overload`; precondition `A run is active`; ordered transition `If S-01>=3, set S-01=0 and add 3 to S-02; otherwise retain all state.` Observable outcome: show `Beacon overloaded` on success or `Need 3 charge` otherwise. Edge cases: Charge exactly `3` scores once; below `3` is an accepted no-op with the insufficient-charge feedback. | new `R-03`, `S-01`, `S-02`, feedback | Adds only the requested local action. | Development Handoff Draft confirmation pending |
| `D-05` | verification-case table in the authoritative specification | Retain `V-01`; add planned cases: `V-02`: initial `0,0`, inputs `Gather, Gather, Gather, Overload`, expected `0,3`; `V-03`: initial `0,0`, inputs `Gather, Gather, Gather, Release`, expected `1,1`; `V-04`: initial `0,0`, input `Overload`, expected unchanged `0,0` and `Need 3 charge`; `V-05`: initial `0,0`, input `Unknown`, expected unchanged state and no feedback. | `R-01` through `R-03`, unknown-input behavior | Verification only; no prototype, spend, or deployment added. | Development Handoff Draft confirmation pending |

### Evidence and Risks

| Item | Classification | Actual command or input | Observed output or observation | Artifact/log path and version | Limitation or follow-up |
| --- | --- | --- | --- | --- | --- |
| Fixture approvals E1 and E2 | simulated approval | Approval strings in the fixture input | The fixture marks the Design Brief and core/prototype scope confirmed. | `tests/scenarios/02-system-extension/input.md`; fixture revision unspecified | Valid only for this fictional forward test. They are not actual user decisions and create no real-project approval. |
| Existing verification `V-01` | not run / expected outcome | `Gather, Gather, Release` listed in fixture | Expected final state is Charge `0`, Score `1`; no observed run is supplied. | `tests/scenarios/02-system-extension/input.md`; no version or execution artifact | Must not be treated as rule-verification evidence. |
| Proposed `V-02` through `V-05` | not run / expected outcome | Inputs specified by `D-05` | Expected outcomes are stated in `D-05`; no implementation was run. | This review record; no executable version or log | Run after implementation and record actual evidence. |
| Player experience | Player Validation | None | No player observation or feedback is supplied. | None | Fun, balance, comprehension, accessibility, and feasibility remain unvalidated. |

### Open Decisions and Handoff Boundary

| Item | Owner | Needed before implementation or release | Status |
| --- | --- | --- | --- |
| Confirm the corrected Development Handoff Draft as the fictional project's canonical extension. | user | Implementation authorization; without it, `D-01` through `D-05` remain proposed only. | open |
| Run and record `V-01` through `V-05` against an implementation. | developer | Rule-verification evidence before asserting rules function as specified. | open |
| Obtain Player Validation if experience claims or release confidence depend on it. | designer | Evidence for player-facing claims; not required to maintain this qualified draft. | open |

## Development Handoff Draft

### Authority

- Project: `Beacon Ledger` (fictional fixture project)
- Project record: `tests/scenarios/02-system-extension/input.md`, section `Existing Project Record`
- Design Brief approval: `SIMULATED USER APPROVAL E1, 2026-09-30` (fixture-only)
- Core gameplay and prototype scope approval: `SIMULATED USER APPROVAL E2, 2026-09-30` (fixture-only)
- Review record: `.superpowers/sdd/2026-09-30-game-designer/dispatch-forward-test.md`
- Authoritative rule source: `tests/scenarios/02-system-extension/input.md`, `S-01`, `R-01`, `R-02`; proposed `R-03`
- Status: `draft pending confirmation`
- Development Handoff Draft approval: none

### Implementation Boundary

| Included item | Authoritative rule/state/feedback IDs | Required behavior and observable outcome | Edge cases | Excluded work |
| --- | --- | --- | --- | --- |
| Expand Charge capacity and display | `S-01`, `D-01` | Store Charge as integer `0..3`; start at `0`; after each accepted action display `Charge: n/3`. | State must never leave `0..3`. | Changes to Score range, persistence, UI redesign, or economy. |
| Update Gather | `R-01`, `D-02` | With an active run, Gather adds one Charge below `3`; at `3`, retain state and show `Charge full`. | The full-charge action remains accepted and does not change Score. | Alternate gather rates or resource types. |
| Preserve and clarify Release | `R-02`, `D-03` | With an active run and Charge at least `2`, subtract `2`, add `1` Score, and show `Beacon scored`; otherwise retain state and show `Need 2 charge`. | At Charge `3`, finish at Charge `1` and Score increases once. Unknown inputs excluding the three named actions remain ignored with no feedback. | Changes to Release cost, reward, or low-charge outcome. |
| Add Overload | proposed `R-03`, `D-04` | With an active run and Charge at least `3`, set Charge to `0`, add `3` Score, and show `Beacon overloaded`; below `3`, retain state and show `Need 3 charge`. | Charge exactly `3` succeeds once; below `3` is an accepted no-op. | Additional actions, effects, spending, remote services, or deployment. |
| Add verification coverage | `D-05` | Execute and record `V-01` through `V-05` with their specified inputs and expected outcomes. | Evidence must include actual input/command, observed output, artifact/log path, and version. | Player research or claims derived from developer tests. |

### Developer Questions and Dependencies

| Item | Owner | Effect if unresolved | Status |
| --- | --- | --- | --- |
| Explicit confirmation of this corrected fictional handoff draft. | user | The proposed deltas cannot become authoritative or authorize implementation. | open |
| Implementation target/version and execution log location for `V-01` through `V-05`. | developer | Verification remains planned only. | open |

### Verification and Qualifications

| Check or claim | Status | Evidence or required next step | Limitation |
| --- | --- | --- | --- |
| Existing `V-01` | not run / expected outcome | Execute `Gather, Gather, Release`; expect Charge `0`, Score `1`. | No actual run, version, or artifact is provided. |
| Overload success `V-02` | not run / expected outcome | Execute `Gather, Gather, Gather, Overload`; expect Charge `0`, Score `3`, and success feedback. | No implementation has been run. |
| Release from three `V-03` | not run / expected outcome | Execute `Gather, Gather, Gather, Release`; expect Charge `1`, Score `1`, and success feedback. | No implementation has been run. |
| Overload insufficiency `V-04` | not run / expected outcome | Execute `Overload` at Charge `0`; expect unchanged state and `Need 3 charge`. | No implementation has been run. |
| Unknown input `V-05` | not run / expected outcome | Execute an unknown input; expect unchanged state and no feedback. | No implementation has been run. |
| Player experience | Player Validation | Conduct player sessions if claims about comprehension, fun, balance, accessibility, or feasibility are needed. | No Player Validation is supplied; this does not itself block the pending draft. |

## Provenance and Limitations

- This record was derived solely from the five files listed in `Consulted Files`; the expected review, PRD, plans, implementation reports, and past-behavior tests were intentionally not read.
- The fixture's approvals and project facts are simulated inputs. They were honored only to evaluate the fictional `Beacon Ledger` scenario and do not approve, alter, or authorize any real repository project.
- This review proposes exact canonical deltas but does not apply them to the fixture's authoritative specification. Until an explicit fictional user approval is recorded, the handoff checkpoint remains pending.
- No source code, prototype, test command, external system, or Player Validation was used. All verification cases remain `not run / expected outcome`.
