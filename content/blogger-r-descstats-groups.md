Title: Descriptive Statistics of Groups in R
Date: 2012-09-20
Tags: analysis, datasets, describe.by, psych, R
Category: R
Slug: 2012/09/descriptive-statistics-of-groups-in-r.html
Author: Mollie Taylor
Summary: Descriptive statistics by group

The [sleep data set](http://stat.ethz.ch/R-manual/R-patched/library/datasets/html/sleep.html)—provided by the **datasets** package—shows the effects of two different drugs on ten patients. ```Extra``` is the increase in hours of sleep; ```group``` is the drug given, 1 or 2; and ```ID``` is the patient ID, 1 to 10.

I'll be using this data set to show how to perform descriptive statistics of groups within a data set, when the data set is [long (as opposed to wide)](http://www.r-bloggers.com/reshape-package-in-r-long-data-format-to-wide-back-to-long-again/).

First, we'll need to load up the psych package. The datasets package containing our data is probably already loaded.

	:::r
	library(psych)

The ```describe.by``` function in the **psych** package is what does the magic for us here. It will group our data by a variable we give it, and output descriptive statistics for each of the groups.

	:::r
	> describe.by(sleep, sleep$group)
	group: 1
	       var  n mean   sd median trimmed  mad  min  max range skew kurtosis   se
	extra    1 10 0.75 1.79   0.35    0.68 1.56 -1.6  3.7   5.3 0.42    -1.30 0.57
	group*   2 10 1.00 0.00   1.00    1.00 0.00  1.0  1.0   0.0  NaN      NaN 0.00
	ID*      3 10 5.50 3.03   5.50    5.50 3.71  1.0 10.0   9.0 0.00    -1.56 0.96
	------------------------------------------------------------ 
	group: 2
	       var  n mean   sd median trimmed  mad  min  max range skew kurtosis   se
	extra    1 10 2.33 2.00   1.75    2.24 2.45 -0.1  5.5   5.6 0.28    -1.66 0.63
	group*   2 10 2.00 0.00   2.00    2.00 0.00  2.0  2.0   0.0  NaN      NaN 0.00
	ID*      3 10 5.50 3.03   5.50    5.50 3.71  1.0 10.0   9.0 0.00    -1.56 0.96

Of course, there are other ways to find the descriptive statistics of groups, and since you'll probably be doing further analysis on the groups, and you may be splitting the whole data into subsets by groups, it may be easiest to just use describe on each subset. But that's a topic for another post. And this is an easy way to quickly look at many groups, and a quick look is particularly essential for descriptive statistics.