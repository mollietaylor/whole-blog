Title: Shapefiles in R
Date: 2013-02-28
Tags: fortify, geom_polygon, get_map, ggmap, gps, maptools, R, RColorBrewer, readShapePoly, visualization
Category: R
Slug: 2013/02/shapefiles-in-r
Author: Mollie Taylor
Summary: Let's learn how to use Shapefiles in R. This will allow us to map data for complicated areas or jurisdictions like zipcodes or school districts.

Let's learn how to use [Shapefiles](http://en.wikipedia.org/wiki/Shapefile) in R. This will allow us to map data for complicated areas or jurisdictions like zipcodes or school districts. For the United States, many shapefiles are available from the [Census Bureau](http://www.census.gov/geo/www/tiger/tgrshp2010/tgrshp2010.html. Our example will map U.S. national parks.

First, download the [U.S. Parks and Protected Lands shape files from Natural Earth](http://www.naturalearthdata.com/downloads/10m-cultural-vectors/parks-and-protected-lands/). We'll be using the ne_10m_parks_and_protected_lands_area.shp file.

Next, start working in R. First, we'll load the shapefile and **maptools**:

	:::r
	# load up area shape file:
	library(maptools)
	area <- readShapePoly("ne_10m_parks_and_protected_lands_area.shp")

	# # or file.choose:
	# area <- readShapePoly(file.choose())

Next we can set the colors we want to use. And then we can set up our [basemap]({filename}r-basemaps.md).

	:::r
	library(RColorBrewer)
	colors <- brewer.pal(9, "BuGn")

	library(ggmap)
	mapImage <- get_map(location = c(lon = -118, lat = 37.5),
		color = "color",
		source = "osm",
		# maptype = "terrain",
		zoom = 6)

Next, we can use the ```fortify``` function from the *ggplot2* package. This converts the crazy shape file with all its nested attributes into a data frame that ggmap will know what to do with.

	:::r
	area.points <- fortify(area)

Finally, we can map our shape files!

	:::r
	ggmap(mapImage) +
		geom_polygon(aes(x = long,
				y = lat,
				group = group),
			data = area.points,
			color = colors[9],
			fill = colors[6],
			alpha = 0.5) +
	labs(x = "Longitude",
		y = "Latitude")

![National Parks and Protected Lands in California and Nevada]({filename}/images/shapefiles-osm.png)

![Same figure, with a Stamen terrain basemap with ColorBrewer palette "RdPu"]({filename}/images/shapefiles-stamen.png)

##Citations and Further Reading
* <http://www.naturalearthdata.com/downloads/10m-cultural-vectors/parks-and-protected-lands/>
* <http://stackoverflow.com/questions/11428176/plotting-a-shape-file-with-ggplot2-error>
* <http://geography.uoregon.edu/GeogR/topics/maps.htm>
* Basemaps from [OpenStreetMap](http://www.openstreetmap.org/) and [Stamen](http://stamen.com/maps)

