Title: Reality TV Show Name Generator App
Date: 2015-01-20
Tags: Objective-C, iOS
Category: Objective-C
Slug: reality-tv-app
Author: Mollie Taylor
Summary: My first iOS app is a silly reality TV show name generator. Read about my process of creating the app.



## The Idea

I had come across webpages like [They Fight Crime](http://www.theyfightcrime.org/) and the [Fantasy Name Generator](http://rinkworks.com/namegen/), so creating a random reality TV show name generator app was not at all an original idea. 

When I was flipping through channels one day and saw an endless stream of a naming convention, inspiration struck. I noticed that most reality shows have a name that's just an adjective and a noun: American Idol, Hell's Kitchen, Pawn Stars, Top Chef, just to name a few. This seemed like a really simple concept to implement while learning a new language. Really, it's the simplest unique app I've thought of.

## The Javascript Implementation

In 2013, I created a [Javascript version](http://realitytvgenerator.com/) of the app. I was just learning Javascript when I thought of the idea, and it was an easy first project to complete.

![Javascript version]({filename}images/reality-js.png){.size-auto}

## The Objective-C Implementation

When I started learning Objective-C in December, I followed the [Crystal Ball app tutorial on Team Treehouse](http://teamtreehouse.com/library/build-a-simple-iphone-app-ios7), and after that, I had enough knowledge to build the most simple version of the Reality TV app.

Basically, all the simplest version needs to do is:

* Have two arrays
* Pick a random item from the first array
* Pick a random item from the second array
* Concatenate them
* Display the name
* Have a straightforward way to refresh and get a new random name

Here's a screenshot of an early version:

![Early Objective-C version]({filename}images/reality-early.png)

### Components

As I advanced in Objective-C, I wanted to add more features. The first thing I added was a "share" button. This was surprisingly simple.

Once I started taking the [Mobile Engineering class at The Iron Yard](http://theironyard.com/academy/mobile-engineering/), I began to add more features. I wanted to add a "recent names" list and a "favorites" list and to have a way for people to add a name to their favorites.

Once we learned about TableViewControllers, adding the recent names list was fairly straightforward.

![Early Recent Items]({filename}images/reality-early-recent.png)

![Early Share & Recent]({filename}images/reality-early-recent-share.png)

What was more complicated was adding a "favorites" list. I wanted to have the favorites persist between app uses. This is something we haven't covered yet in class, but I got a tip from John–one of our TAs–and I managed to figure out how to implement it using ```NSUserDefaults```.

Now that all of the functionality worked, what was left was the design. I needed icons for favoriting and sharing, and I wanted to make a custom TV design instead of using one someone else made since it was such a central part of the app.


### Design

I wasn't happy with the way the original design looked, so I changed the color palette.

<table>
<tr><td style="width: 70px; height: 50px; background-color:#009762">#009762</td><td style="width: 70px; height: 50px; background-color:#13BD81">#13BD81</td><td style="width: 70px; height: 50px; background-color:#000000">#000000</td><td style="width: 70px; height: 50px; background-color:#ffffff">#ffffff</td></tr>
</table>

Looking better!

One thing I'd had no intention of making was a sliding drawer that would give you more options. I didn't really even think of this as being an option! But then in class we made a drawer for one of our apps, and I realized it would be the perfect way to handle all the buttons I wanted to have (favorite, favorites, recent, share). I designed a drawer and added it to the app.

![Drawer]({filename}images/reality-drawer.png)

For the icons in the drawer (favorite, menu, and share) and the refresh icon, I used [Font Awesome](http://fortawesome.github.io/Font-Awesome/) and [Ionicons](https://ionicons.com), which are both free-to-use icon packages. 

For the TV image, I wanted to create something custom, since it was so prominently displayed in the app. I played around some in Photoshop. Even though I can't draw at all, I can sure use a rectangle tool, and I think I managed to come up with something that looks acceptable. You can see my design on [Dribbble](https://dribbble.com/shots/1887417-TV). I also used this TV as my app icon, but I gave the app version wider antennae to make them easier to see in the smaller size.

I've been learning Sketch, but I've really only used it for UI mockups, not drawing things. Hopefully soon I'll be able to use a more appropriate tool like Sketch or Illustrator instead of using Photoshop for this kind of work, but for the moment, I'm still more comfortable in Photoshop.

![Custom TV]({filename}images/reality-new-tv.png)

The last design decision I had to make was how to handle:

1. Favoriting recent names
2. Sharing recent names and favorites

Originally, I had a share icon on the side of each cell on the recent items list. But once I added favorites, I would have needed to have two icons in each cell, one for sharing and one for favoriting. I decided this would be too cluttered, so I decided to return users to the main view when they tap on a name in a list. From there, they can do anything they would have been able to do when the name first appeared. This setup has the additional benefit of allowing people to make screenshots of items from their recent items list or favorites list.

### Complete

You can download the iPhone app [here](https://itunes.apple.com/us/app/reality-tv-show-name-generator/id961844793?ls=1&mt=8). The code is available [on Github](https://github.com/mollietaylor/reality-tv-iOS).