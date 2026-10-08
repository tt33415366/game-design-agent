(function (root) {
  "use strict";
  const WALK_SPEED = 160;
  const SWIM = { MAX: 150, ACCEL: 700, DRAG: 3.2 };
  const RADIUS = 10;
  const FRAME_CAP = 0.25;
  const PHYSICS_STEP = 0.05;
  const STEP_MAX = 4;
  const TIDE_SECONDS = 20;
  function inputVector(keys) {
    const l = keys.ArrowLeft || keys.KeyA, r = keys.ArrowRight || keys.KeyD;
    const u = keys.ArrowUp || keys.KeyW, d = keys.ArrowDown || keys.KeyS;
    let x = (r ? 1 : 0) - (l ? 1 : 0), y = (d ? 1 : 0) - (u ? 1 : 0);
    if (x && y) { x *= Math.SQRT1_2; y *= Math.SQRT1_2; }
    return { x, y };
  }
  function moveCalm(player, keys, elapsed, world, stones) {
    const direction = inputVector(keys);
    let remaining = Math.min(Math.max(elapsed || 0, 0), FRAME_CAP);
    const next = { ...player };
    const options = { stones, calm: true };
    while (remaining > 0) {
      const dt = Math.min(PHYSICS_STEP, remaining); remaining -= dt;
      const dx = direction.x * WALK_SPEED * dt, dy = direction.y * WALK_SPEED * dt;
      const steps = Math.max(1, Math.ceil(Math.max(Math.abs(dx), Math.abs(dy)) / STEP_MAX));
      for (let i = 0; i < steps; i += 1) {
        const sx = dx / steps, sy = dy / steps;
        if (!world.blockedAt(next.x + sx, next.y, RADIUS, options)) next.x += sx;
        if (!world.blockedAt(next.x, next.y + sy, RADIUS, options)) next.y += sy;
      }
    }
    if (direction.x || direction.y) next.facing = Math.abs(direction.x) > Math.abs(direction.y) ? (direction.x > 0 ? "east" : "west") : (direction.y > 0 ? "south" : "north");
    return next;
  }
  function moveSwim(player, keys, elapsed, world, stones) {
    const direction = inputVector(keys);
    let remaining = Math.min(Math.max(elapsed || 0, 0), FRAME_CAP);
    const next = { ...player };
    const options = { stones, calm: false };
    while (remaining > 0) {
      const dt = Math.min(PHYSICS_STEP, remaining); remaining -= dt;
      next.vx = (next.vx || 0) + direction.x * SWIM.ACCEL * dt;
      next.vy = (next.vy || 0) + direction.y * SWIM.ACCEL * dt;
      const drag = Math.max(0, 1 - SWIM.DRAG * dt);
      next.vx *= drag; next.vy *= drag;
      if (Math.hypot(next.vx, next.vy) < 0.5) { next.vx = 0; next.vy = 0; }
      const sp = Math.hypot(next.vx, next.vy);
      if (sp > SWIM.MAX) { next.vx *= SWIM.MAX / sp; next.vy *= SWIM.MAX / sp; }
      const dx = next.vx * dt, dy = next.vy * dt;
      const steps = Math.max(1, Math.ceil(Math.max(Math.abs(dx), Math.abs(dy)) / STEP_MAX));
      for (let i = 0; i < steps; i += 1) {
        const sx = dx / steps, sy = dy / steps;
        if (!world.blockedAt(next.x + sx, next.y, RADIUS, options)) next.x += sx; else next.vx = 0;
        if (!world.blockedAt(next.x, next.y + sy, RADIUS, options)) next.y += sy; else next.vy = 0;
      }
    }
    if (Math.hypot(next.vx || 0, next.vy || 0) > 12) next.facing = Math.abs(next.vx) > Math.abs(next.vy) ? (next.vx > 0 ? "east" : "west") : (next.vy > 0 ? "south" : "north");
    return next;
  }
  // Drag: player adjacent to a stone and pressing along the channel's vertical axis moves
  // the stone toward the open notch. One-way: once snapped placed it cannot return.
  function drag(player, keys, world, stones) {
    const direction = inputVector(keys);
    if (!direction.x && !direction.y) return { stones, moved: false, player, placedIndex: -1 };
    const nextStones = stones.slice();
    let nextPlayer = { ...player }, moved = false, placedIndex = -1;
    for (let i = 0; i < world.channels.length; i += 1) {
      const ch = world.channels[i];
      const pos = nextStones[i] || { ...ch.stone.home };
      if (!world.segmentBlocked(i, nextStones)) continue; // already placed/open
      const dist = Math.hypot(nextPlayer.x - pos.x, nextPlayer.y - pos.y);
      if (dist > 16 + RADIUS + 6) continue;
      // Stones slide vertically between home and open notches.
      const toward = ch.stone.open.y < ch.stone.home.y ? -1 : 1;
      if (direction.y * toward <= 0) continue;
      const step = 2 * toward;
      const targetY = pos.y + step;
      const overshoot = toward < 0 ? targetY <= ch.stone.open.y : targetY >= ch.stone.open.y;
      if (overshoot) {
        nextStones[i] = { ...ch.stone.open };
        placedIndex = i;
      } else {
        nextStones[i] = { x: pos.x, y: targetY };
      }
      nextPlayer = { ...nextPlayer, y: nextPlayer.y + step };
      moved = true;
      break;
    }
    return { stones: nextStones, moved, player: nextPlayer, placedIndex };
  }
  function allPlaced(world, stones) { return world.channels.every((_, i) => !world.segmentBlocked(i, stones)); }
  function anyPlaced(world, stones) { return world.channels.some((_, i) => !world.segmentBlocked(i, stones)); }
  function onStartRock(player, world) { const s = world.startRock; return player.x > s.x && player.x < s.x + s.width && player.y > s.y && player.y < s.y + s.height; }
  function reset(world) { return { x: world.spawn.x, y: world.spawn.y, facing: world.spawn.facing, vx: 0, vy: 0 }; }
  function resetStones(world) { return world.channels.map((ch) => ({ ...ch.stone.home })); }
  root.TidalRules = { WALK_SPEED, SWIM, RADIUS, FRAME_CAP, PHYSICS_STEP, STEP_MAX, TIDE_SECONDS, inputVector, moveCalm, moveSwim, drag, allPlaced, anyPlaced, onStartRock, reset, resetStones };
})(globalThis);
