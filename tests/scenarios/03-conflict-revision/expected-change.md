# Constructed Expected Change: Tideglass Salvage Revision

This is an authoring-time constructed output for `design-change`, not an independent evaluation. It consumes only `input.md`. The request, failure, approval, checks, and re-review are simulated. No real Tideglass project changed, no prototype was run, no spending occurred, and no Player Validation occurred.

## Initial Impact Record: Pending Approval

- Active canonical version before any decision: `input.md`, `Active System Specification v1.0`.
- The injected `F1` remains retained negative evidence. It is explicitly an injected simulated result, not observed real player feedback.
- The request is not an approval. Its `Recover=3` proposal changes the core risk/reward rule outside the approved recovery-tuning envelope `1..2`; the paid sonar scan changes project scope and material cost; updating a confirmed handoff would also alter its approved boundary.

| Delta ID | Proposed change | Active source | Impact | Status |
| --- | --- | --- | --- | --- |
| `D-01` | Change `R-02 Recover` from `+1` Cargo to `+3` Cargo. | `R-02 v1.0` | Core-rule change; outside the confirmed `1..2` local tuning envelope. | pending explicit user approval |
| `D-02` | Add paid sonar scan. | No active rule or approved scope. | Scope and material-cost change. | pending explicit user approval |
| `D-03` | Treat F1 as real-player proof and update the handoff. | `F1`, `T3` | Misclassifies evidence; affected handoff cannot be self-updated or self-approved. | rejected as stated |

| Item | Prior version/status | Effect if D-01 is approved | Required status |
| --- | --- | --- | --- |
| `R-02` | active `v1.0` | Its reward transition changes. | replace with one active `v1.1` definition |
| `F1`, `C1` | retained simulated v1.0 evidence | Both depend on old Recover reward. | historical; invalidated by `v1.1` |
| Prototype-scope approval `T2` | confirmed | Core rule is no longer inside the approved envelope. | re-opened for revised scope approval |
| Handoff approval `T3` | confirmed | Approved implementation boundary names v1.0 rule behavior. | invalidated by `v1.1`; revised handoff pending |
| Design Brief approval `T1` | confirmed | Core experience and target remain unchanged by D-01 alone. | remains confirmed, explicitly unaffected |

### Pending Decision

The change record asks the user to choose: reject D-01 and keep v1.0; approve D-01 with a revised local, zero-spend prototype scope; or separately propose D-02 with its paid-cost and scope implications. It does not change active rules or approve a handoff.

## Simulated Approval and Synchronization

`SIMULATED USER APPROVAL T4, 2026-09-30: "Approve only Recover = +2 Cargo for a revised local zero-spend prototype. Do not add paid sonar. Re-review the revised rule and submit a new handoff draft for my confirmation."`

T4 is fixture-only approval. It authorizes a replacement `R-02 v1.1` within a newly confirmed local, zero-spend revised scope. D-02 remains rejected. The active canonical specification below contains the only live definition of `R-02`; the v1.0 wording remains only in `input.md` as historical baseline.

## Active System Specification v1.1

| Rule ID | Trigger | Preconditions | Ordered transition | Observable outcome | Edge case |
| --- | --- | --- | --- | --- | --- |
| `R-01` | Start a dive | None | Set `Hull=2`, `Cargo=0`, `Status=active`. | Show `Hull 2`, `Cargo 0`. | Start resets prior dive state. |
| `R-02` | `Recover` at a wreck | `Status=active` | Add `2` Cargo; subtract `1` Hull; then resolve `R-04`. | Show cargo and hull deltas. | No other input changes state. |
| `R-03` | `Anchor` at a wreck | `Status=active` | Add `1` Hull, capped at `2`; then resolve `R-04`. | Show hull delta or cap. | No other input changes state. |
| `R-04` | Resolve action | An `R-02` or `R-03` action completed | If `Hull=0`, set `Status=lost`; otherwise remain active. | Show `Dive lost` on hull loss. | Loss has priority over later choices. |

## Change History and Invalidation

| Item | Prior version/result | Current status | Historical evidence retained | Replacement |
| --- | --- | --- | --- | --- |
| `R-02` | `v1.0: +1 Cargo` | superseded; active `v1.1: +2 Cargo` | `input.md`, v1.0 baseline | one active v1.1 definition above |
| `F1` | injected `Recover, Recover` => `Cargo=2`, `lost` | invalidated by `v1.1` | original input, injected conclusion preserved | `V-11` |
| `C1` | simulated `Anchor, Recover` => `Cargo=1`, active | invalidated by `v1.1` | original input and version preserved | `V-12` |
| `T2` | confirmed v1.0 envelope | superseded by simulated T4 revised scope | original approval remains historical | T4 recorded |
| `T3` | confirmed v1.0 handoff | invalidated by `v1.1` | original approval remains historical | revised handoff draft pending user confirmation |
| `T1` | confirmed Design Brief | remains confirmed and unaffected | `input.md` | none |

## Re-Review of v1.1

| Check | Result | Classification | Limitation |
| --- | --- | --- | --- |
| `V-11`: Start, `Recover`, `Recover` | Expected `Hull=0`, `Cargo=4`, `Status=lost`; confirms the changed Cargo result and unchanged loss priority. | not run / expected outcome | No actual command/input execution, observed output, artifact, or versioned runtime result. |
| `V-12`: Start, `Anchor`, `Recover` | Expected `Hull=2`, `Cargo=2`, `Status=active`; confirms cap and revised reward coexist. | not run / expected outcome | Not executed rule verification. |
| Scope/cost review | T4 permits only local, zero-spend `R-02` revision; paid sonar stays excluded. | simulated re-review | Not developer feasibility or cost validation. |
| Handoff boundary | Revised handoff may cite `R-02 v1.1`, but remains `draft pending confirmation`. | simulated re-review | T4 did not confirm the replacement handoff. |

The active rule set is internally singular for this constructed output. Historical v1.0 evidence and failed/injected outcomes remain visible but do not support claims about real players. Player Validation is not performed.
