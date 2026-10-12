# Qualify multi-host behavior and document support limits

**Status:** closed
**Labels:** implementation:task
**Parent:** [Multi-Host Game Designer Support](../../../docs/superpowers/specs/2026-10-12-multi-host-support.md)
**Assignee:** Lea
**Blocked by:** [Generate the Antigravity adapter from canonical sources](03-antigravity-adapter.md)

## Outcome and Ownership

Update `README.md` and `tests/README.md`; create
`tests/behavior/multi-host-support.md` and focused integration checks in
`tests/host_support/test_qualification.py`. Document normal per-host entry points,
regeneration, generated-file ownership, and the limits of each support claim.

## Contract and Acceptance

- Run all offline checks in the active integration checkout and a temporary copy.
  Test `test_every_host_has_all_routes_and_roles`,
  `test_no_unscoped_or_foreign_host_configuration`, and
  `test_no_runtime_verification_claim_without_evidence` against retained evidence.
- Record the integration baseline and compare unchanged Codex TOML/design rules.
  Run `test_canonical_sources_match_baseline` against the immutable digest/path
  manifest from the first ticket; changes fail qualification. Preserve historical
  fixtures. Document rollback without global-config changes.
- Record each live case required by the spec as `passed`, `failed`, or `not run`.
  Request specific authorization before any paid/authenticated exercise; lacking
  authorization, record exact unrun cases and retain `configured` status only.
- Include versions, effective permissions, prompts/commands, outputs, commit, and
  artifact references for actual runs. Keep CLI and Antigravity application rows
  separate; static examples do not count as host outputs or independent review.
- Include effective native delegation-tool exclusion for all five roles and the
  Antigravity child-workspace round trip in the live case matrix. Shell policy
  compliance is not misreported as a portable tool-level sandbox guarantee.

Run the full unit suite, renderer `--check`, link audit, and `git diff --check`.
Commit and merge the latest integration tip before handoff. After integration, the
root runs `code-review` for standards and spec compliance, routes fixes through one
implementer, reruns checks, closes tickets with evidence, and removes only merged,
clean implementer worktrees. All work remains local, with no PR or push.

## Resolution

Closed on 2026-10-12 after qualification commit `7527f61` merged into the
integration branch. Thirty-six host-support tests passed, renderer `--check`
passed in the integration checkout and a temporary path containing spaces, link
audit passed with zero broken targets, and `git diff --check` passed. Every live
CLI/application case remains explicitly `NOT RUN`; all hosts are configured only.
The unrelated Playwright prototype suite was not run because its dependency is
not installed. No push.
