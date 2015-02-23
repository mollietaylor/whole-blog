Title: geom_point Legend with Custom Colors in ggplot
Date: 2013-03-07
Tags: geom_point, geom_segment, ggplot2, R, RColorBrewer, scale_color_manual, visualization
Category: R
Slug: 2013/03/geompoint-legend-with-custom-colors-in
Author: Mollie Taylor
Summary: Custom colors for plot and legend in R's ggplot

Formerly, I showed [how to make line segments using ggplot]({filename}r-line-segments.md).

Working from that previous example, there are only a few things we need to change to add custom colors to our plot and legend in **ggplot**.

First, we'll add the colors of our choice. I'll do this using RColorBrewer, but you can choose [whatever method you'd like]({filename}r-palettes.md).

	:::r
	library(RColorBrewer)
	colors = brewer.pal(8, "Dark2")

The next section will be exactly the same as the previous example, except for removing the ```scale_color_discrete``` line to make way for the ```scale_color_manual``` we'll be adding later.

	:::r
	library(ggplot2)

	data <- as.data.frame(USPersonalExpenditure) # data from package datasets
	data$Category <- as.character(rownames(USPersonalExpenditure)) # this makes things simpler later

	ggplot(data,
		aes(x = Expenditure,
			y = Category)) +
	labs(x = "Expenditure",
		y = "Category") +
	geom_segment(aes(x = data$"1940",
			y = Category,
			xend = data$"1960",
			yend = Category),
		size = 1) +
	geom_point(aes(x = data$"1940",
			color = "1940"), # these can be any string, they just need to be unique identifiers
		size = 4,
		shape = 15) +
	geom_point(aes(x = data$"1960",
			color = "1960"),
		size = 4,
		shape = 15) +
	theme(legend.position = "bottom") +

And finally, we'll add a ```scale_color_manual``` line to our plot. We need to define the name, labels, and colors of the plot.

	scale_color_manual(name = "Year", # or name = element_blank()
		labels = c(1940, 1960),
		values = colors)

And here's our final plot, complete with whatever custom colors we've chosen in both the plot and legend:

![geom_point in ggplot with custom colors in the graph and legend]({filename}/images/ggplot-custom-legend.png)

I've updated the [gist](https://gist.github.com/mollietaylor/4543148#file-customlegend-r) from the previous post to also include a file that has custom colors.