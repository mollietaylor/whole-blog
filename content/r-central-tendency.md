Title: Adding Measures of Central Tendency to Histograms in R
Date: 2012-10-04
Tags: abline, hist, R, visualization
Category: R
Slug: 2012/10/adding-measures-of-central-tendency-to
Author: Mollie Taylor
Summary: Building on the basic histogram with a density plot, we can add measures of central tendency (in this case, mean and median) and a legend.

Building on the [basic histogram with a density plot]({filename}r-histogram-density.md), we can add measures of central tendency (in this case, mean and median) and a legend.

Like last time, we'll use the beaver data from the **datasets** package.

	:::r
	hist(beaver1$temp, # histogram
		col = "peachpuff", # column color
		border = "black", 
		prob = TRUE, # show densities instead of frequencies
		xlim = c(36,38.5),
		ylim = c(0,3),
		xlab = "Temperature",
		main = "Beaver #1")
	lines(density(beaver1$temp), # density plot
		lwd = 2, # thickness of line
		col = "chocolate3")

Next we'll add a line for the mean: 

	:::r
	abline(v = mean(beaver1$temp),
		col = "royalblue",
		lwd = 2)

And a line for the median: 

	:::r
	abline(v = median(beaver1$temp),
		col = "red",
		lwd = 2)

And then we can also add a legend, so it will be easy to tell which line is which. 
	:::r
	legend(x = "topright", # location of legend within plot area
		c("Density plot", "Mean", "Median"),
		col = c("chocolate3", "royalblue", "red"),
		lwd = c(2, 2, 2))

All of this together gives us the following graphic:

![Beaver #1 central tendency]({filename}images/r-histogram-tendency-1.png)

In this example, the mean and median are very close, as we can see by using ```median()``` and ```mode()```.

	:::r
	> mean(beaver1$temp)
	[1] 36.86219
	> median(beaver1$temp)
	[1] 36.87

We can do like we did in the previous post and graph beaver1 and beaver2 together by adding a layout line and changing the limits of x and y. The full code for this is available in a [gist](https://gist.github.com/3768715#file_histdens2.r).

Here's the output from that code: 

![Beaver #1 and #2 central tendency]({filename}images/r-histogram-tendency-2.png)

