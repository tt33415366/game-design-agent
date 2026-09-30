(function (root) {
  "use strict";
  const SPEED = 160;
  const RADIUS = 10;
  const FRAME_CAP = 0.25;
  const PHYSICS_STEP = 0.05;
  const STEP_MAX = 4;
  function inputVector(keys) {
    const left = keys.ArrowLeft || keys.KeyA;
    const right = keys.ArrowRight || keys.KeyD;
    const up = keys.ArrowUp || keys.KeyW;
    const down = keys.ArrowDown || keys.KeyS;
    let x = (right ? 1 : 0) - (left ? 1 : 0);
    let y = (down ? 1 : 0) - (up ? 1 : 0);
    if (x && y) { x *= Math.SQRT1_2; y *= Math.SQRT1_2; }
    return { x, y };
  }
  function move(player, keys, elapsed, world) {
    const direction = inputVector(keys);
    let remaining = Math.min(Math.max(elapsed || 0, 0), FRAME_CAP);
    const next = { ...player };
    while (remaining > 0) {
      const dt = Math.min(PHYSICS_STEP, remaining); remaining -= dt;
      const dx = direction.x * SPEED * dt, dy = direction.y * SPEED * dt;
      const steps = Math.max(1, Math.ceil(Math.max(Math.abs(dx), Math.abs(dy)) / STEP_MAX));
      for (let i = 0; i < steps; i += 1) {
        const stepX = dx / steps, stepY = dy / steps;
        if (!world.blockedAt(next.x + stepX, next.y, RADIUS)) next.x += stepX;
        if (!world.blockedAt(next.x, next.y + stepY, RADIUS)) next.y += stepY;
      }
    }
    if (direction.x || direction.y) next.facing = Math.abs(direction.x) > Math.abs(direction.y) ? (direction.x > 0 ? "east" : "west") : (direction.y > 0 ? "south" : "north");
    return next;
  }
  function reset(world) { return { x: world.spawn.x, y: world.spawn.y, facing: world.spawn.facing }; }
  root.ValleyRules = { SPEED, RADIUS, FRAME_CAP, PHYSICS_STEP, STEP_MAX, inputVector, move, reset };
})(globalThis);
