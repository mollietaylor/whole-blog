Title: Subfigures in LaTeX
Date: 2012-11-15
Tags: LaTeX, Series: LaTeX, subcaption, subfigure, subfloat
Category: LaTeX
Slug: 2012/11/subfigures-in-latex.html
Author: Mollie Taylor
Summary: How can you create subfigures or subfloats in LaTeX?

How can you create subfigures or subfloats in LaTeX? It's often easy to combine multiple figures from within a statistical package or image software, but it's generally best not to if you want to include subcaptions as text, for improved searchability.

Fortunately the **subcaption** package in LaTeX allows us to do this easily. (The subfigure and subfig packages have been deprecated, so it's best to use subcaption instead.)

How can you make more than one image or table be part of a LaTeX figure while still being able to create text captions for each?

Using the word clouds from my R word cloud tutorial, let's look at an example:

![Wordcloud of national conventions]({filename}images/latex-wordcloud.png)

In order to make the figure containing the subfigures, we'll need to decide a few things first. Then it's just a matter of letting LaTeX know our preferences:

* The precise or proportional width of the subfigures
* The filenames
* The subcaptions
* How much horizontal or vertical space should be between subfigures
* The overall figure caption

We also need to let LaTeX know to use the **caption** and **subcaption** packages. The full code for the example image above is included below, and also [in a gist](https://gist.github.com/3984730).

	:::latex
	\documentclass{article}

	\usepackage{graphicx}
	\usepackage{caption}
	\usepackage{subcaption}

	\begin{document}

	\begin{figure}
		\centering
		\begin{subfigure}{0.4\textwidth} % width of left subfigure
			\includegraphics[width=\textwidth]{rncalt.png}
			\caption{RNC} % subcaption
		\end{subfigure}
		\vspace{1em} % here you can insert horizontal or vertical space
		\begin{subfigure}{0.4\textwidth} % width of right subfigure
			\includegraphics[width=\textwidth]{dncalt.png}
			\caption{DNC} % subcaption
		\end{subfigure}
		\caption{Wordcloud of national conventions} % caption for whole figure
	\end{figure}

	\end{document}

For more information, [this wikibooks article](http://en.wikibooks.org/wiki/LaTeX/Floats,_Figures_and_Captions#Subfloats) is useful.

> This post is one part of my series on LaTeX.