---
title: 应用兼容性数据库
toc: true
weight: 2
type: apps
cascade:
  type: apps
---

libLoL 应用兼容性数据由社区贡献者维护，兼容性报告对应的应用版本、来源和更新时间等信息均在页面中列出。其中兼容性使用如下方式表示：

- {{< compatibility-icon 4 >}} 应用程序已经提供新世界 ABI 版本或提供了源代码，无需使用旧世界上的软件包；
- {{< compatibility-icon 3 >}} 应用程序的功能均可正常使用，尚未发现功能异常；
- {{< compatibility-icon 2 >}} 应用程序已知部分功能不可用或存在问题；
- {{< compatibility-icon 1 >}} 应用程序完全无法正常使用；
- {{< compatibility-icon 0 >}} 尚未测试该应用程序。

请注意，一些应用可能会需要额外操作才能实现相对应的兼容性。

## 应用来源

如果您发现某些应用无法通过 libLoL 运行，请联系我们。报告方式详见[报告兼容性问题](/docs/report/)页面。

{{< cards >}} 
{{< card link="/docs/apps/loongapps/" title="龙芯应用合作社" icon="loongapp" >}}
{{< card link="/docs/apps/other/" title="其他来源" icon="globe" >}}
{{< card link="/docs/report/" title="报告兼容性问题" icon="exclamation-circle" >}}
{{< /cards >}}
