# Prototype Evidence Log

## Context

- Project record: `<path>`
- Rules checked: `<rule IDs>`
- Authorization and budget reference: `<reference>`
- Scope/spending decision: `<within scope; amount>`

## Iteration Accounting

| Iteration | Change or check | Evidence | Result | Budget remaining |
| --- | --- | --- | --- | --- |
| `1` | `<work>` | `<path/command>` | `<result>` | `<value>` |

## Actual Evidence

| Date | Input or command | Observed output | Artifact/log path and version | Classification | Evidence kind and limitation or negative result |
| --- | --- | --- | --- | --- |
| `<YYYY-MM-DD>` | `<command/input>` | `<output>` | `<path and revision/version>` | `rule verification | developer observation | simulated result | Player Validation` | `rule correctness | unassisted observation | assisted understanding | desirability; <limitation>` |

## Evidence Strength

| Result status | Required record |
| --- | --- |
| `direct result` | `<approved success signal actually observed>` |
| `relative improvement only` | `<baseline, observed improvement, and still-unproven success signal>` |
| `unavailable` | `<failed or unavailable capability and resulting limitation>` |

## Verification Independence

| Intended independent check | Availability or delegation result | Self-validation actually performed | Deferred independent recheck |
| --- | --- | --- | --- |
| `<review, implementation, or test>` | `<available, failed delegation, or unavailable capability>` | `<narrow scope, or none>` | `<owner and required follow-up>` |

Self-validation must never be recorded as independent verification.

## Outstanding Validation

- `<unvalidated player-experience claim and required follow-up>`
- `<unavailable tooling or failed check retained without reinterpretation>`
