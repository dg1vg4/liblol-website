---
title: 打包注意事项
toc: true
weight: 2
---

本文面向发行版打包人员，介绍了打包 libLoL 的方法，以及需要注意的内容。

本文描述的内容都是基于 libLoL 0.1.5 版本的现状而总结的。
本文的最后更新日期是 2024.04.02。

## libLoL 的打包方法 {#packaging-of-liblol}

目前，libLoL 项目的运行时部分实质上是 `patchelf` 工具和 glibc 的补丁合集，以及
AOSC OS（或 Debian）的构建脚本。

大体的构建过程如下：

* 为 `patchelf` 打上补丁，构建出专用的 `patchelf` 工具；
* 构建 glibc 的动态链接库及 libxcrypt；
* 用先前准备的专用 `patchelf` 为得到的动态链接库进行后处理；
* 将处理过的库，作为优先加载的库，安装到预定的目录布局。

细节上看，由于 glibc 的构建系统十分复杂，为防止 `patchelf` 之后的产物被覆盖，需要做不少特殊处理。
其他部分，如库搜索路径配置、目标系统的目录布局等，也存在特别处理，详见 libLoL 的构建脚本。

这一构建过程较为复杂，并且难以用发行版无关的方式描述，因此 libLoL 难以简单地被打包到其它发行版中，用户也很难自行构建。
目前，libLoL 项目提供适配 AOSC OS 和 Debian 的发行包。
其他需要打包 libLoL 的发行版开发人员需要根据本发行版对 glibc 的处理方式，以及目录布局等相关情况，
按照上述基本流程为本发行版定制 libLoL 构建方式。

## libLoL 与 `patchelf` {#liblol-and-patchelf}

新旧世界的 glibc 的架构初始版本不同，为了能让修改过的 glibc 支持旧世界可执行文件加载新世界的动态链接库，
必须要同时提供新旧世界的符号版本。这意味着，对于 glibc 中大多数没有经历过 ABI 版本变更的符号，
要同时创建两个版本的符号指向同一个函数；对于经历过 ABI 版本变更的那些符号，也要类似地调整。
理论上，通过修改 glibc 的代码，可以达到这一目的。但是，这样的修改会使得 glibc 的代码修改量巨大，
难以维护。

为此，libLoL 选择了另一种实现思路，即在编译 glibc 完成后，通过“后处理程序”，
修改其动态符号表和符号版本表，使得该 glibc 同时提供新旧世界的符号版本。

`patchelf` 是一个可以修改 ELF 文件的工具，但缺乏上述功能。为此，libLoL 为 `patchelf`
增加了这一重新映射符号版本的功能，以支持 libLoL 的需求。
但在 libLoL 维护者目前看来，该功能的适用场景过于罕见，因而不适合被合并到 `patchelf` 上游。
这就是为何打包者们需要在 libLoL 的构建过程中，构建专用 `patchelf`，或打一个单独的 `patchelf-liblol` 之类的包并使 libLoL 在构建时依赖之。

## libLoL 运行时的 glibc 版本 {#glibc-version-of-liblol}

libLoL 使得旧世界的可执行程序可以加载新世界的动态链接库。对被载入的新世界的动态链接库而言，
它所依赖的 glibc 实际上已经是来自 libLoL 而非宿主了；
但由于构建这些新世界原生库时使用的 glibc 是宿主系统的，因此这些新世界库将会期待在 libLoL libc
中看到宿主 glibc 版本的 ELF 符号。

这意味着：libLoL 自身提供的 glibc 版本不可以低于新世界宿主系统的 glibc 版本。

目前，libLoL 0.1.5 提供的 glibc 基于 2.39 版本。
libLoL 项目与打包者们需要紧密跟踪 glibc 的新版本，如果未来某个版本的 glibc 引入了新的 ELF 符号版本，libLoL
便要做相应更新。
