# Three Stones: Validation and Budget

Authority: brief.md (confirmed), gameplay-proposal.md (Candidate A confirmed), system.md v1.0. Start: 2026-10-08 03:04:57 UTC. Absolute stop: 05:04:57 UTC (2h). 1 iteration. Zero spend.

## Experience Question

Does build-then-traverse hold for this user: (F6) initial attraction — does the user engage the stones unprompted; structure test — during the swim, does the user recognize and value that the route is self-authored, and would they do a second cycle differently?

## Evidence

### Implementation

Completed 2026-10-08, within budget. **Downgraded independence**: implemented in-thread by root (worker subagent routing remained unreliable this session) and self-verified.

Verification evidence:
- Full suite: 6 tests pass (`prototypes/tidal/tests/test_tidal.py`) — calm walk + collision, drag-to-open one-way snap, tide trigger + pool reachability state, swim physics, full transient reset, real-frame movement with page-error collection.
- Real-browser smoke: all three phases traversed (calm → rising → swim); tide triggered by start rock; pool reveal fired once with flavor text and "The Stranded Pool" label; zero page/console errors. Screenshots: `calm-initial.png`, `rising.png`, `swim-pool.png` under `prototypes/tidal/tests/evidence/`.
- Execution errors preserved: a snap-threshold mismatch (segmentBlocked geometric threshold vs drag overshoot) caused drag to stall at 1-7px from the notch twice; a test frame-cap misunderstanding (0.5s > 0.25s FRAME_CAP); a probe-radius-0 strict-inequality false negative. All fixed; recorded as execution errors, not instruction gaps.

### Player Validation

Not performed. Awaiting the user's unassisted first play per F8, with a post-play question on whether the route felt self-authored.
