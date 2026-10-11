/* =========================================================
   PLUM921 · 交互脚本（原生 JS，无依赖）
   内容全部来自 js/data.js，改内容不用动这个文件
   ========================================================= */
(function () {
  "use strict";

  // 标记 JS 可用：进入动画只在此标记下生效，避免脚本异常时内容被隐藏
  document.documentElement.classList.add("has-js");

  var DATA = window.SITE_DATA || {};
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  var $  = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };

  /* 占位图（文件缺失时兜底，永远不会白屏） */
  function fallbackImg(label) {
    var svg =
      '<svg xmlns="http://www.w3.org/2000/svg" width="240" height="240" viewBox="0 0 240 240">' +
      '<rect width="240" height="240" fill="#F6EFE2"/>' +
      '<g fill="#EFDCDA">' +
      '<rect x="0" y="0" width="40" height="40"/><rect x="80" y="0" width="40" height="40"/><rect x="160" y="0" width="40" height="40"/>' +
      '<rect x="40" y="40" width="40" height="40"/><rect x="120" y="40" width="40" height="40"/><rect x="200" y="40" width="40" height="40"/>' +
      '<rect x="0" y="80" width="40" height="40"/><rect x="80" y="80" width="40" height="40"/><rect x="160" y="80" width="40" height="40"/>' +
      '<rect x="40" y="120" width="40" height="40"/><rect x="120" y="120" width="40" height="40"/><rect x="200" y="120" width="40" height="40"/>' +
      '<rect x="0" y="160" width="40" height="40"/><rect x="80" y="160" width="40" height="40"/><rect x="160" y="160" width="40" height="40"/>' +
      '<rect x="40" y="200" width="40" height="40"/><rect x="120" y="200" width="40" height="40"/><rect x="200" y="200" width="40" height="40"/>' +
      "</g>" +
      '<rect x="88" y="88" width="64" height="64" fill="#FBF6EC" stroke="#B4575D" stroke-width="6"/>' +
      '<rect x="108" y="108" width="24" height="24" fill="#B4575D"/>' +
      '<text x="120" y="200" text-anchor="middle" font-family="monospace" font-size="18" fill="#8B3A43">' +
      (label || "NO IMAGE") +
      "</text></svg>";
    return "data:image/svg+xml;charset=utf-8," + encodeURIComponent(svg);
  }

  function isPlaceholder(src) {
    return !src || /placeholder/i.test(src);
  }

  function esc(str) {
    return String(str == null ? "" : str)
      .replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  }

  /* ---------------- 基础信息 ---------------- */
  function renderProfile() {
    var p = DATA.profile || {};

    var name = $("#heroName");        if (name)  name.textContent = p.name || "";
    var role = $("#heroRole");        if (role)  role.textContent = p.role || "";
    var intro = $("#heroIntro");      if (intro) intro.textContent = p.intro || "";
    var fn = $("#footerName");        if (fn)    fn.textContent = p.footerName || p.name || "";

    var av = $("#avatarImg");
    if (av && p.avatar) {
      av.src = p.avatar;
      av.onerror = function () { av.onerror = null; av.src = fallbackImg("AVATAR"); };
    }

    // 顶部像素横幅
    var fig = $("#banner"), bn = $("#bannerImg");
    if (fig && bn) {
      if (p.banner) {
        bn.src = p.banner;
        bn.alt = p.bannerAlt || "banner";
        bn.onerror = function () { bn.onerror = null; bn.src = fallbackImg("BANNER"); };
      } else {
        fig.hidden = true;
      }
      var cap = $("#bannerCap");
      if (cap && p.bannerCap != null) cap.textContent = p.bannerCap;
      var meta = $("#bannerMeta");
      if (meta && p.bannerMeta != null) meta.textContent = p.bannerMeta;
    }

    ["#aboutP1", "#aboutP2"].forEach(function (sel, i) {
      var el = $(sel);
      if (el && DATA.about && DATA.about[i] != null) el.textContent = DATA.about[i];
    });
    // 关于页正文多于两段时自动追加
    if (DATA.about && DATA.about.length > 2) {
      var host = $(".about__text");
      for (var i = 2; i < DATA.about.length; i++) {
        var pEl = document.createElement("p");
        pEl.textContent = DATA.about[i];
        host.appendChild(pEl);
      }
    }

    document.title = (p.name || "PLUM921") + " · 个人主页";
  }

  /* ---------------- 社交链接 ---------------- */
  function renderLinks() {
    var list = $("#socials");
    if (!list) return;
    (DATA.links || []).forEach(function (l) {
      var li = document.createElement("li");
      var a = document.createElement("a");
      a.href = l.href || "#";
      a.textContent = l.label || "";
      if (l.href && l.href !== "#") { a.target = "_blank"; a.rel = "noopener"; }
      a.title = l.href === "#" ? "链接待填写" : l.label;
      li.appendChild(a);
      list.appendChild(li);
    });
  }

  /* ---------------- 终端打字机 ---------------- */
  function renderTerminal() {
    var host = $("#terminal");
    var lines = (DATA.profile && DATA.profile.terminal) || [];
    if (!host) return;

    var html = "";
    lines.forEach(function (line) {
      html += '<span class="t-line">' + line + "</span>\n";
    });

    if (reduce) { host.innerHTML = html; return; }

    // 逐行淡入
    host.innerHTML = "";
    var i = 0;
    (function step() {
      if (i >= lines.length) return;
      var span = document.createElement("span");
      span.className = "t-line";
      span.style.opacity = "0";
      span.innerHTML = lines[i] + "\n";
      host.appendChild(span);
      requestAnimationFrame(function () { span.style.transition = "opacity .12s steps(3)"; span.style.opacity = "1"; });
      i++;
      setTimeout(step, 160);
    })();
  }

  /* ---------------- 跑马灯 ---------------- */
  function renderTicker() {
    var track = $("#tickerTrack");
    var items = (DATA.profile && DATA.profile.ticker) || [];
    if (!track || !items.length) return;

    var chunk = items.map(function (t) {
      return "<span><i></i>" + esc(t) + "</span>";
    }).join("");

    track.innerHTML = chunk + chunk;   // 复制一份实现无缝滚动
  }

  /* ---------------- 卡片 ---------------- */
  function makeCard(item, index, kind) {
    var card = document.createElement("article");
    card.className = "card reveal";
    card.dataset.tags = (item.tags || []).join(",");

    var empty = !item.src;
    if (empty) card.classList.add("card--empty");

    var thumb = document.createElement("button");
    thumb.className = "card__thumb";
    thumb.type = "button";
    thumb.setAttribute("aria-label", "查看 " + (item.title || ""));
    if (empty) thumb.disabled = true;

    if (!empty) {
      var img = document.createElement("img");
      img.loading = "lazy";
      img.decoding = "async";
      img.alt = item.title || "";
      img.src = item.src;
      img.onerror = function () { img.onerror = null; img.src = fallbackImg("NO IMAGE"); };
      thumb.appendChild(img);

      if (isPlaceholder(item.src)) {
        var badge = document.createElement("span");
        badge.className = "badge-slot";
        badge.textContent = "样例占位";
        thumb.appendChild(badge);
      }
    }
    card.appendChild(thumb);

    var body = document.createElement("div");
    body.className = "card__body";

    var h3 = document.createElement("h3");
    h3.className = "card__title";
    h3.innerHTML = "<span>" + esc(item.title || "") + "</span>" +
                   '<span class="card__index">' + String(index + 1).padStart(2, "0") + "</span>";
    body.appendChild(h3);

    if (item.desc) {
      var d = document.createElement("p");
      d.className = "card__desc";
      d.textContent = item.desc;
      body.appendChild(d);
    }

    if (item.tags && item.tags.length) {
      var tags = document.createElement("div");
      tags.className = "card__tags";
      item.tags.forEach(function (t) {
        var s = document.createElement("span");
        s.textContent = t;
        tags.appendChild(s);
      });
      body.appendChild(tags);
    }

    if (item.link) {
      var links = document.createElement("p");
      links.className = "card__links";
      links.innerHTML = '<a href="' + esc(item.link) + '" target="_blank" rel="noopener">查看项目 →</a>';
      body.appendChild(links);
    }

    card.appendChild(body);
    if (!empty) {
      card._item = item;
      card._kind = kind || "art";
    }
    return card;
  }

  /* ------------- 分页视图（数量没有硬上限，这里只控制首屏显示几条） ------------- */
  var state = {};

  function applyView(key, gridSel, moreSel) {
    var grid = $(gridSel);
    if (!grid) return;
    var st = state[key];
    if (!st) return;

    var cards = $$(".card", grid);
    var filtered = 0, visible = 0;
    cards.forEach(function (card) {
      var ok = st.filter === "全部" ||
               (card.dataset.tags || "").split(",").indexOf(st.filter) >= 0;
      if (ok) filtered++;
      var show = ok && (st.page === 0 || visible < st.page);
      card.classList.toggle("is-hidden", !show);
      if (show) visible++;
    });

    var box = $(moreSel);
    if (!box) return;
    box.innerHTML = "";
    var remaining = filtered - visible;
    if (st.page > 0 && remaining > 0) {
      var btn = document.createElement("button");
      btn.type = "button";
      btn.className = "btn";
      btn.textContent = "加载更多 · 还有 " + remaining + " 件";
      btn.addEventListener("click", function () {
        st.page += st.step;
        applyView(key, gridSel, moreSel);
        $$(".card", grid).forEach(function (c) { c.classList.add("is-in"); });
      });
      box.appendChild(btn);
    }
  }

  function initView(key, sizeKey, defSize) {
    var ps = DATA.pageSize || {};
    var n = ps[sizeKey] == null ? defSize : ps[sizeKey];
    state[key] = { filter: "全部", page: n, step: n === 0 ? 0 : n };
  }

  function renderArt() {
    var grid = $("#artGrid");
    var filterBox = $("#artFilters");
    if (!grid) return;

    var items = DATA.artworks || [];
    items.forEach(function (item, i) { grid.appendChild(makeCard(item, i, "art")); });

    if (filterBox) {
      var tags = [];
      items.forEach(function (it) {
        (it.tags || []).forEach(function (t) { if (tags.indexOf(t) < 0) tags.push(t); });
      });

      var all = ["全部"].concat(tags);
      all.forEach(function (tag, i) {
        var b = document.createElement("button");
        b.type = "button";
        b.textContent = tag;
        if (i === 0) b.classList.add("is-active");
        b.addEventListener("click", function () {
          $$("button", filterBox).forEach(function (x) { x.classList.remove("is-active"); });
          b.classList.add("is-active");
          state.art.filter = tag;
          applyView("art", "#artGrid", "#artMore");
        });
        filterBox.appendChild(b);
      });
    }
    applyView("art", "#artGrid", "#artMore");
  }

  function renderCode() {
    var grid = $("#codeGrid");
    if (!grid) return;
    (DATA.codeDemos || []).forEach(function (item, i) {
      grid.appendChild(makeCard(item, i, "code"));
    });
    applyView("code", "#codeGrid", "#codeMore");
  }

  /* ---------------- 视频演示 ---------------- */
  function renderVideos() {
    var list = $("#videoList");
    if (!list) return;

    var rerender = list.childElementCount > 0;
    list.innerHTML = "";

    (DATA.videos || []).forEach(function (item) {
      var row = document.createElement("article");
      row.className = "video-item reveal" + (rerender ? " is-in" : "") +
                      (item.src ? "" : " video-item--empty");

      var posterBtn = document.createElement("button");
      posterBtn.className = "video-item__poster";
      posterBtn.type = "button";
      posterBtn.setAttribute("aria-label", "播放 " + (item.title || ""));

      var img = document.createElement("img");
      img.loading = "lazy";
      img.decoding = "async";
      img.alt = item.title || "";
      img.src = item.poster || fallbackImg("VIDEO");
      img.onerror = function () { img.onerror = null; img.src = fallbackImg("VIDEO"); };
      posterBtn.appendChild(img);

      var play = document.createElement("span");
      play.className = "video-item__play";
      posterBtn.appendChild(play);

      if (item.src) {
        posterBtn.addEventListener("click", function () { openVideo(item); });
      } else {
        posterBtn.disabled = true;
        posterBtn.title = "还没有视频文件，把 assets/video/ 里的文件填进 js/data.js";
      }
      row.appendChild(posterBtn);

      var body = document.createElement("div");
      body.className = "video-item__body";
      body.innerHTML =
        '<h3 class="video-item__title">' + esc(item.title || "") + "</h3>" +
        (item.desc ? '<p class="video-item__desc">' + esc(item.desc) + "</p>" : "") +
        '<div class="video-item__meta">' +
          "<span>" + (item.date ? esc(item.date) : "&nbsp;") + "</span>" +
          '<span>' + (item.src ? "可播放" : "待上传") + "</span>" +
        "</div>";
      row.appendChild(body);

      list.appendChild(row);
    });

    // 视频分页
    var st = state.video;
    if (!st) return;
    var rows = $$(".video-item", list);
    var visible = 0;
    rows.forEach(function (row) {
      var show = st.page === 0 || visible < st.page;
      row.classList.toggle("is-hidden", !show);
      if (show) visible++;
    });
    var box = $("#videoMore");
    if (box) {
      box.innerHTML = "";
      var remaining = rows.length - visible;
      if (st.page > 0 && remaining > 0) {
        var btn = document.createElement("button");
        btn.type = "button";
        btn.className = "btn";
        btn.textContent = "加载更多 · 还有 " + remaining + " 条";
        btn.addEventListener("click", function () {
          st.page += st.step;
          renderVideos();
        });
        box.appendChild(btn);
      }
    }
  }

  /* ---------------- 关于页数字 / 工具 ---------------- */
  function renderStatsSkills() {
    var box = $("#stats");
    if (box) {
      (DATA.stats || []).forEach(function (s) {
        var el = document.createElement("div");
        el.className = "stat";
        el.innerHTML = '<div class="stat__num">' + esc(s.num) + '</div>' +
                       '<div class="stat__label">' + esc(s.label) + "</div>";
        box.appendChild(el);
      });
    }
    var ul = $("#skills");
    if (ul) {
      (DATA.skills || []).forEach(function (s) {
        var li = document.createElement("li");
        li.textContent = s;
        ul.appendChild(li);
      });
    }
  }

  /* ---------------- 灯箱 ---------------- */
  var lb = $("#lightbox"), lbImg = $("#lbImg"), lbTitle = $("#lbTitle"), lbMeta = $("#lbMeta");
  var lbIndex = 0, lbList = [];

  function paint() {
    var card = lbList[lbIndex];
    if (!card) return;
    var item = card._item;
    lbImg.src = item.src;
    lbImg.alt = item.title || "";
    lbTitle.textContent = item.title || "";
    lbMeta.textContent = (item.tags || []).join(" / ") + (item.date ? "  ·  " + item.date : "") +
                         "   [" + (lbIndex + 1) + "/" + lbList.length + "]";
  }

  function openLightbox(gridEl, card) {
    lbList = $$(".card:not(.is-hidden)", gridEl);
    lbIndex = Math.max(0, lbList.indexOf(card));
    paint();
    lb.hidden = false;
    document.body.style.overflow = "hidden";
    $("#lbClose").focus();
  }
  function closeLightbox() {
    lb.hidden = true;
    lbImg.src = "";
    document.body.style.overflow = "";
  }
  function step(delta) {
    if (!lbList.length) return;
    lbIndex = (lbIndex + delta + lbList.length) % lbList.length;
    paint();
  }

  function bindLightbox() {
    if (!lb) return;
    $("#lbClose").addEventListener("click", closeLightbox);
    $("#lbPrev").addEventListener("click", function () { step(-1); });
    $("#lbNext").addEventListener("click", function () { step(1); });
    lb.addEventListener("click", function (e) { if (e.target === lb) closeLightbox(); });

    document.addEventListener("keydown", function (e) {
      if (!lb.hidden && e.key === "Escape") closeLightbox();
      if (!lb.hidden && e.key === "ArrowLeft") step(-1);
      if (!lb.hidden && e.key === "ArrowRight") step(1);
    });

    // 事件委托：卡片缩略图点击（画作 + 代码截图都能放大看）
    ["#artGrid", "#codeGrid"].forEach(function (sel) {
      var grid = $(sel);
      if (!grid) return;
      grid.addEventListener("click", function (e) {
        var btn = e.target.closest ? e.target.closest(".card__thumb") : null;
        if (!btn || btn.disabled) return;
        var card = btn.closest(".card");
        if (card) openLightbox(grid, card);
      });
    });
  }

  /* ---------------- 视频弹窗 ---------------- */
  var vm = $("#videoModal"), player = $("#vmPlayer");

  function openVideo(item) {
    if (!vm) return;
    $("#vmTitle").textContent = (item.title || "video") + (item.date ? " · " + item.date : "");
    player.src = item.src;
    vm.hidden = false;
    document.body.style.overflow = "hidden";
    var play = player.play();
    if (play && play.catch) play.catch(function () { /* 自动播放被拦，等用户点播放 */ });
    $("#vmClose").focus();
  }
  function closeVideo() {
    if (!vm) return;
    try { player.pause(); } catch (e) {}
    player.removeAttribute("src");
    player.load();
    vm.hidden = true;
    document.body.style.overflow = "";
  }
  function bindVideo() {
    if (!vm) return;
    $("#vmClose").addEventListener("click", closeVideo);
    vm.addEventListener("click", function (e) { if (e.target === vm) closeVideo(); });
    document.addEventListener("keydown", function (e) {
      if (!vm.hidden && e.key === "Escape") closeVideo();
    });
  }

  /* ---------------- 顶栏：滚动高亮 + 移动菜单 ---------------- */
  function bindNav() {
    var links = $$(".nav__link");
    var sections = links
      .map(function (a) { return document.getElementById(a.getAttribute("href").slice(1)); })
      .filter(Boolean);

    if ("IntersectionObserver" in window && sections.length) {
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (en) {
          if (!en.isIntersecting) return;
          links.forEach(function (a) {
            a.classList.toggle("is-active", a.getAttribute("href") === "#" + en.target.id);
          });
        });
      }, { rootMargin: "-30% 0px -60% 0px", threshold: 0 });
      sections.forEach(function (s) { io.observe(s); });
    }

    var toggle = $("#navToggle"), nav = $("#nav");
    if (toggle && nav) {
      toggle.addEventListener("click", function () {
        var open = nav.classList.toggle("is-open");
        toggle.setAttribute("aria-expanded", open ? "true" : "false");
      });
      nav.addEventListener("click", function (e) {
        if (e.target.tagName === "A") {
          nav.classList.remove("is-open");
          toggle.setAttribute("aria-expanded", "false");
        }
      });
    }
  }

  /* ---------------- 滚动进入动画 ---------------- */
  function bindReveal() {
    var els = $$(".reveal");
    if (!els.length) return;

    var showAll = function () {
      els.forEach(function (el) { el.classList.add("is-in"); });
    };

    if (reduce || !("IntersectionObserver" in window)) {
      showAll();
      return;
    }
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (!en.isIntersecting) return;
        var el = en.target;
        var delay = Math.min(parseInt(el.dataset.delay || "0", 10) || 0, 400);
        setTimeout(function () { el.classList.add("is-in"); }, delay);
        io.unobserve(el);
      });
    }, { rootMargin: "0px 0px -10% 0px" });
    els.forEach(function (el, i) {
      el.dataset.delay = String((i % 4) * 60);
      io.observe(el);
    });
    // 兜底：无论如何，1.5s 后全部显示，绝不留白
    setTimeout(showAll, 1500);
  }

  /* ---------------- 时间 / 年份 ---------------- */
  function clock() {
    var el = $("#statusClock");
    if (!el) return;
    var tick = function () {
      var d = new Date();
      el.textContent = String(d.getHours()).padStart(2, "0") + ":" +
                       String(d.getMinutes()).padStart(2, "0");
    };
    tick();
    setInterval(tick, 20000);
  }

  function setupYear() {
    var y = $("#year");
    if (y) y.textContent = String(new Date().getFullYear());
  }

  /* ---------------- 启动 ---------------- */
  function init() {
    initView("art", "artworks", 12);
    initView("code", "codeDemos", 8);
    initView("video", "videos", 4);
    renderProfile();
    renderLinks();
    renderTerminal();
    renderTicker();
    renderArt();
    renderCode();
    renderVideos();
    renderStatsSkills();
    bindLightbox();
    bindVideo();
    bindNav();
    setupYear();
    clock();
    // 卡片渲染完再挂观察器
    requestAnimationFrame(bindReveal);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
