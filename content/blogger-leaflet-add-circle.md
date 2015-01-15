Title: Add and Remove Leaflet Circle on Click
Date: 2014-01-23
Tags: addTo, Javascript, L.circle, Leaflet, on, removeLayer
Category: Leaflet
Slug: 2014/01/add-and-remove-leaflet-circle-on-click.html
Author: Mollie Taylor
Summary: Similar to the popup example in the Leaflet tutorial, you might want to allow a user to add a circle centered on the point they click.

Similar to the popup example in the Leaflet tutorial, you might want to allow a user to add a circle centered on the point they click.

After defining your map, you first need to declare the variable you'll be using:

	:::js
	var clickCircle;

While popups automatically disappear on the next click, circles do not. The following code removes the former circle from the leaflet map before drawing the new circle:

	:::js
	function onMapClick(e) {
		if (clickCircle != undefined) {
			map.removeLayer(clickCircle);
		};

Next, we want our function to draw the new circle (NB: "1609 * 3" is the radius of the circle. This makes the radius equal 3 miles):

	:::js
		clickCircle = L.circle(e.latlng, 1609 * 3, {
			color: '#f07300',
			fillOpacity: 0,
			opacity: 0.5
	  }).addTo(map);
	}

And finally, we need to add an event listener so that the function will be run when a user clicks on the map:

	:::js
	map.on('click', onMapClick);

The full code is available in [a gist](https://gist.github.com/mollietaylor/8564724).

##References
* <http://leafletjs.com/examples/quick-start.html>
* <http://stackoverflow.com/questions/15507737/adding-removing-l-control-from-leaflet-js-map>
* <http://stackoverflow.com/questions/11272552/remove-polygon-from-the-map>

