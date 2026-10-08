# Sunlight Shelf: Validation and Budget

Authority: brief.md (confirmed), gameplay-proposal.md (Candidate A confirmed), system.md v1.0. Start: 2026-10-08 02:29:28 UTC. Absolute stop: 04:29:28 UTC (2h). 1 iteration. Zero spend.

## Experience Question

Does Candidate A hold for this user: (F6) initial attraction — does the user investigate unprompted, and does the crevice *tempt*; sustained interest — after the first reveal, does the user seek another sight or dare the crevice?

## Evidence

### Planned (all `not run`)

See system.md Planned Verification: swim physics, collision, reset, blur, camera, topology (arch sole crossing, crevice reachable without arch), rendered-vs-collider, affordance honesty, real game-loop smoke, reveal-once, screenshots. First play session unassisted.

### Implementation

Completed 2026-10-08, within budget. **Downgraded independence**: the delegated worker subagent failed twice (upstream 502-class provider errors), so root implemented in-thread per the orchestrator fallback rule and self-verified.

Verification evidence:
- Full suite: 8 tests pass (`prototypes/undersea/tests/test_undersea.py`) — swim inertia/coast/stop, low-fps, collision, reset/blur, topology (sights + crevice reachable, narrows gap open, arch optional), boulder push, reveal-once, resize, real-frame movement with page-error collection.
- Real-browser smoke: boulder pushed to a locked arch; arch and crevice reveals fired once with flavor text; crevice shows a radial dark vignette and "The Crevice" place label; zero page/console errors. Screenshots in `prototypes/undersea/tests/evidence/` (`initial`, `boulder-push`, `arch-reveal`, `crevice-edge`, `crevice-heart`).
- Execution errors preserved: one world.js syntax error caught by `node --check`; three initial test failures (drag asymptote, a mis-aimed topology probe, and a wrong "sole crossing" assumption) — the last required a design clarification: the narrows gap is always swimmable, the arch is a wider optional shortcut, not the sole crossing. system.md R08 wording should be corrected to match (noted as a documentation debt, does not change behavior).

### Player Validation

Not performed. Awaiting the user's unassisted first play per F8.
