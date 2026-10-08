(function () {
  "use strict";
  const canvas = document.querySelector("#game");
  const ctx = canvas.getContext("2d");
  const place = document.querySelector("#place");
  const resetButton = document.querySelector("#reset");
  const world = globalThis.TidalWorld;
  const rules = globalThis.TidalRules;
  const keys = {};
  let player = rules.reset(world);
  let stones = rules.resetStones(world);
  let phase = "calm"; // calm | rising | swim
  let tide = 0; // seconds elapsed in rising
  const revealed = {};
  let flavorText = "", flavorUntil = 0;
  let camera = { x: 0, y: 0 };
  let viewport = { width: innerWidth, height: innerHeight, dpr: 1 };
  let last = performance.now();

  function clearKeys() { Object.keys(keys).forEach((k) => delete keys[k]); }
  function reset() {
    clearKeys(); player = rules.reset(world); stones = rules.resetStones(world);
    phase = "calm"; tide = 0;
    Object.keys(revealed).forEach((k) => delete revealed[k]);
    place.textContent = ""; flavorText = ""; flavorUntil = 0;
    last = performance.now(); updateCamera();
  }
  function resize() {
    viewport = { width: innerWidth, height: innerHeight, dpr: Math.min(devicePixelRatio || 1, 2) };
    canvas.width = Math.round(viewport.width * viewport.dpr);
    canvas.height = Math.round(viewport.height * viewport.dpr);
    canvas.style.width = `${viewport.width}px`; canvas.style.height = `${viewport.height}px`;
    updateCamera();
  }
  function updateCamera() {
    camera.x = Math.max(0, Math.min(world.width - viewport.width, player.x - viewport.width / 2));
    camera.y = Math.max(0, Math.min(world.height - viewport.height, player.y - viewport.height / 2));
  }
  function floodLevel() { return phase === "swim" ? 1 : phase === "rising" ? Math.min(1, tide / rules.TIDE_SECONDS) : 0; }
  function drawReef(o) {
    ctx.fillStyle = "#7a7264"; ctx.beginPath(); ctx.arc(o.x, o.y, o.radius, 0, Math.PI * 2); ctx.fill();
    ctx.fillStyle = "rgba(255,255,255,.1)"; ctx.beginPath(); ctx.arc(o.x - o.radius * .3, o.y - o.radius * .3, o.radius * .45, 0, Math.PI * 2); ctx.fill();
  }
  function drawChannels() {
    const flood = floodLevel();
    world.channels.forEach((ch, i) => {
      const open = !world.segmentBlocked(i, stones);
      // Channel bed: damp sand, or water if flooded and open.
      if (open && flood > 0) {
        ctx.fillStyle = `rgba(90,160,190,${0.35 + flood * 0.55})`;
        ctx.fillRect(ch.rect.x, ch.rect.y, ch.rect.width * (flood >= 1 ? 1 : flood), ch.rect.height);
      } else {
        ctx.fillStyle = "rgba(230,215,170,.35)"; ctx.fillRect(ch.rect.x, ch.rect.y, ch.rect.width, ch.rect.height);
      }
      // Blocked segment stays visibly rocky unless opened.
      if (!open) { ctx.fillStyle = "#8a8272"; ctx.fillRect(ch.blockedSeg.x, ch.blockedSeg.y, ch.blockedSeg.width, ch.blockedSeg.height); }
      // Stone.
      const pos = stones[i] || ch.stone.home;
      ctx.fillStyle = open ? "#6f8f7a" : "#8f6f5a";
      ctx.beginPath(); ctx.arc(pos.x, pos.y, 16, 0, Math.PI * 2); ctx.fill();
      ctx.strokeStyle = "rgba(40,30,20,.5)"; ctx.lineWidth = 2; ctx.stroke();
      // Open notch marker.
      ctx.strokeStyle = "rgba(120,160,120,.6)"; ctx.setLineDash([4, 6]);
      ctx.beginPath(); ctx.arc(ch.stone.open.x, ch.stone.open.y, 16, 0, Math.PI * 2); ctx.stroke(); ctx.setLineDash([]);
    });
  }
  function drawStartRock() {
    const s = world.startRock;
    ctx.fillStyle = "#8d8578"; ctx.fillRect(s.x, s.y, s.width, s.height);
    ctx.strokeStyle = "#5c5648"; ctx.lineWidth = 2; ctx.strokeRect(s.x, s.y, s.width, s.height);
  }
  function drawPool() {
    ctx.fillStyle = "#4a90a8"; ctx.beginPath(); ctx.arc(world.pool.x, world.pool.y, world.pool.radius, 0, Math.PI * 2); ctx.fill();
    ctx.strokeStyle = "rgba(240,248,250,.5)"; ctx.lineWidth = 3; ctx.beginPath(); ctx.arc(world.pool.x, world.pool.y, world.pool.radius - 6, 0, Math.PI * 2); ctx.stroke();
  }
  function drawPlayer() {
    const bob = phase === "swim" ? Math.sin(performance.now() / 300) * 2 : 0;
    ctx.fillStyle = "rgba(40,50,40,.22)"; ctx.beginPath(); ctx.ellipse(player.x, player.y + 10, 11, 4, 0, 0, Math.PI * 2); ctx.fill();
    ctx.fillStyle = "#f0d8a8"; ctx.beginPath(); ctx.arc(player.x, player.y - 6 + bob, 7, 0, Math.PI * 2); ctx.fill();
    ctx.fillStyle = phase === "swim" ? "#2e7d8c" : "#7a5a8c";
    ctx.beginPath(); ctx.ellipse(player.x, player.y + 3 + bob, 7, 10, 0, 0, Math.PI * 2); ctx.fill();
  }
  function render() {
    ctx.setTransform(viewport.dpr, 0, 0, viewport.dpr, 0, 0);
    ctx.fillStyle = "#d9c99a"; ctx.fillRect(0, 0, viewport.width, viewport.height); // dry flat
    ctx.save(); ctx.translate(-camera.x, -camera.y);
    ctx.fillStyle = "rgba(255,250,225,.3)"; for (let x = 100; x < world.width; x += 220) for (let y = 90; y < world.height; y += 200) { ctx.beginPath(); ctx.ellipse(x, y, 55, 16, 0, 0, Math.PI * 2); ctx.fill(); }
    world.grassTiles.forEach(([x, y]) => { ctx.fillStyle = "#8aa06a"; ctx.beginPath(); ctx.arc(x, y, 12, 0, Math.PI * 2); ctx.fill(); });
    drawChannels();
    drawStartRock();
    drawPool();
    world.blockers.filter((o) => o.kind === "reef").forEach(drawReef);
    world.blockers.filter((o) => o.kind === "wall").forEach((o) => { ctx.fillStyle = "#7a7264"; ctx.fillRect(o.x, o.y, o.width, o.height); });
    // Tide Arch scenery.
    ctx.strokeStyle = "#8a8272"; ctx.lineWidth = 20; ctx.lineCap = "round"; ctx.beginPath(); ctx.arc(1150, 500, 55, Math.PI, 0); ctx.stroke();
    // Reveal auras.
    world.sights.forEach((s) => {
      if (!s.reveal || !revealed[s.id]) return;
      ctx.save(); ctx.strokeStyle = "rgba(255,244,180,.55)"; ctx.lineWidth = 3; ctx.setLineDash([8, 10]);
      ctx.beginPath(); ctx.arc(s.reveal.x, s.reveal.y, s.reveal.radius * .6, 0, Math.PI * 2); ctx.stroke(); ctx.restore();
    });
    drawPlayer(); ctx.restore();
    // Swim-phase water tint over the whole viewport.
    if (phase !== "calm") {
      ctx.setTransform(viewport.dpr, 0, 0, viewport.dpr, 0, 0);
      ctx.fillStyle = `rgba(70,140,180,${floodLevel() * 0.28})`; ctx.fillRect(0, 0, viewport.width, viewport.height);
    }
    const sight = world.nearestSight(player.x, player.y);
    place.textContent = sight ? sight.name : "";
    if (performance.now() < flavorUntil && flavorText) {
      ctx.setTransform(viewport.dpr, 0, 0, viewport.dpr, 0, 0);
      ctx.font = "italic 15px Georgia, serif"; ctx.textAlign = "center";
      ctx.fillStyle = "rgba(40,44,36,.95)"; ctx.fillText(flavorText, viewport.width / 2, viewport.height - 28);
    }
  }
  function frame(now) {
    const elapsed = (now - last) / 1000;
    if (phase === "calm") {
      const d = rules.drag(player, keys, world, stones);
      if (d.moved) { stones = d.stones; player = d.player; }
      else player = rules.moveCalm(player, keys, elapsed, world, stones);
      if (rules.allPlaced(world, stones) || (rules.anyPlaced(world, stones) && rules.onStartRock(player, world))) {
        phase = "rising"; tide = 0;
      }
    } else if (phase === "rising") {
      tide += elapsed;
      player = rules.moveCalm(player, keys, elapsed, world, stones);
      if (tide >= rules.TIDE_SECONDS) { phase = "swim"; player = { ...player, vx: 0, vy: 0 }; }
    } else {
      player = rules.moveSwim(player, keys, elapsed, world, stones);
    }
    const reveal = world.revealFor(player.x, player.y);
    if (reveal && !revealed[reveal.id]) { revealed[reveal.id] = true; flavorText = reveal.text; flavorUntil = now + 4000; }
    last = now; updateCamera(); render(); requestAnimationFrame(frame);
  }
  addEventListener("keydown", (e) => { if (["ArrowUp","ArrowDown","ArrowLeft","ArrowRight","KeyW","KeyA","KeyS","KeyD"].includes(e.code)) { keys[e.code] = true; e.preventDefault(); } });
  addEventListener("keyup", (e) => { delete keys[e.code]; });
  addEventListener("blur", () => { clearKeys(); last = performance.now(); });
  document.addEventListener("visibilitychange", () => { if (document.hidden) clearKeys(); last = performance.now(); });
  addEventListener("resize", resize); resetButton.addEventListener("click", reset);
  globalThis.__tidalDebug = {
    get player() { return { ...player }; }, get camera() { return { ...camera }; }, get heldKeys() { return Object.keys(keys); },
    get stones() { return stones.map((s) => ({ ...s })); }, get phase() { return phase; }, get tide() { return tide; },
    get revealed() { return { ...revealed }; }, get flavor() { return flavorText; },
    setPlayer(x, y) { player = { ...player, x, y, vx: 0, vy: 0 }; updateCamera(); },
    setStone(i, x, y) { stones[i] = { x, y }; },
    reset, world, rules };
  resize(); requestAnimationFrame(frame);
})();
