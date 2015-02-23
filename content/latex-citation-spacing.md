Title: Add Spaces Between Citations in LaTeX
Date: 2013-12-12
Tags: cite, LaTeX
Category: LaTeX
Slug: 2013/12/add-spaces-between-citations-in-latex
Author: Mollie Taylor
Summary: I had an issue where LaTeX wasn't adding spaces between references when I had multiple references in the same place.

I had an issue where LaTeX wasn't adding spaces between references when I had multiple references in the same place.

So this:

	:::latex
	of their own \cite{moretti:2012,saxenian:1996,casper:2007}. 

was compiling as this:

	:::latex
	of their own [Moretti, 2012,Saxenian, 1996,Casper, 2007].

To fix the problem, I simply added the space option for the **cite** package.

	:::latex
	\usepackage[space]{cite}

And now it looks as it should:

	:::latex
	of their own [Moretti, 2012, Saxenian, 1996, Casper, 2007].

If you have spaces and don't want them, you can instead use the ```nospace``` option to remove the space between each citation.

##References
* <http://texdoc.net/texmf-dist/doc/latex/cite/cite.pdf>

