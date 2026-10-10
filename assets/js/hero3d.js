/* Three.js: أيقونات أبواب وشبابيك 3D في خلفية أول سيكشن — بتتحرك مع الماوس (ميلان + بارالاكس) وبتثبت لما الماوس يقف */
(function () {
  "use strict";
  var canvas = document.getElementById("hero3d");
  if (!canvas || !window.THREE) return;
  var THREE = window.THREE;
  
  var renderer;
  try { renderer = new THREE.WebGLRenderer({ canvas: canvas, alpha: true, antialias: true }); }
  catch (e) { canvas.remove(); return; }
  renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 2));

  var scene = new THREE.Scene();
  var camera = new THREE.PerspectiveCamera(35, 1, 0.1, 100);
  camera.position.set(0, 0, 20);

  /* ---------- geometry helpers ---------- */
  function rrect(w, h, r, cx, cy) {
    cx = cx || 0; cy = cy || 0;
    var s = new THREE.Shape(), x = cx - w / 2, y = cy - h / 2;
    s.moveTo(x + r, y); s.lineTo(x + w - r, y); s.quadraticCurveTo(x + w, y, x + w, y + r);
    s.lineTo(x + w, y + h - r); s.quadraticCurveTo(x + w, y + h, x + w - r, y + h);
    s.lineTo(x + r, y + h); s.quadraticCurveTo(x, y + h, x, y + h - r);
    s.lineTo(x, y + r); s.quadraticCurveTo(x, y, x + r, y);
    return s;
  }
  function holePath(w, h, cx, cy) { var p = new THREE.Path(); p.setFromPoints(rrect(w, h, 0.08, cx, cy).getPoints(6)); return p; }
  function frame(w, h, t, depth, holes) {
    var s = rrect(w, h, 0.18);
    (holes || [[w - 2 * t, h - 2 * t, 0, 0]]).forEach(function (hl) { s.holes.push(holePath(hl[0], hl[1], hl[2], hl[3])); });
    var g = new THREE.ExtrudeGeometry(s, { depth: depth, bevelEnabled: true, bevelSize: 0.04, bevelThickness: 0.04, bevelSegments: 2, curveSegments: 5 });
    g.translate(0, 0, -depth / 2);
    return new THREE.Mesh(g, frameMat);
  }
  function glass(w, h, x, y) { var m = new THREE.Mesh(new THREE.PlaneGeometry(w, h), glassMat); m.position.set(x || 0, y || 0, 0); return m; }
  function handle(x, y, z) {
    var g = new THREE.Group();
    g.add(new THREE.Mesh(new THREE.BoxGeometry(0.12, 0.34, 0.06), accentMat));
    var lever = new THREE.Mesh(new THREE.BoxGeometry(0.08, 0.34, 0.08), accentMat); lever.position.set(0, -0.14, 0.07); g.add(lever);
    g.position.set(x, y, z); return g;
  }

  var frameMat = new THREE.MeshStandardMaterial({ color: 0xeef4f9, roughness: 0.4, metalness: 0.06 });
  var glassMat = new THREE.MeshStandardMaterial({ color: 0x7cc8f0, transparent: true, opacity: 0.3, roughness: 0.05, metalness: 0.35, side: THREE.DoubleSide });
  var accentMat = new THREE.MeshStandardMaterial({ color: 0x3ba3e3, roughness: 0.3, metalness: 0.5 });

  function makeDoor() {
    var g = new THREE.Group();
    g.add(frame(2.3, 3.9, 0.2, 0.32));
    var pivot = new THREE.Group(); pivot.position.set(-0.95, 0, 0.05);
    var leaf = new THREE.Group();
    leaf.add(frame(1.9, 3.5, 0.2, 0.22, [[1.4, 1.5, 0, 0.75], [1.4, 1.2, 0, -0.95]]));
    leaf.add(glass(1.4, 1.5, 0, 0.75));
    var panel = new THREE.Mesh(new THREE.BoxGeometry(1.4, 1.2, 0.08), frameMat); panel.position.set(0, -0.95, 0); leaf.add(panel);
    leaf.add(handle(0.72, -0.1, 0.16));
    leaf.position.x = 0.95; pivot.add(leaf); pivot.rotation.y = -0.6;
    g.add(pivot);
    return g;
  }
  function makeFrench() {
    var g = new THREE.Group();
    g.add(frame(3.2, 3.6, 0.18, 0.3, [[1.3, 3.2, -0.72, 0], [1.3, 3.2, 0.72, 0]]));
    g.add(glass(1.3, 3.2, -0.72, 0)); g.add(glass(1.3, 3.2, 0.72, 0));
    g.add(handle(-0.14, 0, 0.2)); g.add(handle(0.14, 0, 0.2));
    return g;
  }
  function makeCasement() {
    var g = new THREE.Group();
    g.add(frame(3.0, 3.0, 0.2, 0.3, [[1.2, 2.6, -0.65, 0], [1.2, 2.6, 0.65, 0]]));
    g.add(glass(1.2, 2.6, -0.65, 0)); g.add(glass(1.2, 2.6, 0.65, 0));
    g.add(handle(-0.12, 0, 0.2)); g.add(handle(0.12, 0, 0.2));
    return g;
  }
  function makeSliding() {
    var g = new THREE.Group();
    g.add(frame(3.3, 2.5, 0.18, 0.36));
    var a = new THREE.Group(); a.add(frame(1.75, 2.15, 0.16, 0.12)); a.add(glass(1.43, 1.83)); a.position.set(-0.6, 0, 0.09); a.add(handle(0.72, 0, 0.1));
    var b = new THREE.Group(); b.add(frame(1.75, 2.15, 0.16, 0.12)); b.add(glass(1.43, 1.83)); b.position.set(0.6, 0, -0.09);
    g.add(a); g.add(b);
    return g;
  }
  function makeRound() {
    var g = new THREE.Group();
    var s = new THREE.Shape(); s.absarc(0, 0, 1.5, 0, Math.PI * 2, false);
    var h = new THREE.Path(); h.absarc(0, 0, 1.25, 0, Math.PI * 2, true); s.holes.push(h);
    var geo = new THREE.ExtrudeGeometry(s, { depth: 0.3, bevelEnabled: true, bevelSize: 0.04, bevelThickness: 0.04, curveSegments: 40 }); geo.translate(0, 0, -0.15);
    g.add(new THREE.Mesh(geo, frameMat));
    var gl = new THREE.Mesh(new THREE.CircleGeometry(1.25, 40), glassMat); g.add(gl);
    var bar1 = new THREE.Mesh(new THREE.BoxGeometry(2.5, 0.12, 0.2), frameMat), bar2 = new THREE.Mesh(new THREE.BoxGeometry(0.12, 2.5, 0.2), frameMat);
    g.add(bar1); g.add(bar2);
    return g;
  }

  /* placement in normalized screen space (-1..1), depth z, scale */
  var defs = [
    { make: makeDoor,     nx: 0.02,  ny: 0.88,  z: -2, s: 0.46 },
    { make: makeSliding,  nx: 0.12,  ny: -0.88, z: -3, s: 0.5 },
    { make: makeCasement, nx: 0.97,  ny: -0.88, z: -4, s: 0.46 },
    { make: makeRound,    nx: -0.97, ny: -0.86, z: -3, s: 0.46 },
    { make: makeFrench,   nx: 0.55,  ny: 0.92,  z: -5, s: 0.4 },
    { make: makeCasement, nx: -0.6,  ny: 0.94,  z: -6, s: 0.4 }
  ];
  var items = defs.map(function (d, i) {
    var m = d.make(); m.scale.setScalar(d.s); scene.add(m);
    return { m: m, d: d, phase: i * 0.7 };
  });

  scene.add(new THREE.AmbientLight(0xffffff, 0.6));
  var key = new THREE.DirectionalLight(0xffffff, 0.95); key.position.set(-6, 7, 10); scene.add(key);
  var rim = new THREE.DirectionalLight(0x6cc1f0, 0.9); rim.position.set(7, -3, 4); scene.add(rim);

  function applyTheme() {
    var light = document.documentElement.getAttribute("data-theme") === "light";
    frameMat.color.set(light ? 0xffffff : 0xeef4f9);
    glassMat.opacity = light ? 0.24 : 0.3;
  }
  applyTheme();

  var narrow = false;
  function layout() {
    var w = canvas.clientWidth, h = canvas.clientHeight;
    if (!w || !h) return;
    renderer.setSize(w, h, false);
    camera.aspect = w / h; camera.updateProjectionMatrix();
    narrow = w < 760;
    items.forEach(function (it, i) {
      var dist = camera.position.z - it.d.z;
      it.vh = 2 * Math.tan(THREE.MathUtils.degToRad(camera.fov / 2)) * dist;
      it.vw = it.vh * camera.aspect;
      it.bx = it.d.nx * it.vw / 2 * 0.92;
      it.by = it.d.ny * it.vh / 2 * 0.9;
      it.ox = it.ox || 0; it.oy = it.oy || 0; it.spin = it.spin || 0;
      it.m.visible = !(narrow && i > 3);
      it.m.scale.setScalar(it.d.s * (narrow ? 0.75 : 1));
    });
  }

  /* mouse position relative to the hero (-1..1); movement is user-driven so it stays on even with reduced-motion */
  var target = { x: 0, y: 0 }, cur = { x: 0, y: 0 }, mouseIn = false, running = false, last = 0;
  function tick(now) {
    cur.x += (target.x - cur.x) * 0.09;
    cur.y += (target.y - cur.y) * 0.09;
    var moving = Math.abs(target.x - cur.x) > 0.0008 || Math.abs(target.y - cur.y) > 0.0008;
    items.forEach(function (it) {
      if (!it.m.visible) return;
      var depth = 1 + (-it.d.z) * 0.12;
      // parallax: noticeable shift that grows with depth
      var px = it.bx + cur.x * 1.3 * depth, py = it.by - cur.y * 0.9 * depth;
      // repel: icons slide away from the cursor when it gets close
      var mx = cur.x * it.vw / 2, my = -cur.y * it.vh / 2;
      var dx = px - mx, dy = py - my, d = Math.sqrt(dx * dx + dy * dy) || 0.001, R = 4.2;
      var push = mouseIn && d < R ? (R - d) * 0.75 : 0;
      it.ox += ((dx / d) * push - it.ox) * 0.12;
      it.oy += ((dy / d) * push - it.oy) * 0.12;
      it.spin += ((push ? (dx > 0 ? 0.9 : -0.9) : 0) - it.spin) * 0.08;
      if (Math.abs(it.ox) > 0.002 || Math.abs(it.oy) > 0.002 || Math.abs(it.spin) > 0.002) moving = true;
      var fx = Math.max(-it.vw / 2 * 0.97, Math.min(it.vw / 2 * 0.97, px + it.ox));
      var fy = Math.max(-it.vh / 2 * 0.95, Math.min(it.vh / 2 * 0.95, py + it.oy));
      it.m.position.set(fx, fy, it.d.z);
      it.m.rotation.y = -0.35 + Math.sin(it.phase) * 0.2 + cur.x * 1.1 + it.spin;
      it.m.rotation.x = 0.1 + cur.y * 0.8;
      it.m.rotation.z = Math.cos(it.phase) * 0.06 - cur.x * 0.12;
    });
    renderer.render(scene, camera);
    if (moving) requestAnimationFrame(tick); else running = false;
  }
  function kick() { if (!running) { running = true; requestAnimationFrame(tick); } }

  var hero = canvas.parentNode;
  window.addEventListener("pointermove", function (e) {
    var r = hero.getBoundingClientRect();
    mouseIn = e.clientY >= r.top && e.clientY <= r.bottom;
    target.x = Math.max(-1.2, Math.min(1.2, ((e.clientX - r.left) / r.width - 0.5) * 2));
    target.y = Math.max(-1.2, Math.min(1.2, ((e.clientY - r.top) / r.height - 0.5) * 2));
    kick();
  }, { passive: true });
  hero.addEventListener("pointerleave", function () { mouseIn = false; kick(); });
  window.addEventListener("resize", function () { layout(); kick(); });
  document.addEventListener("themechange", function () { applyTheme(); kick(); });
  layout(); kick();
})();
