---
title: 在illustrator中使用latex公式
date: 2017-12-04 07:39:43
updated: 2017-12-04 07:39:43
tags: tool
categories: tool
---

Adobe Illustrator 是一款强大的矢量图形软件，当我们在里面做好图形后，可能需要在里面插入一些数学符号或者数学公式什么的，这时一般考虑使用 Latex 来输出这些特殊文本。下面介绍一下如何在 Illustrator 中使用 Latex 。

<!--more-->

## 安装 LaTeX
LaTeX 有很多发行版，在[这里](http://latex.org/know-how/latex-distributions)可以查看到。我在windows环境下使用的是 [MikTeX](https://miktex.org/)，在[这里](https://miktex.org/download)下载了安装包后，按照正常的Windows软件安装流程进行安装，途中可能会提示安装一些依赖，按照提示进行操作即可。

安装完 Latex 后，需要确认一下，从 PATH 环境变量里能否搜索到 pdflatex 命令，如果不能，则需要将 pdflatex 所在的文件夹添加到 PATH 环境变量里。

## 安装 LaTeX 字体
LaTeX 会使用一些特殊的字体，为了让导出的文本能够在 Illustrator 中正常显示，需要让 Illustrator 能够搜索到这些字体。比较简单省事的做法是将这些字体拷贝到adobe的字体文件夹里。例如在Windows上，将 `D:\Program Files\MiKTeX 2.9\fonts\type1\public\amsfonts\cm` 文件夹里的文件全部拷贝到 `C:\Program Files\Common Files\Adobe\Fonts` 文件夹。

## 将 LaTeX 导出到 Illustrator
Illustrator 可以从PDF文件中导入单独的页面，因此，可以先将 Latex 代码编译成PDF(可以使用pdflatex)，再将PDF导入到 Illustrator 中去。

为了简化 `Latex -> PDF -> Illustrator` 这一过程，有一些脚本可供使用，例如 [latex-illustrator](https://github.com/mkuznets/latex-illustrator) 和 [illustratorLatexEquations](https://dl.dropboxusercontent.com/s/otp2zdmqx2peaf5/illustratorLatexEquations.zip?dl=0)等。

根据我的实际使用情况，我对脚本做了一下修改，代码如下：
```js
// latex2illustrator.js
var PDF_LATEX_EXE = "pdflatex.exe"; // Add full path if necessary
var LAST_TEX_CODE_FILE = 'latex2illustrator_lastcode.txt';
var TEX_FILE = 'latex2illustrator.tex';
var PDF_FILE = 'latex2illustrator.pdf';
var BAT_FILE = 'latex2illustrator.bat';
var TEMP_PATH = getWorkPath();

function getWorkPath() {
    // determining the local temporary directory
    var temppath = Folder.temp.fsName; // path already in Windows syntax: c:\...
    var i = temppath.indexOf("Temporary Internet Files");
    if (i >= 0) temppath = temppath.substr(0, i + 4);
    //temppath should now contain something like C:\Documents and Settings\<user>\Local Settings\Temp
    return temppath
}

function getLastCode() {
    // remember the last user input in a text file
    var lastCode = "$$"
    var lastCodeFile = File(TEMP_PATH + "\\" + LAST_TEX_CODE_FILE);
    if (lastCodeFile.exists) {
        lastCodeFile.open("r");
        lastCode = lastCodeFile.read();
        lastCodeFile.close();
    }
    return lastCode
}

function writeLatexFile(latexCode) {
    // add latex header etc. to create a complete latex document
    var latexFile = new File(TEMP_PATH + '\\' + TEX_FILE);
    latexFile.open("w");
    // latexFile.writeln("\\documentclass{standalone}");
    latexFile.writeln("\\documentclass{article}");
    // add or remove additional latex packages here
    latexFile.writeln("\\usepackage{amsmath}");
    latexFile.writeln("\\usepackage{amsthm}");
    latexFile.writeln("\\usepackage{amssymb}");
    latexFile.writeln("\\usepackage{gensymb}"); // for \degree
    latexFile.writeln("\\usepackage{textcomp}"); // for \textdegree
    latexFile.writeln("\\usepackage{bm}"); // bold math
    latexFile.writeln("\\begin{document}");
    latexFile.writeln("\\pagestyle{empty}"); // no page number
    latexFile.writeln(latexCode);
    latexFile.writeln("\\end{document}");
    latexFile.close();
}

function generate(latexcode) {
    var pdfFile = File(TEMP_PATH + "\\" + PDF_FILE);
    if (pdfFile.exists)
        pdfFile.remove();

    // create a batch file calling latex
    var batchFile = new File(TEMP_PATH + '\\' + BAT_FILE);
    batchFile.open("w");
    batchFile.writeln(PDF_LATEX_EXE + ' -aux-directory="' + TEMP_PATH + '" -include-directory="' + TEMP_PATH + '" -output-directory="' + TEMP_PATH + '" "' + TEMP_PATH + '\\' + TEX_FILE + '"');
    //batchFile.writeln('pause');
    batchFile.writeln('del "' + TEMP_PATH + '\\' + BAT_FILE + '"');
    batchFile.close();
    batchFile.execute();

    for (; batchFile.exists;)
        // wait until the batch file has removed itself
        var pdfFile = File(TEMP_PATH + "\\" + PDF_FILE);

    if (pdfFile.exists) {
        // import pdf file into the current document
        var grp = app.activeDocument.activeLayer.groupItems.createFromFile(pdfFile);
        // The imported objects are grouped twice. Now move the subgroup
        // items to the main group and skip the last item which is the page frame
        for (var i = grp.pageItems[0].pageItems.length; --i >= 0;)
            grp.pageItems[0].pageItems[i].move(grp, ElementPlacement.PLACEATEND);

        var last = grp.pageItems.length - 1;
        if (last >= 0 && grp.pageItems[last].typename == 'PathItem')
            grp.pageItems[last].remove();

        // Move the imported objects to the center of the current view.
        grp.translate(app.activeDocument.activeView.centerPoint[0] - grp.left, app.activeDocument.activeView.centerPoint[1] - grp.top);
    } else
        alert("File " + TEMP_PATH + "\\" + pdfFile.name + " could not be created. LaTeX error?");
}

function latex2illustrator() {
    TEMP_PATH = 'E:/data';

    var latexCode = getLastCode();
    if (latexCode != null) {
        writeLatexFile(latexCode);
        generate(latexCode);
    }
}

latex2illustrator()
```
在`E:/data/latex2illustrator_lastcode.txt`中写入latex公式，然后在Illustrator中使用ctrl+F12执行latex2illustrator.js脚本，就可以插入数学公式了。

参考链接:
1. [Combining LaTeX and Illustrator](http://latex.org/know-how/latexs-friends/61-latexs-friends-others/381-combining-latex-and-illustrator)
2. [Scripting Adobe Illustrator to create images from LaTeX equations](http://larsonvonh.github.io/data/tools/adobe_tools/latex_equations_illustrator/latex_equations_illustrator.html)
