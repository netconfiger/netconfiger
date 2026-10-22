# NetConfiger GitHub Pages V6 发布与验收

**范围：仅 `https://github.com/netconfiger/netconfiger` 静态仓库。** 不修改 `netconfiger.com` 生产网站、Windows 程序、数据库及业务后台。

## 部署前确认

1. 记录仓库 `main` 当前最新 commit SHA。保留现有版本以便 `git revert`。
2. 检查 GitHub Settings → Pages 的实际发布源（通常 `main / (root)`；请以仓库配置为准）。
3. GitHub 当前可能出现网页缓存与 raw 分支文件不同步，**不得仅凭仓库普通文件页缓存判断发布失败**。以目标分支最新 commit + 实际公网 HTML 的 `nc-build` 一同核验。

## 覆盖文件

将压缩包**根目录**以下文件上传/覆盖到 `netconfiger/netconfiger` 仓库 `main` 分支根目录：

- `index.html` — 中文默认主页。
- `en.html` — 独立英文页面。
- `zh.html` — 兼容旧地址，自动跳转中文首页。
- `assets/site.css`、`assets/site.js` — 页面共用资源。
- `README.md` — 面向访客的产品介绍，**不是部署日志**。
- `DEPLOY.md` — 本文件。
- `.nojekyll` — GitHub Pages 静态发布标记。
- `tools/verify_site.py` — 静态自检脚本，不参与网页运行。

**仅有条件地清理：** 旧 `styles.css` 是 V3 遗留的深色样式，V6 未引用。核对仓库没有其他页面引用后可删除，避免误导维护者。不要不检查就删除其他 `assets/` 文件。

## 本地自动验收

在解压后的仓库根目录执行：

```powershell
python tools/verify_site.py
```

脚本验证页面语言、必要文件、跨语言跳转、共享 CSS/JS、旧 `zh.html` 重定向、相对静态资源和 HTML 基础结构。**不会检查外网图片是否加载或宣称浏览器截图已通过。**

## 发布后公网验收

1. [中文默认页](https://netconfiger.github.io/netconfiger/) 和 [中文 index.html](https://netconfiger.github.io/netconfiger/index.html)：应是同一个中文 V6 页面。
2. [英文页](https://netconfiger.github.io/netconfiger/en.html)：页面与标题均为英文，点击“中文”回到中文页。
3. [旧中文入口](https://netconfiger.github.io/netconfiger/zh.html)：跳转至 `index.html`。
4. [CSS](https://netconfiger.github.io/netconfiger/assets/site.css)、[JS](https://netconfiger.github.io/netconfiger/assets/site.js)：响应 200，页面能加载，且 `nc-build` 为 `gh-pages-v6-20261022`。
5. 检查 HTTPS 加载的 `https://netconfiger.com/icon.png` 和 `https://netconfiger.com/app-screenshot.png`：如某一图片加载失败，应从**官网真实源文件**下载、保存至 `assets/`，再替换引用；不要重新绘制 Logo 或伪造软件截图。
6. 使用真实浏览器在桌面 1366 宽度，以及手机 360 / 375 / 390 / 430 宽度检查：无横向溢出，菜单可打开/关闭，英文/中文切换正确，按钮和场景文章均指向对应语言的官方网站。
7. 将提交 SHA、Pages 工作流运行记录、线上响应与桌面/手机截图保存为独立验收证据。**没有真实的截图或访问结果，不能标记线上验收完成。**

## 已知依赖与限制

- 品牌 Logo 与真实软件截图仍然来自官网 URL。包内没有伪造的替代素材；**尚未完成图片本地化**。如要完全不依赖远程网站，需要从有权限访问官网的设备取得原始二进制图片。
- 这是静态介绍页；下载、价格、许可证和联系统一跳转实时官网，避免内容因版本变化而过期。
- 此包仅是已制作的覆盖更新文件，**不是**已直接推送的 GitHub commit，也不是线上部署完成证明。

## 回滚

使用部署前记录的 SHA 对本次提交执行 GitHub `Revert`，等待 Pages 重新发布，再验证入口页面与资源版本。不要 force push、不要修改生产官网或域名 DNS。
