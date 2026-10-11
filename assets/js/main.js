(function () {
  "use strict";
  var root = document.documentElement;
  var reduceMotion = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ---------- Theme (saved choice) ---------- */
  function storedTheme() { try { return localStorage.getItem("skyline-theme"); } catch (e) { return null; } }
  function saveTheme(t) { try { localStorage.setItem("skyline-theme", t); } catch (e) {} }
  function currentTheme() {
    return root.getAttribute("data-theme") === "light" ? "light" : "dark";
  }
  var themeBtn = document.querySelector(".theme-toggle");
  if (themeBtn) {
    themeBtn.setAttribute("aria-label", currentTheme() === "dark" ? "تفعيل الوضع الفاتح" : "تفعيل الوضع الداكن");
    themeBtn.addEventListener("click", function () {
      var next = currentTheme() === "dark" ? "light" : "dark";
      root.setAttribute("data-theme", next);
      saveTheme(next);
      themeBtn.setAttribute("aria-label", next === "dark" ? "تفعيل الوضع الفاتح" : "تفعيل الوضع الداكن");
      document.dispatchEvent(new CustomEvent("themechange"));
    });
  }

  /* ---------- Mobile menu ---------- */
  var menuBtn = document.querySelector(".menu-toggle");
  var nav = document.querySelector(".nav");
  if (menuBtn && nav) {
    menuBtn.addEventListener("click", function () {
      var open = nav.classList.toggle("open");
      menuBtn.setAttribute("aria-expanded", open ? "true" : "false");
    });
  }

  /* ---------- Scroll reveal ---------- */
  var AUTO_REVEAL = ".jcard, .svc-card, .why-card, .step, .trust-card, .mat-groups > div, .section-head, .vcard, .gitem, .svc, .stat, .card, .faq details, .fact-table, .cta-band, .more-box, .pill-list li, .check-list li, .filters, .hero-media";
  function setupReveal(scope) {
    var root = scope || document;
    // tag common blocks so everything loads in while scrolling
    root.querySelectorAll(AUTO_REVEAL).forEach(function (el) { if (!el.classList.contains("reveal")) el.classList.add("reveal"); });
    // stagger siblings inside grids/lists
    root.querySelectorAll(".reveal:not(.in)").forEach(function (el) {
      if (el.style.transitionDelay) return;
      var sibs = Array.prototype.filter.call(el.parentNode.children, function (c) { return c.classList.contains("reveal"); });
      if (sibs.length > 2) el.style.transitionDelay = ((sibs.indexOf(el) % 4) * 0.09).toFixed(2) + "s";
    });
    var els = root.querySelectorAll(".reveal:not(.in)");
    if (!("IntersectionObserver" in window)) {
      els.forEach(function (el) { el.classList.add("in"); });
      return;
    }
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add("in"); io.unobserve(en.target); }
      });
    }, { threshold: 0.12, rootMargin: "0px 0px -12% 0px" });
    els.forEach(function (el) { io.observe(el); });
  }

  /* images: shimmer placeholder until loaded, then fade in */
  function setupImgLoad(scope) {
    (scope || document).querySelectorAll(".vcard-media img, .gbtn img, .hero-media img").forEach(function (img) {
      if (img.dataset.lw) return; img.dataset.lw = "1";
      var box = img.parentNode; box.classList.add("img-loading");
      function done() { img.classList.add("img-in"); box.classList.remove("img-loading"); }
      if (img.complete && img.naturalWidth) done(); else { img.addEventListener("load", done); img.addEventListener("error", done); }
    });
  }
  window.SkylineReveal = setupReveal;

  /* ---------- Video cards ---------- */
  var ICON_PIN = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2a7 7 0 0 0-7 7c0 5.2 6.1 12.2 6.4 12.5a.8.8 0 0 0 1.2 0C12.9 21.2 19 14.2 19 9a7 7 0 0 0-7-7Zm0 9.6A2.6 2.6 0 1 1 12 6.4a2.6 2.6 0 0 1 0 5.2Z"/></svg>';
  var ICON_PLAY = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M7 4.8v14.4a1 1 0 0 0 1.5.86l11.6-7.2a1 1 0 0 0 0-1.72L8.5 3.94A1 1 0 0 0 7 4.8Z"/></svg>';
  var ICON_EXT = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M14 4h6v6M20 4l-9 9M18 14v5a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1V7a1 1 0 0 1 1-1h5"/></svg>';

  function postUrl(p) {
    return p.kind === "reel"
      ? "https://www.facebook.com/reel/" + p.id + "/"
      : "https://www.facebook.com/skylineupvcwindow/videos/" + p.id + "/";
  }
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }

  function cardHTML(p, i) {
    var cats = window.SKYLINE_CATEGORIES || {};
    return '<article class="vcard reveal reveal-d' + (i % 4) + '" data-cat="' + p.category + '">' +
      '<button class="vcard-media" type="button" data-id="' + p.id + '" aria-label="' + (p.embed === false ? "مشاهدة على فيسبوك: " : "تشغيل فيديو: ") + esc(p.title) + ' — ' + esc(p.location) + '"' + (p.embed === false ? ' title="الفيديو ده بيفتح على فيسبوك"' : '') + '>' +
        '<img src="assets/projects/' + p.id + '.jpg" alt="لقطة من فيديو مشروع Skyline في ' + esc(p.location) + '" loading="lazy" width="640" height="800">' +
        '<span class="play">' + ICON_PLAY + '</span>' +
        '<span class="badge badge-type">' + esc(cats[p.category] || "") + '</span>' +
        (p.duration ? '<span class="badge badge-dur">' + p.duration + '</span>' : '') +
      '</button>' +
      '<div class="vcard-body">' +
        '<span class="loc">' + ICON_PIN + esc(p.location) + '</span>' +
        '<h3 class="vcard-title">' + esc(p.title) + '</h3>' +
        '<ul class="specs">' + p.specs.map(function (s) { return "<li>" + esc(s) + "</li>"; }).join("") + '</ul>' +
        '<a class="vcard-link" href="' + postUrl(p) + '" target="_blank" rel="noopener">' + ICON_EXT + '<span>المنشور الأصلي</span></a>' +
      '</div>' +
    '</article>';
  }

  function renderGrid(el, list) {
    el.innerHTML = list.map(cardHTML).join("");
    setupReveal(el); setupImgLoad(el);
  }

  /* progressive "load more while scrolling" with skeleton placeholders */
  function progressive(el, htmlList, first, batch, skelClass) {
    var i = 0, sentinel = document.createElement("div"), loading = false;
    sentinel.className = "load-sentinel"; sentinel.setAttribute("aria-hidden", "true");
    sentinel.innerHTML = '<span class="dots"><i></i><i></i><i></i></span>';
    el.parentNode.insertBefore(sentinel, el.nextSibling);
    function add(n, instant) {
      var chunk = htmlList.slice(i, i + n); i += chunk.length;
      if (!chunk.length) return;
      if (instant) { el.insertAdjacentHTML("beforeend", chunk.join("")); setupReveal(el); setupImgLoad(el); done(); return; }
      loading = true;
      var sk = chunk.map(function () { return '<div class="' + skelClass + ' skeleton"></div>'; }).join("");
      el.insertAdjacentHTML("beforeend", sk);
      setTimeout(function () {
        el.querySelectorAll(".skeleton").forEach(function (x) { x.remove(); });
        el.insertAdjacentHTML("beforeend", chunk.join(""));
        setupReveal(el); setupImgLoad(el); loading = false; done();
        if (el.__onAdd) el.__onAdd();
      }, reduceMotion ? 0 : 550);
    }
    function done() { if (i >= htmlList.length) { sentinel.remove(); if (io) io.disconnect(); } }
    var io = null;
    add(first, true);
    if (i < htmlList.length) {
      if ("IntersectionObserver" in window) {
        io = new IntersectionObserver(function (en) { if (en[0].isIntersecting && !loading) add(batch); }, { rootMargin: "0px 0px 120px 0px" });
        io.observe(sentinel);
      } else add(htmlList.length, true);
    }
    return { all: function () { if (i < htmlList.length) { el.querySelectorAll(".skeleton").forEach(function (x) { x.remove(); }); add(htmlList.length - i, true); } } };
  }

  var data = window.SKYLINE_PROJECTS || [];
  var grid = document.getElementById("video-grid");
  var featured = document.getElementById("featured-grid");
  if (featured) {
    var pick = (featured.getAttribute("data-ids") || "").split(",");
    renderGrid(featured, pick.map(function (id) { return data.find(function (p) { return p.id === id; }); }).filter(Boolean));
  }
  if (grid) {
    var prog = progressive(grid, data.map(cardHTML), 4, 4, "vcard");
    var filters = document.getElementById("filters");
    var cats = window.SKYLINE_CATEGORIES || {};
    var html = "";
    Object.keys(cats).forEach(function (k) {
      var n = k === "all" ? data.length : data.filter(function (p) { return p.category === k; }).length;
      if (n === 0) return;
      html += '<button class="chip" type="button" data-filter="' + k + '" aria-pressed="' + (k === "all") + '">' + cats[k] + '<span class="count">' + n + '</span></button>';
    });
    filters.innerHTML = html;
    filters.addEventListener("click", function (e) {
      var b = e.target.closest(".chip");
      if (!b) return;
      var f = b.getAttribute("data-filter");
      prog.all();
      filters.querySelectorAll(".chip").forEach(function (c) { c.setAttribute("aria-pressed", c === b ? "true" : "false"); });
      grid.querySelectorAll(".vcard").forEach(function (c) {
        c.hidden = !(f === "all" || c.getAttribute("data-cat") === f);
        c.classList.add("in");
      });
    });
  }

  /* ---------- Video modal (Facebook embed) ---------- */
  var modal = document.getElementById("video-modal");
  if (modal) {
    var frame = modal.querySelector(".modal-frame");
    var locEl = modal.querySelector(".modal-loc");
    var linkEl = modal.querySelector(".modal-fb");
    var lastFocus = null;
    function open(id) {
      var p = data.find(function (x) { return x.id === id; });
      if (!p) return;
      if (p.embed === false) { window.open(postUrl(p), "_blank", "noopener"); return; }
      lastFocus = document.activeElement;
      var href = "https://www.facebook.com/skylineupvcwindow/videos/" + p.id + "/";
      frame.innerHTML = '<iframe title="فيديو مشروع ' + esc(p.location) + '" src="https://www.facebook.com/plugins/video.php?href=' +
        encodeURIComponent(href) + '&show_text=false&width=360&height=640&autoplay=true" allow="autoplay; clipboard-write; encrypted-media; picture-in-picture; web-share" allowfullscreen></iframe>';
      locEl.innerHTML = ICON_PIN + esc(p.location) + " — " + esc(p.title);
      linkEl.href = postUrl(p);
      modal.classList.add("open");
      document.body.style.overflow = "hidden";
      modal.querySelector(".modal-close").focus();
    }
    function close() {
      modal.classList.remove("open");
      frame.innerHTML = "";
      document.body.style.overflow = "";
      if (lastFocus) lastFocus.focus();
    }
    document.addEventListener("click", function (e) {
      var b = e.target.closest(".vcard-media");
      if (b) { open(b.getAttribute("data-id")); return; }
      if (e.target === modal || e.target.closest(".modal-close")) close();
    });
    document.addEventListener("keydown", function (e) { if (e.key === "Escape" && modal.classList.contains("open")) close(); });
  }

  /* ---------- Quote form (WhatsApp + measurements photo) ---------- */
  var waForm = document.getElementById("wa-form");
  if (waForm) {
    var photoInput = document.getElementById("photo");
    var dz = document.getElementById("dropzone");
    var pv = document.getElementById("upload-preview");
    var pvImg = document.getElementById("preview-img");
    var errEl = document.getElementById("wa-error");
    var okEl = document.getElementById("wa-success");
    var photo = null, pvUrl = null;
    function showErr(msg) { errEl.textContent = msg; errEl.hidden = !msg; }
    function setPhoto(file) {
      if (pvUrl) { URL.revokeObjectURL(pvUrl); pvUrl = null; }
      photo = null; pv.hidden = true; dz.hidden = false;
      if (!file) { photoInput.value = ""; return; }
      if (!/^image\//.test(file.type)) { showErr("الملف لازم يكون صورة (JPG أو PNG)."); photoInput.value = ""; return; }
      if (file.size > 10 * 1024 * 1024) { showErr("حجم الصورة أكبر من 10 ميجا."); photoInput.value = ""; return; }
      showErr("");
      photo = file; pvUrl = URL.createObjectURL(file); pvImg.src = pvUrl;
      document.getElementById("preview-name").textContent = file.name;
      document.getElementById("preview-size").textContent = (file.size / 1024 / 1024).toFixed(1) + " ميجا";
      pv.hidden = false; dz.hidden = true;
    }
    photoInput.addEventListener("change", function () { setPhoto(photoInput.files[0]); });
    document.getElementById("remove-photo").addEventListener("click", function () { setPhoto(null); photoInput.focus(); });
    ["dragenter", "dragover"].forEach(function (ev) { dz.addEventListener(ev, function (e) { e.preventDefault(); dz.classList.add("drag"); }); });
    ["dragleave", "drop"].forEach(function (ev) { dz.addEventListener(ev, function (e) { e.preventDefault(); dz.classList.remove("drag"); }); });
    dz.addEventListener("drop", function (e) { var f = e.dataTransfer && e.dataTransfer.files[0]; if (f) setPhoto(f); });

    waForm.addEventListener("submit", function (e) {
      e.preventDefault();
      var f = waForm.elements;
      var name = f.name.value.trim(), phone = f.phone.value.trim();
      okEl.hidden = true;
      if (!name || !phone) { showErr("من فضلك اكتب الاسم ورقم الموبايل."); (name ? f.phone : f.name).focus(); return; }
      showErr("");
      var lines = ["السلام عليكم، عايز عرض سعر.", "الاسم: " + name, "الموبايل: " + phone];
      if (f.area.value.trim()) lines.push("المنطقة: " + f.area.value.trim());
      if (f.profile.value.trim()) lines.push("نوع القطاع: " + f.profile.value.trim());
      if (f.color.value.trim()) lines.push("اللون: " + f.color.value.trim());
      if (f.details.value.trim()) lines.push("تفاصيل: " + f.details.value.trim());
      if (photo) lines.push("(صورة المقاسات مرفقة)");
      var text = lines.join("\n");
      var waUrl = "https://wa.me/201111934900?text=" + encodeURIComponent(text);

      if (photo && navigator.canShare && navigator.canShare({ files: [photo] })) {
        navigator.share({ files: [photo], text: text, title: "طلب عرض سعر — Skyline" }).then(function () {
          okEl.innerHTML = "تمام! اختار واتساب وابعت لرقم Skyline ‎+20 11 11934900‎. لو ماظهرش، <a href=\"" + waUrl + "\" target=\"_blank\" rel=\"noopener\">افتح المحادثة من هنا</a> وارفق الصورة.";
          okEl.hidden = false;
        }).catch(function () { window.open(waUrl, "_blank", "noopener"); });
        return;
      }
      window.open(waUrl, "_blank", "noopener");
      okEl.innerHTML = photo
        ? "اتفتحت محادثة واتساب بالرسالة. <strong>ارفق صورة المقاسات</strong> في المحادثة (زرار 📎 أو اسحب الصورة جوه الشات) وبعدين ابعت."
        : "اتفتحت محادثة واتساب بالرسالة — اضغط إرسال.";
      okEl.hidden = false;
    });
  }

  /* ---------- Gallery grid + lightbox ---------- */
  var gGrid = document.getElementById("gallery-grid");
  if (gGrid) {
    var gItems = (window.SKYLINE_GALLERY || []).map(function (g, i) {
      var p = data.find(function (x) { return x.id === g.project; }) || {};
      return '<figure class="gitem reveal reveal-d' + (i % 4) + '"><button type="button" class="gbtn" data-full="' + g.src + '" data-cap="' + esc(p.location + " — " + p.title) + '">' +
        '<img src="' + g.src + '" alt="' + esc(p.title + " — " + p.location) + '" loading="lazy" width="640" height="800"></button>' +
        '<figcaption><span class="loc">' + ICON_PIN + esc(p.location) + '</span></figcaption></figure>';
    });
    progressive(gGrid, gItems, 5, 5, "gitem");
  }
  var lb = document.getElementById("lightbox");
  if (lb) {
    var lbImg = lb.querySelector("img"), lbCap = lb.querySelector("figcaption"), lbLast = null;
    document.addEventListener("click", function (e) {
      var g = e.target.closest(".gbtn");
      if (g) { lbLast = g; lbImg.src = g.getAttribute("data-full"); lbImg.alt = g.getAttribute("data-cap"); lbCap.textContent = g.getAttribute("data-cap"); lb.classList.add("open"); document.body.style.overflow = "hidden"; lb.querySelector(".lb-close").focus(); return; }
      if (lb.classList.contains("open") && (e.target === lb || e.target.closest(".lb-close"))) { lb.classList.remove("open"); document.body.style.overflow = ""; if (lbLast) lbLast.focus(); }
    });
    document.addEventListener("keydown", function (e) { if (e.key === "Escape" && lb.classList.contains("open")) { lb.classList.remove("open"); document.body.style.overflow = ""; if (lbLast) lbLast.focus(); } });
  }

  /* ---------- Hero rotating words ---------- */
  var rot = document.querySelector(".rot-word");
  if (rot && !reduceMotion) {
    var words = ["شبابيك جرار", "تقفيل بلكونات", "شبابيك بانوراما", "شيش حصيرة"], wi = 0;
    setInterval(function () {
      rot.classList.remove("in"); rot.classList.add("out");
      setTimeout(function () { wi = (wi + 1) % words.length; rot.textContent = words[wi]; rot.classList.remove("out"); rot.classList.add("in"); }, 340);
    }, 2800);
  }

  /* ---------- Counters (count up once when visible) ---------- */
  var nums = document.querySelectorAll(".stat-num[data-count]");
  function fmtCount(el, v) {
    if (el.getAttribute("data-format") === "k") {
      if (v < 1000) return Math.round(v) + "";
      var k = v / 1000, s = k >= 100 ? Math.floor(k) : Math.floor(k * 10) / 10;
      return (s % 1 === 0 ? s.toFixed(0) : s.toFixed(1)) + "K+";
    }
    return Math.round(v) + (el.getAttribute("data-suffix") || "");
  }
  function runCount(el) {
    var end = +el.getAttribute("data-count");
    el.__counted = true;
    if (reduceMotion) { el.textContent = fmtCount(el, end); return; }
    var t0 = null, dur = 1600;
    function step(ts) {
      if (!t0) t0 = ts;
      var k = Math.min((ts - t0) / dur, 1), e = 1 - Math.pow(1 - k, 3);
      el.textContent = fmtCount(el, end * e);
      if (k < 1) requestAnimationFrame(step); else el.textContent = fmtCount(el, end);
    }
    requestAnimationFrame(step);
  }
  /* live Facebook followers: stats.json is refreshed automatically by a GitHub Action */
  var fbEl = document.getElementById("fb-followers");
  if (fbEl && window.fetch) {
    fetch("assets/data/stats.json?t=" + Date.now(), { cache: "no-store" }).then(function (r) { return r.ok ? r.json() : null; }).then(function (d) {
      if (!d || !(d.facebook_followers > 0)) return;
      fbEl.setAttribute("data-count", d.facebook_followers);
      if (fbEl.__counted) fbEl.textContent = fmtCount(fbEl, d.facebook_followers);
    }).catch(function () {});
  }
  if (nums.length) {
    if ("IntersectionObserver" in window) {
      var cio = new IntersectionObserver(function (en) { en.forEach(function (x) { if (x.isIntersecting) { runCount(x.target); cio.unobserve(x.target); } }); }, { threshold: 0.5 });
      nums.forEach(function (n) { cio.observe(n); });
    } else nums.forEach(runCount);
  }

  /* ---------- Scroll effects: progress bar, header shrink, gentle parallax ---------- */
  var header = document.querySelector(".site-header");
  var bar = document.createElement("div");
  bar.className = "scroll-progress"; bar.setAttribute("aria-hidden", "true");
  document.body.appendChild(bar);
  var pImgs = [];
  var ticking = false;
  function onScroll() {
    ticking = false;
    var y = window.scrollY, max = document.documentElement.scrollHeight - window.innerHeight;
    bar.style.transform = "scaleX(" + (max > 0 ? Math.min(y / max, 1) : 0) + ")";
    if (header) header.classList.toggle("scrolled", y > 30);
    pImgs.forEach(function (img, i) {
      var r = img.getBoundingClientRect();
      if (r.bottom < 0 || r.top > window.innerHeight) return;
      var c = (r.top + r.height / 2 - window.innerHeight / 2) / window.innerHeight;
      img.style.transform = "translateY(" + (c * (i === 0 ? -18 : 14)).toFixed(1) + "px) scale(1.06)";
    });
  }
  window.addEventListener("scroll", function () { if (!ticking) { ticking = true; requestAnimationFrame(onScroll); } }, { passive: true });
  onScroll();

  /* ---------- 3D logo tilt on hover ---------- */
  if (!reduceMotion) {
    document.querySelectorAll(".brand").forEach(function (b) {
      b.addEventListener("pointermove", function (e) {
        var r = b.getBoundingClientRect();
        var x = (e.clientX - r.left) / r.width - 0.5, y = (e.clientY - r.top) / r.height - 0.5;
        b.style.setProperty("--ry", (x * 26).toFixed(1) + "deg");
        b.style.setProperty("--rx", (-y * 22).toFixed(1) + "deg");
      });
      b.addEventListener("pointerleave", function () { b.style.setProperty("--ry", "0deg"); b.style.setProperty("--rx", "0deg"); });
    });
  }

  setupReveal(); setupImgLoad();

  /* ---------- Anchor links (e.g. "عن الشركة" -> #about): land exactly under the header ---------- */
  function goToHash(smooth) {
    if (!location.hash) return;
    var el = document.getElementById(decodeURIComponent(location.hash.slice(1)));
    if (!el) return;
    var hdr = document.querySelector(".site-header");
    var y = el.getBoundingClientRect().top + window.scrollY - (hdr ? hdr.offsetHeight : 0) - 28;
    window.scrollTo({ top: Math.max(0, y), behavior: smooth ? "smooth" : "auto" });
  }
  document.addEventListener("click", function (e) {
    var a = e.target.closest('a[href*="#"]');
    if (!a) return;
    var url = new URL(a.href, location.href);
    if (url.pathname !== location.pathname || !url.hash) return;
    e.preventDefault();
    history.pushState(null, "", url.hash);
    if (nav) nav.classList.remove("open");
    goToHash(true);
  });
  if (location.hash) {
    window.addEventListener("load", function () { goToHash(false); setTimeout(function () { goToHash(false); }, 300); });
  }

  /* ---------- Customer reviews: assets/data/reviews.json is refreshed from Facebook by a GitHub Action ---------- */
  var rvGrid = document.getElementById("reviews-grid");
  if (rvGrid) {
    var rvEsc = function (s) { return String(s || "").replace(/[&<>"']/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]; }); };
    var rvDate = function (d) { try { return d ? new Date(d + "T12:00:00").toLocaleDateString("ar-EG", { year: "numeric", month: "long" }) : ""; } catch (e) { return d || ""; } };
    var showEmpty = function () { var e = document.getElementById("rv-empty"); if (e) { e.hidden = false; e.classList.add("in"); } };
    fetch("assets/data/reviews.json?t=" + Date.now(), { cache: "no-store" }).then(function (r) { return r.ok ? r.json() : null; }).then(function (d) {
      var items = (d && d.items) || [];
      if (!items.length) { showEmpty(); return; }
      var rec = items.filter(function (x) { return x.recommends !== false; }).length;
      var sum = document.getElementById("rv-summary");
      if (sum) {
        document.getElementById("rv-count").textContent = Math.max(items.length, d.total_on_facebook || 0);
        sum.hidden = false;
      }
      var rvHead = function (x) {
        var name = (x.name || "").trim() || "عميل Skyline";
        var inner = '<span class="rv-avatar" aria-hidden="true">' + rvEsc(name.charAt(0)) + '</span><div><strong>' + rvEsc(name) + '</strong><span>' + (rvDate(x.date) ? rvEsc(rvDate(x.date)) : (x.profile ? "على فيسبوك ↗" : "")) + '</span></div>';
        var link = x.profile && /^https:\/\/(www\.)?facebook\.com\//.test(x.profile);
        return '<header>' + (link ? '<a class="rv-who" href="' + rvEsc(x.profile) + '" target="_blank" rel="noopener noreferrer nofollow" title="حساب ' + rvEsc(name) + ' على فيسبوك">' + inner + '</a>' : '<div class="rv-who">' + inner + '</div>') +
          '<span class="rv-badge' + (x.recommends === false ? " no" : "") + '">' + (x.recommends === false ? "لا يرشّح" : "يرشّح Skyline") + '</span></header>';
      };
      rvGrid.innerHTML = items.map(function (x, i) {
        return '<article class="rv-card reveal reveal-d' + (i % 4) + '" data-i="' + i + '"><span class="rv-quote" aria-hidden="true">”</span>' + rvHead(x) +
          '<p class="rv-text">' + rvEsc(x.text).replace(/\n/g, "<br>") + '</p>' +
          '<button type="button" class="rv-more" aria-haspopup="dialog">عرض المزيد</button></article>';
      }).join("");
      // show the button only on reviews that are actually cut off
      var markLong = function () { rvGrid.querySelectorAll(".rv-card").forEach(function (c) { var p = c.querySelector(".rv-text"); c.classList.toggle("is-long", p.scrollHeight > p.clientHeight + 2); }); };
      markLong(); window.addEventListener("resize", markLong); if (document.fonts && document.fonts.ready) document.fonts.ready.then(markLong);
      rvGrid.addEventListener("pointermove", function (e) {
        var c = e.target.closest(".rv-card"); if (!c) return; var r = c.getBoundingClientRect();
        c.style.setProperty("--rv-x", (e.clientX - r.left) + "px"); c.style.setProperty("--rv-y", (e.clientY - r.top) + "px");
      });
      // full review in a light pop-up
      var modal = document.createElement("div");
      modal.className = "rv-modal"; modal.hidden = true;
      modal.innerHTML = '<div class="rv-modal-card rv-card" role="dialog" aria-modal="true" aria-label="التقييم كامل"><button type="button" class="rv-close" aria-label="إغلاق">✕</button><div class="rv-modal-body"></div></div>';
      document.body.appendChild(modal);
      var lastBtn = null, closeT = null;
      var openRv = function (i, btn) {
        var x = items[i]; if (!x) return; lastBtn = btn; clearTimeout(closeT);
        modal.querySelector(".rv-modal-body").innerHTML = rvHead(x) + '<p class="rv-text full">' + rvEsc(x.text).replace(/\n/g, "<br>") + '</p>';
        modal.hidden = false; document.documentElement.classList.add("rv-lock");
        requestAnimationFrame(function () { requestAnimationFrame(function () { modal.classList.add("open"); modal.querySelector(".rv-close").focus(); }); });
      };
      var closeRv = function () {
        if (modal.hidden) return; modal.classList.remove("open"); document.documentElement.classList.remove("rv-lock");
        closeT = setTimeout(function () { modal.hidden = true; if (lastBtn) lastBtn.focus(); }, 220);
      };
      rvGrid.addEventListener("click", function (e) { var b = e.target.closest(".rv-more"); if (b) openRv(+b.closest(".rv-card").dataset.i, b); });
      modal.addEventListener("click", function (e) { if (e.target === modal || e.target.closest(".rv-close")) closeRv(); });
      document.addEventListener("keydown", function (e) { if (e.key === "Escape") closeRv(); });
      if (typeof setupReveal === "function") setupReveal(rvGrid);
    }).catch(showEmpty);
  }

  /* ---------- Hero video: silent, looping like a GIF ---------- */
  var hv = document.getElementById("hero-video");
  if (hv) { hv.muted = true; hv.defaultMuted = true; var pr = hv.play(); if (pr && pr.catch) pr.catch(function () {}); }
})();
