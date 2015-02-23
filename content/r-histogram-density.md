Title: Histogram + Density Plot Combo in R
Date: 2012-09-27
Tags: hist, lines, R, visualization
Category: R
Slug: 2012/09/histogram-density-plot-combo-in-r
Author: Mollie Taylor
Summary: Plotting a histogram using hist from the graphics package is pretty straightforward, but what if you want to view the density plot on top of the histogram?

Plotting a histogram using ```hist``` from the **graphics** package is pretty straightforward, but what if you want to view the density plot on top of the histogram? This combination of graphics can help us compare the distributions of groups.

Let's use some of the data included with R in the package **datasets**. It will help to have two things to compare, so we'll use the [```beaver``` data sets](http://stat.ethz.ch/R-manual/R-patched/library/datasets/html/beavers.html), ```beaver1``` and ```beaver2```: the body temperatures of two beavers, taken at 10 minute intervals.

First we want to plot the histogram of one beaver:

	:::r
	hist(beaver1$temp, # histogram
		col="peachpuff", # column color
		border="black",
		prob = TRUE, # show densities instead of frequencies
		xlab = "temp",
		main = "Beaver #1")

![Histogram]({filename}images/r-histogram.png)

Next, we want to add in the density line, using ```lines```:

	:::r
	hist(beaver1$temp, # histogram
		col="peachpuff", # column color
		border="black",
		prob = TRUE, # show densities instead of frequencies
		xlab = "temp",
		main = "Beaver #1")
	lines(density(beaver1$temp), # density plot
		lwd = 2, # thickness of line
		col = "chocolate3")

![Histogram and density]({filename}images/r-histogram-density.png)

Now let's show the plots for both beavers on the same image. We'll make a histogram and density plot for Beaver #2, wrap the graphs in a ```layout``` and ```png```, and change the x-axis to be the same, using ```xlim```.

![Histogram and density]({filename}images/r-histogram-density-2.png)

Here's the final code, [also available on gist](https://gist.github.com/3685924):

	:::r
	png("beaverhist.png")
	layout(matrix(c(1:2), 2, 1,
		byrow = TRUE))
	hist(beaver1$temp, # histogram
		col = "peachpuff", # column color
		border = "black",
		prob = TRUE, # show densities instead of frequencies
		xlim = c(36,38.5),
		xlab = "temp",
		main = "Beaver #1")
	lines(density(beaver1$temp), # density plot
		lwd = 2, # thickness of line
		col = "chocolate3")
	hist(beaver2$temp, # histogram
		col = "peachpuff", # column color
		border = "black",
		prob = TRUE, # show densities instead of frequencies
		xlim = c(36,38.5),
		xlab = "temp",
		main = "Beaver #2")
	lines(density(beaver2$temp), # density plot
		lwd = 2, # thickness of line
		col = "chocolate3")
	dev.off()



