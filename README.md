# PLUM921 · 个人主页

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
、字体授权

字体文件按 SIL Open Font License 1.1 授权，完整文本见 `fonts/OFL.txt`。
要求保留字体名称「方舟像素 / Ark Pixel」，页脚已按规范署名并回链项目地址，**请勿删除页脚署名**。

当前附带的是官方 `2026.09.25` 版的 12px 比例模式（proportional）woff2：

- `fonts/ark-pixel-12px-proportional-latin.woff2`
- `fonts/ark-pixel-12px-proportional-zh-hans.woff2`

如需更新，去 [Releases](https://github.com/TakWolf/ark-pixel-font/releases) 下载 `...-12px-proportional-otf.woff2-*.zip` 覆盖同名文件即可（建议保持文件名不变）。
