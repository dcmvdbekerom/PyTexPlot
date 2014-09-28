PyTexPlot
=========
By Dirk van den Bekerom

This package allows one to include plots in LaTeX by generating them with Python files.

Installation
============

1. Copy pytexplot.sty and pytexplot.py in the same directory as your texfile
2. Make a folder that contains the python files for plots you want to include
3. Enable shell escapes by adding --enable-write18 or -shell-escape to your build options

Useage
======

See the file 'demo.tex' for a demo of how to use this package

What it does
============

Pytexplot provides a new command \includepytexplot{} that works similar to \includegraphics{}, (including all the optional arguments), but takes python scripts rather than image files as an argument.

After setting the folder where the python scripts are to be found with e.g. \pytexplotscripts{scripts}, the command \includegraphics{plot1} will run the governing program pytexplot.py, that will look in the folder 'scripts' for the file 'plot1.py'.

The file 'plot1.py' is expected to be a python script that generates a visual output using the method 'matplotlib.pyplot.show()'. This line is replaced by pytexplot.py to 'matplotlib.pyplot.savefig(path)', so that the file is saved. Note that the python script 'plot1.py' should not save images by itself!! (Though this is not a problem, the image will not be used by pytexplot)

The image thus generated is stored in the folder specified in LaTeX by e.g. \pytexplotplots{figures}. The filename is the same as the python file, but with an .png extension. So in the case of 'plot1.py' it will be 'plot1.png'.

After the image is produced, LaTeX will look for an image with this name in the specified plots folder and include it, taking regard of any optional parameters given to \includegraphics{}

Before executing any plot file, pytexplot.py will first check whether the plot needs to be redrawn at all. It will check whether the image exists (if not, redraw) and whether the python file has changed (if so, redraw).

Testing if the image exists is trivial, checking whether the file has changed is done by a CRC32 checksum.
Whenever \includepytexplot{} is issued and so pytexplot.py is executed, the latter will calculate the checksum of the script to be executed and store it in a file called 'pydump', which is generated in the main folder. If a second time a script is to be run, the checksum will be compared against the checksum of the previous run. If equal, the plotting script will not be executed. This results in the plots only to be redrawn when it is really necessary.


