# Prototype Validation Plan

## Authority and Authorization

- Project and current record: `<path>`
- Authoritative rules: `<path and rule IDs>`
- Design Brief approval: `<explicit reference>`
- Prototype-scope approval: `<explicit reference>`
- Input/approval classification: `sourced fact | Design Assumption | simulated input | simulated approval`

## Question and Fidelity

- Validation question: `<observable question>`
- Intended appeal: `<what the player may enjoy discovering, performing, expressing, or feeling>`
- Observable signals: `<what an unassisted player does, says, or chooses that bears on the question>`
- Decision after evidence: `continue | clarify | revise | stop`; `<criteria and owner>`
- Minimum playable content: `<controls, state feedback, terminal result>`
- Minimum fidelity: `<what must be represented and why>`
- Simplified or omitted aspects: `<items and validation limitation>`

## Scope and Budget

- Included scope: `<list>`
- Excluded scope: `<list>`
- Maximum iterations: `<project-supplied value, or conservative proposed value pending confirmation>`
- Time limit: `<value or missing>`
- Spending limit: `<value or missing>`
- External actions authorized: `<none/local only/etc.>`
- Stop condition: `<testable completion or budget boundary>`

## Evidence Plan

| Check | Method | Expected evidence | Execution status | Limitation |
| --- | --- | --- | --- | --- |
| `<rule case>` | `<deterministic test>` | `<output>` | `not run / expected outcome` | `<does not prove experience>` |
| `<rendered-vs-collider correspondence>` | `<deterministic probe points against shared geometry>` | `<output>` | `not run / expected outcome` | `<does not prove readability or experience>` |
| `<affordance honesty: drawn routes do not imply blocked traversal>` | `<visual diff or probe>` | `<output>` | `not run / expected outcome` | `<does not prove appeal>` |
| `<connection integrity: required connections exist and cannot be bypassed>` | `<topology check>` | `<output>` | `not run / expected outcome` | `<coarse grids may miss runtime collision>` |
| `<interaction traversal>` | `<live input: approach -> initiate -> complete -> leave changed state>` | `<recorded reachable interaction and safe exit>` | `not run / expected outcome` | `<does not prove appeal or authorship>` |
| `<opportunity promise-to-payoff chain>` | `<notice cue -> enter or avoid -> payoff or retreat -> choose next; record reason>` | `<choice sequence and stated/observable reason>` | `not run / expected outcome` | `<does not prove sustained appeal alone>` |
| `<authorship>` | `<player creates two materially different states/routes/outcomes and explains what each enabled>` | `<actions and consequences>` | `not run / expected outcome` | `<opening a prescribed route fails this check>` |
| `<unassisted observation>` | `<participant attempts without explanation>` | `<actions, hesitation, and outcome>` | `not run / expected outcome` | `<comprehension/desirability limit>` |
| `<assisted understanding>` | `<explanation followed by question>` | `<response>` | `not run / expected outcome` | `<cannot replace unassisted observation>` |
| `<desirability question>` | `<separate approved playtest>` | `<response/choice>` | `not run / expected outcome` | `<not yet run>` |

Planned checks are not evidence. Record the actual command or input, observed output, artifact or log path, and version in the evidence log before classifying a completed check as rule verification, developer observation, simulated result, or Player Validation.

When independent implementation or review cannot be performed, add a planned independent recheck and record the unavailable capability rather than replacing it with self-validation.
