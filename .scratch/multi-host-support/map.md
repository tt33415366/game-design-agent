# Extend Game Designer across Codex, Claude Code CLI, and Google Antigravity CLI

**Status:** closed
**Labels:** wayfinder:map
**Assignee:**

## Destination

An implementation-ready compatibility plan for the six Game Designer skills,
the explorer/worker/tester/reviewer/researcher roles, and their orchestration in
Codex, Claude Code CLI, and Google Antigravity CLI. Preserve Codex support and
allow Antigravity itself to use the same agents as its CLI.

## Notes

- Planning only: this map settles decisions; it does not implement adapters.
- The user reply `Approved` on 2026-10-12 accepted the
  [implementation spec](../../docs/superpowers/specs/2026-10-12-multi-host-support.md)
  at revision `509aeba28941fa2816887d455cfaec9e21f6b201`. The decision map is complete;
  execution proceeds in the separate [implementation graph](implementation/README.md).
- Scope confirmed in the conversation on 2026-10-12: the user identified Google
  Antigravity CLI and its shared agents, then confirmed all six skills, all five
  supporting roles, and orchestration.
- Keep design rules and role responsibilities shared. Host-specific discovery,
  model selection, and tool configuration may differ. The physical source layout
  and synchronization mechanism still require a decision.
- Consult `wayfinder` each session; use `grilling` and `domain-modeling` for
  decision tickets, and `research` for external facts. Use `openai-docs` when
  investigating Codex behavior. Never fabricate a human decision.
- The Game Designer contract and its confirmation/evidence requirements must
  remain intact. This is repository infrastructure work, not a new game design.
- Use the [local tracker convention](README.md). Research findings belong on a
  throwaway `research/multi-host-compatibility` branch, not in implementation.
- The user requested local-only retention on 2026-10-12. Keep the map and research
  committed locally; do not push or open a PR. Research is retained at commit
  `71f8bffdb85e7032bbe9bb7fa4c4f5c8b480e522` on
  `research/multi-host-compatibility`; do not merge that research branch.
- A documented feature is not proof that the installed host supports it. Record
  product identity, version evidence, source dates, and untested behavior.

## Decisions so far

- [Establish instruction and skill discovery on each host](issues/01-instruction-discovery.md): Native discovery paths and instruction differences are documented; shared content still needs host-specific entry points.
- [Establish role and orchestration capabilities on each host](issues/02-agent-orchestration.md): All three hosts document subagents, but role formats, model selection, and tool permissions require host-specific treatment and live validation.
- [Choose the cross-host support contract](issues/03-support-contract.md): Native delegation with preserved Codex settings and explicit per-host qualification levels.
- [Choose shared sources and host adapter boundaries](issues/04-shared-sources.md): Existing canonical sources feed checked-in generated native adapters and a shared orchestration policy.
- [Choose compatibility evidence and rollout gates](issues/05-acceptance-evidence.md): Offline preservation/safety checks qualify configured support; live verification requires separate authorization and evidence.

## Not yet specified

None. The approved spec handles capability gaps through explicit qualification
limits and protects existing customizations through ownership/conflict checks.

## Out of scope

- Implementing or deploying the compatibility adapters during this planning map.
- New game-design stages, gameplay changes, or changes to approval checkpoints.
- Requiring identical model vendors or model identifiers on every host.
- Publishing a global installer, marketplace package, or hosted service.
