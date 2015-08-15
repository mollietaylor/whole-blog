Title: CodeAcross 2015: Creating an Asset Map of South Downtown Atlanta
Date: 2015-02-23
Tags: Leaflet, Javascript, competitions
Category: Leaflet
Slug: codeacross-asset-map
Author: Mollie Taylor
Summary: This weekend, I attended the [CodeAcross](http://www.codeforamerica.org/events/codeacross-2015/) Atlanta [hack weekend](https://nvite.com/codeacross/e7c8), run by [Code for Atlanta](http://www.codeforatlanta.org/) and hosted by the [Center for Civic Innovation](http://www.civicatlanta.org/). The topic of the hack weekend was the South Downtown neighborhood of Atlanta.

This weekend, I attended the [CodeAcross](http://www.codeforamerica.org/events/codeacross-2015/) Atlanta [hack weekend](https://nvite.com/codeacross/e7c8), run by [Code for Atlanta](http://www.codeforatlanta.org/) and hosted by the [Center for Civic Innovation](http://www.civicatlanta.org/). The topic of the hack weekend was the South Downtown neighborhood of Atlanta.

> South Downtown is a neighborhood that's been long ignored and overlooked. But it's brimming with potential. The buildings are there, the density is there, and the people are arriving. South Downtown is waking up.
> 
> Our hosts at the Center for Civic Innovation are kicking off a long-term effort to shape the future of South Downtown, and Code for Atlanta is partnering with them on this goal.
> 
> We're going to get out of the building and take some walking tours of the area to get a real feel for it, then we'll hear from those who live, work, and play in South Downtown. Based on what we learn, we'll then get to business and start hacking on projects. There will be maps to make and data to open.
> 
> This is a rare opportunity to help revitalize a neighborhood at the perfect moment. South Downtown will be a great neighborhood in the near future, and you'll help shape it at CodeAcross Atlanta. &mdash;[Code For Atlanta](http://www.meetup.com/codeforatlanta/events/220190345/)


##Learning about South Downtown

To kick off our hack weekend, Luigi gave an intro to civic hacking. Then Kyle Kessler gave a presentation on the South Downtown neighborhood, past and present. He covered the formation of Atlanta as "Terminus", the Civil War and burning of Atlanta, Atlanta's reemergence, civil rights, Underground Atlanta, the Olympics, and more. This presentation provided a helpful overview to thinking about how South Downtown can be revitalized.

One nice thing about the event was that it actually occurred in South Downtown, the area of interest. CodeAcross was hosted by the Center for Civic Innovation, at the M. Rich Building. As a result, we all got to take a nice walking tour of the neighborhood, to better frame the work we would do over the weekend. Personally, I'm pretty familiar with South Downtown. I'm currently attending [The Iron Yard Academy](http://theironyard.com/), which is located in the same building, and even before that course, I've biked through South Downtown quite a bit. That said, the walking tour was still beneficial to me. A few people in our group had detailed knowledge about the neighborhood, and it was helpful to know more details. The walking tour probably also helped make our map feel more real to the other contributors.

##Three Groups

After lunch, we split up into groups. Three topic were presented, and people were allowed to choose which group they wanted to participate in.

> A branding campaign and storytelling website for South Downtown that begins to change the hearts and minds of Atlantans and their impressions of the neighborhood. Yes, we need folks who can code and launch a website. But just as importantly, we need designers to think about the real-world implications of what a strong brand means for a neighborhood. And we'll need gifted storytellers to convey the gravity of the history of the neighborhood and the role it played in the civil rights movement.
> 
> An interactive asset map that comprehensively displays existing properties in the neighborhood and opportunities for economic development. We need mapping experts to write the code to build the map, but we also need people with expertise in commercial real estate and city planning to help guide the design of the map. We need volunteers to go out into the neighborhood and figure out what exactly is there, because the data about the neighborhood is in many instances incorrect or out-of-date.
> 
> A participatory tool that amplifies the voices of those who live and work in South Downtown. This tool needs to work both on-line and on-the-ground. In many instances of economic development, the powerful, monied interests coming in simply don't listen to the people already in the area. We'll build a platform that collects input from the community and actually delivers that input to key stakeholders. To design it well, it'll require the "soft skills" of listening and empathy. To make it effective, it'll need guidance from those experienced in advocacy and lobbying the powerful. &mdash;[Luigi Montanez](http://www.civicatlanta.org/blog/2015/2/18/civic-hacking-is-for-everybody)

[Unsurprisingly](http://mollietaylor.com/), I chose the asset map group.

##The Asset Map Group

The first step for the asset map group was to whiteboard out what layers we would like to see on the map. We also had to decide who the target audience was for the map. We came to the conclusion that it would be best to have different maps for different audiences (e.g. developers, advocates, visitors), but our focus for the weekend should be to find as many data layers as we could that would have relevance to any of the audiences. Then&mdash;after the weekend&mdash;we will split the map up into multiple maps. Here are just a few of the layers from our list of ideal data:

* Zoning
* Population density and demographics
* Parking
* Transit
* Infrastructure
* Organizations and social events
* Art
* Filming locations

Luigi was the leader of the asset map group. There were around 12 people who chose to work primarily on the asset map. We decided it would be most efficient with such a large group to split up into two sub-groups, one working on research and data, and the other sub-group working on creating the map. It was the first group's job to research each of the map layers we wanted, find if data was readily available, and if it was available, they would get it ready to send along to the map team. If it wasn't readily available, they would try to determine who might have the data and how it could be obtained. 

I was the leader of the sub-group creating the map. We were tasked with making an interactive map showing all the layers of data found by the research and data cleaning team.

##Making the Map

####Day 1

On day one, the research and data cleaning sub-group created a google doc and drive folder and began collecting data to add to the map. Our coding sub-group got the preliminary map set up, and I threw in a couple data layers that I already had handy from previous map projects. The Leaflet newbies ran through a quick tutorial and we looked at alternative mapping platforms like Mapbox and Tilemill. Also on day 1, Bryan and Jimmy in the coding sub-group started working on a geocoder in Ruby, since we knew some of the data the researchers would provide us wouldn't have coordinates.

<blockquote class="twitter-tweet" lang="en"><p>Had a lot of fun today hacking maps w/ <a href="https://twitter.com/codeforatlanta">@codeforatlanta</a> -- can&#39;t wait to do it all over again tomorrow. <a href="https://twitter.com/hashtag/CodeAcross?src=hash">#CodeAcross</a></p>&mdash; jimmylocoding (@jimmylocoding) <a href="https://twitter.com/jimmylocoding/status/569337434460135425">February 22, 2015</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

In our Leaflet map, we made use of a few libraries to help make our job of mapping easier and make our finished product look good quickly. Leaflet only supports GeoJSON by default, but by using [leaflet-omnivore](https://github.com/mapbox/leaflet-omnivore) and [leaflet.shapefile](https://github.com/calvinmetcalf/leaflet.shapefile)/[shapefile-js](https://github.com/calvinmetcalf/shapefile-js), we are able to import CSV, GPX, shapefiles, and more. This is helpful for the fast prototyping needed to get something substantial finished over a weekend like this. We also used  [Font Awesome](http://fortawesome.github.io/Font-Awesome/) and [Leaflet.awesome-markers](https://github.com/lvoogdt/Leaflet.awesome-markers) to create impressive looking map markers rapidly.

This is what our map looked like at the end of day 1:

![Day 1 Progress]({filename}/images/codeacross-day1.png){.size-auto}

####Day 2

<blockquote class="twitter-tweet" lang="en"><p>We are in day two of <a href="https://twitter.com/hashtag/CodeAcross?src=hash">#CodeAcross</a> on the topic of reimagining South Downtown Atlanta. Can&#39;t wait to share the fruits of everyone&#39;s labor!</p>&mdash; Civic Innovation (@civicatlanta) <a href="https://twitter.com/civicatlanta/status/569567696242794497">February 22, 2015</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

On day 2, the research and data sub-group continued finding data sources, and sent many of them along to our mapping group. They also helped us out with some GIS work by taking some of the shapefiles they had found and cropping them down to our area of interest. Additionally, they provided domain expertise, helping us interpret the data and deciding with us which data fields should be shown in map popups.

In the coding sub-group, Jimmy completed the geocoder and used it on a few of the data sources. We added those to the map, as well as adding several other point layers that already had coordinate data. During the night, I had implemented queries of the  [Foursquare API](https://developer.foursquare.com/), so we spent some time on day 2 thinking of what kinds of venues we wanted to pull from Foursquare. We added government buildings, entertainment, residential buildings, and food from the Foursquare API. I also learned how to do image overlays, so we threw in a couple of maps the data group had gathered. Finally, we added in some shapefiles the data group had found. All-in-all, we had 14 map data layers at the end of day 2. When we presented our work, it seemed people were impressed by how much stuff is in South Downtown and at how quickly we were able to assemble and map so much of it.

![Day 2]({filename}/images/codeacross-day2.png){.size-auto}

I was equally impressed with the branding/storytelling and participatory groups. The branding and storytelling group thought up neighborhood slogans and set up a preliminary website to host information about South Downtown. The participatory group came up with a basic survey that can be filled out via text or web and thought up ways to advertise the survey and engage individuals with interactive street displays. I was greatly impressed by how much we got done in a weekend project. 

Even better yet, Code For Atlanta has structured a meetup so we can continue working on this project in the future. Usually when I do hackathons and other hack events, I'm disappointed by the project not continuing and often not getting to see my work get used. I'm really looking forward to meeting up once a month with the other hackers to continue our efforts.

And we certainly have plenty more to do. There's still much more data that the research team found that we haven't had a chance to implement in the map yet. There's also more data we haven't found yet, and data we haven't even begun to be sure how to measure (e.g. community). We also want to create separate maps for different audiences and integrate the map into the website.

I enjoyed helping to lead the asset mapping team, and I'm greatly looking forward to continuing to work on this project. I really care about South Downtown, and this weekend made me feel like I was helping the neighborhood, while also getting to do something I love with really great people. I highly recommend joining [Code for Atlanta](http://www.codeforatlanta.org/) (or [your local Code for America brigade](http://www.codeforamerica.org/brigade/)). As I think our mapping project showed, even if you aren't a coder, there are huge ways you can contribute. Thanks to my team and to the organizers of the event for making it the best hack weekend or hackathon I've attended!

The map will eventually be available at [southdowntown.org](http://southdowntown.org/), but for now you can find the code on [Github](https://github.com/codeforatlanta/asset-map).



