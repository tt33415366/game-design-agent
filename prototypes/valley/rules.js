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
  function move(player, keys, elapsed, world, logState) {
    const direction = inputVector(keys);
    let remaining = Math.min(Math.max(elapsed || 0, 0), FRAME_CAP);
    const next = { ...player };
    const options = {};
    if (logState) {
      if (logIsPlankPosition(world, logState)) options.plank = true;
      else if (!logState.ignoreForPlayer) options.logBlocked = logState;
    }
    while (remaining > 0) {
      const dt = Math.min(PHYSICS_STEP, remaining); remaining -= dt;
      const dx = direction.x * SPEED * dt, dy = direction.y * SPEED * dt;
      const steps = Math.max(1, Math.ceil(Math.max(Math.abs(dx), Math.abs(dy)) / STEP_MAX));
      for (let i = 0; i < steps; i += 1) {
        const stepX = dx / steps, stepY = dy / steps;
        if (!world.blockedAt(next.x + stepX, next.y, RADIUS, options)) next.x += stepX;
        if (!world.blockedAt(next.x, next.y + stepY, RADIUS, options)) next.y += stepY;
      }
    }
    if (direction.x || direction.y) next.facing = Math.abs(direction.x) > Math.abs(direction.y) ? (direction.x > 0 ? "east" : "west") : (direction.y > 0 ? "south" : "north");
    return next;
  }
  function logIsPlankPosition(world, logState) { return world.logIsPlank(logState); }
  function push(player, keys, world, logState) {
    if (!logState || logIsPlankPosition(world, logState)) return { log: logState, moved: false, player };
    const direction = inputVector(keys);
    if (!direction.x && !direction.y) return { log: logState, moved: false, player };
    const log = world.logRect(logState);
    const nearX = player.x > log.x - RADIUS - 4 && player.x < log.x + log.width + RADIUS + 4;
    const nearY = player.y > log.y - RADIUS - 4 && player.y < log.y + log.height + RADIUS + 4;
    if (!nearX || !nearY) return { log: logState, moved: false, player };
    const pushingEast = direction.x > 0 && player.x < log.x, pushingWest = direction.x < 0 && player.x > log.x + log.width;
    const pushingSouth = direction.y > 0 && player.y < log.y, pushingNorth = direction.y < 0 && player.y > log.y + log.height;
    if (!pushingEast && !pushingWest && !pushingSouth && !pushingNorth) return { log: logState, moved: false, player };
    const step = 2;
    let target = { x: logState.x + (pushingEast ? step : pushingWest ? -step : 0), y: logState.y + (pushingSouth ? step : pushingNorth ? -step : 0) };
    // Lock the log the first time it would fully span the narrows: clamp to the centered
    // plank position instead of sliding past, so it stays usable as a crossing.
    if (!logIsPlankPosition(world, logState) && world.logIsPlank(target)) {
      const n = world.narrows;
      target = { x: n.x + n.width / 2, y: logState.y };
    }
    const targetRect = world.logRect(target);
    const overlapsNarrows = world.logIsPlank(target);
    const narrowsRect = world.rect(world.narrows.x, world.narrows.y, world.narrows.width, world.narrows.height, "narrows");
    const partiallyInNarrows = targetRect.x < narrowsRect.x + narrowsRect.width && targetRect.x + targetRect.width > narrowsRect.x && targetRect.y < narrowsRect.y + narrowsRect.height && targetRect.y + targetRect.height > narrowsRect.y;
    const hitsWorld = world.water.concat(world.blockers).filter((s) => {
      if (s.kind !== "water" || !partiallyInNarrows) return true;
      return !(s.y <= narrowsRect.y && s.y + s.height >= narrowsRect.y + narrowsRect.height);
    }).some((s) => world.shapeBlocks(targetRect.x + targetRect.width / 2, targetRect.y + targetRect.height / 2, Math.max(targetRect.width, targetRect.height) / 2, s));
    if (hitsWorld && !overlapsNarrows) return { log: logState, moved: false, player };
    // Advance the player by the same step so pusher and log stay in contact. The log at
    // its new position is ignored for this step so it does not block the player's follow.
    const followed = { ...player };
    if (pushingEast) followed.x += step; else if (pushingWest) followed.x -= step;
    if (pushingSouth) followed.y += step; else if (pushingNorth) followed.y -= step;
    return { log: target, moved: true, player: followed };
  }
  function reset(world) { return { x: world.spawn.x, y: world.spawn.y, facing: world.spawn.facing }; }
  function resetLog(world) { return { x: world.log.startX, y: world.log.startY }; }
  root.ValleyRules = { SPEED, RADIUS, FRAME_CAP, PHYSICS_STEP, STEP_MAX, inputVector, move, push, reset, resetLog, logIsPlankPosition };
})(globalThis);
