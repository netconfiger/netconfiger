# NetConfiger — Windows VPN 共享与 HTTP/SOCKS5 局域网分发

**让一台已经连通业务网络的 Windows 主机，服务多个支持代理的工作站。**

[**中文产品页面**](https://netconfiger.github.io/netconfiger/) · [**English landing page**](https://netconfiger.github.io/netconfiger/en.html) · [**官方网站**](https://netconfiger.com/zh) · [**下载并试用 3 天**](https://netconfiger.com/zh/download) · [**使用指南**](https://netconfiger.com/zh/knowledge)

<p align="center"><a href="https://netconfiger.com/zh"><img src="https://netconfiger.com/icon.png" width="68" height="68" alt="NetConfiger 官方标识" /></a></p>

## 这是什么软件？

很多团队已经在 Windows 电脑上连接了 SoftEther、PacketiX、办公 VPN 或其他业务网络，但仍有广告运营电脑、客服工位、浏览器环境和虚拟机需要接入。重复安装上游客户端不仅麻烦，也增加交接和维护成本。

**NetConfiger** 运行在已连通的 Windows 主机上，将客户自己准备并授权的网络连接提供为 **HTTP/SOCKS5 局域网代理入口**。支持显式代理的下游应用配置主机的 LAN IP 和监听端口，即可按需使用这条连接。

> **能力边界：** NetConfiger 不销售 VPN 账号、代理节点或线路；当前公开版本是显式 HTTP/SOCKS5 代理分发，**不是整机透明网关或二层网络桥接**。实际接入取决于应用对代理的支持以及主机、防火墙、DNS 等网络条件。

### 软件实际界面

[![NetConfiger Windows 软件界面](https://netconfiger.com/app-screenshot.png)](https://netconfiger.com/zh/software)

*图像来自 NetConfiger 官方网站。以官网下载的当前版本为准。*

## 适用场景

| 真实需求 | 使用方式 | 详细说明 |
| --- | --- | --- |
| **SoftEther / PacketiX 客户端共享** | 上游客户端保留在 Windows 主机，其他支持代理的电脑和虚拟机连接统一入口 | [办公室复用方案](https://netconfiger.com/zh/packetix-softether-windows-network-reuse) |
| **Facebook Ads / Instagram 团队** | 广告、主页、客服和浏览器工位复用团队已经准备好的业务网络环境 | [社媒运营团队场景](https://netconfiger.com/zh/facebook-ads-browser-environment) |
| **BitBrowser / AdsPower 工位** | 给浏览器配置文件、虚拟机、运营电脑统一记录代理入口和操作流程 | [浏览器工位方案](https://netconfiger.com/zh/bitbrowser-adspower-network-environment) |

## 三步使用

1. **连通 Windows 主机。** 先在主机上连接并验证客户自己的 Windows VPN 或业务网络。
2. **开启 NetConfiger。** 按实际需求启用 HTTP 和/或 SOCKS5，确认主机局域网地址与软件显示的监听端口。
3. **配置下游应用。** 在支持显式代理的浏览器、业务软件或虚拟机中填写该地址和端口，并验证真实业务是否走预期出口。

**试用和授权：** 官网提供中文及英文 Windows 安装程序和 3 天试用信息；正式授权、设备数量、版本与价格请以 [官方下载安装页面](https://netconfiger.com/zh/download) 和 [授权套餐](https://netconfiger.com/zh/pricing) 为准。此仓库不提供商业软件安装包或授权文件。

---

## English — Windows VPN sharing for proxy-aware LAN clients

**Reuse an existing, authorized Windows network connection across compatible PCs, VMs and browser workstations.** NetConfiger runs on the Windows host and exposes HTTP/SOCKS5 LAN endpoints. Downstream applications explicitly configure the host LAN IP and listening port; no upstream client is required on every compatible workstation.

Typical workflows include [PacketiX / SoftEther client reuse](https://netconfiger.com/packetix-softether-windows-network-reuse), [Facebook Ads / Instagram operations](https://netconfiger.com/facebook-ads-browser-environment), and [BitBrowser / AdsPower workstations](https://netconfiger.com/bitbrowser-adspower-network-environment).

**Important:** NetConfiger does not supply VPN accounts or proxy lines. The currently published product uses explicit HTTP/SOCKS5 proxy configuration; it is not a transparent whole-device gateway.

[**English product page**](https://netconfiger.github.io/netconfiger/en.html) · [**Official download & 3-day trial**](https://netconfiger.com/download) · [**Documentation**](https://netconfiger.com/knowledge) · [**Features**](https://netconfiger.com/features)

---

### 关于这个 GitHub 仓库 / About this repository

此仓库托管 NetConfiger 官方 **GitHub Pages 双语产品介绍页面**，**并非 NetConfiger 商业软件的开源代码仓库**。除非另有独立的许可说明，不应据此推断软件源代码已开源。

This repository contains the bilingual static GitHub Pages companion site, **not the source code of the commercial Windows application**. Do not assume the application is open source.

网站部署、变更验证及回滚说明见 [`DEPLOY.md`](./DEPLOY.md)。如需安装、授权、技术支持，请从 [netconfiger.com](https://netconfiger.com/zh) 进入。
