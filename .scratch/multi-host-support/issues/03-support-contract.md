# Choose the cross-host support contract

**Status:** closed
**Labels:** wayfinder:grilling
**Parent:** [Extend Game Designer across Codex, Claude Code CLI, and Google Antigravity CLI](../map.md)
**Assignee:** Lea
**Blocked by:** [Establish instruction and skill discovery on each host](01-instruction-discovery.md); [Establish role and orchestration capabilities on each host](02-agent-orchestration.md)

## Question

Given the verified host capabilities, what does supported mean for each host and
which minimum versions, prerequisites, and capability differences are acceptable?

Decide whether missing native delegation or isolation blocks support or permits
an explicitly disclosed sequential/manual workflow. Decide how model selection
is configured without imposing Codex model identifiers on other hosts. Preserve
the distinction between self-validation and independent review, the design
approval checkpoints, and host permission boundaries. State which behavior must
also work in the Antigravity application and which claims are CLI-only.

Resolve through a live exchange with the user, not inferred preferences.

## Proposal for Review

The [draft spec's support contract](../../../docs/superpowers/specs/2026-10-12-multi-host-support.md#a-support-contract)
proposes native delegation, host-native inherited models outside Codex, and
separate configured/runtime-verified claims. Approval is pending; this is not a
resolution comment or permission to begin implementation.

## Resolution comments

### 2026-10-12 - Support contract approved

The user reply `Approved` accepted decision A of spec revision
`509aeba28941fa2816887d455cfaec9e21f6b201`: native delegation, unchanged Codex
settings, inherited models on new hosts, and per-host configured/runtime-verified
claims. Live tests remain separately authorized. The proposal above records the
earlier draft state; this explicit decision resolves it.
