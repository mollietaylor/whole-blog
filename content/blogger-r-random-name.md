Title: Random Name Generator in R
Date: 2012-10-11
Tags: anyDuplicated, cat, duplicated, length, R, sample, sort
Category: R
Slug: 2012/10/random-name-generator-in-r.html
Author: Mollie Taylor
Summary: Just for the heck of it, let's recreate my Reality TV Show Name Generator in R.

Just for the heck of it, let's recreate my [Reality TV Show Name Generator](http://realitytvgenerator.com/) in R. This isn't really the sort of thing you'd normally do in R, but we can try out a bunch of different functions this way: random integers/sampling, concatenation, sorting, and determining the length of an object.

First, let's create a dictionary for R to randomly pull names from. In this case, we want a first word and a last word, that we'll later combine to create a name similar to so many current TV shows. (Note: In some cases, I've made the first "word" or last "word" multiple words for some variety.) Feel free to make your own lists.

	:::r
	first <- c("Fear", "Frontier", "Nanny", "Job", "Yard", "Airport", "Half Pint", "Commando", "Fast Food", "Basketball", "Bachelorette", "Diva", "Baggage", "College", "Octane", "Clean", "Sister", "Army", "Drama", "Backyard", "Pirate", "Shark", "Project", "Model", "Survival", "Justice", "Mom", "New York", "Jersey", "Ax", "Warrior", "Ancient", "Pawn", "Throttle", "The Great American", "Knight", "American", "Outback", "Celebrity", "Air", "Restaurant", "Bachelor", "Family", "Royal", "Surf", "Ulitmate", "Date", "Operation", "Fish Tank", "Logging", "Hollywood", "Amateur", "Craft", "Mystery", "Intervention", "Dog", "Human", "Rock", "Ice Road", "Shipping", "Modern", "Crocodile", "Farm", "Amish", "Single", "Tool", "Boot Camp", "Pioneer", "Kid", "Action", "Bounty", "Paradise", "Mega", "Love", "Style", "Teen", "Pop", "Wedding", "An American", "Treasure", "Myth", "Empire", "Motorway", "Room", "Casino", "Comedy", "Undercover", "Millionaire", "Chopper", "Space", "Cajun", "Hot Rod", "The", "Colonial", "Dance", "Flying", "Sorority", "Mountain", "Auction", "Extreme", "Whale", "Storage", "Cake", "Turf", "UFO", "The Real", "Wild", "Duck", "Queer", "Voice", "Fame", "Music", "Rock Star", "BBQ", "Spouse", "Wife", "Road", "Star", "Renovation", "Comic", "Chef", "Band", "House", "Sweet")

	second <- c("Hunters", "Hoarders", "Contest", "Party", "Stars", "Truckers", "Camp", "Dance Crew", "Casting Call", "Inventor", "Search", "Pitmasters", "Blitz", "Marvels", "Wedding", "Crew", "Men", "Project", "Intervention", "Celebrities", "Treasure", "Master", "Days", "Wishes", "Sweets", "Haul", "Hour", "Mania", "Warrior", "Wrangler", "Restoration", "Factor", "Hot Rod", "of Love", "Inventors", "Kitchen", "Casino", "Queens", "Academy", "Superhero", "Battles", "Behavior", "Rules", "Justice", "Date", "Discoveries", "Club", "Brother", "Showdown", "Disasters", "Attack", "Contender", "People", "Raiders", "Story", "Patrol", "House", "Gypsies", "Challenge", "School", "Aliens", "Towers", "Brawlers", "Garage", "Whisperer", "Supermodel", "Boss", "Secrets", "Apprentice", "Icon", "House Party", "Pickers", "Crashers", "Nation", "Files", "Office", "Wars", "Rescue", "VIP", "Fighter", "Job", "Experiment", "Girls", "Quest", "Eats", "Moms", "Idol", "Consignment", "Life", "Dynasty", "Diners", "Chef", "Makeover", "Ninja", "Show", "Ladies", "Dancing", "Greenlight", "Mates", "Wives", "Jail", "Model", "Ship", "Family", "Videos", "Repo", "Rivals", "Room", "Dad", "Star", "Exes", "Island", "Next Door", "Missions", "Kings", "Loser", "Shore", "Assistant", "Comedians", "Rooms", "Boys")

Whew, that was long. Instead, let's look at a random sample of those.

We can make random lists using ```sample```. Sample wants you to provide it with a vector, the sample size you want, and whether or not it should reuse items from the vector. In this case, we don't want any duplicates, so we add ```replace = FALSE```.

	:::r
	first <- sample(first,
		10,	replace = FALSE)

	second <- sample(second,
		12,
		replace = FALSE)

This gives us something more like

	:::r
	> first
	 [1] "Teen"       "Fame"       "Basketball" "Sister"     "Bachelor" 
	 [6] "Half Pint"  "Myth"       "Paradise"   "Frontier"   "Fast Food"
	> second
	 [1] "Comedians"    "Boss"         "Experiment"   "Wives"        "Wedding"    
	 [6] "Intervention" "Days"         "Raiders"      "Attack"       "Sweets"     
	[11] "Jail"         "Whisperer"

It's random, so your list will probably be different.

If you want to ```sort``` them alphabetically, use

	:::r
	first <- sort(first)

If we had wanted to randomly resort the whole "first" list, we could have entered the command

	:::r
	first <- sample(first, length(first), replace = FALSE)

Using ```length``` makes it easy to resort the whole list. You don't have to look up how many items there are in ```first```.

Let's use ```length``` again to choose a random number that we'll use to grab a number from the ```first``` list, and then again to choose a random number that we'll use to grab a number from the ```second``` list:

	:::r
	rand1 <- sample(1:length(first), 1)
	rand2 <- sample(1:length(second), 1)

And finally, we want to pull an item from each list and con```cat```enate them. We could concatenate to a file, but here we'll just let it print to the console.

	:::r
	cat(first[rand1], second[rand2], "\n")

"```\n```" produces a line break so we can do ```source(reality.R)``` again and have another name pop up on the next line.

If you've made a dictionary of your own and want to check for duplicates, you can do the following:

	:::r
	anyDuplicated(first) # if not 0, there are that many duplicates
	duplicated(first) # this will show which items are duplicates

Feel free to improve on my dictionary or generator. I'd love to see it.

Code available as a [gist](https://gist.github.com/3837835).
