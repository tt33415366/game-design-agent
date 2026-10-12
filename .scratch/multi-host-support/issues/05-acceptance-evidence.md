# Choose compatibility evidence and rollout gates

**Status:** closed
**Labels:** wayfinder:grilling
**Parent:** [Extend Game Designer across Codex, Claude Code CLI, and Google Antigravity CLI](../map.md)
**Assignee:** Lea
**Blocked by:** [Choose shared sources and host adapter boundaries](04-shared-sources.md)

## Question

What evidence and rollout gates are sufficient to claim the chosen multi-host
contract is implemented without regressing Codex or overstating untested hosts?

Agree on static discovery/link checks, representative skill-routing and approval
scenarios, role invocation, host-native tool-name and permission checks, and the live CLI smoke tests
needed per host. Decide how unavailable binaries, credentials, model access, or
Antigravity application access affect the support claim and handoff. Specify what
can be tested without paid calls and which live checks require authorization.
Define the implementation handoff and rollback expectations, not implementation
tasks disguised as decision tickets.

Resolve through a live exchange with the user.

## Proposal for Review

The [draft spec's safety and acceptance rules](../../../docs/superpowers/specs/2026-10-12-multi-host-support.md#c-safety-and-acceptance)
separate offline validation from separately authorized live exercises and require
explicit unrun cases. Approval is pending; no proposed test is recorded as passed.

## Resolution comments

### 2026-10-12 - Safety and qualification gates approved

The user reply `Approved` accepted decision C and the verification/delivery
contract in spec revision `509aeba28941fa2816887d455cfaec9e21f6b201`. Offline checks
may qualify configured support; live capability claims need separately authorized
evidence. The approval does not turn any proposed test into a pass, authorize paid
calls, or relax local-only publication boundaries.
