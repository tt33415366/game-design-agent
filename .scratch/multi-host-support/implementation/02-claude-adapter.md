# Generate the Claude Code adapter from canonical sources

**Status:** closed
**Labels:** implementation:task
**Parent:** [Multi-Host Game Designer Support](../../../docs/superpowers/specs/2026-10-12-multi-host-support.md)
**Assignee:** Lea
**Blocked by:** [Make orchestration host-neutral while preserving Codex](01-shared-orchestration.md)

## Outcome and Ownership

Create `CLAUDE.md`, `scripts/sync_host_adapters.py`, `agents/host-adapters.json`,
`agents/generated-host-files.json`, five `.claude/agents/<role>.md` files, and
complete `.claude/skills/<design-route>/` projections. Own
`tests/host_support/test_adapter_sync.py` and `test_claude_adapter.py`.

## Contract and Acceptance

- Implement the spec's renderer CLI, collision handling, ownership manifest, and
  output-safety contract. This ticket supplies the Claude host metadata; the next
  ticket adds Antigravity through the same renderer, not a second generator.
- Read canonical TOML with `tomllib`; keep role body content and six skill trees
  unchanged. Serialize frontmatter values safely. Import `@AGENTS.md` from the
  hand-maintained Claude entry point; do not generate or overwrite that file.
- Pin Claude role metadata to `model: inherit`, normal permissions, and explicit
  capability allowlists. Read-only roles cannot acquire shell/write tools.
- Test `test_role_body_matches_source`, `test_six_skill_trees_match`,
  `test_host_fields_do_not_leak`, `test_read_only_tools`,
  `test_all_roles_exclude_native_delegation`,
  `test_repeat_write_is_identical`, `test_check_does_not_write`,
  `test_changed_generated_file_is_preserved`, `test_unmanaged_collision`,
  `test_stale_output_cleanup`, `test_rejects_symlink_escape`, and
  `test_invalid_inputs_write_nothing`, including paths with spaces and invocation
  from outside the repository root.
- `test_apply_failure_keeps_old_manifest` injects an output replacement failure
  after an earlier output succeeds: write returns nonzero, the prior manifest
  remains, `--check` fails, and unrelated/local edits stay intact. This tests the
  documented nontransactional failure mode rather than promising rollback.

Run failing unit tests before implementation, then the full host-support suite,
`python3 scripts/sync_host_adapters.py --write`, `--check`, and the link checker.
No host/model invocation is needed for this ticket. Record unverified native
discovery rather than marking it passed. Commit and merge the latest integration
tip into the ticket branch before handoff.

## Resolution

Closed on 2026-10-12 after local implementation `c9b7c8d` and merger-verified
integration at `9d9f803`. Root independently reran all 25 host-support tests with
Python 3.11 successfully. Renderer write/check and link audit passed (83 files,
117 local targets, zero broken links); `git diff --check` passed. TDD evidence is
retained locally at `/tmp/claude-adapter-evidence.md`. Native discovery and paid
model exercises were not run; this establishes configured support only. No push.
