# Change Impact Record

## Authority and Request

- Project and current record: `<path>`
- Request source and classification: `<sourced fact | Design Assumption | simulated input | injected failure>`
- Active authoritative documents and versions: `<path, rule IDs, versions>`
- Confirmed scope/budget envelope: `<approval reference and explicit bounds>`
- Current checkpoints and approvals: `<list>`
- Change decision: `pending | approved | rejected`
- Explicit user approval reference: `<none until recorded>`

## Proposed Delta, Kept Separate from Active Rules

| Delta ID | Requested change | Current active source | Conflict or fit | Decision needed | Status |
| --- | --- | --- | --- | --- | --- |
| `D-<id>` | `<proposal>` | `<path, rule ID, version>` | `<scope/rule/evidence/cost impact>` | `<user decision or none>` | `proposed only | approved for synchronization | rejected` |

No row above changes the active authoritative rules while the decision is pending.

## Impact Analysis

| Impact ID | Affected rule, scope, evidence, or checkpoint | Effect | In-scope tuning envelope? | Required action | Status |
| --- | --- | --- | --- | --- | --- |
| `I-<id>` | `<item>` | `<effect>` | `yes with approval reference | no` | `<approval, invalidation, or no action>` | `pending | resolved` |

Core experience, project scope, or material-cost changes require explicit user confirmation. A local tune is allowed only when a recorded approval explicitly covers the parameter and its envelope.

When feedback rejects an experience premise, retain it in the ledger and propose replacement framing through the applicable intake/change route before any expansion.

## Invalidation Ledger

| Item | Prior version and status | Affected by delta | Required status after approval | Historical evidence retained | Replacement required |
| --- | --- | --- | --- | --- | --- |
| `<rule/test/evidence/checkpoint>` | `<version/status>` | `<D-id>` | `invalidated by <version> | remains confirmed` | `<input/output/artifact path>` | `<new case/re-review/none>` |

## Pending Decision and Boundary

| Decision or question | Owner | Needed before | Status |
| --- | --- | --- | --- |
| `<item>` | `user | developer | designer` | `<synchronization, implementation, or release>` | `open | resolved` |

The handoff remains pending unless a separate explicit user confirmation approves it. This record cannot self-approve a change or handoff.
