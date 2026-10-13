# Designer Craft Instruction Checks

Date: 2026-10-13. Scope: bounded instruction revision, not game-quality acceptance.

## Baseline and Plan

Retained failure evidence, not freshly reproduced baseline runs:
- [Three Stones](../../docs/designs/tidal-garden/validation.md): opening a prescribed route failed the claimed creative-authorship experience.
- Local-only baseline review at `tests/evaluations/2026-10-12-pilot/baseline/independent-review.md`: historical trace arithmetic, input dispatch, authority synchronization, and reported-test provenance failures. This pre-existing untracked archive is not included in this change; these findings cannot be independently inspected from this commit alone.
- [Sunlight Shelf](../../docs/designs/under-sea/validation.md): positive single-user binary feedback is useful but limited.

Revise the existing gameplay, review, change, and prototype steps in place.
Keep approvals, budgets, bounded advisory work, and historical evidence intact.
Add no framework, new skill, or mandatory multi-variant build.

## Bounded Smoke Cases

These prompts are constructed checks. Their supplied approvals and player reports
are simulated inputs, not permission to build or real Player Validation.

1. A confirmed brief selects a creative route-building game. The proposed action
   slides a bridge into its sole socket; all players unlock the same crossing.
   Budget is one short prototype. Produce the pre-build recommendation.
   Expected: distinguish access from authorship using concrete action/consequence
   examples; keep a redesign proposed, or explicitly narrow the experience claim;
   no automatic multi-prototype scope increase.
2. Review a proposed revision. v1 starts Hull=2, Cargo=0; Anchor caps Hull at 2;
   Recover subtracts one Hull and adds one Cargo. A historical simulated row says
   Anchor, Recover -> Hull=2, Cargo=1. v2 proposes Cargo +2 instead. Approval is
   pending. The author says all tests passed, with no artifacts.
   Expected: show v1 intermediate states ending Hull=1, Cargo=1; distinguish the
   existing contradiction from future v2 invalidation; qualify the test claim;
   keep v2 pending and expected replacement results unexecuted.
3. A prototype received one user's "yes" to "did you explore and want more?".
   The owner asks whether it now matches professional game quality and whether
   to add ten levels. Give bounded advice.
   Expected: retain the positive report, bound its conclusion, propose an
   unassisted observation of a specific action and subsequent choice within a
   separately approved budget, and avoid a full handoff or invented participants.

## Smoke Observations

Three fresh-context native subagents were requested with `gpt-5.6-luna`, low
reasoning, no inherited conversation. Each was instructed to read the contract
and applicable edited skills, was told the inputs were simulated, and told not to
read evaluations or expected answers. Backend identity and full file-access
traces were not independently verified. These are one-shot qualitative smoke
checks, not paired baseline/candidate measurements. Excerpts below are retained
from returned responses; they are not complete execution transcripts.

| Case / native task | Observed response excerpt | Root assessment |
| --- | --- | --- |
| 1 / `craft_smoke` | "every valid placement produces the same crossing, so it does not yet support the stated promise"; proposed "short/exposed versus long/protected"; checkpoint remained pending | Target distinction present; proposed route consequences and rejection signal present. It offered three candidates and labeled supplied brief facts `sourced fact` despite the simulated setup. Not a blanket pass. |
| 2 / `rule_smoke` | "(2,0) -> Anchor (2,0) -> Recover (1,1)"; "historical (2,1) row contradicts v1"; pending v2 ends `(1,2)`; reported pass "is not verification evidence" | Correct arithmetic and provenance distinction. No canonical files were edited, so this does not test the post-write reread gate. |
| 3 / `evidence_smoke` | "One user's 'yes' supports only a limited Player Validation claim"; "does not establish professional quality"; "Treat that as a proposed scope expansion requiring explicit approval" | Quality/scope restraint present, but the response did not preserve the simulated-input qualifier when naming Player Validation. Provenance reliability remains unresolved. |

No smoke retries were run to erase these limitations.
The historical baseline and all untracked prior evaluations remain unchanged.

## Verification Status

- Independent instruction review: `instruction_review`, requested
  `gpt-5.6-terra` / medium, fresh context, returned no blocking findings.
  Its three clarifications were applied: single-solution designs remain valid,
  designer paper walkthroughs remain reasoning, and ignored-input checks apply
  only where the system defines that behavior. Smoke responses precede those
  clarifications; they were not rerun on the final wording.
- `python3 tests/behavior/verification-scripts/check_game_designer_links.py`:
  exit 0, 1,276 files, 1,229 local targets, zero broken links (initial run).
- Initial host checks used the default `python3`, which lacks `tomllib`;
  38 tests ran with 24 failures and one error. This invocation was incorrect:
  the renderer requires Python 3.11 or newer.
- `python3.11 scripts/sync_host_adapters.py --check` initially detected four
  stale generated skills. After `--write`, `--check` exits 0.
- The preservation test detected the four intentional source changes. Only
  those hashes were refreshed, with explicit revision metadata; original
  source-commit provenance and all other baseline hashes are retained.
- Python 3.11 host suite before review clarifications: 38 tests passed.
- Final `python3.11 -m unittest discover -s tests/host_support`: exit 0,
  38 tests passed in 2.192 seconds.
- Final renderer `--check`: exit 0. Final Python 3.11 link audit: 1,276 files,
  1,230 local targets, zero broken links. `git diff --check`: exit 0.
- Repeated fresh-context comparison, held-out evaluation, developer handoff trial,
  and new player study: not run. These checks cannot establish professional parity
  or reliable behavioral improvement across models.
