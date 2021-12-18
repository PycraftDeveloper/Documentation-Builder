# Documentation-Builder
This is a small project written to help build documentation for projects in less time.

## About

This project builds documentation for your project, it also formats the code to the style I use in my documentation for Pycraft; which you can find here: https://python-pycraft.readthedocs.io/en/pycraft-v0.9.3/ (Link subject to change).

This project attempts to accelerate the process of writing documentation by building a library of known code, and an explanation of what it does, so it can auto-fill repeated lines of code (regardless of indentation). If you change the project, whether that’s rearranging the entire thing or adding new code for example in an update, then the documentation will be rebuilt using the library of known code and descriptions. If there is a line of code that is not in the library, the project will prompt you for a description of what it does.

Please note; you can only see the outputted documentation once the code has gone through without asking for help with known lines.

## Setup and Use

This project is really simple to setup and use, requiring only a version of python 3 to run. You download the code from this page, and then you will see a folder and 3 files (once you have extracted the project).

The file labelled OUTPUT.txt will be where the finished documentation will be outputted to.
The file labelled ENTRIES.json stores the library of known code.
The file 'Doc-rewriter.py' is the code for the project.

The folder 'Files' is where the code you want to be documented should be, please rename the files in the structure: '1 (num).py'
