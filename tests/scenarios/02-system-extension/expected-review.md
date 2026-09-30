# Constructed Expected Review: Beacon Charge Extension

This is an authoring-time constructed exercise of `design-review`, not a controller-run evaluation. It consumes only the raw fixture in `input.md`. All approvals and review results are simulated; no implementation, rule execution, developer feasibility confirmation, or Player Validation occurred.

## Authority and Scope

- Project: `Beacon Ledger`
- Project record and authoritative rules: `tests/scenarios/02-system-extension/input.md`
- Design Brief approval: `SIMULATED USER APPROVAL E1, 2026-09-30`
- Core gameplay and prototype scope approval: `SIMULATED USER APPROVAL E2, 2026-09-30`
- Requested change: add local, zero-spend `Overload` while preserving `Gather` and `Release`
- Input classification: `simulated input` and `simulated approval`

## Review Outcome

- Initial contradictory draft readiness: `blocked`
- Corrected draft readiness: `qualified handoff draft`
- Development Handoff Draft checkpoint: `pending`; no simulated handoff approval is supplied.
- Player Validation: `not performed`. This qualifies the handoff: player comprehension, fun, balance, and accessibility remain unestablished. It does not block the corrected, bounded handoff draft.

## Observed Constructed Checks

| Finding ID | Check | Sources reviewed | Observation | Severity | Required resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `F-01` | state range | `S-01`, contradictory `R-03` | `R-03` requires charge `3`, but `S-01` permits only `0..2`; the precondition cannot be represented. | critical | Change `S-01` to integer `0..3` and update its feedback capacity. | resolved by `D-01` |
| `F-02` | legal transition | `R-01`, contradictory `R-03` | `R-01` retains state at charge `2`, so no legal input reaches the `R-03` precondition. | critical | Change `R-01` to add charge while `S-01<3`, with full feedback at `3`. | resolved by `D-02` |
| `F-03` | preservation and scope | `R-02`, request, corrected draft | `Release` must retain its threshold, transition, and visible outcomes; the extension adds one action only. | high | State that `R-02` is unchanged and exclude scoring, UI, network, and persistence redesign. | resolved by `D-03` |
| `F-04` | evidence and player claim | `V-01`, requested extension | Existing and new verification cases are planned only. No Player Validation is available. | medium | Retain `not run / expected outcome`; obtain a separately approved player test before claims about comprehension, fun, balance, or accessibility. | open qualification |

The critical contradictions make the submitted draft unimplementable. The corrected deltas below are the only proposed canonical changes; until a user confirms the handoff, they are a draft rather than an authoritative replacement for the raw fixture rules.

## Corrected Draft Deltas

| Delta ID | Canonical source | Corrected change | Rules/state/feedback affected | Scope effect |
| --- | --- | --- | --- | --- |
| `D-01` | `S-01` | Change range to integer `0..3`; show `Charge: n/3`. | `S-01`, `R-01`, `R-03` feedback | Supports the new reachable threshold only. |
| `D-02` | `R-01` | If `S-01<3`, add `1`; otherwise retain all state. Show `Charge full` at `3`. | `R-01` | Preserves Gather as an accepted no-op only at the new full capacity. |
| `D-03` | `R-02`, new `R-03` | Keep `R-02` unchanged. Add `R-03`: `Overload` is legal in an active run; when `S-01>=3`, set `S-01=0`, add `3` to `S-02`, and show `Beacon overloaded`; below `3`, retain all state and show `Need 3 charge`. Other inputs remain ignored as specified by `R-02`. | `R-02`, `R-03` | Adds one local action; excludes network, saving, art, economy rebalance, and any change to Release. |

## Corrected Verification Cases

| Case | Initial state | Inputs in order | Expected rule IDs and final state | Status |
| --- | --- | --- | --- | --- |
| `V-01` | `S-01=0`, `S-02=0` | `Gather`, `Gather`, `Release` | `R-01`, `R-01`, `R-02`; `S-01=0`, `S-02=1` | `not run / expected outcome` |
| `V-02` | `S-01=0`, `S-02=0` | `Gather`, `Gather`, `Gather`, `Overload` | `R-01`, `R-01`, `R-01`, `R-03`; `S-01=0`, `S-02=3` | `not run / expected outcome` |
| `V-03` | `S-01=0`, `S-02=0` | `Gather`, `Overload` | `R-01`, `R-03`; `S-01=1`, `S-02=0`; show `Need 3 charge` | `not run / expected outcome` |
| `V-04` | `S-01=3`, `S-02=0` | `Gather` | `R-01`; state unchanged; show `Charge full` | `not run / expected outcome` |

## Evidence and Remaining Risk

| Item | Classification | Actual input or observation | Observed output | Artifact/version | Limitation |
| --- | --- | --- | --- | --- | --- |
| Contradictory-draft review | simulated result | Constructed comparison of `S-01`, `R-01`, and proposed `R-03` in `input.md` | `F-01` and `F-02` block readiness | This document, constructed fixture | Not an executed implementation check. |
| Corrected-draft review | simulated result | Constructed delta comparison above | Critical state and reachability contradictions resolved | This document, constructed fixture | Developer feasibility is not confirmed. |
| Verification cases | not run / expected outcome | `V-01` through `V-04` | No observed runtime output | none | Planned outcomes are not rule-verification evidence. |
| Player experience | Player Validation | none | Not performed | none | No comprehension, fun, balance, or accessibility claim is supported. |

## Development Handoff Draft

### Authority

- Status: `draft pending confirmation`
- Development Handoff Draft approval: `none`
- Canonical source after approval: the `S-01`, `R-01`, and `R-03` deltas above; `R-02` remains the existing canonical rule.

| Included item | Authoritative IDs | Required behavior and observable outcome | Edge cases | Excluded work |
| --- | --- | --- | --- | --- |
| Charge capacity and Gather update | `S-01`, `R-01` | Store `0..3` Charge; show `/3`; Gather fills through `3` and reports full there. | Gather at `3` leaves state unchanged. | Change to Release, persistence, network, economy rebalance. |
| Overload action | `R-03` | At Charge `3`, reset Charge to `0`, add `3` Score, and show overload result. | Below `3`, retain state and show `Need 3 charge`; unrelated inputs remain ignored. | New currencies, art, sound, accounts, save/load. |

| Open item | Owner | Effect if unresolved | Status |
| --- | --- | --- | --- |
| Confirm this Development Handoff Draft and the exact canonical deltas. | user | No implementation authorization. | open |
| Confirm implementation feasibility and test harness location. | developer | Scope estimate and executable evidence remain unknown. | open |
| Run `V-01` through `V-04` against an implementation after confirmation. | developer | Rule behavior remains unverified. | open |
| Run a separately approved player test before experience claims. | user/designer | Comprehension, fun, balance, and accessibility remain unvalidated. | open |
