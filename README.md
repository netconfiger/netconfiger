# NetConfiger GitHub Pages V3 修正版

- `index.html`：默认简体中文首页。
- `en.html`：英文页面，右上角切换。
- `assets/site.css`：统一响应式样式。
- 页面中三个功能图标使用本地内联 SVG，不依赖第三方图标库。
- NetConfiger 品牌图标仍引用 `https://netconfiger.com/favicon.ico`，因为无法从当前环境下载核实官网真实图标。**此项尚未完成本地化**，请勿将其视为已完整修复。

## 部署
把 `index.html`、`en.html`、`assets/` 放在 GitHub Pages 仓库 main 分支根目录。删除旧 `zh.html` 或保留它作为历史文件（本版不再引用）。

本版是中文优先、功能图标完整的修正版，但不是官网 CSS 源码的逐像素复制。
