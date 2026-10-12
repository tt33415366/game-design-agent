# Multi-host support tracker

This effort uses local Markdown issues because no issue tracker integration was
provided. Run `/setup-matt-pocock-skills` to configure a different tracker.

## Wayfinding operations

- Identity: an issue's filename, relative to this directory, is its stable ID.
- Map: `map.md`, labelled `wayfinder:map`.
- Children: files in `issues/` whose `Parent` points to the map.
- Labels: only `wayfinder:` labels; the label determines the ticket type.
- Claim: set `Assignee` to the driving developer before work. An empty value
  means unclaimed. A worker may be noted separately but is not the claim.
- Blocking: `Blocked by` lists links to prerequisite issues. Local Markdown has
  no native dependency mechanism, so this field is the dependency relationship.
- Frontier query: scan children in filename order and select those with
  `Status: open`, an empty `Assignee`, and every `Blocked by` issue closed. Read metadata
  first; load question bodies only when taking or investigating a ticket.
- Resolution: append a dated entry under `Resolution comments`, set `Status` to
  `closed`, and append a named link with a one-line gist to the map's index.
- Research assets: record their throwaway branch, commit, and file path in the
  research ticket. Keep the branch local as requested by the user; do not push,
  open a PR, or merge it.

Keep the map an index, not a duplicate of ticket answers. Claim and update only
the ticket being worked; re-read metadata before changing it if another session
may have edited it. This file-based convention has no atomic multi-user claim
service, so concurrent sessions must coordinate their claims.

## Implementation Proposal

The [implementation graph](implementation/README.md) is separate from the
Wayfinder decision tickets and uses `implementation:` labels. The user approved
the spec and plan on 2026-10-12; its approval gate and the Wayfinder decisions are
closed. Implementation still follows each ticket's remaining dependencies.
