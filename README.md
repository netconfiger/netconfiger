# NetConfiger GitHub Pages V5

覆盖包：`netconfiger/netconfiger` 静态 Pages 仓库根目录。`index.html` 为简体中文默认页，`en.html` 为独立英文页，`zh.html` 将旧中文地址转到首页。共享 CSS/JS 均使用相对 `./assets/` 路径，可部署于 `/netconfiger/` 子路径。

导航目标按官网当前中文 `/zh` 与英文 `/` 页面校准；下载入口指向官网语言对应的下载页。页面保留官网原始 Logo (`https://netconfiger.com/icon.png`) 与产品截图 (`https://netconfiger.com/app-screenshot.png`) 原址，不重绘品牌。当前执行环境无法以网络请求取得图片二进制，因此这两个真实原站资源仍为远程引用；浏览器联网可用时会由官网提供。

包内文件：index.html、en.html、zh.html、assets/site.css、assets/site.js、.nojekyll、README.md、DEPLOY.md。上传后请在 GitHub Pages 子路径检查四个入口、资源加载和移动端实际交互。