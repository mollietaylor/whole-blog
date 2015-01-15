Title: Palettes in R
Date: 2012-10-25
Tags: brewer.pal, palette, R, RColorBrewer, visualization
Category: R
Slug: 2012/10/palettes-in-r.html
Author: Mollie Taylor
Summary: In its simplest form, a palette in R is simply a vector of colors. This vector can be include the hex triplet or R color names.

In its simplest form, a palette in R is simply a vector of colors. This vector can be include the hex triplet or R color names.

The default palette can be seen through ```palette()```: 

	:::r
	> palette("default") # you'll only need this line if you've previously changed the palette from the default
	> palette()
	[1] "black"   "red"     "green3"  "blue"    "cyan"    "magenta" "yellow"
	[8] "gray"

##Defining your own palettes
If you want to make your own palette, you can just create your own vector of colors. It's fine for your vector to include a mixture of hex triplets and R color names. You can use the ```palette``` function above, but generally it's best to just store each palette as a standard vector. For one thing, you can use more than one palette that way. Here's how you can define your own palette:

	:::r
	colors <- c("#A7A7A7",
		"dodgerblue",
		"firebrick",
		"forestgreen",
		"gold")

Now let's try using our palette. For now let's just color each bar of a histogram. This is a silly example, but I think it's the easiest way to show how to get R to utilize your palette. In the following example, there are six bars, but only five colors. You can see that R will cycle through your palette to fill all the shapes.

	:::r
	hist(discoveries,
		col = colors)

![One color per bar]({filename}images/r-palette-color-by-bar.png)

A more sensible use of color is to use a different color for each of a number of summary statistics:

	:::r
	colors <- c("#A7A7A7",
		"dodgerblue",
		"firebrick",
		"forestgreen",
		"gold")
	hist(discoveries,
		col = colors[1])
	abline(v = mean(discoveries),
		col = colors[2],
		lwd = 5)
	abline(v = median(discoveries),
		col = colors[3],
		lwd = 5)
	abline(v = min(discoveries),
		col = colors[4],
		lwd = 5)
	abline(v = max(discoveries),
		col = colors[5],
		lwd = 5)
	legend(x = "topright", # location of legend within plot area
		col = colors[2:5],

	c("Mean", "Median", "Minimum", "Maximum"),
		lwd = 5)

![Summary statistics]({filename}images/r-palette-stats.png)

##Predefined palettes: default R palettes
The package **grDevices** (you probably already have this loaded) contains a number of palettes.

	:::r
	?rainbow
	rainbowcols <- rainbow(6)
	hist(discoveries,
		col = rainbowcols)

![Rainbow palette]({filename}images/r-palette-rainbow.png)

For ```rainbow```, you can adjust the saturation and value. For example:

	rainbowcols <- rainbow(6,
		s = 0.5)
	hist(discoveries,
		col = rainbowcols)

![Rainbow palette desaturated]({filename}images/r-palette-rainbow-pale.png)

	:::r
	heatcols <- heat.colors(6)
	hist(discoveries,
		col = heatcols)

![heat.colors palette]({filename}images/r-palette-heat.png)

As well as ```rainbow``` and ```heat.colors```, there are also ```terrain.colors```, ```topo.colors```, and ```cm.colors```.

##Predefined palettes: RColorBrewer

	:::r
	library(RColorBrewer)
	display.brewer.all()

The above lines will show us all the **RColorBrewer** palettes (output shown below). The top section of palettes are sequential, the middle section are qualitative, and the lower section are diverging. [Here is some information about how to choose a good palette](http://blog.ggplot2.org/post/24607351280/choosing-colour-palettes-part-ii-educated-choices).

![RColorBrewer palettes]({filename}images/r-display-brewer-all.png)

**RColorBrewer** works a little different than how we've defined palettes previously. We'll have to use ```brewer.pal``` to create a palette.

	:::r
	library(RColorBrewer)
	darkcols <- brewer.pal(8, "Dark2")
	hist(discoveries,
		col = darkcols)

![Dark2 color palette]({filename}images/r-palette-dark2.png)

Even though we have to provide ```brewer.pal``` with the number of colors we want, we won't necessarily need to use all those colors later. We can still choose a color from the vector like we have previously. When we're setting a ```col``` setting to the full palette, we'll be more concerned with how many colors are included in the palette , but even there, we can choose a subset of the whole palette:

	:::r
	darkcols <- brewer.pal(8, "Dark2")
	hist(discoveries,
		col = darkcols[1:2])

![Dark 2 color palette, two colors]({filename}images/r-palette-dark2-2.png)

[Here](https://gist.github.com/3943476)'s the code from this post.

Now that we're familiar with making our own palettes and using the built-in palettes in **grDevices** and **RColorBrewer**, I'm planning a future post about a more practical (but also more complicated) example of using palettes: making maps.
