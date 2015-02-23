Title: Embed Audio in Leaflet Pop-up
Date: 2014-01-16
Tags: audio, bindPopup, geojson, HTML, Javascript, Leaflet
Category: Leaflet
Slug: 2014/01/embed-audio-in-leaflet-pop-up
Author: Mollie Taylor
Summary: Here's how to embed audio in a leaflet map.

Here's how to embed audio in a leaflet map. This example will also show you how to embed most other HTML in a leaflet map, or how to embed audio in an HTML file.

In your map code:

	:::js
	function onEachAudio(feature, layer) {
		layer.bindPopup(feature.properties.name + "<br>" + feature.properties.html);
	};

	new L.GeoJSON.AJAX("audio.geojson", {
		onEachFeature: onEachAudio,
		pointToLayer: function(feature, latlng) {
		  return L.marker(latlng, {icon: audioIcon});
		}
	}).addTo(map);

And here's the geojson format where you'll include your audio HTML and the coordinates where you want to view each file:

	:::json
	{
		"type": "FeatureCollection",
		"features": [
		{
			"type": "Feature",
			"properties": {
				"name": "<a href='http://www.freesound.org/people/genghis%20attenborough/sounds/212798/'>Deep basement</a>",
				"html": "<p><audio width='300' height='32' src='http://www.freesound.org/data/previews/212/212798_205108-lq.mp3' controls='controls'><br />Your browser does not support the audio element.<br /></audio></p>"
			},
			"geometry": {
				"type": "Point",
				"coordinates": [-100,34]
			}
		},{
			"type": "Feature",
			"properties": {
				"name": "<a href='http://www.freesound.org/people/John%20Sipos/sounds/125696/'>Atlantis docks then lands.</a>",
				"html": "<p><audio width='300' height='32' src='http://www.freesound.org/data/previews/125/125696_593024-lq.mp3' controls='controls'><br />Your browser does not support the audio element.<br /></audio></p>"
			},
			"geometry": {
				"type": "Point",
				"coordinates": [-84,40]
			}
		}
		]
	}

Just substitute in the address of your audio files for the sample files above in the "html" property of the geojson features.

![Example Leaflet map with audio]({filename}/images/embed-audio-leaflet.png)

The full code is available in [a gist](https://gist.github.com/mollietaylor/8230639).

