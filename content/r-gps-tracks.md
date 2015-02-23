Title: Mapping GPS Tracks in R
Date: 2012-12-13
Tags: geom_point, ggmap, GPSBabel, R, Series: GPS Tracks, visualization
Category: R
Slug: 2012/12/mapping-gps-tracks-in-r
Author: Mollie Taylor
Summary: This is an explanation of how I used R to combine all my GPS cycling tracks from my Garmin Forerunner 305.

This is an explanation of how I used R to combine all my GPS cycling tracks from my Garmin Forerunner 305.

##Converting to CSV

You can convert pretty much any GPS data to .csv by using [GPSBabel](http://www.gpsbabel.org/htmldoc-1.4.4/readme.html). For importing directly from my Garmin, I used the command:

	:::console
	gpsbabel -t -i garmin -f usb: -o unicsv -F out.csv

[Note: you'll probably need to work as root to access your device directly]

For importing from a .tcx file, you can use:

	:::console
	gpsbabel -t -i gtrnctr -f test2.tcx -o unicsv -F old.csv

##Mapping in R

After converting to .csv, we'll have a file with several columns, such as latitude, longitude, date, and time. We can now easily import this into R.

	:::r
	gps <- read.csv("out.csv", 
		header = TRUE)

Next we want to load up ggmap and get our base map. To determine how zoomed in we are, we can set ```zoom``` and ```size```. We can also choose the ```maptype```, with options of terrain, satellite, roadmap, or hybrid (satellite + roadmap).

	:::r
	library(ggmap)
	mapImageData <- get_googlemap(center = c(lon = median(gps$Longitude), lat = median(gps$Latitude)),
		zoom = 11,
	# size = c(500, 500),
		maptype = c("terrain"))

I chose to set the ```center``` of the map to the median of my latitudes and the median of my longitudes. I've done some biking when traveling, so median made more sense for me than mean.
Finally we want to map our GPS data. There are several [```pch``` options](http://www.endmemo.com/program/R/pchsymbols.php) to try.

	:::r
	ggmap(mapImageData,
		extent = "device") + # takes out axes, etc.
		geom_point(aes(x = Longitude,
			y = Latitude),
		data = gps,
		colour = "red",
		size = 1,

![All my metro Atlanta bike rides]({filename}images/r-gps-tracks.png)

Previously, I've used Google Earth to create these maps, but I actually found it to be easier and way less time and resource efficient to do it in R. The only tricky part was converting the data into .csv, and there are [other ways](http://www.gpsvisualizer.com/convert_input?convert_output=gpx) to do that, if GPSBabel isn't working for you. You might also be interested in trying [Google Earth]({filename}google-earth-gpx.md) for mapping your tracks, instead of R.

[Here's the gist](https://gist.github.com/4210660) with the code.


> This post is one part of [my series on Mapping GPS Tracks](http://blog.mollietaylor.com/tag/series-gps-tracks.html).

##Citations and Further Reading
* <http://www.gpsbabel.org/htmldoc-1.4.4/readme.html>
* <http://www.olberg.se/?q=node/25>
* <http://stackoverflow.com/questions/11648870/offline-plotting-of-map-coordinates-on-static-maps-of-google>
* <http://stackoverflow.com/questions/11590193/saving-image-in-ggplot-ggmap>



 pch = 20)