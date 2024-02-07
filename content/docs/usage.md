---
title: 如何使用
toc: true
weight: 1
---

## 安装libLoL

### 对于AOSC OS

请先将系统升级到最新：

```
sudo oma upgrade
```

下载最新版本`libLol`即[liblol_0.1.4.pre2](https://github.com/AOSC-Dev/liblol/releases)，进入下载目录，执行安装命令：

```
sudo oma install liblol_0.1.4.pre2-0_loongarch64.deb
```

### 对于Debian系统

首先下载[liblol-dkms](https://github.com/AOSC-Dev/la_ow_syscall/releases/tag/debian%2F0.1.0)，进入下载目录，执行安装命令：

```
sudo apt-get install ./liblol-dkms_0.1.0_loong64.deb
```

下载 [liblol_0.1.4.pre2-1_loong64.deb](https://github.com/AOSC-Dev/liblol/releases/download/debian%2Fv0.1.4_pre2-1/liblol_0.1.4.pre2-1_loong64.deb),
进入下载目录，执行安装命令：

```
sudo apt-get install ./liblol_0.1.4.pre2-1_loong64.deb
```

## 安装应用

您可在[龙芯应用合作社](http://app.loongapps.cn/#/home)或其他分发渠道下载并安装旧世界应用。

## 特殊操作

对于大部分旧世界应用，`libLOL`
已经做到让其在运行在新世界上。遗憾的是，仍有部分应用需要执行额外操作才能运行，详情请参考[应用兼容性](/docs/)。

## 运行应用

恭喜，在完成上述步骤后，您可以在”新世界“享受”旧世界”应用了！



