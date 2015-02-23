Title: Plot Weekly or Monthly Totals in R
Date: 2013-08-29
Tags: as.Date, cut, ggplot2, R, scale_x_date, scales, stat_summary, visualization
Category: R
Slug: 2013/08/plot-weekly-or-monthly-totals-in-r
Author: Mollie Taylor
Summary: When plotting time series data, you might want to bin the values so that each data point corresponds to the sum for a given month or week.

When plotting time series data, you might want to bin the values so that each data point corresponds to the sum for a given month or week. This post will show an easy way to use ```cut``` and **ggplot2**'s ```stat_summary``` to plot month totals in R without needing to reorganize the data into a second data frame.

Let's start with a simple sample data set with a series of dates and quantities:

	:::r
	library(ggplot2)
	library(scales)

	# load data:
	log <- data.frame(Date = c("2013/05/25","2013/05/28","2013/05/31","2013/06/01","2013/06/02","2013/06/05","2013/06/07"), 
	  Quantity = c(9,1,15,4,5,17,18))
	log
	str(log)


	:::r
	> log
	        Date Quantity
	1 2013/05/25        9
	2 2013/05/28        1
	3 2013/05/31       15
	4 2013/06/01        4
	5 2013/06/02        5
	6 2013/06/05       17
	7 2013/06/07       18

	> str(log)
	'data.frame': 7 obs. of  2 variables:
	 $ Date    : Factor w/ 7 levels "2013/05/25","2013/05/28",..: 1 2 3 4 5 6 7
	 $ Quantity: num  9 1 15 4 5 17 18

Next, if the date data is not already in a date format, we'll need to [convert it to date format]({filename}r-date-formats.md):

	:::r
	# convert date variable from factor to date format:
	log$Date <- as.Date(log$Date,
		"%Y/%m/%d") # tabulate all the options here
	str(log)


	:::r
	> str(log)
	'data.frame': 7 obs. of  2 variables:
	 $ Date    : Date, format: "2013-05-25" "2013-05-28" ...
	 $ Quantity: num  9 1 15 4 5 17 18

Next we need to create variables stating the week and month of each observation. For week, ```cut``` has an option that allows you to break weeks as you'd like, beginning weeks on either Sunday or Monday.

	:::r
	# create variables of the week and month of each observation:
	log$Month <- as.Date(cut(log$Date,
	  breaks = "month"))
	log$Week <- as.Date(cut(log$Date,
	  breaks = "week",
	  start.on.monday = FALSE)) # changes weekly break point to Sunday
	log

	> log
	        Date Quantity      Month       Week
	1 2013-05-25        9 2013-05-01 2013-05-19
	2 2013-05-28        1 2013-05-01 2013-05-26
	3 2013-05-31       15 2013-05-01 2013-05-26
	4 2013-06-01        4 2013-06-01 2013-05-26
	5 2013-06-02        5 2013-06-01 2013-06-02
	6 2013-06-05       17 2013-06-01 2013-06-02
	7 2013-06-07       18 2013-06-01 2013-06-02

Finally, we can create either a line or bar plot of the data by month and by week, using ```stat_summary``` to sum up the values associated with each week or month:

	:::r
	# graph by month:
	ggplot(data = log,
		aes(Month, Quantity)) +
		stat_summary(fun.y = sum, # adds up all observations for the month
			geom = "bar") + # or "line"
		scale_x_date(
			labels = date_format("%Y-%m"),
			breaks = "1 month") # custom x-axis labels

![Time series plot, binned by month]({filename}/images/plot-monthly-total.png)

	:::r
	# graph by week:
	ggplot(data = log,
		aes(Week, Quantity)) +
		stat_summary(fun.y = sum, # adds up all observations for the week
			geom = "bar") + # or "line"
		scale_x_date(
			labels = date_format("%Y-%m-%d"),
			breaks = "1 week") # custom x-axis labels

![Time series plot, totaled by week]({filename}/images/plot-weekly-total.png)

The full code is available in a [gist](https://gist.github.com/mollietaylor/5846843).

> In a [comment](mollietaylor.blogspot.com/2013/08/plot-weekly-or-monthly-totals-in-r.html), Achim Zeileis pointed out that the aggregation part can be more easily handled using time series packages like **zoo** or **xts**.

##References
* <http://stackoverflow.com/questions/3496536/barplot-totals-by-month-with-ggplot>

