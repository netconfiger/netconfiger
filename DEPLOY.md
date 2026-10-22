# GitHub Pages V5 覆盖部署与验证清单

> 部署范围：`netconfiger/netconfiger` 仓库。绝对不要将本包上传到 `netconfiger.com` 生产服务器。

## 0. 先保留当前仓库版本

访问 https://github.com/netconfiger/netconfiger ，记录目前 main 的 commit SHA，确保可通过 GitHub Revert 恢复。不要 force push。

## 1. 覆盖文件与清理

将 ZIP 根目录中的以下文件合并/覆盖到 **仓库 main 根目录**（不是上一级，也不是创建同名子文件夹）：

- `index.html`, `en.html`, `zh.html`, `.nojekyll`, `README.md`, `DEPLOY.md`
- `assets/site.css`, `assets/site.js`

检查仓库原 `styles.css` 是否仍被任何 HTML 使用。如果无人引用，建议删掉；不能只上传文件而保留另一套仍可访问的过期入口。原仓库已存在 `assets/`，合并而非盲目删除其中未知文件。

## 2. Pages 发布源

GitHub → Repository Settings → Pages → Build and deployment，核实 `Deploy from a branch` 对应 `main / (root)`，或核实当前 Actions 的构建目录。此前公开网页与仓库源代码存在旧/新不一致，必须实际查出发布路径或缓存原因。

## 3. 验证最新公网内容

以下 URL 全部打开核实：

- https://netconfiger.github.io/netconfiger/
- https://netconfiger.github.io/netconfiger/index.html
- https://netconfiger.github.io/netconfiger/en.html
- https://netconfiger.github.io/netconfiger/zh.html
- https://netconfiger.github.io/netconfiger/assets/site.css
- https://netconfiger.github.io/netconfiger/assets/site.js

查看 `index.html` 源码含 `<meta name="nc-build" content="gh-pages-v5-20261022">`，网页正文第一屏有 `Windows 网络分发` 且是中文，不得继续返回 “More control over your network path.” 旧英文页面。无痕窗口再检查一次。`zh.html` 应跳转 `index.html`。

移动端 360 / 375 / 390 / 430 宽度：菜单可展开、关闭，页面无横向滚动；英文和中文切换可用。检查真实 Logo、截图是否加载；本站依赖官网的 2 张图片 URL，若加载失败，应先将**原图**保存到仓库再切本地引用，而不是重绘标识。

## 4. 交付范围与未完成

本 ZIP 可直接作为覆盖包，已做静态结构检查和本地浏览器截图检查（详见随包截图、若提供）。没有操作用户 GitHub 账户，**没有 commit SHA、没有 GitHub Pages 实际发布完成记录，也不能标记线上 CLOSED**。

旧文件迁移仍需在真实仓库执行；图像本地化仍需在可访问官网时完成。

## 5. 回滚

记录本次更新前的 SHA；如果实际发布出现错误，使用 GitHub Revert 撤销本次 commit 并等候 Pages 下一轮部署，然后确认原页面内容。不要删除仓库历史、修改 CNAME/DNS 或强推。
