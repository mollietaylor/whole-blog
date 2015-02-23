Title: Merge by City and State in R
Date: 2014-02-20
Tags: complete.cases, merge, R
Category: R
Slug: 2014/02/merge-by-city-and-state-in-r
Author: Mollie Taylor
Summary: Often, you'll need to merge two data frames based on multiple variables.

Often, you'll need to merge two data frames based on multiple variables. For this example, we'll use the common case of needing to merge by city and state.

First, you need to read in both your data sets:

	:::r
	# import city coordinate data:
	coords <- read.csv("cities-coords.csv",
		header = TRUE,
		sep = ",")

	# import population data:
	data <- read.csv("cities-data.csv",
		header = TRUE,
		sep = ",")

Next comes the merge. You can use ```by.x``` and ```by.y``` to declare which variables the merge will be based on. If the variables have exactly the same name in both data sets, you can use by instead of ```by.x``` and ```by.y```.

```x``` and ```y``` represent the two data sets you are merging, in that order.

You also want to state whether you want to include all data from either data set, using ```all``` or ```all.x``` and ```all.y```. In this case, we want to make sure we hold onto all our city data, even data for the cities we do not have coordinates for.

	:::r
	# merge data & coords by city & state:
	dataCoords <- merge(coords, data, 
		by.x = c("City", "State"),
		by.y = c("city", "state"),
		all.x = FALSE,
		all.y = TRUE)

Running that code shows what we would expect. Houston is included in the final data set even though there are no coordinates for it, while Dallas is not included since it has coordinates but no data:

	:::r
                City State Latitude  Longitude year population
	1        Chicago    IL 41.85003  -87.65005 2012    2714856
	2       Columbus    GA 32.46098  -84.98771 2012     198413
	3       Columbus    OH 39.96118  -82.99879 2012     809798
	4       Columbus    OH 39.96118  -82.99879 2010     787033
	5    Los Angeles    CA 34.05223 -118.24368 2012    3857799
	6       New York    NY 40.71427  -74.00597 2012    8336697
	7       New York    NY 40.71427  -74.00597 2010    8175133
	8  San Francisco    CA 37.77823 -122.44250 2012     825863
	9  San Francisco    CA 37.77823 -122.44250 2010     805235
	10       Houston    TX       NA         NA 2012    2160821

##Bonus

If you'd like to get a list of which cases got merged in but lack coordinate data, there's a simple line of code to do that:

	:::r
	> dataCoords[!complete.cases(dataCoords[,c(3,4)]),]
	      City State Latitude Longitude year population
	10 Houston    TX       NA        NA 2012    2160821


Also, you might want to tidy up the names of your variables, if they followed different conventions in their respective initial data sets:

	:::r
	> names(dataCoords) <- c("City", "State", "Latitude", "Longitude", "Year", "Population")
	> dataCoords
	            City State Latitude  Longitude Year Population
	1        Chicago    IL 41.85003  -87.65005 2012    2714856
	2       Columbus    GA 32.46098  -84.98771 2012     198413
	3       Columbus    OH 39.96118  -82.99879 2012     809798
	4       Columbus    OH 39.96118  -82.99879 2010     787033
	5    Los Angeles    CA 34.05223 -118.24368 2012    3857799
	6       New York    NY 40.71427  -74.00597 2012    8336697
	7       New York    NY 40.71427  -74.00597 2010    8175133
	8  San Francisco    CA 37.77823 -122.44250 2012     825863
	9  San Francisco    CA 37.77823 -122.44250 2010     805235
	10       Houston    TX       NA         NA 2012    2160821

The full sample code is available as [a gist](https://gist.github.com/mollietaylor/8565624).

##References

* <https://stat.ethz.ch/pipermail/r-help/2006-August/111120.html>
