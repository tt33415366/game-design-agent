# Closed Fictional Forward Test: `design-change`

Date: 2026-09-30

## Scope and Provenance

This is a closed fictional forward test. The only project facts, approvals, evidence, and failure result used are the raw constructed fixture below. Its simulated approvals are treated as valid only within this test. They are not real authorization, Player Validation, implementation evidence, or permission to modify a product.

No prototype code, repository product files, external systems, commits, paid actions, networked/trading functionality, or child agents were used. The only repository file written is this evidence report. The simulated document workspace is `/tmp/game-designer-change-eval`.

Consulted files, in order:

1. `agents/game-designer.md`
2. `.agents/skills/design-change/SKILL.md`
3. `tests/scenarios/03-conflict-revision/input.md`
4. `.agents/skills/design-change/templates/change-impact.md`
5. `.agents/skills/design-change/templates/change-history.md`
6. `.agents/skills/design-review/SKILL.md` (justified by design-change's mandatory re-review)
7. `.agents/skills/design-review/templates/design-review.md`
8. `.agents/skills/design-review/templates/development-handoff.md`

Not consulted: `expected-change.md`, PRD, plan, reports outside this file, and behavior tests.

## Turn 1: Raw Conflicting Request

### Input

The raw fixture requester said: "Make `Recover` grant 3 Cargo so players always choose it. Also add a paid sonar scan and update the approved handoff now. The injected failure proves real players dislike the current route."

### Actual pending-response output (verbatim)

```md
# Turn 1 Actual Pending Response

## Classification

- Request source: simulated input from `tests/scenarios/03-conflict-revision/input.md`.
- Injected failure `F1`: injected simulated result, not Player Validation and not real implementation output.
- Active source: `Active System Specification v1.0` in the constructed input.
- Active `R-02`: `Add 1 Cargo; subtract 1 Hull; then resolve R-04.`
- Confirmed envelope: `SIMULATED USER APPROVAL T2, 2026-09-30`, limited to one local zero-spend balance adjustment to `R-02` recovery value in `1..2`; no core-loop, scope, cost, or handoff change.

## Pending Impact Record

### Authority and Request

- Project and current record: constructed fixture `tests/scenarios/03-conflict-revision/input.md` (fictional only).
- Request source and classification: conflicting requester statement; simulated input. `F1` is an injected simulated result.
- Active authoritative documents and versions: constructed fixture, `Active System Specification v1.0`, `R-01` through `R-04`.
- Confirmed scope/budget envelope: T2 as stated above.
- Current checkpoints and approvals: Design Brief T1 confirmed; core gameplay and prototype scope T2 confirmed; Development Handoff Draft T3 confirmed.
- Change decision: pending. No new approval is recorded in this turn.
- Explicit user approval reference: none for this requested revision.

### Proposed Delta, Kept Separate from Active Rules

| Delta ID | Requested change | Current active source | Conflict or fit | Decision needed | Status |
| --- | --- | --- | --- | --- | --- |
| `D-01` | Make `Recover` grant `3 Cargo`. | `R-02 v1.0` | Exceeds the approved recovery-value range `1..2`; the request itself is not approval. | User must reject, or separately approve expanded scope. | proposed only |
| `D-02` | Add paid sonar scan. | No active rule; current loop has only `Recover` and `Anchor`. | Adds a paid input, material cost, and scope outside T2. | Explicit user approval for scope/cost/core-loop change. | proposed only |
| `D-03` | Update approved handoff now. | Handoff checkpoint T3/v1.0. | A handoff author/request cannot approve a revised handoff; no revised canonical rules exist. | Separate explicit handoff approval after a revised draft. | proposed only |
| `P-01` | Smallest bounded alternative: change `R-02` recovery reward from `1` to `2 Cargo`, leaving hull loss and `R-04` unchanged. | `R-02 v1.0` | Fits T2's local zero-spend `R-02` recovery-value range `1..2`; it does not establish that players dislike the route. | Explicit decision whether to synchronize this bounded correction in response to F1. | proposed only |

No row above changes the active authoritative rules while the decision is pending.

### Impact Analysis

| Impact ID | Affected rule, scope, evidence, or checkpoint | Effect | In-scope tuning envelope? | Required action | Status |
| --- | --- | --- | --- | --- | --- |
| `I-01` | `R-02 v1.0` | `3 Cargo` would exceed the bounded range. | no | Do not synchronize without a new explicit approval. | pending |
| `I-02` | Prototype scope and costs | Paid sonar introduces a new action and spending. | no | Do not synchronize without explicit expanded scope/cost approval. | pending |
| `I-03` | T3 Development Handoff Draft | The requested immediate update has no revised rule approval. | no | Keep current handoff untouched; a revised handoff would need separate confirmation. | pending |
| `I-04` | `P-01`, `R-02`, F1 | A `+2 Cargo` value is the only bounded alternative identified. | yes, T2 defines `1..2`, but no decision to use it is recorded in this turn. | Obtain explicit decision; preserve F1 as historical simulated evidence. | pending |

### Invalidation Ledger

| Item | Prior version and status | Affected by delta | Required status after approval | Historical evidence retained | Replacement required |
| --- | --- | --- | --- | --- | --- |
| `SIMULATED INJECTED FAILURE F1` | v1.0, injected simulated result | `P-01` if approved | invalidated by `v1.1` | `Recover, Recover` -> `Hull=0, Cargo=2, Status=lost`; `constructed fixture / v1.0` | replacement rule check |
| `SIMULATED RULE CHECK C1` | v1.0, simulated result | `P-01` if approved | invalidated by `v1.1` | `Anchor, Recover` -> `Hull=2, Cargo=1, Status=active`; `constructed fixture / v1.0` | replacement rule check |
| T1 Design Brief | confirmed | `P-01` if approved | remains confirmed | T1 approval text in fixture | none; core experience unchanged |
| T2 Core/prototype scope | confirmed | `P-01` if approved | remains confirmed | T2 approval text in fixture | none; exact `R-02` range, local, and zero-spend bounds remain satisfied |
| T3 Development Handoff Draft | confirmed v1.0 | `P-01` if approved | re-opened/pending for v1.1 | T3 approval text in fixture | revised handoff and separate approval only if a handoff is sought |

### Pending Decision and Boundary

| Decision or question | Owner | Needed before | Status |
| --- | --- | --- | --- |
| Reject or separately approve `D-01` (`3 Cargo`). | user | synchronization | open |
| Reject or separately approve `D-02` (paid sonar). | user | synchronization | open |
| Approve `P-01`: `R-02` grants `2 Cargo`, with all other `R-02` terms unchanged. | user | canonical synchronization | open |
| Approve a revised handoff, if one is desired. | user | handoff confirmation | open |

Implementation boundary: no prototype code, paid feature, handoff revision, or real repository product change is authorized or performed. The current v1.0 rules remain active.
```

## Turn 2: Explicit Simulated User Decision

### Input

`Keep this project offline and single-player; reject the trading addition. I approve the smallest bounded core-rule correction you proposed to address the injected failure, within the existing local zero-spend prototype scope. This approves the revised core rules, not a new handoff or a claim that old tests still pass.`

### Applied interpretation

For this fictional evaluation only, this is `SIMULATED USER APPROVAL T4, 2026-09-30`. It rejects `D-01` (`3 Cargo`), rejects `D-02` (paid sonar/trading), and approves only `P-01`: `R-02` recovery reward changes from `1` to `2 Cargo`. The `Recover` hull cost and `R-04` remain unchanged. The existing v1.0 handoff approval is reopened/pending, not replaced or re-approved.

### Produced simulated document states (verbatim)

#### `/tmp/game-designer-change-eval/project-record-v1.1-simulated.md`

```md
# Tideglass Salvage Simulated Project Record v1.1

## Authority

- Project: `Tideglass Salvage`.
- Simulation boundary: closed fictional evaluation only; no real authorization or repository product change.
- Baseline: constructed fixture `tests/scenarios/03-conflict-revision/input.md`, project record and `Active System Specification v1.0`.
- Revised canonical specification: `active-system-specification-v1.1-simulated.md`.
- Change impact: `change-impact-v1.1-simulated.md`.
- Change history: `change-history-v1.1-simulated.md`.
- Re-review: `design-review-v1.1-simulated.md`.

## Checkpoints

| Checkpoint | State | Explicit approval reference | Impact |
| --- | --- | --- | --- |
| Design Brief | confirmed | `SIMULATED USER APPROVAL T1, 2026-09-30: "Approve the Tideglass Salvage Design Brief."` | Unaffected: core experience is unchanged. |
| Core gameplay and prototype scope | confirmed | `SIMULATED USER APPROVAL T2, 2026-09-30: "Approve one local zero-spend prototype with the recover-or-anchor loop, two iterations, and recovery tuning only from 1 to 2."` | Unaffected: v1.1 remains local, zero-spend, uses the two-action loop, and changes recovery reward from 1 to 2. |
| Development Handoff Draft | pending re-confirmation | `SIMULATED USER APPROVAL T3, 2026-09-30` applies to v1.0 only. | Re-opened by v1.1; the simulated T4 approval expressly does not approve a new handoff. |

## Simulated Approval

`SIMULATED USER APPROVAL T4, 2026-09-30: "Keep this project offline and single-player; reject the trading addition. I approve the smallest bounded core-rule correction you proposed to address the injected failure, within the existing local zero-spend prototype scope. This approves the revised core rules, not a new handoff or a claim that old tests still pass."`

Interpretation recorded for this closed fictional test: reject `D-01` (`3 Cargo`) and `D-02` (paid sonar/trading addition); approve only `P-01`, changing `R-02` recovery reward from `1` to `2 Cargo`. The explicit offline/single-player constraint confirms that no networked, trading, paid, or multiplayer extension is authorized.
```

#### `/tmp/game-designer-change-eval/active-system-specification-v1.1-simulated.md`

```md
# Active System Specification v1.1 (Simulated)

Canonical source for the closed fictional evaluation. This replaces `R-02 v1.0` atomically; it contains one active definition for each rule ID.

| Rule ID | Trigger | Preconditions | Ordered transition | Observable outcome | Edge case |
| --- | --- | --- | --- | --- | --- |
| `R-01` | Start a dive | None | Set `Hull=2`, `Cargo=0`, `Status=active`. | Show `Hull 2`, `Cargo 0`. | Start resets prior dive state. |
| `R-02` | `Recover` at a wreck | `Status=active` | Add `2` Cargo; subtract `1` Hull; then resolve `R-04`. | Show cargo and hull deltas. | No other input changes state. |
| `R-03` | `Anchor` at a wreck | `Status=active` | Add `1` Hull, capped at `2`; then resolve `R-04`. | Show hull delta or cap. | No other input changes state. |
| `R-04` | Resolve action | An `R-02` or `R-03` action completed | If `Hull=0`, set `Status=lost`; otherwise remain active. | Show `Dive lost` on hull loss. | Loss has priority over later choices. |

`R-02 v1.0` wording is superseded and is retained only in `change-history-v1.1-simulated.md` and the baseline fixture.
```

#### `/tmp/game-designer-change-eval/change-impact-v1.1-simulated.md`

```md
# Change Impact Record v1.1 (Simulated)

## Authority and Request

- Project and current record: `project-record-v1.1-simulated.md`.
- Request source and classification: T4 is a simulated approval in this fictional evaluation. F1 remains an injected simulated result.
- Active authoritative documents and versions: baseline `Active System Specification v1.0`; active replacement `active-system-specification-v1.1-simulated.md`, `R-01` through `R-04`.
- Confirmed scope/budget envelope: T2, local zero-spend `R-02` recovery value only, range `1..2`.
- Current checkpoints and approvals: T1 confirmed; T2 confirmed; T3 reopened/pending re-confirmation.
- Change decision: approved for the bounded `P-01` only; `D-01`, `D-02`, and `D-03` rejected/not approved.
- Explicit user approval reference: simulated T4 quoted in `project-record-v1.1-simulated.md`.

## Proposed Delta, Kept Separate from Active Rules

| Delta ID | Requested change | Current active source | Conflict or fit | Decision needed | Status |
| --- | --- | --- | --- | --- | --- |
| `D-01` | `Recover` grants `3 Cargo`. | `R-02 v1.0` | Outside T2 range. | None; T4 rejects it. | rejected |
| `D-02` | Paid sonar scan/trading addition. | No active rule. | Outside local, zero-spend, offline single-player scope; paid and extended input. | None; T4 rejects it. | rejected |
| `D-03` | Update approved handoff now. | T3/v1.0 handoff approval. | T4 does not approve a new handoff. | Separate explicit handoff approval, if needed later. | rejected |
| `P-01` | `R-02`: `Add 1 Cargo` -> `Add 2 Cargo`; hull loss and `R-04` remain unchanged. | `R-02 v1.0` | Within T2 range and T4 bounded correction. | T4 recorded. | approved for synchronization |

## Impact Analysis

| Impact ID | Affected rule, scope, evidence, or checkpoint | Effect | In-scope tuning envelope? | Required action | Status |
| --- | --- | --- | --- | --- | --- |
| `I-01` | `R-02 v1.0` | Replaced by one canonical `R-02 v1.1` definition with `2 Cargo`. | yes, T2 | Synchronize active specification. | resolved |
| `I-02` | F1 and C1 historical observations | Their cargo expectations/results were produced under v1.0. | yes | Invalidate while retaining exact historical evidence; create replacements. | resolved |
| `I-03` | T1, T2 | Core loop, cost, and scope remain unchanged. | yes | Retain confirmation with explicit unaffected rationale. | resolved |
| `I-04` | T3 handoff approval | Rule/evidence supporting v1.0 handoff changed. | no new handoff approval | Reopen as pending; do not generate or approve a new handoff. | resolved |

## Invalidation Ledger

| Item | Prior version and status | Affected by delta | Required status after approval | Historical evidence retained | Replacement required |
| --- | --- | --- | --- | --- | --- |
| `SIMULATED INJECTED FAILURE F1` | v1.0, injected simulated result | `P-01` | invalidated by v1.1 | `Recover, Recover` -> `Hull=0, Cargo=2, Status=lost`; `constructed fixture / v1.0` | `V-01`, not run / expected outcome |
| `SIMULATED RULE CHECK C1` | v1.0, simulated result | `P-01` | invalidated by v1.1 | `Anchor, Recover` -> `Hull=2, Cargo=1, Status=active`; `constructed fixture / v1.0` | `V-02`, not run / expected outcome |
| T1 Design Brief | v1.0, confirmed | `P-01` | remains confirmed | fixture T1 | none; no core-experience change |
| T2 Core/prototype scope | v1.0, confirmed | `P-01` | remains confirmed | fixture T2 | none; explicit `1..2`, local, zero-spend envelope applies |
| T3 Development Handoff Draft | v1.0, confirmed | `P-01` | invalidated by v1.1; pending re-confirmation | fixture T3 | revised draft plus separate approval only if handoff resumes |

## Pending Decision and Boundary

| Decision or question | Owner | Needed before | Status |
| --- | --- | --- | --- |
| Run `V-01` and `V-02` against a local prototype implementation. | developer/designer | any verification claim | open |
| Decide whether to prepare a revised handoff. | user | handoff work | open |
| Approve any revised handoff draft. | user | implementation authorization via handoff | open |

Boundary: this simulated document synchronization authorizes no implementation, paid feature, trading, online/multiplayer capability, external action, or new handoff.
```

#### `/tmp/game-designer-change-eval/change-history-v1.1-simulated.md`

```md
# Change History v1.1 (Simulated)

## Approved Revision

- Project record: `project-record-v1.1-simulated.md`.
- Approval reference: simulated T4, 2026-09-30, quoted in the project record.
- Approved date and source: 2026-09-30 / explicitly simulated user turn for this fictional evaluation.
- Active authoritative source and version: `active-system-specification-v1.1-simulated.md` / v1.1.
- Re-review record: `design-review-v1.1-simulated.md`.

## Canonical Synchronization

| Rule or document | Superseded version | Active version | Approved change | Historical location |
| --- | --- | --- | --- | --- |
| `R-02` | v1.0: `Add 1 Cargo; subtract 1 Hull; then resolve R-04.` | v1.1: `Add 2 Cargo; subtract 1 Hull; then resolve R-04.` | One active `R-02` definition; no sonar, trading, paid, online, multiplayer, or handoff change. | baseline fixture and this history |

## Historical Evidence and Invalidation

| Item | Prior classification and result | Version status | Retained evidence | Replacement status |
| --- | --- | --- | --- | --- |
| F1 | injected simulated result: `Recover, Recover` -> `Hull=0, Cargo=2, Status=lost`; fixture author asserts too punishing | invalidated by v1.1 | constructed fixture / v1.0 | `V-01` not run / expected outcome: `Recover, Recover` -> `Hull=0, Cargo=4, Status=lost` |
| C1 | simulated result: `Anchor, Recover` -> `Hull=2, Cargo=1, Status=active` | invalidated by v1.1 | constructed fixture / v1.0 | `V-02` not run / expected outcome: `Anchor, Recover` -> `Hull=2, Cargo=2, Status=active` |
| T3 handoff | simulated approval of v1.0 handoff | invalidated by v1.1; pending re-confirmation | fixture T3 | no revised handoff prepared or approved |

## Re-Review and Remaining Approvals

| Item | Result | Evidence classification | Required next step |
| --- | --- | --- | --- |
| Revised `R-02` review | consistent with `R-04` and approved bounds | simulated approval and rule analysis; no execution | Run replacement checks before claiming rule verification. |
| Handoff | pending re-confirmation | simulated approval history | User must explicitly approve a revised handoff if one is produced. |
| Player experience | unavailable | no Player Validation | Do not infer dislike, balance, or preference from F1. |
```

#### `/tmp/game-designer-change-eval/design-review-v1.1-simulated.md`

```md
# Design Review Record v1.1 (Simulated)

## Authority and Scope

- Project: `Tideglass Salvage`.
- Review date and source: 2026-09-30 / fictional simulated T4 approval and v1.1 canonical rules.
- Project record: `project-record-v1.1-simulated.md`.
- Design Brief approval: simulated T1.
- Core gameplay and prototype scope approval: simulated T2.
- Authoritative system specification: `active-system-specification-v1.1-simulated.md`.
- Canonical terminology: `R-01` through `R-04` in v1.1.
- Requested change or handoff scope: bounded `R-02` reward correction only; no handoff revision.
- Input classification: simulated input, simulated approval, and injected simulated result.

## Review Outcome

- Readiness: qualified handoff draft is not produced; current v1.0 handoff is pending re-confirmation because its supporting rule changed.
- Blocking findings: none for the narrowly synchronized rule set; verification and handoff approval remain unavailable.
- Player Validation: not performed; no preference or balance conclusion is supported.
- Development Handoff Draft checkpoint: pending; no explicit v1.1 handoff approval.

## Consistency and Actionability Checks

| Finding ID | Check | Sources reviewed | Observation | Severity | Required resolution or follow-up | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `F-01` | transition | `R-02 v1.1`, `R-04 v1.1` | `R-02` still subtracts one Hull before resolving loss; `R-04` still makes loss terminal at zero Hull. `Cargo=2` does not conflict with state transitions. | low | None for rule consistency. | resolved |
| `F-02` | scope/approval | T2, T4, `R-02 v1.1` | `+2 Cargo` is inside range `1..2`, local and zero-spend; paid sonar/trading is excluded. | low | Preserve exclusion in any future work. | resolved |
| `F-03` | evidence | F1, C1, v1.1 | v1.0 outputs cannot verify v1.1. F1 is not Player Validation. | medium | Run V-01/V-02 before any rule-verification claim. | open |
| `F-04` | handoff approval | T3, T4 | T3 approved v1.0 only; T4 expressly withholds a new handoff. | high | Keep checkpoint pending until a separately approved revised draft exists. | open |

## Requested and Corrected Deltas

| Delta ID | Canonical source | Requested or corrected change | Rules/state/feedback affected | Scope effect | Approval needed |
| --- | --- | --- | --- | --- | --- |
| `P-01` | `R-02 v1.1` | `Add 2 Cargo; subtract 1 Hull; then resolve R-04.` | `R-02`, observable cargo delta; no state-model expansion | included bounded local tune | simulated T4 recorded |
| `D-02` | none | paid sonar/trading | would add an input, cost, and scope | excluded | rejected by simulated T4 |

## Evidence and Risks

| Item | Classification | Actual command or input | Observed output or observation | Artifact/log path and version | Limitation or follow-up |
| --- | --- | --- | --- | --- |
| F1 | injected simulated result | `Recover, Recover` | `Hull=0, Cargo=2, Status=lost`; assertion that this is too punishing | constructed fixture / v1.0 | invalidated by v1.1; no Player Validation |
| C1 | simulated result | `Anchor, Recover` | `Hull=2, Cargo=1, Status=active` | constructed fixture / v1.0 | invalidated by v1.1 |
| V-01 | not run / expected outcome | `Recover, Recover` | expected `Hull=0, Cargo=4, Status=lost` | v1.1 planned case | no actual prototype command/input or output |
| V-02 | not run / expected outcome | `Anchor, Recover` | expected `Hull=2, Cargo=2, Status=active` | v1.1 planned case | no actual prototype command/input or output |

## Open Decisions and Handoff Boundary

| Item | Owner | Needed before implementation or release | Status |
| --- | --- | --- | --- |
| Execute V-01/V-02 in a local prototype. | developer/designer | verification claim | open |
| Create a revised handoff draft. | designer/user | any v1.1 handoff | open |
| Approve a revised handoff draft. | user | handoff confirmation | open |

No Development Handoff Draft was created because T4 expressly approves revised core rules only, not a new handoff.
```

## Limits

- F1 and C1 are retained simulated historical evidence and were invalidated by v1.1; no replacement verification was run.
- The v1.1 expected outputs are rule-analysis expectations only, not implementation verification.
- No Player Validation exists. The fixture's assertion that players dislike the route is not supported.
- T1 and T2 remain confirmed only in this constructed fixture because v1.1 stays inside their explicit boundary. T3 is pending re-confirmation. T4 does not approve a new handoff.
- All approvals, sources, and effects described here are fictional and limited to this forward test.

## Corrected-Script Second Run (Appended, Preserving Prior History)

The preceding Turn 2 records the controller test-harness wording that incorrectly referred to trading. It is retained unchanged as historical output. This separate rerun uses only the unchanged original pending response, the raw fixture, and the applicable `design-change` / `design-review` workflow. It does not alter the prior section or create product effects.

### Corrected scripted input

`Keep this project local and zero-spend; reject the paid sonar addition. I approve the smallest bounded correction you proposed within the existing confirmed tuning envelope. This approves that rule adjustment, not a new handoff or any claim that old tests still pass.`

### Full actual corrected-run output (verbatim)

```md
# Corrected-Script Second Run: Actual Output

## Provenance and Authority

- Derived from the unchanged original pending response: `turn-1-pending-response.md`.
- Baseline authoritative rules: `Active System Specification v1.0` in `tests/scenarios/03-conflict-revision/input.md`.
- This is a closed fictional simulation. All approvals and evidence remain simulated fixture material only.
- Corrected simulated user input: `Keep this project local and zero-spend; reject the paid sonar addition. I approve the smallest bounded correction you proposed within the existing confirmed tuning envelope. This approves that rule adjustment, not a new handoff or any claim that old tests still pass.`
- Recorded approval reference: `SIMULATED USER APPROVAL T5, 2026-09-30` (corrected scripted second turn only).

## Decision

| Delta | Corrected decision | Reason |
| --- | --- | --- |
| `D-01`: `Recover` grants `3 Cargo` | not approved; not synchronized | The corrected input approves only the smallest bounded proposal; it does not expand the confirmed `1..2` range. |
| `D-02`: paid sonar scan | rejected | T5 explicitly rejects the paid sonar addition; it also violates local, zero-spend scope. |
| `D-03`: update the approved handoff | not approved | T5 explicitly does not approve a new handoff. |
| `P-01`: `R-02` reward `1` -> `2 Cargo` | approved for synchronization | This is the smallest bounded correction proposed in the unchanged pending response and is within T2's local, zero-spend `1..2` recovery-value envelope. |

## Simulated Project Record v1.1 Corrected

| Checkpoint | State | Basis and impact |
| --- | --- | --- |
| Design Brief | confirmed | Simulated T1 remains unaffected: core experience is unchanged. |
| Core gameplay and prototype scope | confirmed | Simulated T2 remains unaffected: v1.1 is a local, zero-spend `R-02` reward adjustment from `1` to `2`, within `1..2`. |
| Development Handoff Draft | pending re-confirmation | Simulated T3 applied to v1.0. `R-02` and supporting evidence changed; T5 explicitly does not approve a new handoff. |

## Active System Specification v1.1 Corrected

This replaces `R-02 v1.0` atomically. It has one active definition per rule ID.

| Rule ID | Trigger | Preconditions | Ordered transition | Observable outcome | Edge case |
| --- | --- | --- | --- | --- | --- |
| `R-01` | Start a dive | None | Set `Hull=2`, `Cargo=0`, `Status=active`. | Show `Hull 2`, `Cargo 0`. | Start resets prior dive state. |
| `R-02` | `Recover` at a wreck | `Status=active` | Add `2` Cargo; subtract `1` Hull; then resolve `R-04`. | Show cargo and hull deltas. | No other input changes state. |
| `R-03` | `Anchor` at a wreck | `Status=active` | Add `1` Hull, capped at `2`; then resolve `R-04`. | Show hull delta or cap. | No other input changes state. |
| `R-04` | Resolve action | An `R-02` or `R-03` action completed | If `Hull=0`, set `Status=lost`; otherwise remain active. | Show `Dive lost` on hull loss. | Loss has priority over later choices. |

`R-02 v1.0` is superseded only in this corrected simulation's history; it is not retained beside the active v1.1 rule.

## Change Impact and Invalidation Ledger

| Item | Previous status | Corrected v1.1 status | Retained historical evidence | Replacement |
| --- | --- | --- | --- | --- |
| `R-02` | v1.0: `Add 1 Cargo; subtract 1 Hull; then resolve R-04.` | v1.1: `Add 2 Cargo; subtract 1 Hull; then resolve R-04.` | baseline fixture v1.0 | active canonical rule synchronized |
| F1 | injected simulated result: `Recover, Recover` -> `Hull=0, Cargo=2, Status=lost`; injected conclusion claims route is too punishing | invalidated by v1.1 | constructed fixture / v1.0 | `V-01` not run / expected: `Recover, Recover` -> `Hull=0, Cargo=4, Status=lost` |
| C1 | simulated result: `Anchor, Recover` -> `Hull=2, Cargo=1, Status=active` | invalidated by v1.1 | constructed fixture / v1.0 | `V-02` not run / expected: `Anchor, Recover` -> `Hull=2, Cargo=2, Status=active` |
| T1 | confirmed | remains confirmed | fixture T1 | none; core experience unchanged |
| T2 | confirmed | remains confirmed | fixture T2 | none; within explicit tuning envelope |
| T3 | confirmed for v1.0 handoff | invalidated by v1.1; pending re-confirmation | fixture T3 | revised handoff and separate approval only if later requested |

## Re-Review

| Finding | Result | Evidence classification | Required next step |
| --- | --- | --- | --- |
| `R-02 v1.1` transition and `R-04` terminal resolution | consistent: `R-02` still removes one Hull before `R-04`; cargo reward changes only | simulated approval and rule analysis | none for consistency |
| Scope and approval | consistent: `+2 Cargo` is inside T2's `1..2`, local, zero-spend boundary; paid sonar remains excluded | simulated approval | preserve boundary |
| Historical evidence | v1.0 outputs do not verify v1.1 | injected/simulated historical evidence | run V-01/V-02 before a rule-verification claim |
| Handoff | pending | simulated approval history | a separate explicit approval is required for any revised handoff |

## Limits and Boundary

- No prototype, code, command-based verification, Player Validation, external action, or repository product change occurred.
- F1 remains an injected simulated result, not evidence that real players dislike the route.
- V-01 and V-02 are planned expectations only and have not been run.
- T5 approves this revised core rule only. It does not approve a handoff or preserve a claim that old tests pass.
```

The exact standalone corrected output is also preserved at `/tmp/game-designer-change-eval/corrected-second-run-output.md`. It has no trading request, decision, or output.
