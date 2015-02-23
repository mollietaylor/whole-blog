Title: Mapping GPS Tracks in Google Earth
Date: 2012-12-20
Tags: Google Earth, Series: GPS Tracks, visualization
Category: 
Slug: 2012/12/mapping-gps-tracks-in-google-earth
Author: Mollie Taylor
Summary: How to import a bunch of GPS tracks into Google Earth and map them

Even though I find the [R solution]({filename}r-gps-tracks.md) easier, I'm sure not everyone agrees with me, so here's the Google Earth way to import a bunch of GPS tracks and map them:

##Export to TCX

From inside Garmin Training Center or other GPS device software, export a huge TCX file with all your tracks.

##Mapping in Google Earth

![Opening your TCX file]({filename}images/earth-gpx-open.png){.size-auto}

Select File -> Open. Change the dropbox for "Files of type" to "Gps", and then find your file and open it. Make sure the "Create KML LineStrings" box is checked and the "Create KML Tracks" box is unchecked. This will save us some work later.

![Import settings]({filename}images/earth-gpx-import.png){.size-auto}

Next, zoom in, zoom out, and recenter as desired. If you want North to be up, you can click the "N" in the compass in the upper right. 

In the layers (bottom left), I personally like to check Roads and uncheck everything else.

In the places (just above layers), right click "GPS device" and select "Properties". Click over to the "Style, Color" tab, and then click "Share Style".

![Share style]({filename}images/earth-gpx-style.png){.size-auto}

I like to use the following settings:

Lines:

* Color: red
* Width: 3.0
* Opacity: 100%

Label:

* Opacity: 0%

Icon:

* Opacity: 0%

![Example style and color settings]({filename}images/earth-gpx-settings.png){.size-auto}

Make sure you've selected all the dates you want on the date slider. Then you can select "Print" to export to a PDF, or you can take a screenshot.

![Export image]({filename}images/earth-gpx-export.png){.size-auto}

![Date slider and final map]({filename}images/earth-gpx-final.png){.size-auto}

And that's all there is to it. Large maps may take a long time to load and edit.

> This post is one part of [my series on Mapping GPS Tracks](http://blog.mollietaylor.com/tag/series-gps-tracks.html).




