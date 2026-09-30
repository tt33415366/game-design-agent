# Constructed Input: Beacon Charge Extension

This is raw constructed input for an existing-system extension. It is intentionally separate from the expected review output in `expected-review.md`; a controller can provide this file alone for an independent forward test. The project facts and approvals below are simulated inputs, not actual user decisions, implementation evidence, or Player Validation.

## Existing Project Record

- Project: `Beacon Ledger`
- Document language: `English`
- Current stage: `handoff`
- Authoritative system rules: this file, `Existing Authoritative System Specification`
- Canonical terminology: `Charge`, `Score`, `Gather`, `Release`, and `Overload` are defined only below.

| Checkpoint | State | Explicit approval reference | Notes |
| --- | --- | --- | --- |
| Design Brief | confirmed | `SIMULATED USER APPROVAL E1, 2026-09-30: "Approve the English Beacon Ledger Design Brief."` | Fixture only. |
| Core gameplay and prototype scope | confirmed | `SIMULATED USER APPROVAL E2, 2026-09-30: "Approve the existing two-action Beacon Ledger system and local zero-spend scope."` | Fixture only. |
| Development Handoff Draft | pending | none | No simulated handoff approval has been supplied. |

## Existing Authoritative System Specification

### State and Initial Parameters

| State ID | Meaning | Type or range | Initial value | Observable feedback |
| --- | --- | --- | --- | --- |
| `S-01` | Charge stored in the beacon | integer `0..2` | `0` | `Charge: n/2` after every accepted action |
| `S-02` | Completed beacon score | integer `0..unbounded` | `0` | `Score: n` after every accepted action |

### Rule Catalog

| Rule ID | Trigger or legal input | Preconditions | Ordered state transition | Observable outcome | Edge cases |
| --- | --- | --- | --- | --- | --- |
| `R-01` | `Gather` | A run is active | If `S-01<2`, add `1` to `S-01`; otherwise retain all state. | Show the new charge, or `Charge full` at `2`. | `Gather` at `2` is an accepted no-op; it does not change `S-02`. |
| `R-02` | `Release` | A run is active | If `S-01>=2`, subtract `2` from `S-01` and add `1` to `S-02`; otherwise retain all state. | Show `Beacon scored` on success, or `Need 2 charge` otherwise. | Charge exactly `2` scores once. Inputs other than `Gather` or `Release` are ignored with no state or feedback change. |

### Existing Verification Case

| Case | Initial state | Inputs in order | Expected final state | Execution status and evidence |
| --- | --- | --- | --- | --- |
| `V-01` | `S-01=0`, `S-02=0` | `Gather`, `Gather`, `Release` | `S-01=0`, `S-02=1` | `not run / expected outcome` |

## Requested Extension

The simulated requester asks: "Add an `Overload` action. It should require three Charge, reset Charge to zero, and add three Score. Keep Gather and Release behaving as they do today. The addition stays local and zero-spend. Please prepare it for a Development Handoff Draft."

## Contradictory Proposed Draft

The submitted draft adds this row and changes nothing else:

| Rule ID | Trigger or legal input | Preconditions | Ordered state transition | Observable outcome | Edge cases |
| --- | --- | --- | --- | --- | --- |
| `R-03` | `Overload` | `S-01>=3` | Set `S-01=0`; add `3` to `S-02`. | Show `Beacon overloaded`. | `Overload` below `3` retains all state. |

The draft does not modify `S-01` or `R-01`.
