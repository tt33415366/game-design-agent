# Establish role and orchestration capabilities on each host

**Status:** closed
**Labels:** wayfinder:research
**Parent:** [Extend Game Designer across Codex, Claude Code CLI, and Google Antigravity CLI](../map.md)
**Assignee:** Lea
**Blocked by:** None

## Question

How can Codex, Claude Code CLI, and Google Antigravity CLI represent and invoke
the existing explorer, worker, tester, reviewer, and researcher roles, and which
orchestration capabilities are actually supported on each host?

Inspect `.codex/config.toml`, `.codex/agents/`, and the `astra-orchestrator` skill.
Verify role discovery, model selection, reasoning settings, delegation, parallel
execution, context isolation, tool restrictions, approvals, and resumption against
primary sources. Confirm what Google Antigravity CLI shares with its application;
do not infer parity from similarly named products. Record documentation dates and
locally available CLI versions without modifying credentials or global settings.
Separate documented features from tested behavior and unknowns. Identify where
the current independent-review promises cannot yet be substantiated; do not choose
fallback behavior or resolve a human support-policy decision.

## Resolution comments

### 2026-10-12 - Research completed; retained locally

Codex documents project TOML roles; Claude Code documents `.claude/agents`
Markdown roles; Antigravity documents `.agents/agents` Markdown roles shared
between its CLI and application. The report compares delegation, context,
model selection, permissions, and resumption without assuming cross-host parity.
Root review verified the Codex agent configuration keys against current official
documentation and added Google's warning about invalid tool names hanging agents.

Safe version checks observed Codex `0.162.1`, Claude Code `2.1.285`, and Antigravity
`1.2.12`. No authenticated session or cross-host role execution was tested. These
versions are observations, not chosen minimum supported versions.

Research asset: `docs/research/2026-10-12-multi-host-orchestration.md` on
`research/multi-host-compatibility`, commit
`71f8bffdb85e7032bbe9bb7fa4c4f5c8b480e522`. Read the retained asset with:

```sh
git show 71f8bffdb85e7032bbe9bb7fa4c4f5c8b480e522:docs/research/2026-10-12-multi-host-orchestration.md
```

The user requested local-only retention. Do not push or merge the research branch.
No fallback or support-policy decision was made.
