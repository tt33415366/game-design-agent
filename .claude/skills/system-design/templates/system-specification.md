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

## Pressure Semantics

| Intended pressure | Atmospheric cue | Spatial commitment | Punishment or fail state | Numeric resource | Deliberate exclusions |
| --- | --- | --- | --- | --- | --- |
| `<pressure or none>` | `<sensory or environmental signal>` | `<what route, timing, or position commits the player>` | `<rule ID or none>` | `<state ID or none>` | `<what is intentionally not used and why>` |

Atmospheric pressure is not evidence of a numeric resource system. Specify each separately so implementation does not introduce an unapproved meter, countdown, damage model, or fail state.

## Verification Cases

| Case | Initial state | Inputs in order | Expected rule IDs and final state | Execution status and evidence |
| --- | --- | --- | --- | --- |
| `V-<id>` | `<state>` | `<inputs>` | `<deterministic expected result>` | `not run / expected outcome; retain simulated labels where applicable` |

Planned cases are specifications, not executed rule-verification evidence. Promote a case only with the actual command or input, observed output, artifact or log path, and version.

## Unvalidated Claims and Handoff Notes

| Item | Classification | Limitation or developer question |
| --- | --- | --- |
| `<balance/experience/technical item>` | `<classification>` | `<value>` |
