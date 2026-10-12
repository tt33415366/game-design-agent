# Choose shared sources and host adapter boundaries

**Status:** closed
**Labels:** wayfinder:grilling
**Parent:** [Extend Game Designer across Codex, Claude Code CLI, and Google Antigravity CLI](../map.md)
**Assignee:** Lea
**Blocked by:** [Choose the cross-host support contract](03-support-contract.md)

## Question

Which files will be authoritative for the shared design contract, skills, role
responsibilities, and orchestration policy, and how will each host consume them
without divergent copies or unsupported discovery assumptions?

Choose the smallest compatible approach among direct discovery, thin importing
entry points, symlinks, or generated adapters, using the settled support contract.
Specify ownership of host-specific model/tool settings, any synchronization or
drift checks, and how existing Codex configuration remains usable. Identify any
architecture-specific migration decision that becomes concrete and needs its own
ticket; do not implement the chosen layout here.

Resolve through a live exchange with the user.

## Proposal for Review

The [draft spec's shared-source layout](../../../docs/superpowers/specs/2026-10-12-multi-host-support.md#b-shared-sources-and-adapters)
keeps canonical skills and Codex role prose in place, with generated checked-in
host adapters and drift checks. Approval is pending; the existing rule sources
and host configuration have not changed.

## Resolution comments

### 2026-10-12 - Shared sources and adapter boundaries approved

The user reply `Approved` accepted decision B of spec revision
`509aeba28941fa2816887d455cfaec9e21f6b201`: retain canonical skills and Codex role
prose, share orchestration policy, and generate checked-in native adapters with
ownership/drift checks. The proposal above is historical; implementation is now
authorized through the separate implementation graph.
