# Generate the Antigravity adapter from canonical sources

**Status:** closed
**Labels:** implementation:task
**Parent:** [Multi-Host Game Designer Support](../../../docs/superpowers/specs/2026-10-12-multi-host-support.md)
**Assignee:** Lea
**Blocked by:** [Generate the Claude Code adapter from canonical sources](02-claude-adapter.md)

## Outcome and Ownership

Extend `agents/host-adapters.json` and `scripts/sync_host_adapters.py` to produce
five `.agents/agents/<role>.md` files and update the generated-file manifest.
Own `tests/host_support/test_antigravity_adapter.py`. Reuse root `AGENTS.md` and
the six canonical skill directories without making a second Google-specific copy.

## Contract and Acceptance

- Emit native subagent metadata, inherited models, sandbox command policy, and
  explicit role tool allowlists. Confirm exact tool identifiers from primary
  documentation/installed metadata; unknown tools fail qualification rather than
  defaulting to unrestricted access.
- Test `test_all_five_roles`, `test_native_subagent_fields`,
  `test_read_only_roles_have_no_command_or_write_tools`,
  `test_all_roles_exclude_native_delegation`,
  `test_researcher_can_search_without_mutation`,
  `test_codex_model_fields_absent`, and `test_shared_skill_tree_is_not_copied`.
- Preserve Claude renderer results byte-for-byte and test both hosts together.
  Add an unsupported-tool fixture to prove rejection before writes. Record the
  schema/tool reference used; no SDK tool name is assumed valid solely by analogy.
- Verify the shared policy requests `inherit` at invocation without inventing
  agent frontmatter. Record a live qualification case checking child working
  directory and parent/tester visibility of a disposable worker-created file;
  do not pass that case from static policy inspection alone.

Use TDD, then run the full host-support suite, renderer `--write`/`--check`, and
link audit. CLI and application discovery remain distinct live qualification
cases. Commit and merge the integration tip into the ticket branch before handoff.

## Resolution

Closed on 2026-10-12 after local implementation `d196e62` merged into the
integration branch. Python 3.11 host-support tests passed (33 total), renderer
write/check passed, link audit passed with 117 local targets and zero broken
links, and `git diff --check` passed. Native CLI/application discovery and the
Antigravity `inherit` workspace round trip were not run; support remains
configured rather than runtime-verified. No push.
