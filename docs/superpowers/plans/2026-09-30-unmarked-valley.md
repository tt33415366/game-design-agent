# Unmarked Valley Implementation Plan

> **For agentic workers:** Use bounded delegated implementation, then independent verification/review. Root owns scope, authoritative rules, approval/budget ledger, and integration. Do not alter existing uncommitted work.

**Goal:** Deliver the U2-approved local browser exploration slice within three hours and at most two iterations.

**Architecture:** Static direct-open browser page, Canvas rendering, one authored world geometry source, pure movement/collision helpers shared with tests. Local visual assets with retained licenses. No build tool, runtime network requirement, physics simulation, or gameplay framework needed for this bounded original traversal model.

**Tech Stack:** Native browser Canvas/JavaScript; existing Python Playwright tooling for browser-executed tests.

**Spec:** `docs/designs/browser-exploration/brief.md` and `system.md` in that directory. Actual U2 selects and approves A; other concepts are not authorized.

## Global Constraints

- Scope/budget and rule authority remain in the linked spec; no extra mechanics, giant world, 3D, combat, collecting, or quest checklist.
- Deadline 2026-09-30 11:12:39 UTC; maximum two iterations; stop and report if exhausted.
- Asset worker owns `prototypes/valley/assets/` only. Game implementer owns other `prototypes/valley/` files. Root owns project design docs and this plan. Verification/review are read-only unless a bounded fix is assigned.
- Preserve all prior changes, especially salvage and agent instructions. No commits or publishing requested.

## Tasks

- [x] Source free local visual assets and retain license/provenance; report atlas rectangles to implementer.
- [x] Write failing tests for movement, collision, reset, and route connectivity; implement shared rules and authored level.
- [x] Build the playable full-viewport scene with movement, camera, place feedback, and restart.
- [x] Run browser tests, independent route checks, screenshots and visual inspection at desktop/mobile sizes; log results and any defects.
- [x] Apply at most one bounded corrective iteration if needed; rerun relevant checks.
- [x] Update approval/budget/evidence records and provide the directly openable HTML link with basic controls but no destination recommendation.
