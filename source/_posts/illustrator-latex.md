---
title: 在illustrator中使用latex公式
date: 2017-12-04 07:39:43
updated: 2017-12-04 07:39:43
tags: tool
categories: tool
---

Adobe Illustrator 是一款强大的矢量图形软件，当我们在里面做好图形后，可能需要在里面插入一些数学符号或者数学公式什么的，这时一般考虑使用 Latex 来输出这些特殊文本。下面介绍一下如何在 Illustrator 中使用 Latex 。

## 安装 LaTeX
LaTeX 有很多发行版，在[这里](http://latex.org/know-how/latex-distributions)可以查看到。我在windows环境下使用的是 [MikTeX](https://miktex.org/)，在[这里](https://miktex.org/download)下载了安装包后，按照正常的Windows软件安装流程进行安装，途中可能会提示安装一些依赖，按照提示进行操作即可。

安装完 Latex 后，需要确认一下从 PATH 环境变量里能否搜索到 pdflatex 命令，如果不能，则需要将 pdflatex 所在的文件夹添加到 PATH 环境变量里。

## 安装 LaTeX 字体
LaTeX 会使用一些特殊的字体，为了让导出的文本能够在 Illustrator 中正常显示，需要让 Illustrator 能够搜索到这些字体。比较简单省事的做法是将这些字体拷贝到adobe的字体文件夹里。例如在Windows上，将 `D:\Program Files\MiKTeX 2.9\fonts\type1\public\amsfonts\cm` 文件夹里的文件全部拷贝到 `C:\Program Files\Common Files\Adobe\Fonts` 文件夹。

## 将 LaTeX 导出到 Illustrator
Illustrator 可以从PDF文件中导入单独的页面，因此，可以先将 Latex 代码编译成PDF(可以使用pdflatex)，再将PDF导入到 Illustrator 中去。

为了简化 `Latex -> PDF -> Illustrator` 这一过程，有一些脚本可供使用，例如 [latex-illustrator](https://github.com/mkuznets/latex-illustrator) 和 [illustratorLatexEquations](https://dl.dropboxusercontent.com/s/otp2zdmqx2peaf5/illustratorLatexEquations.zip?dl=0)等。

参考链接:
1. [Combining LaTeX and Illustrator](http://latex.org/know-how/latexs-friends/61-latexs-friends-others/381-combining-latex-and-illustrator)
2. [Scripting Adobe Illustrator to create images from LaTeX equations](http://larsonvonh.github.io/data/tools/adobe_tools/latex_equations_illustrator/latex_equations_illustrator.html)
