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

**U1 defect report (2026-10-08):** During unassisted play the user found the stones unreachable — the stone home positions were centered inside their own blocked segments, so the player could never touch them ("I can't run into the square block, so the stone can't really be touched"). Classification: Player Validation (comprehension/usability failure), negative evidence preserved.

Root cause: design error — stone home == blockedSeg center. Fixed by relocating each stone's home just below its blocked segment (inside the channel, reachable from below) and widening channels to keep them contiguous. Verified: 6/6 suite, real player drags the north stone home(745,430) to open notch(745,250) in ~3 s, full-phase smoke clean with zero page errors.

This is exactly the F1/F4 affordance-honesty class of bug the harvest was meant to catch earlier — flagged as a process note: the drawn-vs-collidable and reachability checks passed, but the *interaction reachability* (can the player physically touch the draggable) was not a planned check. Candidate harvest follow-up: add an "interactable must be reachable" probe to the validation plan template.

Awaiting the user's re-test.

**U2 defect report (2026-10-08):** Pushing the mid stone, the blocked segment disappeared as expected but the player became stuck between the snapped stone and a divider wall. Root cause: a permanent divider wall (y 674-700) sat flush against the mid channel's mouth (700-790), trapping the player in a 24px pocket once the segment opened. Classification: Player Validation (geometry/affordance defect), negative evidence preserved. Fixed by moving divider walls into the gaps between channels (y 545, 945), clear of every channel mouth. Verified: player no longer stuck after the snap (`blockedNow: false`), 6/6 suite, full smoke clean.

Process note: this is the same interactable-reachability / affordance class as U1, reinforcing the candidate harvest follow-up (add "interactable must be reachable and its success state must not trap the player" to the validation plan template).
