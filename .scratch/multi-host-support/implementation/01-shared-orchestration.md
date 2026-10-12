# Make orchestration host-neutral while preserving Codex

**Status:** closed
**Labels:** implementation:task
**Parent:** [Multi-Host Game Designer Support](../../../docs/superpowers/specs/2026-10-12-multi-host-support.md)
**Assignee:** Lea
**Blocked by:** [Approve the multi-host implementation spec](00-approve-spec.md)

## Outcome and Ownership

Create `agents/orchestration.md`; update root `AGENTS.md` and the existing
`astra-orchestrator` skill as specified. Update only the root discovery of the
existing link checker in `tests/behavior/verification-scripts/check_game_designer_links.py`.
Own `tests/host_support/test_shared_contract.py` and
`tests/host_support/preservation-baseline.json` for focused offline regression
checks. Do not change Codex TOML, game-design rules, or historical evidence.

## Contract and Acceptance

- Root routing loads the shared policy for complex work and the Game Designer
  contract only for relevant requests. Codex's existing skill remains callable.
- The policy preserves bounded context, single-writer ownership, native
  delegation, honest independence claims, and approval-controlled publication;
  this implementation stays local. It does not impose Codex model/tool names on
  another host or infer the active host from coexisting configuration directories.
- Tests `test_shared_routing`, `test_codex_profile_unchanged`,
  `test_missing_delegation_is_not_independent_review`, and
  `test_link_audit_uses_its_checkout` pin those requirements. Add
  `test_host_selection_uses_session_identity` for the coexisting-config case.
- Capture the spec's complete immutable source set from the recorded integration
  starting commit, not the edited working tree. Add
  `test_canonical_sources_match_baseline` and negative fixtures proving changed,
  added, and removed canonical files fail; this must work in a copy without Git
  history using the committed digest manifest.
- The link-check regression runs a copied checker from a different working
  directory and checks that it audits the copy, not the original workspace.

Use TDD: add failing checks, run them, implement the contract, rerun, and commit.
Run `python3 -m unittest discover -s tests/host_support -p 'test_shared_contract.py' -v`
and the existing link checker. Record that static policy tests do not prove model
behavior. Merge the latest integration tip into the ticket branch before handoff.

## Resolution comments

### 2026-10-12 - Implemented on integration branch

Implemented in `eae6cf9` on `feat/multi-host-support` after the ticket branch
merged the integration tip. Added the host-neutral orchestration policy, reduced
the Codex skill to a compatibility facade, made the link audit derive its own
checkout, and added canonical-source preservation tests/baseline.

Verification:

- `python3 -m unittest discover -s tests/host_support -p 'test_shared_contract.py' -v`: 7 passed.
- `python3 tests/behavior/verification-scripts/check_game_designer_links.py`:
  `LINK_AUDIT files=62 local_targets=102 broken=0`.
- `git diff --check`: passed.

Static checks do not establish runtime host/model behavior. No authenticated or
paid host invocation was run. A direct merge fallback was used after two merger
helpers failed to return; no independent review claim is made for that fallback.
