## 基本

使用 [Markdown](https://en.wikipedia.org/wiki/Markdown)  来书写内容，创建列表。支持绝大多数相关语法。

### LaTex公式

参考[latex-project.org](https://www.latex-project.org/) 。

### Mermaid图表

参考[Mermaid | Diagramming and charting tool](https://mermaid.js.org/) 。

## 文件名

一般情况下取`应用编号.md`作为文件名。

## 文档头(Front-matter)

```
---
title: 应用名称      //也作为文档的一级标题
toc: true/false    //侧边栏开启/关闭，一般情况下为true。
weight: 应用编号         //文档的排列顺序。一般情况下，取应用编号的值。
draft: true/false  //当值为true时文档作为草稿，不渲染。
---
```

## 文档内容

### 引用站内资源

#### 静态内容

文档中的静态内容存放于仓库目录`/static`中。一般情况下，将`/static`视为根目录，并以**绝对路径**方式引用。

- 引用图片`/static/images`中的`logo.svg`:

```
![](/images/logo.svg)
```

- 引用文件`/static/data`中的`loongapplist-latest.csv`:

```
[loongapplist-latest.csv](/data/loongapplist-latest.csv)
```

#### 引用文档

一般情况下，将仓库目录`/content`视为根目录，以**绝对路径**方式引用，但无需添加文件扩展名。

- 引用`/content/docs/dev/liblol.md`

```
[libLoL](/docs/dev/liblol)
```


### 标题

内容的最高级标题应为H2，H1为文档头的`title: 应用名称` 渲染生成。

### 应用编号

- 龙芯应用合作社

跟随[龙芯应用合作社](http://app.loongapps.cn/#/home) 编号，应用编号也为该应用的文档名。

- 其他来源

按报告顺序以1开始的正整数为编号，应用编号也为该应用的文件名。

### 历史版本

历史版本以应用的历史版本号作为标题，将对应版本的文档内容挪入。

结构参考`/template`

### 兼容性

* 可用
* 部分功能可用
* 不可用

### 额外操作
* 无
* 有

![应用详情文档结构](/static/images/应用详情文档结构.png)

