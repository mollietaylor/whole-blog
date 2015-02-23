Title: Adding a marker with a custom image to a Mapbox map in Swift
Date: 2015-01-29
Tags: Mapbox, Swift, Series: Mapping in Swift, bridging, RMMapViewDelegate, RMMapView, RMMapboxSource
Category: Swift
Slug: swift-mapbox-image-marker
Author: Mollie Taylor
Summary: There aren't a lot of Swift mapping tutorials out there, so I'm writing a series of blog posts on the topic. First up is how to create a map marker with a custom image in a Mapbox map.

There aren't a lot of Swift mapping tutorials out there, so I'm writing a series of blog posts on the topic. First up is how to create a map marker with a custom image in a Mapbox map.

First, [install the Mapbox SDK as described here](https://www.mapbox.com/mapbox-ios-sdk/#binary).

Next, since we're using Swift, you'll need to create a bridging header by creating a new Objective-C file (empty file) in the project and answering "Yes" to "Would you like to configure an Objective-C bridging header?" In the ```Project Name-Bridging-Header.h``` file that was just created, add:

	:::obj-c
	#import <UIKit/UIKit.h>
	#import "Mapbox.h"

Now, in your ```ViewController.swift``` (or wherever you choose), make sure your class is a ```RMMapViewDelegate```.

In ```viewDidLoad```, add your API access token. You can get your API access token [here](https://www.mapbox.com/projects/).

	:::swift
	RMConfiguration().accessToken = "your-token-goes-here"

Next, add the map view:

	:::swift        
	var mapFrame = CGRectMake(0, 20, view.bounds.width, view.bounds.height)
	var mapTiles = RMMapboxSource(mapID: "your-map-id")
	var mapView = RMMapView(frame: mapFrame, andTilesource: mapTiles)
	mapView.delegate = self

If you want, you can also zoom and center the map now:

	:::swift    
	mapView.zoom = 10
	mapView.centerCoordinate = CLLocationCoordinate2DMake(33.755, -84.39)

Now, take the file you want to use as your map marker and add it to the ```Images.xcassets```.

Back in your View Controller (or other file), add:

	:::swift
	var location:CLLocationCoordinate2D = CLLocationCoordinate2DMake(33.78,-84.41)
	var annotation = RMAnnotation(mapView: mapView, coordinate: location, andTitle: "Proximity Viz LLC")
	annotation.subtitle = "Maps & Apps"
	annotation.userInfo = "company"

Of course here you will put in your own coordinates, title, and subtitle. ```userInfo``` is a handy place to put any other information you might want, i.e. categories that the icon will be based on. E.g. "company" would have one icon and "park" would have another.

Now is when the delegate action comes in, so make sure you included ```RMMapViewDelegate``` at the beginning of your file. Let's add the function that will create a layer for each of our annotations. If you only have one image for your markers, you can use this code:

	:::swift
	func mapView(mapView: RMMapView!, layerForAnnotation annotation: RMAnnotation!) -> RMMapLayer! {
		
		var marker: RMMarker = RMMarker(UIImage: UIImage(named: "proximity"))
		marker.canShowCallout = true
		
		return marker
		
	}

Or if you have multiple images for different categories, you can use this code:

	:::swift
	func mapView(mapView: RMMapView!, layerForAnnotation annotation: RMAnnotation!) -> RMMapLayer! {

		var marker: RMMarker = RMMarker(UIImage: UIImage(named: "proximity"))
		marker.canShowCallout = true

		var parkMarker: RMMarker = RMMarker(UIImage: UIImage(named: "park"))
		parkMarker.canShowCallout = true

		if(annotation.userInfo as NSString == "park"){
			return parkMarker
		} else {
			return marker
		}

	}

Now when you run the app, you should see your custom marker(s)!

![Mapbox map with custom marker]({filename}/images/swift-mapbox-image-marker.png)

The code is available in a [gist](https://gist.github.com/mollietaylor/883c6cf2836f25a82f07).

> This post is one part of [my series on Mapping in Swift](http://blog.mollietaylor.com/tag/series-mapping-in-swift.html).
