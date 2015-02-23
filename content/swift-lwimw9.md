Title: LWIMW 9
Date: 2015-01-25
Tags: Swift, MapKit, Xcode, GPS, LWIMW, competitions
Category: Swift
Slug: lwimw9
Author: Mollie Taylor
Summary: I just finished my submission for Look What I Made Weekend 9.

I just finished my submission for [Look What I Made Weekend 9](http://lookwhatimadeweekend.com/). Look What I Made Weekend (LWIMW) is a chance for people to create something over the course of 48 hours. The concept is based on [Ludum Dare](http://www.ludumdare.com/) and other game jams, but for LWIMW you don't have to make a game. Instead, you are free to pursue any creative endeavor and show off your results at the end.

> NB: The content below is mostly a reprint of [my submission at LWIMW](http://lookwhatimadeweekend.com/contest/9/submission/110/).

This is my first app using Swift and also my first app using MapKit.

It's a simple app that takes an average of several GPS coordinates so that you can get a more accurate estimate of the coordinates of a point.

![Main VC]({filename}/images/swift-lwimw-main.png)

Before the weekend, all I had done was a quick sketch of what the app might look like.

What I got done this weekend: 

* GPS tracking (auto mode) 
* Averaging 
* Displaying tracking and averaging on map 
* App icon 
* Sharing

![Averaged Coordinates]({filename}/images/swift-lwimw-averaged.png)

![Saved Coordinates]({filename}/images/swift-lwimw-saved.png)

What still needs to be done: 

* Persistent storing of data 
* Manual mode 
* Multiple coordinate formats 
* Some testing and miscellaneous improvements

You can view the code or download the app on [Github](https://github.com/mollietaylor/GPS-Averager/).