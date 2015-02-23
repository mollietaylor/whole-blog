Title: Table as an Image in R
Date: 2013-10-24
Tags: ggplot2, gridExtra, qplot, R, table, tableGrob, visualization
Category: R
Slug: 2013/10/table-as-image-in-r
Author: Mollie Taylor
Summary: Usually, it's best to keep tables as text, but if you're making a lot of graphics, it can be helpful to be able to create images of tables.

Usually, it's best to keep tables as text, but if you're making a lot of graphics, it can be helpful to be able to create images of tables.

![PNG table]({filename}/images/r-table-image.png)

##Creating the Table
After loading the data, let's first use [this trick](http://www.mollietaylor.com/2013/10/line-breaks-between-words-in-axis.html) to put line breaks between the levels of the effect variable. Depending on your data, you may or may not need or want to do this.

	:::r
	library(OIdata)
	data(birds)
	library(gridExtra)

	# line breaks between words for levels of birds$effect:
	levels(birds$effect) <- gsub(" ", "\n", levels(birds$effect))

Next let's make our table: 

	:::r
	xyTable <- table(birds$sky, birds$effect)

Now we can create an empty plot, center our table in it, and use the ```grid.table``` function from the **gridExtra** package to display the table and choose a font size.

	:::r
	plot.new()
	grid.table(xyTable,
		# change font sizes:
		gpar.coltext = gpar(cex = 1.2),
		gpar.rowtext = gpar(cex = 1.2))

Now you can view and save the image just like any other plot.

[The code is available in a gist](https://gist.github.com/mollietaylor/6930567#file-tableasimage-simple-r).
##Citations and Further Reading
* <http://stackoverflow.com/questions/12318120/adding-table-within-the-plotting-region-of-a-ggplot-in-r>
* <http://stackoverflow.com/questions/12518387/can-i-create-an-empty-ggplot2-plot-in-r>
