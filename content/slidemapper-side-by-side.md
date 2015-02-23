Title: Changing Leaflet Slidemapper to a Side-by-Side View
Date: 2014-03-13
Tags: Javascript, Leaflet, slidemapper, smapp-map, smapp-show
Category: Leaflet
Slug: 2014/03/changing-leaflet-slidemapper-to-side-by
Author: Mollie Taylor
Summary: The default setup in slidemapper is to have the slides either above or below the map. However, it is also possible to place the slides to one side of the map.

The default setup in [slidemapper](https://github.com/cavis/slidemapper) is to have the slides either above or below the map. However, it is also possible to place the slides to one side of the map.

![Slides beside map]({filename}/images/slidemapper-side.png){.size-auto}

##CSS changes

We need to make a couple of changes to how the smapp-show and smapp-map classes are displayed. You'll want to play around with these some, but this is what worked well for me:

	:::css
	.smapp-show { 
		width:50%; 
	}
	.smapp-show .slide { 
		overflow-y:visible; 
	}
	.smapp-map { 
		margin:10px; 
		width:48%; 
		height:95%; 
		position:absolute; 
		top:0; 
		right:0; 
    }

##Slidemapper changes

On the slidemapper side of things, the only edit we need to make is changing the options of our slideshow. Specifically, we need to edit the slideHeight and mapHeight to something appropriate for having the slides beside the map. For example, I chose:

	:::js
	$mySlideMap = $('#slideshow-container').slideMapper({
		slideHeight: 540,
		mapHeight: '98%'
	});

And that's all the changes you need to make to have a side-by-side slideshow in slidemapper! The full code is available as [a gist](https://gist.github.com/mollietaylor/9128521).

##References

* <https://github.com/cavis/slidemapper>

