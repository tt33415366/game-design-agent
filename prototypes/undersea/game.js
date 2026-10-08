(function () {
  "use strict";
  const canvas = document.querySelector("#game");
  const ctx = canvas.getContext("2d");
  const place = document.querySelector("#place");
  const resetButton = document.querySelector("#reset");
  const world = globalThis.UnderseaWorld;
  const rules = globalThis.UnderseaRules;
  const keys = {};
  let player = rules.reset(world);
  let boulder = rules.resetBoulder(world);
  const revealed = {};
  let flavorText = "", flavorUntil = 0;
  let camera = { x: 0, y: 0 };
  let viewport = { width: innerWidth, height: innerHeight, dpr: 1 };
  let last = performance.now();

  function clearKeys() { Object.keys(keys).forEach((key) => delete keys[key]); }
  function reset() {
    clearKeys(); player = rules.reset(world); boulder = rules.resetBoulder(world);
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
  function drawCoral(x, y, r, tone) {
    const colors = { reef: "#e07856", fan: "#d95f8a", brain: "#c9a05a", dark: "#4a3d5c" };
    ctx.fillStyle = colors[tone] || colors.reef;
    ctx.beginPath(); ctx.arc(x, y, r, 0, Math.PI * 2); ctx.fill();
    ctx.fillStyle = "rgba(255,255,255,.18)";
    ctx.beginPath(); ctx.arc(x - r * .3, y - r * .3, r * .45, 0, Math.PI * 2); ctx.fill();
  }
  function drawWreck() {
    ctx.save(); ctx.translate(330, 1170); ctx.rotate(-0.35);
    ctx.fillStyle = "#5a4633";
    ctx.beginPath(); ctx.ellipse(0, 0, 95, 30, 0, 0, Math.PI * 2); ctx.fill();
    ctx.fillStyle = "#3d2f22"; ctx.fillRect(-70, -10, 140, 8);
    ctx.fillStyle = "#2c2118"; ctx.fillRect(20, -34, 10, 34);
    ctx.restore();
  }
  function drawReefArch() {
    ctx.strokeStyle = "#8a7a5c"; ctx.lineWidth = 26; ctx.lineCap = "round";
    ctx.beginPath(); ctx.arc(480, 445, 60, Math.PI, 0); ctx.stroke();
  }
  function drawGarden() {
    for (let i = 0; i < 12; i += 1) {
      const a = (i / 12) * Math.PI * 2, r = 30 + (i % 3) * 16;
      const x = 1520 + Math.cos(a) * r, y = 380 + Math.sin(a) * r;
      ctx.strokeStyle = i % 2 ? "#7fd4c0" : "#a0e0d0"; ctx.lineWidth = 3;
      ctx.beginPath(); ctx.moveTo(x, y); ctx.lineTo(x + Math.cos(a) * 10, y + Math.sin(a) * 10); ctx.stroke();
    }
  }
  function drawBoulder() {
    const b = world.boulderCircle(boulder);
    ctx.fillStyle = world.boulderIsArch(boulder) ? "#6a6a72" : "#7d7268";
    ctx.beginPath(); ctx.arc(b.x, b.y, b.radius, 0, Math.PI * 2); ctx.fill();
    ctx.fillStyle = "rgba(255,255,255,.12)"; ctx.beginPath(); ctx.arc(b.x - 8, b.y - 8, b.radius * .4, 0, Math.PI * 2); ctx.fill();
  }
  function drawPlayer() {
    const bob = Math.sin(performance.now() / 300) * 2;
    ctx.fillStyle = "rgba(10,30,40,.25)"; ctx.beginPath(); ctx.ellipse(player.x, player.y + 10, 11, 4, 0, 0, Math.PI * 2); ctx.fill();
    ctx.fillStyle = "#f0d8a8"; ctx.beginPath(); ctx.arc(player.x, player.y - 6 + bob, 7, 0, Math.PI * 2); ctx.fill();
    ctx.fillStyle = "#2e7d8c";
    ctx.beginPath(); ctx.ellipse(player.x, player.y + 3 + bob, 7, 10, 0, 0, Math.PI * 2); ctx.fill();
    const fin = player.facing === "west" ? -1 : 1;
    ctx.beginPath(); ctx.moveTo(player.x, player.y + 11 + bob); ctx.lineTo(player.x - 8 * fin, player.y + 18 + bob); ctx.lineTo(player.x + 2 * fin, player.y + 14 + bob); ctx.fill();
  }
  function render() {
    ctx.setTransform(viewport.dpr, 0, 0, viewport.dpr, 0, 0);
    const grad = ctx.createLinearGradient(0, 0, 0, viewport.height);
    grad.addColorStop(0, "#7ecfe0"); grad.addColorStop(1, "#3e8fb5");
    ctx.fillStyle = grad; ctx.fillRect(0, 0, viewport.width, viewport.height);
    ctx.save(); ctx.translate(-camera.x, -camera.y);
    ctx.fillStyle = "rgba(240,230,180,.16)"; for (let x = 80; x < world.width; x += 200) for (let y = 60; y < world.height; y += 180) { ctx.beginPath(); ctx.ellipse(x, y, 60, 18, 0, 0, Math.PI * 2); ctx.fill(); }
    // Current channel rock walls.
    world.channel.forEach((s) => { ctx.fillStyle = "#5c5a54"; ctx.fillRect(s.x, s.y, s.width, s.height); ctx.fillStyle = "rgba(255,255,255,.08)"; for (let y = s.y + 10; y < s.y + s.height; y += 34) ctx.fillRect(s.x + 6, y, s.width - 12, 4); });
    world.blockers.filter((o) => o.kind === "coral").forEach((o) => drawCoral(o.x, o.y, o.radius, o.tone));
    world.blockers.filter((o) => o.kind === "rock").forEach((o) => { ctx.fillStyle = "#6d6a63"; ctx.beginPath(); ctx.arc(o.x, o.y, o.radius, 0, Math.PI * 2); ctx.fill(); });
    drawReefArch(); drawWreck(); drawGarden(); drawBoulder();
    // Reveal auras.
    world.sights.forEach((s) => {
      if (!s.reveal || !revealed[s.id]) return;
      ctx.save(); ctx.strokeStyle = "rgba(255,244,180,.5)"; ctx.lineWidth = 3; ctx.setLineDash([8, 10]);
      ctx.beginPath(); ctx.arc(s.reveal.x, s.reveal.y, s.reveal.radius * .6, 0, Math.PI * 2); ctx.stroke(); ctx.restore();
    });
    if (revealed.crevice) { ctx.save(); ctx.strokeStyle = "rgba(200,220,255,.55)"; ctx.lineWidth = 3; ctx.setLineDash([6, 9]); ctx.beginPath(); ctx.arc(world.crevice.heart.x, world.crevice.heart.y, 30, 0, Math.PI * 2); ctx.stroke(); ctx.restore(); }
    drawPlayer(); ctx.restore();
    // Crevice pressure vignette: darkens as the player enters the pocket.
    const c = world.crevice, dist = Math.hypot(player.x - c.x, player.y - c.y);
    if (dist < c.radius) {
      const depth = 1 - dist / c.radius;
      ctx.setTransform(viewport.dpr, 0, 0, viewport.dpr, 0, 0);
      const v = ctx.createRadialGradient(viewport.width / 2, viewport.height / 2, viewport.height * .2, viewport.width / 2, viewport.height / 2, viewport.height * .75);
      v.addColorStop(0, "rgba(6,10,26,0)"); v.addColorStop(1, `rgba(6,10,26,${0.25 + depth * 0.6})`);
      ctx.fillStyle = v; ctx.fillRect(0, 0, viewport.width, viewport.height);
    }
    const sight = world.nearestSight(player.x, player.y);
    place.textContent = sight ? sight.name : (world.inCrevice(player.x, player.y) ? "The Crevice" : "");
    if (performance.now() < flavorUntil && flavorText) {
      ctx.setTransform(viewport.dpr, 0, 0, viewport.dpr, 0, 0);
      ctx.font = "italic 15px Georgia, serif"; ctx.textAlign = "center";
      ctx.fillStyle = "rgba(240,248,250,.95)"; ctx.fillText(flavorText, viewport.width / 2, viewport.height - 28);
    }
  }
  function frame(now) {
    const elapsed = (now - last) / 1000;
    const pushing = rules.push(player, keys, world, boulder);
    if (pushing.moved) {
      const steps = Math.max(1, Math.round(elapsed / rules.PHYSICS_STEP));
      for (let i = 0; i < steps; i += 1) {
        const s = rules.push(player, keys, world, boulder);
        if (!s.moved) break;
        boulder = s.boulder; player = s.player;
      }
    } else {
      player = rules.move(player, keys, elapsed, world, boulder);
    }
    const reveal = world.revealFor(player.x, player.y);
    if (reveal && !revealed[reveal.id]) { revealed[reveal.id] = true; flavorText = reveal.text; flavorUntil = now + 4000; }
    last = now; updateCamera(); render(); requestAnimationFrame(frame);
  }
  addEventListener("keydown", (event) => { if (["ArrowUp", "ArrowDown", "ArrowLeft", "ArrowRight", "KeyW", "KeyA", "KeyS", "KeyD"].includes(event.code)) { keys[event.code] = true; event.preventDefault(); } });
  addEventListener("keyup", (event) => { delete keys[event.code]; });
  addEventListener("blur", () => { clearKeys(); last = performance.now(); });
  document.addEventListener("visibilitychange", () => { if (document.hidden) clearKeys(); last = performance.now(); });
  addEventListener("resize", resize); resetButton.addEventListener("click", reset);
  globalThis.__underseaDebug = {
    get player() { return { ...player }; }, get camera() { return { ...camera }; }, get heldKeys() { return Object.keys(keys); },
    get boulder() { return { ...boulder }; }, get revealed() { return { ...revealed }; }, get flavor() { return flavorText; },
    setPlayer(x, y) { player = { ...player, x, y, vx: 0, vy: 0 }; updateCamera(); },
    reset, step(seconds) { player = rules.move(player, keys, seconds, world, boulder); updateCamera(); },
    world, rules };
  resize(); requestAnimationFrame(frame);
})();
