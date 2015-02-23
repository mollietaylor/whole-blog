Title: Calculating Gini Coefficients for a Number of Locales at Once in R
Date: 2013-01-17
Tags: aggregate, analysis, ggplot2, gini, R, reldist, sample, stat_density, write.csv
Category: R
Slug: 2013/01/calculating-gini-coefficients-for
Author: Mollie Taylor
Summary: Calculating Gini coefficients for a number of places simultaneously in R

The [Gini coefficient](http://en.wikipedia.org/wiki/Gini_coefficient) is a measure of the inequality of a distribution, most commonly used to compare inequality in income or wealth among countries.

Let's first generate some random data to analyze. You can [download my random data](https://gist.github.com/4432069) or use the code below to generate your own. Of course, if you generate your own, your graphs and results will be different from those shown below.

	:::r
	city <- c("A", "B", "C", "D", "E", "F", "G", "H", "I", "J")
	income <- sample(1:100000,
		100,
		replace = TRUE)
	cities <- data.frame(city, income)

Next, let's graph our data:

	:::r
	library(ggplot2)
	ggplot(cities,
		aes(income)) +
		stat_density(geom = "path",
			position = "identity") +
		facet_wrap(~ city, ncol = 2)

![Histogram of each city's incomes // Your results will differ if using random data]({filename}/images/r-gini-hist.png)

The Gini coefficient is easy enough to calculate in R for a single locale using the ```gini``` function from the **reldist** package.

	:::r
	library(reldist)
	gini(cities[which(cities$city == "A"), ]$income)

But we don't want to replicate this code over and over to calculate the Gini coefficient for a large number of locales. We also want the coefficients to be in a data frame for easy use in R or for export for use in another program.

There are [many ways to automate a function](http://www.slideshare.net/jeffreybreen/grouping-summarizing-data-in-r) to run over many subsets of a data frame. The most straightforward in our particular case is ```aggregate```:

	:::r
	ginicities <- aggregate(income ~ city,
		data = cities,
		FUN = "gini")
	names(ginisec) <- c("city", "gini")

	> ginisec
	   city      gini
	1     A 0.2856827
	2     B 0.3639070
	3     C 0.3288934
	4     D 0.1863783
	5     E 0.3565739
	6     F 0.2587475
	7     G 0.3022642
	8     H 0.3795288
	9     I 0.3311034
	10    J 0.2496933

And finally, let's go ahead and export our data using ```write.csv```:

	:::r
	write.csv(ginicities, "gini.csv",
		row.names = FALSE)

While you're at it, you might want to try using other functions on your dataset, such as ```mean```, ```median```, and ```length```.

The full code is available in a [gist](https://gist.github.com/4432069).

##Citations and Further Reading
* <http://rss.acs.unt.edu/Rdoc/library/reldist/html/gini.html>
* <http://www.slideshare.net/jeffreybreen/grouping-summarizing-data-in-r>

