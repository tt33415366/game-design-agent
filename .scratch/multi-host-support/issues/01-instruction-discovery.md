# Establish instruction and skill discovery on each host

**Status:** closed
**Labels:** wayfinder:research
**Parent:** [Extend Game Designer across Codex, Claude Code CLI, and Google Antigravity CLI](../map.md)
**Assignee:** Lea
**Blocked by:** None

## Question

What officially supported project-local entry points, instruction precedence,
skill discovery/invocation mechanisms, and resource-link rules exist in Codex,
Claude Code CLI, and Google Antigravity CLI, and which are shared with the
Antigravity application?

Verify the exact Google product and CLI rather than substituting Gemini CLI or
an editor-launch command. Compare with `AGENTS.md`, `agents/game-designer.md`,
and the six `.agents/skills/design-*`, `gameplay-design`, and `system-design`
routes in this repository. Distinguish documented guarantees, local observations,
and unknowns; cite primary sources and record the documentation retrieval date.
Identify viable entry points and constraints, but leave architecture and support
promises to the human decision tickets.

## Resolution comments

### 2026-10-12 - Research completed; retained locally

Codex and Antigravity document project skills under `.agents/skills`; Claude Code
uses `.claude/skills` and `CLAUDE.md`. Antigravity documents `AGENTS.md` rules and
shared skill support across its CLI and application. Instruction precedence and
import syntax differ, so file reuse does not establish equivalent behavior.
The report records those differences and the remaining runtime evidence gaps;
this resolution does not select an adapter design or claim tested compatibility.

Research asset: `docs/research/2026-10-12-multi-host-instruction-discovery.md` on
`research/multi-host-compatibility`, commit
`71f8bffdb85e7032bbe9bb7fa4c4f5c8b480e522`. Read the retained asset with:

```sh
git show 71f8bffdb85e7032bbe9bb7fa4c4f5c8b480e522:docs/research/2026-10-12-multi-host-instruction-discovery.md
```

The user requested local-only retention. Do not push or merge the research branch;
the Git reference above is the retained asset, not a published URL.
