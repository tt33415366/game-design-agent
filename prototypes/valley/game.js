(function () {
  "use strict";
  const canvas = document.querySelector("#game");
  const ctx = canvas.getContext("2d");
  const place = document.querySelector("#place");
  const resetButton = document.querySelector("#reset");
  const world = globalThis.ValleyWorld;
  const rules = globalThis.ValleyRules;
  const keys = {};
  const art = new Image();
  art.src = "assets/kenney-tiny-town-tilemap.png";
  const character = new Image();
  character.src = "assets/kenney-tiny-dungeon-tilemap.png";
  let player = rules.reset(world);
  let camera = { x: 0, y: 0 };
  let viewport = { width: innerWidth, height: innerHeight, dpr: 1 };
  let last = performance.now();

  function clearKeys() { Object.keys(keys).forEach((key) => delete keys[key]); }
  function reset() { clearKeys(); player = rules.reset(world); place.textContent = ""; last = performance.now(); updateCamera(); }
  function resize() {
    viewport = { width: innerWidth, height: innerHeight, dpr: Math.min(devicePixelRatio || 1, 2) };
    canvas.width = Math.round(viewport.width * viewport.dpr);
    canvas.height = Math.round(viewport.height * viewport.dpr);
    canvas.style.width = `${viewport.width}px`;
    canvas.style.height = `${viewport.height}px`;
    updateCamera();
  }
  function updateCamera() {
    camera.x = Math.max(0, Math.min(world.width - viewport.width, player.x - viewport.width / 2));
    camera.y = Math.max(0, Math.min(world.height - viewport.height, player.y - viewport.height / 2));
  }
  function drawPath(path) {
    ctx.beginPath();
    path.points.forEach(([x, y], index) => index ? ctx.lineTo(x, y) : ctx.moveTo(x, y));
    ctx.strokeStyle = "#dfc982"; ctx.lineWidth = path.width; ctx.lineCap = "round"; ctx.lineJoin = "round"; ctx.stroke();
    ctx.strokeStyle = "rgba(255,250,210,.44)"; ctx.lineWidth = Math.max(8, path.width - 25); ctx.stroke();
  }
  function drawTree(x, y, radius, dark) {
    ctx.fillStyle = "#62452d"; ctx.beginPath(); ctx.arc(x, y, radius, 0, Math.PI * 2); ctx.fill();
    ctx.fillStyle = "#81583b"; ctx.beginPath(); ctx.arc(x - radius * .18, y - radius * .1, radius * .42, 0, Math.PI * 2); ctx.fill();
    ctx.fillStyle = dark ? "#326543" : "#4d8c48";
    [[0,-1.15,.95],[-.62,-.48,.72],[.62,-.48,.72],[0,-.42,.94]].forEach(([px, py, scale]) => { ctx.beginPath(); ctx.arc(x + radius * px, y + radius * py, radius * scale, 0, Math.PI * 2); ctx.fill(); });
    ctx.fillStyle = "rgba(180,220,100,.25)"; ctx.beginPath(); ctx.arc(x - radius * .3, y - radius * 1.35, radius * .3, 0, Math.PI * 2); ctx.fill();
  }
  function drawAtlasTile(column, row, x, y, scale) {
    if (!art.complete || !art.naturalWidth) return;
    ctx.imageSmoothingEnabled = false;
    ctx.drawImage(art, column * 17, row * 17, 16, 16, x, y, 16 * scale, 16 * scale);
  }
  function drawRuin() {
    ctx.fillStyle = "#737878";
    world.blockers.filter((o) => o.kind === "ruin").forEach((o) => ctx.fillRect(o.x, o.y, o.width, o.height));
    ctx.fillStyle = "#aeb1a7"; ctx.fillRect(383, 225, 92, 20);
    ctx.fillStyle = "#313d40"; ctx.fillRect(404, 275, 33, 72);
  }
  function drawBridge(bridge) {
    ctx.fillStyle = "#64452f"; ctx.fillRect(bridge.x, bridge.y, bridge.width, bridge.height);
    ctx.fillStyle = "#bd8b50"; for (let x = bridge.x + 8; x < bridge.x + bridge.width - 4; x += 18) ctx.fillRect(x, bridge.y + 4, 12, bridge.height - 8);
    ctx.fillStyle = "#3d2a21"; ctx.fillRect(bridge.x, bridge.y, bridge.width, 4); ctx.fillRect(bridge.x, bridge.y + bridge.height - 4, bridge.width, 4);
  }
  function drawPlayer() {
    ctx.fillStyle = "rgba(36,48,33,.22)"; ctx.beginPath(); ctx.ellipse(player.x, player.y + 11, 12, 5, 0, 0, Math.PI * 2); ctx.fill();
    if (character.complete && character.naturalWidth) {
      ctx.imageSmoothingEnabled = false;
      ctx.drawImage(character, 17, 136, 16, 16, player.x - 16, player.y - 20, 32, 32);
    } else {
      ctx.fillStyle = "#d8b173"; ctx.beginPath(); ctx.arc(player.x, player.y - 8, 7, 0, Math.PI * 2); ctx.fill();
      ctx.fillStyle = "#bd4938"; ctx.beginPath(); ctx.arc(player.x, player.y - 11, 8, Math.PI, 0); ctx.lineTo(player.x + 7, player.y - 6); ctx.lineTo(player.x - 7, player.y - 6); ctx.fill();
      ctx.fillStyle = "#2d5967"; ctx.fillRect(player.x - 7, player.y - 3, 14, 15);
    }
  }
  function render() {
    ctx.setTransform(viewport.dpr, 0, 0, viewport.dpr, 0, 0);
    ctx.clearRect(0, 0, viewport.width, viewport.height);
    ctx.fillStyle = "#7fbb5b"; ctx.fillRect(0, 0, viewport.width, viewport.height);
    ctx.save(); ctx.translate(-camera.x, -camera.y);
    ctx.strokeStyle = "#527746"; ctx.lineWidth = 18; ctx.strokeRect(0, 0, world.width, world.height);
    ctx.fillStyle = "rgba(232,240,157,.17)"; for (let x = 60; x < world.width; x += 170) for (let y = 30; y < world.height; y += 145) ctx.fillRect(x, y, 65, 23);
    world.grassTiles.forEach(([x, y], index) => drawAtlasTile(index % 2, index % 2, x, y, 3));
    world.paths.forEach(drawPath);
    world.water.forEach((water) => { ctx.fillStyle = "#4ebbd0"; ctx.fillRect(water.x, water.y, water.width, water.height); ctx.fillStyle = "rgba(232,255,255,.47)"; for (let y = water.y + 15; y < water.y + water.height; y += 28) ctx.fillRect(water.x + 16, y, water.width - 42, 3); });
    world.bridges.forEach(drawBridge);
    world.flowers.forEach(([x, y], i) => { ctx.fillStyle = i % 3 === 0 ? "#ef6f91" : i % 3 === 1 ? "#f2d462" : "#a67aca"; ctx.beginPath(); ctx.arc(x, y, 5, 0, Math.PI * 2); ctx.fill(); });
    drawRuin();
    world.blockers.filter((o) => o.kind === "tree").forEach((o) => drawTree(o.x, o.y, o.radius, o.tone === "pine"));
    world.blockers.filter((o) => o.kind === "rock").forEach((o) => { ctx.fillStyle = "#7a8177"; ctx.beginPath(); ctx.arc(o.x, o.y, o.radius, 0, Math.PI*2); ctx.fill(); });
    if (art.complete && art.naturalWidth) { ctx.imageSmoothingEnabled = false; ctx.drawImage(art, 119, 119, 16, 16, 1680, 1138, 48, 48); }
    drawPlayer(); ctx.restore();
    const landmark = world.nearestLandmark(player.x, player.y); place.textContent = landmark ? landmark.name : "";
  }
  function frame(now) { player = rules.move(player, keys, (now - last) / 1000, world); last = now; updateCamera(); render(); requestAnimationFrame(frame); }
  addEventListener("keydown", (event) => { if (["ArrowUp", "ArrowDown", "ArrowLeft", "ArrowRight", "KeyW", "KeyA", "KeyS", "KeyD"].includes(event.code)) { keys[event.code] = true; event.preventDefault(); } });
  addEventListener("keyup", (event) => { delete keys[event.code]; });
  addEventListener("blur", () => { clearKeys(); last = performance.now(); }); document.addEventListener("visibilitychange", () => { if (document.hidden) clearKeys(); last = performance.now(); });
  addEventListener("resize", resize); resetButton.addEventListener("click", reset);
  globalThis.__valleyDebug = { get player() { return { ...player }; }, get camera() { return { ...camera }; }, get heldKeys() { return Object.keys(keys); }, reset, step(seconds) { player = rules.move(player, keys, seconds, world); updateCamera(); }, world, rules };
  resize(); requestAnimationFrame(frame);
})();
