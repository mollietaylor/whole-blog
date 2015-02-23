Title: White Space in LaTeX
Date: 2012-11-08
Tags: LaTeX
Category: LaTeX
Slug: 2012/11/white-space-in-latex
Author: Mollie Taylor
Summary: There are several ways to force LaTeX to introduce white space to your documents.

Extra spaces and line breaks in your source file are ignored. But there are several ways to force LaTeX to introduce white space to your documents.

The most simple commands to insert a specific amount of white space into your document are \hspace and \vspace.

To produce vertical space, use \vspace followed by the length of the space in brackets. This length can be represented in any [units]({filename}latex-units.md) recognized by LaTeX, e.g. \vspace{2 in}. The space between the number and the unit is optional, so \vspace{2in} will also work.

Similarly, you can use \hspace to insert horizontal space in your document, e.g., \hspace{2 in}.

If \hspace and \vspace are not working as you would like (often at the beginning or end of a line or page), you can instead use \hspace* and \vspace*, which will force space to appear.

If you want to put in as much blank space as possible (while still maintaining page margins, etc.), you can use \hfill and \vfill.

Multiples of \vfill or \hfill on a particular page or in an environment will fill an even amount of the space. (E.g., if there are 6 inches to be filled and 3 \vfill's, each will take 2 inches.)

## Horizontal
As well as \hspace{} and \hfill, there are some horizontal-specific commands for adding white space.

\quad creates a space whose size is relative to the current font size and font face. \quad is equal to \hspace{[1em]({filename}latex-units.md)}. There are other commands that make spaces of sizes relative to \quad:

![Horizontal space commands in LaTeX]({filename}images/latex-quad.png)

##Vertical
Probably the most common white space command is ```\\```. It is used to start a new paragraph.

That's not the only way to tell LaTeX to break a line. Here are a number of ways to do that in different situations:

| command | action |
|---|---|
| \\ | Start a new paragraph |
| \linebreak[number] | Start a new line, option to request, not require |
| \newline | Line break (only in paragraph mode) |

\newline or \linebreak can be beneficial because they work inside the tabular environment (when a ```p``` column definition is used), where \\ will not work within a cell.

As well as using \vspace{} and \vfill, there are some specific commands for vertical white space:

* \smallskip
* \medskip
* \bigskip

The sizes of \smallskip, \medskip, and \bigskip are determined by the documentclass.

![Example of skip sizes]({filename}images/latex-small-skip.png)

There are also several kinds of ways to break a page, which sometimes creates white space:

| command | action |
|---|---|
| \pagebreak | Starts a new page, using white space throughout to fill the full page before the break |
| \newpage | Starts a new page, leaving the rest of the page before the break blank |
| \clearpage | Like \newpage, but also prints all prior figures |
| \cleardoublepage | Like \clearpage, but next page with print will be odd |

[Here's an example](http://tex.stackexchange.com/a/740) of the difference between \pagebreak and \newpage.

## More information

* <http://crab.rutgers.edu/~karel/latex/class5/class5.html>
* <http://help-csli.stanford.edu/tex/latex-pagebreaks.shtml>
* <http://www.personal.ceu.hu/tex/breaking.htm>
* <http://www.mollietaylor.com/2012/11/units-in-latex.html>

