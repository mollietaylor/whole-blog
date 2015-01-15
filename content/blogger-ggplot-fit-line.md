Title: ggplot Fit Line and Lattice Fit Line in R
Date: 2014-02-13
Tags: geom_abline, geom_smooth, ggplot2, lattice, lm, R, type
Category: R
Slug: 014/02/ggplot-fit-line-and-lattice-fit-line-in.html
Author: Mollie Taylor
Summary: Let's add a fit line to a scatterplot!

Let's add a fit line to a scatterplot!

##Fit Line in Base Graphics

Here's how to do it in **base** graphics:

	:::r
	ols <- lm(Temp ~ Solar.R,
		data = airquality)

	summary(ols)

	plot(Temp ~ Solar.R,
		data = airquality)
	abline(ols

![Fit line in base graphics in R]({filename}/images/ggplot-fit-line-base.png)

##Fit Line in ggplot

And here's how to do it in **ggplot**:

	:::r
	library(ggplot2)
	ggplot(data = airquality,
			aes(Solar.R, Temp)) + 
		geom_point(pch = 19) + 
		geom_abline(intercept = ols$coefficients[1],
			slope = ols$coefficients[2])

You can access the info from your regression results through ```ols$coefficients```.

Edit: Thanks to an anonymous commenter, I have learned that you can simplify this by using ```geom_smooth```.  This way you don't have to specify the intercept and slope of the fit line.

	:::r
	ggplot(data = airquality,
			aes(Solar.R, Temp)) + 
		geom_point(pch = 19) + 
		geom_smooth(method = lm,
			se = FALSE)

![Fit line in ggplot in R]({filename}/images/ggplot-fit-line-ggplot.png)

##Fit Line in Lattice

In **lattice**, it's even easier. You don't even need to run a regression; you can just add to the ```type``` option.

	:::r
	library(lattice)

	xyplot(Temp ~ Solar.R,
		data = airquality,
		type = c("p", "r"))

![Fit Line in Lattice in R]({filename}/images/ggplot-fit-line-lattice.png)

The code is available in [a gist](https://gist.github.com/mollietaylor/8203926).

##References

* <http://stackoverflow.com/questions/12972039/plotting-xyplot-with-regression-line-on-lattice-graphics>
