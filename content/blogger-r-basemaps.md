Title: GPS Basemaps in R Using get_map
Date: 2013-02-14
Tags: base map, basemap, geom_path, geom_point, geom_segment, get_cloudmademap, get_googlemap, get_map, get_openstreetmap, get_stamenmap, ggmap, gps, R, visualization
Category: R
Slug: 2013/02/gps-basemaps-in-r-using-getmap.html
Author: Mollie Taylor
Summary: There are many different maps you can use for a background map for your gps or other latitude/longitude data (i.e. any time you're using geom_path, geom_segment, or geom_point.)

There are *many* different maps you can use for a background map for your gps or other latitude/longitude data (i.e. any time you're using ```geom_path```, ```geom_segment```, or ```geom_point```.)

##get_map
Helpfully, there's just one function that will allow you to query Google Maps, OpenStreetMap, Stamen maps, or CloudMade maps: ```get_map``` in the **ggmap** package. You could also use either ```get_googlemap```, ```get_openstreetmap```, ```get_stamenmap```, or ```get_cloudmademap```, but instead you can just use ```get_map``` for the same functionality as all of those combined. This makes it easy to try out different basemaps for your data.

You need to supply ```get_map``` with your location data and the color, source, maptype, and zoom of the base map.

Let's go ahead and map the trails in Elwyn John Wildlife Sanctuary here in Atlanta. [The csv data and R file are available in a gist](https://gist.github.com/mollietaylor/4742865).

	:::r
	gps <- read.csv("elwyn.csv",
		header = TRUE)

	library(ggmap)
	mapImageData <- get_map(location = c(lon = mean(gps$Longitude),
		lat = 33.824),
		color = "color", # or bw
		source = "google",
		maptype = "satellite",
		# api_key = "your_api_key", # only needed for source = "cloudmade"
		zoom = 17)

	pathcolor <- "#F8971F"

	ggmap(mapImageData,
		extent = "device", # "panel" keeps in axes, etc.
		ylab = "Latitude",
		xlab = "Longitude",
		legend = "right") +
		geom_path(aes(x = Longitude, # path outline
		y = Latitude),
		data = gps,
		colour = "black",
		size = 2) +
		geom_path(aes(x = Longitude, # path
		y = Latitude),
		colour = pathcolor,
		data = gps,
		size = 1.4) # +
	# labs(x = "Longitude",
	#   y = "Latitude") # if you do extent = "panel"

We'll be changing the four lines marked above in orange to change what basemap is used.

##source = "google"
```get_map``` option source = "google" (or using get_googlemap) downloads a map from the Google Maps API. The basemaps are © Google. Google Maps have four different maptype options: terrain, satellite, roadmap, and hybrid.

###source = "google", maptype = "terrain"
![source = "google", maptype = "terrain", zoom = 14]({filename}/images/r-google-terrain.png)

Max zoom: 14

###source = "google", maptype = "satellite"
![source = "google", maptype = "satellite", zoom = 17]({filename}/images/r-google-satellite.png)

Max zoom: 20

###source = "google", maptype = "roadmap"
![source = "google", maptype = "roadmap", zoom = 17]({filename}/images/r-google-roadmap.png)

###source = "google", maptype = "hybrid"
Hybrid combines roadmap and satellite.
![source = "google", maptype = "hybrid", zoom = 17]({filename}/images/r-google-hybrid.png)

Max zoom: 14

##source = "osm"

```get_map``` option source = "osm" (or using ```get_openstreetmap```) downloads a map from [OpenStreetMap](http://www.openstreetmap.org/). These maps are Creative Commons licensed, specifically [Attribution-ShareAlike 2.0 (CC-BY-SA)](http://creativecommons.org/licenses/by-sa/2.0/). This means you are free to use the maps for commercial purposes, as long as you release your final product under the same Creative Commons license. OpenStreetMap has no maptype options.


###source = "osm" (no maptype needed)

![source = "osm", zoom = 17]({filename}/images/r-osm.png)

Max zoom: 20

##source = "stamen"
```get_map``` option source = "stamen" (or using ```get_stamenmap```) downloads a map from Stamen Maps. The map tiles are by [Stamen Design](http://stamen.com/), licensed under [CC BY 3.0](http://creativecommons.org/licenses/by/3.0). The data for Stamen Maps is by [OpenStreetMap](http://openstreetmap.org/), licensed under [CC BY SA](http://creativecommons.org/licenses/by-sa/3.0). Stamen has three different maptype options: terrain, watercolor, and toner.

###source = "stamen", maptype = "terrain"

![source = "stamen", maptype = "terrain", zoom = 17]({filename}/images/r-stamen-terrain.png)

Max zoom: 18

###source = "stamen", maptype = "watercolor"

![source = "stamen", maptype = "watercolor", zoom = 17]({filename}/images/r-stamen-watercolor.png)

Max zoom: 18

###source = "stamen", maptype = "toner"

![source = "stamen", maptype = "toner", zoom = 17]({filename}/images/r-stamen-toner.png)

Max zoom: 18

##source = "cloudmade"

> N.B. As of March 2014, CloudMade no longer provides this API service.

CloudMade styles build on top of OpenStreetMap data. Thousands of CloudMade styles are available. You can [browse them on the CloudMade site](http://maps.cloudmade.com/editor#). You can also make your own styles.

To use CloudMade map styles in R, you will first need to get an API key to insert into your R code so it can access the maps. You can [get an API key from the CloudMade site](http://cloudmade.com/user/show).

Here are just a couple examples of CloudMade basemaps:

![source = "cloudmade", maptype = "1", api_key="your_api_key_here, zoom = 17]({filename}/images/r-cloudmade-1.png)

![source = "cloudmade", maptype = "67367", api_key="your_api_key_here, zoom = 17]({filename}/images/r-cloudmade-67367.png)

Max zoom: 18

The code and data are available in a [gist](https://gist.github.com/mollietaylor/4742865).


