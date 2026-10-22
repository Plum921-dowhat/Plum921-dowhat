# PLUM921 · 像素小屋

个人主页静态站点（纯 HTML / CSS / JS，无构建、无依赖），可直接部署到 GitHub Pages。

风格：复古像素 · 低饱和红 + 米白
字体：[方舟像素字体 Ark Pixel Font](https://github.com/TakWolf/ark-pixel-font)（SIL OFL 1.1，文件已随仓库附带）

---

## 一、目录结构

```
Plum921-dowhat/
├── index.html            页面骨架（区块与占位标记都在这里）
├── 404.html              GitHub Pages 的 404 页
├── favicon.svg           站点图标
├── .nojekyll             让 GitHub Pages 原样发布（别删）
├── css/style.css         全部样式，主题色集中在文件顶部 :root
├── js/
│   ├── data.js           ★ 内容配置：文字、链接、作品列表都改这里
│   └── main.js           交互逻辑（一般不用动）
├── fonts/                像素字体 + OFL 授权
└── assets/               素材目录
    ├── banner/           顶部像素横幅（建议 480×60 或更宽的横构图）
    ├── avatar/           头像（1 张）
    ├── artworks/         画作（建议 1:1 方图）
    ├── code/             代码截图 / 动图（建议 16:9）
    └── video/            视频文件与视频封面（建议 16:9）
```

## 二、本地预览

直接双击 `index.html` 就能看（内容是从 `js/data.js` 读的，不依赖服务器）。
注意：用 `file://` 打开时浏览器可能拒绝加载本地字体，**验证字体效果请起一个本地服务**：

```bash
# 在 Plum921-dowhat 目录下执行
python -m http.server 8080

# 然后浏览器打开 http://localhost:8080
```

## 三、换素材（三步）

以加一张画作为例：

1. 把你的图丢进 `assets/artworks/`，例如 `assets/artworks/my-drawing.png`
2. 打开 `js/data.js`，在 `artworks` 数组里加一条：
   ```js
   { title: "我的画", src: "assets/artworks/my-drawing.png", tags: ["插画"], date: "2026", desc: "一句话说明" }
   ```
3. 刷新页面即可。`tags` 里的词会自动生成顶部筛选按钮。

其他区块同理：

| 想改什么 | 改哪里 |
| --- | --- |
| 顶部像素横幅 | `data.js` → `profile.banner` / `bannerCap`（图片放 `assets/banner/`） |
| 名字 / 简介 / 头像 / 终端文字 / 跑马灯 | `data.js` → `profile` |
| 社交链接 | `data.js` → `links` |
| 画作 | `data.js` → `artworks`（图片放 `assets/artworks/`） |
| 代码截图 / 动图 | `data.js` → `codeDemos`（图片放 `assets/code/`） |
| 视频演示 | `data.js` → `videos`（`src` 填 `assets/video/xxx.mp4`，留空则显示"待上传"） |
| 关于我正文 / 数字面板 / 工具标签 | `data.js` → `about`、`stats`、`skills` |
| 主题配色 | `css/style.css` 顶部 `:root` 里的颜色变量 |

**容错**：路径写错或文件不存在时，会自动显示占位图，不会白屏。
**当前 `assets/` 里全是脚本生成的像素占位图**，替换后可以直接删掉不用的那张。

**画作图片浏览器**：在画作画廊点击任意一张图进入大图浏览，支持——
滚轮缩放（以光标为锚点）、工具条 +/−/适应/全屏、拖拽平移、双击在"适应 ↔ 250%"间切换、
键盘 `+` / `-` / `0` 缩放、`F` 全屏（或点工具条「全屏」按钮，ESC 退出）。
进入全屏会自动放大到**图片铺满整个屏幕**（cover：短边撑满、长边溢出可拖拽查看），
再缩小或点「适应」可回到完整视图。双指捏合在触屏上同样可用；`←` `→` 翻页时自动复位。
代码截图区仍是最初的简洁灯箱（不带缩放），两者互不影响。
灯箱关闭方式：按 `ESC` 或点击图片外的深色区域（无关闭按钮）。

## 四、素材数量有没有上限？

**没有硬性上限。** `artworks` / `codeDemos` / `videos` 都是普通数组，想放多少条就放多少条，
页面上现阶段的 6 / 4 / 2 只是占位示例。

为了在素材很多时依然流畅，站点做了分页：每个区块首屏默认显示
`pageSize` 里配置的数量（画作 12 / 代码 8 / 视频 4），超出的部分折叠在
「加载更多」按钮后面，点一次多显示一批。想一页全显示就把数字改大（如 `999`）或设为 `0`：

```js
pageSize: { artworks: 12, codeDemos: 8, videos: 4 }
```

需要留意的客观限制来自托管平台，与代码无关：

- GitHub Pages：单文件 ≤ 100 MB，仓库建议 ≤ 1 GB（超了页面会变慢，建议视频压缩后再传）；
- 浏览器：图片都带 `loading="lazy"`，只有滚动到附近才会真正加载，几百张图也没问题。

## 五、主题色

在 `css/style.css` 的 `:root` 里改这几个变量就能整体换色：

```css
--cream:    #F3EBDE;  /* 米白主背景 */
--red:      #B4575D;  /* 低饱和红（主色） */
--red-deep: #8B3A43;  /* 深红（强调 / 阴影） */
--ink:      #3A2E2B;  /* 文字与描边 */
--mustard:  #C69A57;  /* 点缀色 */
--sage:     #8CA08B;  /* 点缀色 */
```

## 六、部署到 GitHub Pages

1. 新建仓库，例如 `Plum921-dowhat`（或直接用 `<你的用户名>.github.io` 这个仓库名做个人主页根站）。
2. 把本目录内容推到仓库根目录：
   ```bash
   git init
   git add .
   git commit -m "feat: 像素风个人主页"
   git branch -M main
   git remote add origin git@github.com:<你的用户名>/Plum921-dowhat.git
   git push -u origin main
   ```
3. 仓库页面 → **Settings → Pages** → Source 选 `Deploy from a branch`，Branch 选 `main` + `/ (root)`，保存。
4. 等 1 分钟左右访问 `https://<你的用户名>.github.io/Plum921-dowhat/`。

> 站点已放置 `.nojekyll` 并全部使用相对路径，放在子路径下也能正常显示。

## 七、字体授权

字体文件按 SIL Open Font License 1.1 授权，完整文本见 `fonts/OFL.txt`。
要求保留字体名称「方舟像素 / Ark Pixel」，页脚已按规范署名并回链项目地址，**请勿删除页脚署名**。

当前附带的是官方 `2026.09.25` 版的 12px 比例模式（proportional）woff2：

- `fonts/ark-pixel-12px-proportional-latin.woff2`
- `fonts/ark-pixel-12px-proportional-zh-hans.woff2`

如需更新，去 [Releases](https://github.com/TakWolf/ark-pixel-font/releases) 下载 `...-12px-proportional-otf.woff2-*.zip` 覆盖同名文件即可（建议保持文件名不变）。
