# Orchestration Policy

Use this policy for complex repository work that needs delegation, independent
review, or coordinated changes. The root owns scope, decomposition, integration,
and final verification. A small, localized task may remain root-only.

## Host Selection

Choose a host profile from the active CLI/session identity. Do not infer the
host from directory presence because multiple hosts' configuration can coexist.
If the identity is unknown, ask before making host-specific delegation choices.
Do not translate one host's model, reasoning, sandbox, or tool settings into
another host's configuration.

## Delegation and Ownership

Only the root delegates. Give each child bounded context: a bounded task,
necessary file pointers, approval state, expected result, and exclusive
ownership for files it may edit. Keep a single writer for each file or
subsystem. Independent tasks may run concurrently only when the host supports
it and ownership does not overlap; serial native delegation is valid.

Use the active host's native delegation mechanism. Do not create a
process-launching orchestration service or launch another agent through a shell
workaround. The root selects the checkout before dispatch, and a worker's edits
must be visible to its parent and tester in that checkout. When the host offers
workspace modes, request inheritance rather than silently selecting an isolated
mode. If isolation is needed, the root explicitly selects a worktree and owns a
later merge.

## Independence and Context

An unavailable delegation capability or failed native delegation must be
reported with the narrower validation actually performed and a deferred
independent recheck. A same-context self-check can assist validation but cannot
satisfy independent review. Resume work by reloading project records and
evidence rather than assuming a cross-host conversation identifier survives.

## Permissions and Evidence

Respect effective session and organization policy. Do not assume repository
instructions can override more permissive parent policy or grant a permission
bypass. Publication, credential changes, paid calls, and other external effects
remain approval-controlled.

Record the command or input, observed result, artifact path when applicable,
and limitations for delegated or unavailable work. Static instruction checks
establish configuration only; they do not prove runtime model behavior.
