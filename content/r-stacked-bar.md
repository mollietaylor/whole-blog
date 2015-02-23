Title: Stacked Bar Charts in R
Date: 2013-01-10
Tags: barplot, datasets, legend, R, RColorBrewer, visualization
Category: R
Slug: 2013/01/stacked-bar-charts-in-r
Author: Mollie Taylor
Summary: How to create stacked bar charts in R


##Reshape Wide to Long
Let's use the ```Loblolly``` dataset from the **datasets** package. These data track the growth of some loblolly pine trees.

	:::r
	> Loblolly[1:10,]
	   height age Seed
	1    4.51   3  301
	15  10.89   5  301
	29  28.72  10  301
	43  41.74  15  301
	57  52.70  20  301
	71  60.92  25  301
	2    4.55   3  303
	16  10.92   5  303
	30  29.07  10  303
	44  42.83  15  303

First, we need to convert the data to wide form, so each age (i.e. 3, 5, 10, 15, 20, 25) will have its own variable.

	:::r
	wide <- reshape(Loblolly,
		v.names = "height",
		timevar = "age",
		idvar = "Seed",
		direction = "wide")

	> wide[1:5,]
	  Seed height.3 height.5 height.10 height.15 height.20 height.25
	1  301     4.51    10.89     28.72     41.74     52.70     60.92
	2  303     4.55    10.92     29.07     42.83     53.88     63.39
	3  305     4.79    11.37     30.21     44.40     55.82     64.10
	4  307     3.91     9.48     25.66     39.07     50.78     59.07
	5  309     4.81    11.20     28.66     41.66     53.31     63.05

##Create Variables

Then we want to create new columns showing how much each tree has grown between data points. For example, instead of knowing a tree's height at age 10, we want to know how much it's grown between age 5 and age 10, so that can be a bar in our graph.

	:::r
	wide$h0.3 <- wide$height.3
	wide$h3.5 <- wide$height.5 - wide$height.3
	wide$h5.10 <- wide$height.10 - wide$height.5
	wide$h10.15 <- wide$height.15 - wide$height.10
	wide$h15.20 <- wide$height.20 - wide$height.15
	wide$h20.25 <- wide$height.25 - wide$height.20

##Plot Stacked Bar Chart

Finally, we want to plot all the new data points:

	:::r
	library(RColorBrewer)
	sequential <- brewer.pal(6, "BuGn")
	barplot(t(wide[,8:13]),
		names.arg = wide$Seed, # x-axis labels
		cex.names = 0.7, # makes x-axis labels small enough to show all
		col = sequential, # colors
		xlab = "Seed Source",
		ylab = "Height, Feet",
		xlim = c(0,20), # these two lines allow space for the legend
		width = 1) # these two lines allow space for the legend
	legend("bottomright", 
		legend = c("20-25", "15-20", "10-15", "5-10", "3-5", "0-3"), #in order from top to bottom
		fill = sequential[6:1], # 6:1 reorders so legend order matches graph
		title = "Years")

![Stacked bar chart]({filename}images/r-stacked-bars.png)

If you decide you'd rather have clustered bars instead of stacked bars, you can just add the option ```beside = TRUE``` to the ```barplot```.

The full code is available in a [gist](https://gist.github.com/4263515).

##Citations and Further Reading
* Reshape
	* <http://stat.ethz.ch/R-manual/R-patched/library/stats/html/reshape.html>
* Stacked bar graphs
	* <http://www.cs.grinnell.edu/~rebelsky/Courses/MAT115/2008S/R/stacked-bar-graphs.html>
	* <http://www.harding.edu/fmccown/r/#barcharts>

