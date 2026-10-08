(function (root) {
  "use strict";
  const MAX_SPEED = 150;
  const ACCEL = 700;
  const DRAG = 3.2;
  const RADIUS = 10;
  const FRAME_CAP = 0.25;
  const PHYSICS_STEP = 0.05;
  const STEP_MAX = 4;
  function inputVector(keys) {
    const left = keys.ArrowLeft || keys.KeyA, right = keys.ArrowRight || keys.KeyD;
    const up = keys.ArrowUp || keys.KeyW, down = keys.ArrowDown || keys.KeyS;
    let x = (right ? 1 : 0) - (left ? 1 : 0), y = (down ? 1 : 0) - (up ? 1 : 0);
    if (x && y) { x *= Math.SQRT1_2; y *= Math.SQRT1_2; }
    return { x, y };
  }
  function boulderIsArchPosition(world, boulderState) { return world.boulderIsArch(boulderState); }
  function move(player, keys, elapsed, world, boulderState) {
    const direction = inputVector(keys);
    let remaining = Math.min(Math.max(elapsed || 0, 0), FRAME_CAP);
    const next = { ...player };
    const options = {};
    if (boulderState) {
      if (boulderIsArchPosition(world, boulderState)) options.arch = true;
      else if (!boulderState.ignoreForPlayer) options.boulderBlocked = boulderState;
    }
    while (remaining > 0) {
      const dt = Math.min(PHYSICS_STEP, remaining); remaining -= dt;
      // Buoyant swim: accelerate toward input, drag caps speed, inertia on release.
      next.vx = (next.vx || 0) + direction.x * ACCEL * dt;
      next.vy = (next.vy || 0) + direction.y * ACCEL * dt;
      const drag = Math.max(0, 1 - DRAG * dt);
      next.vx *= drag; next.vy *= drag;
      if (Math.hypot(next.vx, next.vy) < 0.5) { next.vx = 0; next.vy = 0; }
      const speed = Math.hypot(next.vx, next.vy);
      if (speed > MAX_SPEED) { next.vx *= MAX_SPEED / speed; next.vy *= MAX_SPEED / speed; }
      const dx = next.vx * dt, dy = next.vy * dt;
      const steps = Math.max(1, Math.ceil(Math.max(Math.abs(dx), Math.abs(dy)) / STEP_MAX));
      for (let i = 0; i < steps; i += 1) {
        const stepX = dx / steps, stepY = dy / steps;
        if (!world.blockedAt(next.x + stepX, next.y, RADIUS, options)) next.x += stepX; else next.vx = 0;
        if (!world.blockedAt(next.x, next.y + stepY, RADIUS, options)) next.y += stepY; else next.vy = 0;
      }
    }
    if (Math.hypot(next.vx || 0, next.vy || 0) > 12) next.facing = Math.abs(next.vx) > Math.abs(next.vy) ? (next.vx > 0 ? "east" : "west") : (next.vy > 0 ? "south" : "north");
    return next;
  }
  function push(player, keys, world, boulderState) {
    if (!boulderState || boulderIsArchPosition(world, boulderState)) return { boulder: boulderState, moved: false, player };
    const direction = inputVector(keys);
    if (!direction.x && !direction.y) return { boulder: boulderState, moved: false, player };
    const b = world.boulderCircle(boulderState);
    const dist = Math.hypot(player.x - b.x, player.y - b.y);
    if (dist > b.radius + RADIUS + 4) return { boulder: boulderState, moved: false, player };
    const toBoulder = Math.atan2(b.y - player.y, b.x - player.x);
    const pushAngle = Math.atan2(direction.y, direction.x);
    const aligned = Math.abs(Math.atan2(Math.sin(toBoulder - pushAngle), Math.cos(toBoulder - pushAngle))) < Math.PI / 3;
    if (!aligned) return { boulder: boulderState, moved: false, player };
    const step = 2;
    const nx = direction.x, ny = direction.y;
    const target = { x: boulderState.x + nx * step, y: boulderState.y + ny * step };
    const overlapsNarrows = world.boulderIsArch(target) || (() => { const n = world.narrows; return target.x + b.radius > n.x && target.x - b.radius < n.x + n.width && target.y + b.radius > n.y && target.y - b.radius < n.y + n.height; })();
    const hitsWorld = world.channel.concat(world.blockers).filter((s) => {
      if (s.kind !== "rockwall" || !overlapsNarrows) return true;
      const n = world.narrows; return !(s.y <= n.y && s.y + s.height >= n.y + n.height);
    }).some((s) => world.shapeBlocks(target.x, target.y, b.radius, s));
    if (hitsWorld) return { boulder: boulderState, moved: false, player };
    // Lock at the narrows center on first full span.
    let locked = target;
    if (!boulderIsArchPosition(world, boulderState) && world.boulderIsArch(target)) {
      const n = world.narrows; locked = { x: n.x + n.width / 2, y: n.y + n.height / 2 };
    }
    const followed = { ...player, x: player.x + nx * step, y: player.y + ny * step };
    return { boulder: locked, moved: true, player: followed };
  }
  function reset(world) { return { x: world.spawn.x, y: world.spawn.y, facing: world.spawn.facing, vx: 0, vy: 0 }; }
  function resetBoulder(world) { return { x: world.boulder.startX, y: world.boulder.startY }; }
  root.UnderseaRules = { MAX_SPEED, ACCEL, DRAG, RADIUS, FRAME_CAP, PHYSICS_STEP, STEP_MAX, inputVector, move, push, reset, resetBoulder, boulderIsArchPosition };
})(globalThis);
