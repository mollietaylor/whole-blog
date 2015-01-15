Title: Center Map on Layer Change in Leaflet
Date: 2014-02-27
Tags: baselayerchange, fitBounds, Javascript, L.circle, L.polygon, Leaflet, panTo, setView
Category: Leaflet
Slug: 2014/02/center-map-on-layer-change-in-leaflet.html
Author: Mollie Taylor
Summary: In Leaflet, it can be helpful to change the bounds of the map when the user adds or changes the visible map layers.

In Leaflet, it can be helpful to change the bounds of the map when the user adds or changes the visible map layers.

##The Basics

First, we'll start with the initial code including our map and polygon layers:

	:::js
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
		zoom: 13
	});

	var overlayMaps = {
		"Circle": circle,
		"Polygon": polygon
	};

	L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
		attribution: '&copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>'
	}).addTo(map);

	L.control.layers(overlayMaps, null, {
		collapsed: false
	}).addTo(map);

So far, most of this should be familiar from the [Leaflet Quick Start Guide](http://leafletjs.com/examples/quick-start.html).

Next, we want to add a listener function that will zoom and re-center upon a change in the circle or polygon layer.

The ```.on``` method of ```map``` allows you to watch for an event to occur and then execute a function when it does. In this case, we want to wait for the event ```'baselayerchange'```. This way the map will automatically zoom and recenter when the user changes layers.

	:::js
	map.on('baselayerchange', function(e) {
		console.log(e);
		map.fitBounds(e.layer);
	});

![The map automatically zooms to the bounds of the shape when the layer is activated.]({filename}/images/center-map-circle.png)

##Options

There are a few options for exactly how the map is zoomed and/or re-centered and for what type of layers are affected.

If you want to do this with overlay layers instead of base layers, you can substitute ```'overlayadd'``` for ```'baselayerchange'```. Using overlay layers is more common for drawing shapes, but treating your layers as base layers makes it easy to display only one at a time.

	:::js
	map.on('overlayadd', function(e) {
		console.log(e);
		map.fitBounds(e.layer);
	});

```fitBounds``` automatically zooms to the tightest zoom level where the whole shape is visible. If you don't want to use ```fitBounds``` (say you're centering on a new overlay layer and don't want to zoom all the way in), you can use ```setView``` or ```panTo``` instead. ```panTo``` animates as the view changes.

	:::js
	map.on('overlayadd', function(e) {
		console.log(e);
		map.panTo(e.layer);
	});

And there you have a few different ways to center and/or zoom in when an overlay layer is added or when the baselayer is changed. I'd recommend you [check out the documentation for fitBounds, setView, and panTo](http://leafletjs.com/reference.html) and play around with the options. The [options for L.control.layers](http://leafletjs.com/reference.html#control-layers) are also helpful. For example, you can set ```collapsed``` to false to encourage users to change the layers.

The full code is available in [a gist](https://gist.github.com/mollietaylor/9127811).

##References

* <http://leafletjs.com/reference.html#map-fitbounds>
* <http://leafletjs.com/reference.html#control-layers-baselayerchange>
* <http://leafletjs.com/reference.html#map-overlayadd>
