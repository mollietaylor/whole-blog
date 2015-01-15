Title: Sorting Within Lattice Graphics in R
Date: 2012-11-29
Tags: barchart, dotplot, key, lattice, legend, R, reorder, visualization
Category: R
Slug: 2012/11/sorting-within-lattice-graphics-in-r.html
Author: Mollie Taylor
Summary: Sorting within lattice graphics in R

##Default

By default, **lattice** sorts the observations by the axis values, starting at the bottom left.

For example,

	:::r
	library(lattice)
	colors = c("#1B9E77", "#D95F02", "#7570B3")
	dotplot(rownames(mtcars) ~ mpg,
		data = mtcars,
		col = colors[1],
		pch = 1)

produces:

![Default lattice dotplot]({filename}images/r-lattice-default.png)

(Note: The ```rownames(cars)``` bit is just because of how this data set is stored. For your data, you might just type the variable name (```model```, for example) instead.)

##Graphing one variable, sorting by another
If we want to show the same data, but we want to sort by another variable (or the same variable, for that matter), we can just add ```reorder(yvar, sortvar)```. For example, to sort by the number of cylinders, we could:

	:::r
	dotplot(reorder(rownames(mtcars), cyl) ~ mpg,
		data = mtcars,
		col = colors[1],

![Sorted by number of cylinders]({filename}images/r-lattice-by-cyl.png)

##Graphing two variables
To better show how this works, let's graph ```cyl``` alongside ```mpg```, so we can see how it is sorting:

	:::r
	dotplot(reorder(rownames(mtcars), cyl) ~ mpg + cyl,
		data = mtcars,
		col = colors,
		pch = c(1, 0))
		pch = 1)

![Graph of mpg and cyl, sorted by cyl]({filename}images/r-lattice-mpg-cyl.png)

##Reverse order
We can also sort in reverse order, by adding a "-" before the variable name:

	:::r
	dotplot(reorder(rownames(mtcars), -cyl) ~ mpg + cyl,
		data = mtcars,
		col = colors,
		pch = c(1, 0))

![Graph of mpg and cyl, sorted by cyl, reversed]({filename}images/r-lattice-mpg-cyl-reverse.png)

##Adding a legend
We can also add a legend:

	:::r
	dotplot(reorder(rownames(mtcars), -cyl) ~ mpg + cyl,
		data = mtcars,
		xlab = "",
		col = colors,
		pch = c(1, 0),
		key = list(points = list(col = colors[1:2], pch = c(1, 0)),
			text = list(c("Miles per gallon", "Number of cylinders")),
			space = "bottom"))

![With legend]({filename}images/r-lattice-legend.png)

##Other lattice types
The same technique will work with other lattice graphs, such as barchart, bwplot, and stripplot.

Full code available as a [gist](https://gist.github.com/4063837).
