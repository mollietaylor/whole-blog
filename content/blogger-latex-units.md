Title: Units in LaTeX
Date: 2012-11-01
Tags: LaTeX
Category: LaTeX
Slug: 2012/11/units-in-latex.html
Author: Mollie Taylor
Summary: Units in LaTeX

##Discrete units
These are your basic units, like inches, centimeters, and points. Conversion of units from [here](http://wiki.lyx.org/FAQ/Units) and [here](http://www.maths.tcd.ie/~dwilkins/LaTeXPrimer/WhiteSpace.html).

These tables show the relative sizes of each unit:

![Relative sizes of units in LaTeX, inches]({filename}images/latex-units-in.png)

![Relative sizes of units in LaTeX, cm]({filename}images/latex-units-cm.png)

##Units defined relative to font sizes
There also are sizes that are relative to the current font face and font size. The size ex is usually the same as the height of an "x", and the size em is usually (but less often) equal to the width of an "M".

Since these are relative to your font, don't be surprised if your attempts look different than mine. Just like their absolute sizes, the size of ex relative to em is not consistent across fonts.

![Examples of font-relative units]({filename}images/latex-units-em.png)

Units defined relative to document
There also are units that have definitions relative to your document. These are determined based on your documentclass, and can also be explicitly changed.

A list of these and how to change them is available [here](http://en.wikibooks.org/wiki/LaTeX/Useful_Measurement_Macros#Length_.27macros.27). Some of the sizes are illustrated [here](http://wiki.lyx.org/Tips/PaperLayout).

| command | size |
|---|---|
| \paperwidth | Width of page |
| \paperheight | Height of page |
| \textwidth | Width of text |
| \textheight | Height of text |
| \linewidth | Width of a line, usually equal to \textwidth, but varies with environment |
| \columnwidth | Width of a column, usually same as \linewidth |
| \columnsep | Distance between columns |
| \tabcolsep | Separation between columns in a tabular environment |
| \parindent | Paragraph indentation |
| \parskip | The extra vertical space between paragraphs |
| \baselineskip | Vertical distance between lines in a paragraph |
| \baselinestretch | Multiplies \baselineskip |
| \unitlength | Units of length in a picture environment |
| \topmargin | Size of top margin |
| \evensidemargin | Margin of even pages |
| \oddsidemargin | Margin of odd pages |

Next, we'll learn how to use these units to add [white space]({filename}blogger-latex-white-space.md).