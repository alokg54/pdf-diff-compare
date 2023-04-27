Readme
========
To install to pdf-diff-compare tool, use pip package available
Command : pip install pdf-diff-comp

Pre-requisite
""""""""""""""
1. Tool has dependency on Calibre Tool for pdftohtml and font support
To Install check :ref: Section Installing Calibre


Installing Calibre
"""""""""""""""""""
Getting pdftohtml
------------------
To get a copy of pdftohtml, without building it from source, here are some options:

Ubuntu
-------
    Use Synaptic Package Manager to fetch poppler-utils

Mac
----
    Download Calibre for Mac. There is a copy of pdftohtml inside of Calibre.app under /Applications/calibre.app/Contents/Frameworks/
    PATH=$PATH:/Applications/calibre.app/Contents/Frameworks
    htmltopdf -xml mybook.pdf

Windows
--------
    Download Calibre for Windows. There is a copy of pdftohtml inside of Calibre under C:\Progam Files\Calibre2.
    Make sure to add C:\\Progam Files\\Calibre2 and C:\\Progam
    Files\\Calibre2\\DLLs to your path, ie:
    PATH=%PATH%; C:\\Progam Files\\Calibre2; C:\\Program
    Files\\Calibre2\\app\\bin
    htmltopdf -xml mybook.pdf

Setting up PDF-diff-comp tool
""""""""""""""""""""""""""""""

To install required libraries -

    Goto command prompt and run below command -

    ``pip install -r requirement.txt``

Requirements
""""""""""""
.. include:: ../../requirement.txt
   :literal:

Troubleshooting
""""""""""""""""

Known-Issue and Limitation
"""""""""""""""""""""""""""
Limitation
++++++++++
1. Tool is capable of doing on text comparison and not with Graphs or Images
2. Currently Tool is tested only for Windows platform and do not have support
   for Linux/Mac

Issue:
++++++
1. pdf-diff-compare tool is to dependent on PyPDF2 and pdftohtml module for
extracting text from PDFs, If PyPDF2 or pdftohtml fails to extract the text,
Tool won't calculate the difference and display unable to parse PDF error.

Execution
""""""""""
To execute the pdf-diff-compare tool

   1. Command line argument
   2. GUI Application
   3. As a Python module

Log Files
""""""""""
Log file for the execution is available at ./Log folder

Examples
"""""""""

Note
"""""

If you have any queries , Please contact Tool Dev team

      1. mandalapu.srinivasarao@ihsmarkit.com
      2. alokkumar.gupta@ihsmarkit.com
      3. sonal.srivastava@ihsmarkit.com

