/* =========================================================
   PLUM921 · 站点内容配置
   ---------------------------------------------------------
   ★ 你以后只需要改这个文件 ★
   图片/视频文件放进 assets/ 对应目录，然后在这里填相对路径。
   路径写错或文件不存在时，页面会自动回退到占位图，不会白屏。
   ========================================================= */

window.SITE_DATA = {

  /* ---------- 0. 每区首屏显示数量（没有硬性上限，只是分页大小） ----------
     数组里的条目超过这个数时，底部会出现「加载更多」按钮；
     想一页全显示就把数字改大（比如 999）或设为 0 表示不分页。 */
  pageSize: {
    artworks: 12,   // 画作
    codeDemos: 8,   // 代码截图 / 动图
    videos: 4       // 视频演示
  },

  /* ---------- 1. 基本信息 ---------- */
  profile: {
    name: "PLUM921",
    role: "画画 / 写代码 / 做点小东西",
    intro: "这里是黄时，个人主页兼顾画作和代码作品，目前还在制作中，其他内容后面会陆续放进来。",
    avatar: "assets/avatar/image.png",   // 【替换】换成 assets/avatar/头像.png
    footerName: "黄时PLUM",// 头像下方的名字
    // 顶部横幅（建议 480×60 或更宽的低分辨率横构图像素图，页面全宽铺满）
    banner: "assets/banner/orchard-480x60.png",       // 【替换】换成你自己的图
    bannerAlt: "风景",// 横幅的 alt 属性
    bannerCap: "ORCHARD",                   // 横幅下沿的说明文字
    bannerMeta: "480 × 60 px",

    // 终端窗口里的文字，逐行显示。可用 <span class="t-red"> 与 <span class="t-dim"> 上色。
    terminal: [
      '$ whoami',
      '<span class="t-red">plum921</span>',
      '$ cat interests.txt',
      '<span class="t-dim">// 画画、代码、像素、复古游戏</span>',
      '$ ls ./works',
      '<span class="t-dim">artworks/  code-demos/  videos/</span>',
      '$ status --now',
      '装修中…… 欢迎随便逛逛 <span class="t-red">_</span>'
    ],

    // 顶部跑马灯文案
    ticker: [
      "祝你阅览愉快",
      "ART & CODE",
      "Plum",
      "正在持续更新中",
      "THANKS FOR VISITING",
      "迎接清晨，欢度学习的每天",
      "祝你阅览愉快",
      "ART & CODE",
      "Plum",
      "正在持续更新中",
      "THANKS FOR VISITING",
      "迎接清晨，欢度学习的每天"
    ]
  },

  /* ---------- 2. 社交链接（增删都可以，href 填 # 时表示还没填） ---------- */
  links: [
    { label: "GitHub",  href: "https://github.com/Plum921-dowhat" },
    { label: "Bilibili", href: "#" },
    { label: "lofter",   href: "#" },
    { label: "Email",   href: "#" }
  ],

  /* ---------- 3. 画作 ----------
     src   : 图片路径（建议放进 assets/artworks/）
     tags  : 会出现在筛选按钮里
  --------------------------------- */
  artworks: [
    { title: "作品 01", src: "assets/artworks/Transformer.png", tags: ["插画"], date: "2026", desc: "占位内容，替换成你自己的画。" },
    { title: "作品 02", src: "assets/artworks/art-02.svg", tags: ["像素画"], date: "2026", desc: "占位内容，替换成你自己的画。" },
    { title: "作品 03", src: "assets/artworks/art-03.svg", tags: ["插画"], date: "2026", desc: "占位内容，替换成你自己的画。" },
    { title: "作品 04", src: "assets/artworks/art-04.svg", tags: ["草图"], date: "2026", desc: "占位内容，替换成你自己的画。" },
    { title: "作品 05", src: "assets/artworks/art-05.svg", tags: ["oc"], date: "2026", desc: "占位内容，替换成你自己的画。" },
    { title: "作品 06", src: "assets/artworks/art-06.svg", tags: ["草图"], date: "2026", desc: "占位内容，替换成你自己的画。" }
  ],

  /* ---------- 4. 代码截图 / 动图 ---------- */
  codeDemos: [
    { title: "项目 01", src: "assets/code/code-01.svg", tags: ["Web"], date: "2026", desc: "项目简介写这里。", link: "" },
    { title: "项目 02", src: "assets/code/code-02.svg", tags: ["工具"], date: "2026", desc: "项目简介写这里。", link: "" },
    { title: "项目 03", src: "assets/code/code-03.svg", tags: ["实验"], date: "2026", desc: "项目简介写这里。", link: "" },
    { title: "项目 04", src: "assets/code/code-04.svg", tags: ["Web"], date: "2026", desc: "项目简介写这里。", link: "" }
  ],

  /* ---------- 5. 视频演示 ----------
     src    : 视频文件（mp4/webm）。留空 "" 时显示"待上传"占位。
     poster : 封面图。留空会自动用占位图。
  --------------------------------- */
  videos: [
    { title: "视频演示 01", src: "", poster: "assets/video/poster-01.svg", date: "", desc: "放一段录屏或动效演示，支持 mp4 / webm。" },
    { title: "视频演示 02", src: "", poster: "assets/video/poster-02.svg", date: "", desc: "在此填充并上传视频。" }
  ],

  /* ---------- 6. 关于页 ---------- */
  about: [
    "你好，很高兴认识你 —— 网站内容为个人自我介绍和作品展示。",
    "这个站点主要用来存放作品与实验，其本身也是实验内容，正在慢慢更新中。"
  ],
  stats: [
    { num: "8",  label: "年的画画经历" },
    { num: "若干",  label: "项目经验" },
    { num: "∞",  label: "在学的东西" },
    { num: "200", label: "余额" }
  ],
  skills: ["Photoshop", "Procreate", "JavaScript", "Python", "Unity", "Blender"]
};
