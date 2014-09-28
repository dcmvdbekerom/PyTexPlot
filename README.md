PyTexPlot
=========
By Dirk van den Bekerom

This package allows one to include plots in LaTeX by generating them with python files.

Installation
============

1. Copy pytexplot.sty and pytexplot.py in the same directory as your texfile
2. Make a folder that contains the python files for plots you want to include
3. Enable shell escapes by adding --enable-write18 or -shell-escape to your build options

Useage
======

% Include the package:
\usepackage{graphicx}  %needed by pytexplot
\usepackage{pytexplot} %the package

% Change the folders:
\pytexplotscripts{scripts} %folder where the python files are stored
\pytexplotplots{figures}   %folder where the generated images will be stored

% And include the images!
\includepytexplot[width=\linewidth]{plot1}
\includepytexplot[width=\linewidth]{plot2}


