Title: Line Breaks Between Words in Axis Labels in ggplot in R
Date: 2013-10-17
Tags: abline, coord_flip, geom_boxplot, ggplot2, gsub, R, regular expressions, visualization
Category: R
Slug: 2013/10/line-breaks-between-words-in-axis.html
Author: Mollie Taylor
Summary: Sometimes when plotting factor variables in R, the graphics can look pretty messy thanks to long factor levels. If the level attributes have multiple words, there is an easy fix to this that often makes the axis labels look much cleaner.

Sometimes when plotting factor variables in R, the graphics can look pretty messy thanks to long factor levels. If the level attributes have multiple words, there is an easy fix to this that often makes the axis labels look much cleaner.

##Without Line Breaks
Here's the messy looking example:

![No line breaks in axis labels]({filename}/images/line-breaks-none.png)

And here's the code for the messy looking example:

	:::r
	library(OIdata)
	data(birds)
	library(ggplot2)

	ggplot(birds,
		aes(x = effect,
			y = speed)) +
	geom_boxplot()

##With Line Breaks
We can use [regular expressions](http://regex.learncodethehardway.org/) to add line breaks to the factor levels by substituting any spaces with line breaks:

	:::r
	library(OIdata)
	data(birds)
	library(ggplot2)

	levels(birds$effect) <- gsub(" ", "\n", levels(birds$effect))
	ggplot(birds,
		aes(x = effect,
			y = speed)) +
	geom_boxplot()

![Line breaks in axis labels]({filename}/images/line-breaks.png)

Just one line made the plot look much better, and it will carry over to other plots you make as well. For example, you could [create a table with the same variable](http://www.mollietaylor.com/2013/10/table-as-image-in-r.html).

##Horizontal Boxes
Here we can see the difference in a box plot with horizontal boxes. It's up to you to decide which style looks better:

![No line breaks in axis labels]({filename}/images/line-breaks-flip-none.png)

![Line breaks in axis labels]({filename}/images/line-breaks-flip.png)

	:::r
	library(OIdata)
	data(birds)
	library(ggplot2)

	levels(birds$effect) <- gsub(" ", "\n", levels(birds$effect))
	ggplot(birds,
		aes(x = effect,
			y = speed)) +
	geom_boxplot() + 
	coord_flip()

Just a note: if you're not using **ggplot**, the multi-line axis labels might overflow into the graph.

[The code is available in a gist](https://gist.github.com/mollietaylor/6930567#file-linebreaks-r).

##Citations and Further Reading
* <http://regex.learncodethehardway.org/>


