Title: Import JSON Data from an External File in Leaflet
Date: 2014-01-09
Tags: geojson, getJSON, Javascript, jQuery, JSON, L.geoJson, Leaflet
Category: Leaflet
Slug: 2014/01/import-json-data-from-external-file-in
Author: Mollie Taylor
Summary: If your JSON or GeoJSON data is long, you might want to store it in a separate file to make your code more readable or to reduce repetition and allow you to access the same data file from multiple pages.

If your JSON or GeoJSON data is long, you might want to store it in a separate file to make your code more readable or to reduce repetition and allow you to access the same data file from multiple pages. You can do that with jQuery.

First, load jQuery 1.10.2 or the newest version of jQuery (2.0 onward does not support Internet Explorer 6, 7, or 8) in the header:

	:::html
	<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>

Next, in your leaflet script at the bottom of the body, you'll need to add all your other code and your basemap, like normal, for example:

	:::js
	var map = L.map('map').setView([38.0740, -55], 3);

	function onEachFeature(feature, layer) {
		layer.bindPopup(feature.properties.City + ", " + feature.properties.State + ", " + feature.properties.Country);
	}

Then, you can just use jQuery to get the JSON or GeoJSON file. A simple version of this would be:

	:::js
	$.getJSON("cities.geoJSON", function (cities) {
		L.geoJson(cities).addTo(map);
	})

But you can also add more options to your ```L.geoJson``` code, just like you would if using data stored in the HTML file. For example:

	:::js
	$.getJSON("cities.geoJSON", function (cities) {
		L.geoJson(cities, {
			onEachFeature: onEachFeature,
			pointToLayer: function (feature, latlng) {
				switch (feature.properties.Remember) {
					case '1': return L.marker(latlng, {icon: visitedIcon});
					case '?': return L.marker(latlng, {icon: uncertainIcon});
					case '0': return L.marker(latlng, {icon: uncertainIcon});
				}
			}
		}).addTo(map);
	})

So just a couple lines of jQuery allow you to store your JSON or GeoJSON data in a separate file.

The [example code is available in a gist](https://gist.github.com/mollietaylor/7582459) and the [example is viewable here](http://gtg339g.com/skills/js/leaflet/cities/).

##Further Reading
* <http://lyzidiamond.com/posts/external-geojson-and-leaflet-the-other-way/>
