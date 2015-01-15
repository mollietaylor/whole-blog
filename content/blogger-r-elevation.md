Title: Elevation Profiles in R
Date: 2013-02-21
Tags: geom_ribbon, ggplot2, gps, R, SMA, sp, spDistsN1, TTR, visualization
Category: R
Slug: 2013/02/elevation-profiles-in-r.html
Author: Mollie Taylor
Summary: Plotting elevation in R

First, let's load up our data. [The data are available in a gist](https://gist.github.com/mollietaylor/4969793). You can convert your own GPS data to .csv by following the instructions [here, using gpsbabel](http://www.mollietaylor.com/2012/12/mapping-gps-tracks-in-r.html).

	:::r
	gps <- read.csv("callan.csv",
		header = TRUE)

Next, we can use the function ```SMA``` from the package **TTR** to calculate a [moving average](http://en.wikipedia.org/wiki/Moving_average) of the altitude or elevation data, if we want to smooth out the curve. We can define a constant for the number of data points we want to average to create each moving average value.

If you don't want to convert meters to feet, a metric version of the code is available in the gist ([callanMetric.R](https://gist.github.com/mollietaylor/4969793)).

	:::r
	library(TTR)
	movingN <- 5 # define the n for the moving average calculations
	gps$Altitude <- gps$Altitude * 3.281 # convert m to ft
	gps$SMA <- SMA(gps$Altitude,
		n = movingN)
	gps <- gps[movingN:length(gps$SMA), ] # remove first n-1 points

Next, we want to calculate the distance of each point. You can skip this step if your dataset already includes distances.

	:::r
	library(sp)
	Dist <- 0
	for(i in 2:length(gps$Longitude)) {
		Dist[i] = spDistsN1(as.matrix(gps[i,c("Longitude", "Latitude")]),
		c(gps$Longitude[i-1], gps$Latitude[i-1]),
		longlat = TRUE) / 1.609 # longlat so distances will be in km, then divide to convert to miles
	}
	gps$Dist <- Dist

	DistTotal <- 0
	for(i in 2:length(gps$Longitude)) {
		DistTotal[i] = Dist[i] + DistTotal[i-1]
	}
	gps$DistTotal <- DistTotal

And finally, we can plot our elevation data using geom_ribbons and ggplot:

	:::r
	library(ggplot2)
	ggplot(gps, aes(x = DistTotal)) +
	geom_ribbon(aes(ymin = 600, # change this to match your min below
			ymax = SMA),
		fill = "#1B9E77") + # put your altitude variable here if not using moving averages
	labs(x = "Miles",
		y = "Elevation") +
	scale_y_continuous(limits = c(600,1200)) # change this to limits appropriate for your region

![Elevation profile in ggplot2]({filename}/images/r-elevation.png){.size-auto}

[Code and data available in a gist](https://gist.github.com/mollietaylor/4969793).
