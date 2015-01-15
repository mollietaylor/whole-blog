Title: Add Icons to Layer Control in Leaflet
Date: 2014-03-27
Tags: Javascript, L.control.layers, Leaflet, overlayMaps
Category: Leaflet
Slug: 2014/03/add-icons-to-layer-control-in-leaflet.html
Author: Mollie Taylor
Summary: When you have multiple layers, it can help to add a legend to the map. This tutorial shows how to add icons to the layer control in Leaflet.

When you have multiple layers, it can help to add a legend to the map. This tutorial shows how to add icons to the layer control in Leaflet. This tutorial shows only marker layers, but you could create icons for polygon layers and use those as well.

![Legend with marker icons]({filename}/images/add-icons-layer-control-legend.png)

The following code sets up our map, layers, and the layer control. This is the standard way maps look in Leaflet, with no visual indication of which layer goes with which markers, without checking the boxes on and off.

	:::js
	var map = L.map('map', {
		center: [33.8, -84.4],
		zoom: 11,
			layers: [trainLayer, treeLayer]
	});

	var overlayMaps = {
		"Train": trainLayer,
		"Tree": treeLayer
	};

	L.control.layers(null, overlayMaps, {
		collapsed: false
	}).addTo(map);

![Default legend]({filename}/images/add-icons-layer-control-no-legend.png)

In order to add a legend to the layer control, you can simply change the overlayMaps code to add any HTML you'd like. In this case, we'll add the map icon pngs with a small height so they will look okay in the layer control:

	:::js
	var overlayMaps = {
		"<img src='http://mollietaylor.com/skills/js/leaflet/train.png' height=24>Train": trainLayer,
		"<img src='http://mollietaylor.com/skills/js/leaflet/arbol.png' height=24>Tree": treeLayer
	};

It's really that simple! I searched the documentation and the web, and I couldn't figure out how to do this, so I figured I'd just try adding the HTML. Turns out it looks great!

Full code available on [CodePen](http://codepen.io/mollie/pen/wEvbd). Map icons by [Nicolas Mollet and Axel Rodriguez](http://mapicons.nicolasmollet.com/).
