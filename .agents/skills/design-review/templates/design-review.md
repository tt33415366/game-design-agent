# Design Review Record

## Authority and Scope

- Project: `<name>`
- Review date and source: `<date and request/reference>`
- Project record: `<path>`
- Design Brief approval: `<reference>`
- Core gameplay and prototype scope approval: `<reference>`
- Authoritative system specification: `<path and revision>`
- Canonical terminology: `<path or pending>`
- Requested change or handoff scope: `<scope>`
- Input classification: `sourced fact | Design Assumption | simulated input | simulated approval`

## Review Outcome

- Readiness: `blocked | qualified handoff draft | ready for confirmation`
- Blocking findings: `<none or IDs>`
- Player Validation: `available | not performed | not applicable`; `<qualification and follow-up>`
- Development Handoff Draft checkpoint: `pending | confirmed`; `<explicit approval reference or none>`

## Consistency and Actionability Checks

| Finding ID | Check | Sources reviewed | Observation | Severity | Required resolution or follow-up | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `F-<id>` | `state/rule/input/transition/feedback/edge case/scope/approval/evidence/dependency` | `<rule IDs and paths>` | `<consistent fact or contradiction>` | `critical | high | medium | low` | `<exact delta, decision, or owner>` | `open | resolved | accepted risk` |

Critical contradictions or unimplementable requirements keep readiness `blocked`. A resolved finding records the exact canonical update; it does not make an unapproved change authoritative.

## Requested and Corrected Deltas

| Delta ID | Canonical source | Requested or corrected change | Rules/state/feedback affected | Scope effect | Approval needed |
| --- | --- | --- | --- | --- | --- |
| `D-<id>` | `<path and rule IDs>` | `<exact change>` | `<IDs>` | `<included/excluded impact>` | `<reference or pending>` |

## Evidence and Risks

| Item | Classification | Actual command or input | Observed output or observation | Artifact/log path and version | Limitation or follow-up |
| --- | --- | --- | --- | --- | --- |
| `<item>` | `rule verification | developer observation | simulated result | Player Validation | not run / expected outcome` | `<actual command/input>` | `<observed output>` | `<path/version>` | `<limitation>` |

Planned cases remain `not run / expected outcome` until an actual command or input, observed output, artifact or log path, and version are recorded. Player experience claims require Player Validation.

## Open Decisions and Handoff Boundary

| Item | Owner | Needed before implementation or release | Status |
| --- | --- | --- | --- |
| `<decision/question>` | `user | developer | designer` | `<why>` | `open | resolved` |

Use the Development Handoff Draft template for the proposed implementation boundary. Its checkpoint remains pending without an explicit user confirmation.
