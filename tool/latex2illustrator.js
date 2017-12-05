var PDF_LATEX_EXE = "pdflatex.exe"; // Add full path if necessary
var LAST_TEX_CODE_FILE = 'latex2illustrator_lastcode.txt';
var TEX_FILE = 'latex2illustrator.tex';
var PDF_FILE = 'latex2illustrator.pdf';
var BAT_FILE = 'latex2illustrator.bat';
var TEMP_PATH = getWorkPath();

function setupGui() {
    var gui = new Window('dialog', 'illustratorLatexEquations', undefined);
    gui.bounds = { x: 20, y: 20, width: 800, height: 670 };
    gui.graphics.font = ScriptUI.newFont('Arial', ScriptUI.FontStyle.REGULAR, 16);
    gui.graphics.backgroundColor = gui.graphics.newBrush(gui.graphics.BrushType.SOLID_COLOR, [0.07, 0.29, 0.52], 1);
    gui.tb_enterEq = gui.add('edittext', { x: 5, y: 510, width: 790, height: 100 }, undefined, { multiline: true, scrollable: true });
    gui.tb_enterEq.text = getLastCode();
    // gui.tb_enterEq.addEventListener('keydown',function(pKey){keyPressed(pKey);});

    gui.btn_ok = gui.add('button', { x: 220, y: 460, width: 100, height: 20 }, 'ok');
    gui.btn_ok.onClick = function () {
        var latexCode = gui.tb_enterEq.text
        alert(latexCode)
        if (latexCode != null) {
            writeLastCode(latexCode);
            writeLatexFile(latexCode);
            generate(latexCode);
        }
        // gui.close();
    }
    gui.btn_cancel = gui.add('button', { x: 320, y: 460, width: 100, height: 20 }, 'cancel');
    gui.btn_cancel.onClick = function () {
        gui.close();
    }
    gui.show();
}

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

function writeLastCode(latexCode) {
    var lastCodeFile = File(TEMP_PATH + "\\" + LAST_TEX_CODE_FILE);
    lastCodeFile.open("w");
    lastCodeFile.write(latexCode);
    lastCodeFile.close();
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

function main() {
    try {
        setupGui()
    } catch (error) {
        alert('An error occured while initializing the user interface:\n' + error.toString());
    }
}

function latex2illustrator() {
    TEMP_PATH = 'E:/share_v/code/hejia-v.github.io/tool/data';

    var latexCode = getLastCode();
    if (latexCode != null) {
        writeLastCode(latexCode);
        writeLatexFile(latexCode);
        generate(latexCode);
    }
}

// main()
latex2illustrator()
