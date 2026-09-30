# Change Impact Record: Arrival Payoff + Richer Space (Candidate A revision)

Date: 2026-09-30. Request source: user's selection "到达回报 / 更丰富的空间" from the three hypotheses recorded in validation.md U4. Classification: sourced fact (user direction), all experience claims below are Design Assumptions. Change decision: **pending** — this record proposes; nothing below changes active rules until the user confirms the revised core-gameplay/prototype-scope checkpoint.

## Authority and Request

- Project record: [brief.md](brief.md) — stage: Player Validation complete, direction stopped as-is.
- Active authoritative documents: [system.md](system.md) v1.1 (R01-R07); [validation.md](validation.md) (U3/U4).
- Confirmed envelope now exhausted: U2 approved 3h, zero spend, 2 iterations; both iterations used (ledger in validation.md).
- Checkpoints: Design Brief confirmed (U1); core gameplay/prototype scope confirmed for the stopped version (U2); handoff pending and moot.

## Proposed Delta, Kept Separate from Active Rules

| Delta ID | Requested change | Current active source | Conflict or fit | Decision needed | Status |
| --- | --- | --- | --- | --- | --- |
| D-1 | Arrival payoff: reaching a landmark reveals something (a short scene, a view change, a found detail) rather than only a place name | system.md R06 (feedback must not award/open modal/assign destination) | R06's restraint conflicts; payoff is a bounded event, not a quest system | Confirm revised R06 semantics | proposed only |
| D-2 | Richer space: traversal itself carries interest (varied terrain pacing, 1-2 micro-interactions such as pushing a log or startling birds) | system.md scope: movement + collision + camera only | Expands the verb set beyond U2's approved slice | Confirm expanded scope | proposed only |
| D-3 | Keep: small authored valley, no checklist/score/inventory, no prescribed order, keyboard browser, local assets | brief.md selected direction | Unaffected; both deltas preserve it | none | proposed only |

## Impact Analysis

| Impact ID | Affected item | Effect | Tuning envelope? | Required action | Status |
| --- | --- | --- | --- | --- | --- |
| I-1 | R06 (place feedback) | Revised to permit arrival reveal events while still forbidding score/modal/assigned destination | no — rule semantics change | Rewrite R06 atomically after approval; old wording to change history | pending |
| I-2 | Prototype scope | Verbs grow from move-only to move + 1-2 micro-interactions | no — core scope change | Revised gameplay proposal + new combined checkpoint | pending |
| I-3 | Budget | U2 envelope exhausted; new iteration/time budget required | no | User supplies or confirms a proposed conservative limit | pending |
| I-4 | Evidence U1-U4, all rule/browser verification | Historical; the stopped version's verification does not transfer to revised rules | n/a | Retain as historical evidence; new rules get new `not run` cases | pending |

## Recommendation (Design Assumption, unvalidated)

Combine D-1 and D-2 in one revised slice rather than testing them separately: U4 showed the loop dies at arrival, and arrival payoff without interesting traversal still leaves a walk-simulator gap. Smallest experiment: keep the same valley map, add one payoff per landmark (tower interior reveal, stream-crossing scene, grove detail) and exactly one micro-interaction (pushable log bridging a ditch, or startled birds marking a hidden nook). Validation question per F6: initial attraction (does the user investigate unprompted) and sustained interest (does the user seek the remaining landmarks after the first payoff).

## Pending Decision and Boundary

| Decision | Owner | Needed before | Status |
| --- | --- | --- | --- |
| Confirm revised core gameplay + prototype scope (D-1 + D-2 + D-3), new iteration/time budget | user | any implementation | open |
| Revised gameplay proposal via gameplay-design | designer | system-design | open, blocked on confirmation |
| Revised system rules (R06 rewrite, new micro-interaction rule IDs) | designer | implementation | open, blocked |

No approval is inferred from this record. Implementation, spending, and checkpoint changes all wait for the user's explicit confirmation.
