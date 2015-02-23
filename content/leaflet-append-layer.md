Title: Append Layer to overlayMaps in Leaflet
Date: 2014-01-30
Tags: geolocation, Javascript, Leaflet, locationfound, overlayMaps
Category: Leaflet
Slug: 2014/01/append-layer-to-overlaymaps-in-leaflet
Author: Mollie Taylor
Summary: What if we want to create a layer based on geolocation, but have the layer only be added to the map once geolocation occurs?

What if we want to create a layer based on geolocation, but have the layer only be added to the map once geolocation occurs? I didn't find this example in any Leaflet tutorials, but it's pretty simple with some basic JavaScript

I'll start with some code that should look familiar from the [Leaflet Quick Start Guide](http://leafletjs.com/examples/quick-start.html), but with each item as its own layer.

	:::js
	var marker = L.marker([51.5, -0.09]);

	var circle = L.circle([51.508, -0.11], 500, {
		color: 'red',
		fillColor: '#f03',
		fillOpacity: 0.5
	});

	var polygon = L.polygon([
		[51.509, -0.08],
		[51.503, -0.06],
		[51.51, -0.047]
	]);

	var map = L.map('map', {
		center: [51.505, -0.09],
		zoom: 13,
		layers: [marker, circle, polygon]
	});

	var overlayMaps = {
		"Marker": marker,
		"Circle": circle,
		"Polygon": polygon
	};
	L.tileLayer('http://tile.cloudmade.com/[API-KEY]/29889/256/{z}/{x}/{y}.png', {
		attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://cloudmade.com">CloudMade</a>',
	  maxZoom: 18
	}).addTo(map);

Next let's add the code that will display the three original layers if geolocation does not occur. In this case, we do not want the geolocated layer to show.

	:::js
	function onLocationError(e) {
		alert(e.message);

		L.control.layers(null, overlayMaps).addTo(map);
	}

	map.on('locationerror', onLocationError);

You can see in the below screenshot that only the three layers are displayed.

![With geolocation off]({filename}/images/append-layer-geolocation-off.png){.size-auto}

Finally, we need to add code that will display all the layers (including the geolocation layer) if geolocation does occur. We simply need to add the "yourLocation" layer to overlayMaps and then display the layers as normal.

	:::js
	function onLocationFound(e) {
		yourLocation = L.marker(e.latlng);

		overlayMaps["You"] = yourLocation;

		L.control.layers(null, overlayMaps).addTo(map);
	}

	map.on('locationfound', onLocationFound);

The screenshots below show what happens once geolocation has occurred.

![With geolocation on]({filename}/images/append-layer-geolocation-on.png){.size-auto}

![Showing geolocation layer]({filename}/images/append-layer-show-geolocation.png){.size-auto}

The full code is available in [a gist](https://gist.github.com/mollietaylor/8700934).

##References
* <http://stackoverflow.com/questions/695050/how-do-i-add-a-property-to-a-javascript-object-using-a-variable-as-the-name>


