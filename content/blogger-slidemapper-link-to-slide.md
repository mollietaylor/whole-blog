Title: Link to Another Slide in Leaflet Slidemapper
Date: 2014-03-06
Tags: class, click, CSS, Javascript, jQuery, Leaflet, move, slidemapper
Category: Leaflet
Slug: 2014/03/link-to-another-slide-in-leaflet.html
Author: Mollie Taylor
Summary: The slidemapper plugin for Leaflet is very useful, but when building large slideshows, it can be annoying that there is no easy way to link to specific slides. 

The [slidemapper plugin for Leaflet](https://github.com/cavis/slidemapper) is very useful, but when building large slideshows, it can be annoying that there is no easy way to link to specific slides. For example, you might want to create a table of contents or link from the last slide back to the first. Fortunately, there's a way to move to specific slides, instead of just advancing or moving back by 1. We'll use jQuery to do this. We already have jQuery loaded for slidemapper.

##Specify Where Links Will Go

After the ```$mySlideMap``` code in your html file, you can create a list of links that you will later add to the slides. Generally, this will be the last thing in the ```<script>``` tag at the end of the body.

For example, in the sample code from the slidemapper example, the ```<script>``` initially contains:

	:::js
	$mySlideMap = $('#slideshow-container')
	.slideMapper();

	$mySlideMap.slideMapper('add', EXAMPLEDATA);

At the end of the script, let's add a link to the first slide and a link to the last slide. The jQuery we use allows any code with a specific class to be transformed into a link. We can combine that with the slidemapper move method to create links to specific slides.

	:::js
	$('.toc').click(function() {
		$mySlideMap.slideMapper('move', 0, true);
	});

	$('.end').click(function() {
		$mySlideMap.slideMapper('move', EXAMPLEDATA.length - 1, true);
	});

##Add the Links

Next, we need to actually include the links in the slides. The links references will go in the data file. In the example, the file is named data.js.

Here's a link to the last slide from the first slide:

	:::html
	// intro marker
	{
		icon: 'other.png',
		marker: [42.516846, -70.898499],
		center: [40.423, -98.7372],
		html: '<table style="margin:0 40px; padding:10px"><tr>' +
				'<td><img src="http://placehold.it/300x180&text=Map+Stuff"/></td>' +
				'<td style="padding-left:10px">' +
					'<h1>SlideMapper FTW!</h1>' +
					'<p>This is a demo of the different sorts of slides you can setup using slidemapper.</p>' +
					'<p><a class="end">Skip to the end.</a></p>' +
				'</td>' +
			'</tr></table>',
		popup: 'So it begins!'
	},

And here's a link from the last slide to the first slide:

	:::html
	// empty slide
	{
		html: '<div style="margin:0 40px; padding:20px 10px">' +
				'<div>' +
					'<h2>The End</h2>' +
					'<p>Goodbye.</p>' +
					'<p><a class="toc">Return to Table of Contents.</a></p>' +
				'</div>' +
			'</div>'
	}

##Prettifying

Because of the unusual way these links are made using jQuery, we should probably add some css to make them look like links. I added the following css to the ```<head>```, but you can add any css to the head or as a separate stylesheet.

	:::css
	<style type="text/css">
		a {
			color: orange;
			cursor: pointer;
			text-decoration: underline;
		}
	</style>

![Here's an example of a link from one slide to another]({filename}/images/slidemapper-link.png)

And now you have an easy way to navigate through a long slidemapper deck. You could even create a table of contents at the beginning and then link back to that from each slide.

The full code is available in [a gist](https://gist.github.com/mollietaylor/9128328).

##References
* <http://stackoverflow.com/questions/950087/how-to-include-a-javascript-file-in-another-javascript-file>
* <https://github.com/cavis/slidemapper#methods>
