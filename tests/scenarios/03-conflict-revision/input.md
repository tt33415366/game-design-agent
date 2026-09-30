# Constructed Input: Tideglass Salvage Revision

This is raw constructed input for a conflicting revision. It deliberately contains no prepared impact analysis, approval outcome, revised rule, or re-review. A fresh evaluator can use this file alone. All facts, approvals, and the injected result are simulated fixture inputs, not real-project evidence, Player Validation, or implementation output.

## Baseline Project Record

- Project: `Tideglass Salvage`
- Current stage: `handoff`
- Active authoritative rules: this file, `Active System Specification v1.0`
- Confirmed local prototype envelope: one local, zero-spend balance adjustment to the `R-02` recovery value only, range `1..2`; no core-loop, scope, cost, or handoff change.

| Checkpoint | State | Explicit approval reference |
| --- | --- | --- |
| Design Brief | confirmed | `SIMULATED USER APPROVAL T1, 2026-09-30: "Approve the Tideglass Salvage Design Brief."` |
| Core gameplay and prototype scope | confirmed | `SIMULATED USER APPROVAL T2, 2026-09-30: "Approve one local zero-spend prototype with the recover-or-anchor loop, two iterations, and recovery tuning only from 1 to 2."` |
| Development Handoff Draft | confirmed | `SIMULATED USER APPROVAL T3, 2026-09-30: "Approve the v1.0 handoff for the local two-action prototype."` |

## Active System Specification v1.0

| Rule ID | Trigger | Preconditions | Ordered transition | Observable outcome | Edge case |
| --- | --- | --- | --- | --- | --- |
| `R-01` | Start a dive | None | Set `Hull=2`, `Cargo=0`, `Status=active`. | Show `Hull 2`, `Cargo 0`. | Start resets prior dive state. |
| `R-02` | `Recover` at a wreck | `Status=active` | Add `1` Cargo; subtract `1` Hull; then resolve `R-04`. | Show cargo and hull deltas. | No other input changes state. |
| `R-03` | `Anchor` at a wreck | `Status=active` | Add `1` Hull, capped at `2`; then resolve `R-04`. | Show hull delta or cap. | No other input changes state. |
| `R-04` | Resolve action | An `R-02` or `R-03` action completed | If `Hull=0`, set `Status=lost`; otherwise remain active. | Show `Dive lost` on hull loss. | Loss has priority over later choices. |

## Historical Prototype Evidence v1.0

| Input or command | Observed output | Artifact/version | Classification |
| --- | --- | --- | --- |
| `SIMULATED INJECTED FAILURE F1: Recover, Recover` | `Hull=0`, `Cargo=2`, `Status=lost`; the fixture author injects the conclusion that the second Recover route is too punishing. | `constructed fixture / v1.0` | injected simulated result, not observed real player feedback |
| `SIMULATED RULE CHECK C1: Anchor, Recover` | `Hull=2`, `Cargo=1`, `Status=active`. | `constructed fixture / v1.0` | simulated result |

## Conflicting Change Request

The simulated requester says: "Make `Recover` grant 3 Cargo so players always choose it. Also add a paid sonar scan and update the approved handoff now. The injected failure proves real players dislike the current route."
