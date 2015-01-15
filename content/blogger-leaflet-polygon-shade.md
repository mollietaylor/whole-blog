Title: Make All Polygons the Same Shade in Leaflet
Date: 2013-12-19
Tags: Javascript, L.polygon, Leaflet, setStyle
Category: Leaflet
Slug: 2013/12/make-all-polygons-same-shade-in-leaflet.html
Author: Mollie Taylor
Summary: What if we want to change the color and style of all (or a set of the) polygons?

The [Quick Start tutorial](http://leafletjs.com/examples/quick-start.html) shows us how to change the color of a polygon:

	:::js
	var circle = L.circle([51.508, -0.11], 500, {
		color: 'red',
		fillColor: '#f03',
		fillOpacity: 0.5
	}).addTo(map);

But what if we want to change the color and style of all (or a set of the) polygons?

First we can define the style:

	:::js
	var defaultStyle = {
		color: 'green',
		fillOpacity: 0.2
	};

And then we can just add that style to our polygons:

	:::js
	var polygon = L.polygon([
		[51.509, -0.08],
		[51.503, -0.06],
		[51.51, -0.047]
	]).setStyle(defaultStyle).addTo(map);

	var circle = L.circle([51.508, -0.11], 500).setStyle(defaultStyle).addTo(map);

The full code (based on [the Quick Start tutorial](http://leafletjs.com/examples/quick-start.html)) is available in a [gist](https://gist.github.com/mollietaylor/7110969).


