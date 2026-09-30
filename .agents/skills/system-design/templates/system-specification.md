# System Specification

## Authority

- Project: `<name>`
- Document language: `<confirmed language>`
- Design Brief approval: `<reference>`
- Core gameplay and prototype scope approval: `<reference>`
- Status: `authoritative | draft pending confirmation`
- Canonical terminology: `<CONTEXT.md or project glossary path>`

Other documents refer to rule IDs in this specification and do not restate their semantics.

## State and Initial Parameters

| State ID | Meaning | Type or range | Initial value | Observable feedback |
| --- | --- | --- | --- | --- |
| `S-<id>` | `<meaning>` | `<type/range>` | `<value>` | `<value>` |

## Rule Catalog

| Rule ID | Trigger or legal input | Preconditions | Ordered state transition | Observable outcome | Edge cases |
| --- | --- | --- | --- | --- | --- |
| `R-<id>` | `<event/action>` | `<conditions>` | `<exact ordered changes>` | `<player-visible result>` | `<boundaries/invalid input>` |

## Content and Feedback

| Content ID | Rule IDs affected | Player-facing purpose | Required art, narrative, or audio cue |
| --- | --- | --- | --- |
| `C-<id>` | `<rule IDs>` | `<value>` | `<value or none>` |

## Verification Cases

| Case | Initial state | Inputs in order | Expected rule IDs and final state | Evidence classification |
| --- | --- | --- | --- | --- |
| `V-<id>` | `<state>` | `<inputs>` | `<deterministic result>` | `rule verification | simulated result` |

## Unvalidated Claims and Handoff Notes

| Item | Classification | Limitation or developer question |
| --- | --- | --- |
| `<balance/experience/technical item>` | `<classification>` | `<value>` |
