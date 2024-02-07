---
title: 
toc: false
---

## <center>`libLoL`: AOSC 为您在新旧世界之间架起桥梁！

众所周知，LoongArch 的新旧世界生态割裂问题已经困扰了社区发行版用户许久：
虽然许多闭源软件都陆续支持了 LoongArch，但都是在采用旧世界 ABI 的商业发行版上，
从而与基于新世界 ABI 的社区发行版和用户群体「绝缘」。
虽然在早先[上证路演的投资者互动环节][sse-roadshow]、11 月 28 日的产品发布会上，
龙芯公司都表态将开发新旧世界应用的兼容方案，
但截至目前，关于龙芯方案的技术细节，满怀热忱的同学们仍未在公开渠道得到正面回应。
考虑到性能喜人的 3A6000 板卡已经陆续上市，不难作出合理推测：
总有群众等不及两年后（无论实际更早或更晚）这些软件的官方新世界版本，而**现在就要用**！

[sse-roadshow]: https://roadshow.sseinfo.com/roadshowIndex.do?id=16536#cd-placeholder-hdjl

[安同开源社区（AOSC）](https://aosc.io/)<icon="aosc">作为「牢记服务用户需求这一宗旨」的一群人，此刻便站了出来。我们给出的答案是
`libLoL`即 LoongArch on LoongArch。

AOSC 开发者[王邈][shankerwangmiao]与[刘子兴][liushuyu]
在内核层面实现了以外挂模块（亦可理解为「驱动」）方式，动态载入的旧世界系统调用支持。
王邈也设计、实现了位于用户态的运行时部分：打包了旧世界参考发行版 Loongnix&reg; 的核心运行时库，
使旧世界应用能够有「回家的感觉」从而正常启动。
目前 AOSC OS 已经能够运行 WPS Office 与龙芯浏览器等诸多旧世界应用。

[shankerwangmiao]: https://github.com/shankerwangmiao

[liushuyu]: https://github.com/liushuyu

在完成配套内核模块的载入向导后，使用龙架构设备的 AOSC OS 用户可按需启用此兼容方案。AOSC
同仁们也欢迎其他新世界发行版维护者考察 `libLoL`，并视自身情况和需求集成此项目的成果。

AOSC双周报[《安记冰室・十二月下》](https://github.com/AOSC-Dev/newsroom/blob/2c5443a792291702438cbf6059d8d4039ca5dc85/coffee-break/20231223/zh_CN.md#%E5%B1%95%E6%9C%9B-liblol%E9%BE%99%E6%9E%B6%E6%9E%84%E6%97%A7%E4%B8%96%E7%95%8C%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F%E5%85%BC%E5%AE%B9%E8%BF%90%E8%A1%8C%E6%97%B6)
与[咱龙了吗？](https://areweloongyet.com/docs/world-compat-details/liblol)记载了这项工作的更多信息，推荐阅读。

{{< cards >}} 
{{< card link="/docs/apps" title="应用兼容性" icon="document-duplicate" >}}
{{< card link="/docs/usage/#对于aosc-os" title="为AOSC OS安装" icon="aosc-os" >}} 
{{< card link="/docs/usage/#对于debian系统" title="为Debian安装" icon="debian" >}} 
{{< card link="/docs/liblol" title="技术文档" icon="aosc" >}} 
{{< /cards >}}
{{< cards >}} 
{{< card link="/docs/apps" title="如何使用" icon="document-duplicate" >}}
{{< card link="usage" title="应用兼容性" icon="document-duplicate" >}} 
{{< card link="usage" title="技术文档" icon="document-duplicate" >}} 
{{< card link="usage" title="报告兼容性" icon="github" >}} 
{{< card link="usage" title="提交应用信息" icon="github" >}} 
{{< card link="usage" title="问题反馈" icon="github" >}} 
{{< /cards >}}


