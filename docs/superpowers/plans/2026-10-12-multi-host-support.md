# Multi-Host Support Implementation Plan

> **For agentic workers:** Use the user's `implement-spec` workflow after approval:
> per-ticket implementer branches/worktrees with `tdd`, merger subagents, and a
> final `code-review`. The user approved execution on 2026-10-12.

**Goal:** Add native Claude Code and Google Antigravity adapters without changing
the existing Game Designer rules or Codex configuration.

**Architecture:** Keep the canonical skills and Codex role prose in place. Share
orchestration policy and deterministically generate the additional host formats,
with a manifest preventing accidental overwrite of local customizations.

**Tech Stack:** Markdown, TOML, JSON, Python 3.11+ standard library, `unittest`.

**Spec:** [Multi-Host Game Designer Support](../specs/2026-10-12-multi-host-support.md)
**Status:** approved; [approval gate](../../../.scratch/multi-host-support/implementation/00-approve-spec.md) is closed.
**Integration baseline:** `509aeba28941fa2816887d455cfaec9e21f6b201` on local `feat/multi-host-support`.

## Global Constraints

- All commits, branches, and evidence stay local; do not push or open a PR.
- Keep `.codex/config.toml` and all five `.codex/agents/*.toml` unchanged.
- Keep design rules, six routes, template meaning, and three checkpoints unchanged.
- Use Python 3.11+ and the standard library; checked-in adapters require no install.
- Preserve unrelated files and historical evidence; do not merge the research branch.
- `configured` is not `runtime-verified`; no paid/live calls are authorized here.

## Review Focus

- Generated files that a developer edited must cause a conflict, not data loss
  (Claude adapter ticket: changed-output and unmanaged-collision tests).
- Paths containing spaces, nested invocation, or a second checkout must not read
  or update another checkout (shared-policy and renderer tests).
- Wrong native tool names or inherited mutation capabilities must not silently
  turn read-only roles into writers (both adapter tickets' negative tool tests).
- Project-specific Codex model names must not reach another host; canonical role
  and skill edits must reach all generated outputs (renderer completeness tests).
  The committed preservation baseline must also detect unintended canonical edits.
- Missing credentials, denied delegation, or unrun application checks must remain
  visible rather than becoming compatibility evidence (qualification ticket).
  Include child checkout visibility and all-role native delegation exclusion.

Renderer tests also inject an apply-time failure: preserve the prior manifest,
return failure, and ensure the next check reports incomplete state.

## File Ownership and Order

Ticket bodies are the detailed acceptance contracts; use their named links rather
than maintaining another task checklist in the Wayfinder map.

| Ticket | Main ownership | Depends on |
| --- | --- | --- |
| [Shared orchestration](../../../.scratch/multi-host-support/implementation/01-shared-orchestration.md) | `AGENTS.md`, `agents/orchestration.md`, Codex skill facade, portable link checker, shared-policy tests | Approval |
| [Claude adapter](../../../.scratch/multi-host-support/implementation/02-claude-adapter.md) | `CLAUDE.md`, renderer, metadata/manifest, `.claude/` projections, renderer/Claude tests | Shared orchestration |
| [Antigravity adapter](../../../.scratch/multi-host-support/implementation/03-antigravity-adapter.md) | Extend renderer/metadata/manifest, `.agents/agents/`, Antigravity tests | Claude adapter |
| [Qualification](../../../.scratch/multi-host-support/implementation/04-qualification.md) | README/test guidance, evidence matrix, integration checks | Antigravity adapter |

The dependency chain is intentional; do not parallelize writers to the renderer
or ownership manifest. The source/CLI/output contracts are fixed in the spec.

## Execution Checklist

- [x] Record user approval and accepted spec revision; resolve the corresponding
  proposal decisions and close the approval gate without inventing consent.
- [x] Create local integration branch `feat/multi-host-support` from the approved
  planning tip and record its base commit for preservation checks.
- [x] For each frontier ticket, assign the driver, create its own worktree/branch
  based on the integration tip, and start a bounded background implementer.
- [x] Implementer writes the named failing tests, records the failing command,
  makes the smallest passing change, reruns checks, and commits the ticket.
- [x] Implementer merges the latest integration tip into its branch and reruns
  affected checks; a merger verifies ownership and merges into integration.
- [x] Append the local resolution comment with commit, checks, and limitations;
  close that ticket and recompute the frontier before dispatching the next.
- [x] Run final standards/spec `code-review`; use one implementer for fixes, then
  rerun checks and retain findings with their disposition.
- [x] Remove only clean, merged implementer worktrees and report the local
  integration branch with honest per-host qualification status.

## Final Verification Commands

These commands are planned, not results; the renderer/tests do not exist yet.

```sh
python3.11 -m unittest discover -s tests/host_support -p 'test_*.py' -v
python3.11 scripts/sync_host_adapters.py --check
python3.11 tests/behavior/verification-scripts/check_game_designer_links.py
git diff --check
```

Repeat the renderer checks in a temporary repository copy with spaces in its path.
Live-case commands are chosen from the installed host's documented interfaces only
after separate authorization; retain their exact invocations in the evidence file.
