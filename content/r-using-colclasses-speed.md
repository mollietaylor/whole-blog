Title: Using colClasses to Load Data More Quickly in R
Date: 2013-09-05
Tags: colClasses, R, read.csv, read.table, Series: Large Data, setup, system.time
Category: R
Slug: 2013/09/using-colclasses-to-load-data-more
Author: Mollie Taylor
Summary: Specifying a colClasses argument to read.table or read.csv can save time on importing data, while also saving steps to specify classes for each variable later.

Specifying a ```colClasses``` argument to ```read.table``` or ```read.csv``` can save time on importing data, while also saving steps to specify classes for each variable later.

For example, loading a 893 MB took 441 seconds to load when not using ```colClasses```, but only 268 seconds to load when using ```colClasses```. The ```system.time``` function in **base** can help you check your own times.

Without specifying ```colClasses```:

	:::r
	   user  system elapsed 
	441.224   8.200 454.155 

When specifying ```colClasses```:

	:::r
	   user  system elapsed 
	268.036   6.096 284.099 

Dates that are in the [form %Y-%m-%d or Y/%m/%d]({filename}r-date-formats.md) will import correctly. [This tip allows you to import dates properly](http://stackoverflow.com/a/13022441) for dates in other formats.

	:::r
	system.time(largeData <- read.csv("huge-file.csv",
		header = TRUE,
		colClasses = c("character", "character", "complex", 
			"factor", "factor", "character", "integer", 
			"integer", "numeric", "character", "character",
			"Date", "integer", "logical")))

If there aren't any classes that you want to change from their defaults, you can read in the first few rows, [determine the classes from that](http://www.biostat.jhsph.edu/~rpeng/docs/R-large-tables.html), and then import the rest of the file:

	:::r
	sampleData <- read.csv("huge-file.csv", header = TRUE, nrows = 5)
	classes <- sapply(sampleData, class)
	largeData <- read.csv("huge-file.csv", header = TRUE, colClasses = classes)
	str(largeData)

If you aren't concerned about the time it takes to read the data file, but instead just want the classes to be correct on import, you have the option of only specifying certain classes:

	:::r
	smallData <- read.csv("small-file.csv", 
		header = TRUE,
		colClasses=c("variableName"="character"))

	> class(smallData$variableName)
	[1] "character"

> This post is one part of [my series on dealing with large datasets](http://blog.mollietaylor.com/tag/series-large-data.html).

##Citations and Further Reading
* <http://stackoverflow.com/questions/2805357/specifying-colclasses-in-the-read-csv>
* <http://www.biostat.jhsph.edu/~rpeng/docs/R-large-tables.html>
* [Date Formats in R]({filename}r-date-formats.md)
* <http://stackoverflow.com/a/13022441>

> In a [comment](http://mollietaylor.blogspot.com/2013/09/using-colclasses-to-load-data-more.html?showComment=1378560018132#c2964058082964060072), Michael pointed out that if you don't need all the columns in your dataset, providing their ```colClass``` as ```NULL``` will exclude them from being loaded.

