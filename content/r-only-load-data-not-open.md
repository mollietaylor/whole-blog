Title: Only Load Data If Not Already Open in R
Date: 2013-09-12
Tags: exists, if, R, read.csv, read.table, Series: Large Data, setup
Category: R
Slug: 2013/09/only-load-data-if-not-already-open-in-r
Author: Mollie Taylor
Summary: I often find it beneficial to check to see whether or not a dataset is already loaded into R at the beginning of a file.

I often find it beneficial to check to see whether or not a dataset is already loaded into R at the beginning of a file. This is particularly helpful when I'm dealing with a large file that I don't want to load repeatedly, and when I might be using the same dataset with multiple R scripts or re-running the same script while making changes to the code.

To check to see if an object with that name is already loaded, we can use the ```exists``` function from the **base** package. We can then wrap our ```read.csv``` command with an ```if``` statement to cause the file to only load if an object with that name is not already loaded.

	:::r
	if(!exists("largeData")) {
		largeData <- read.csv("huge-file.csv",
			header = TRUE)
	}

You will probably also find it useful to use the "[colClasses]({filename}r-using-colclasses-speed.md)" option of ```read.csv``` or ```read.table``` to help the file load faster and make sure your data are in the right format. For example:

	:::r
	if(!exists("largeData")) {
		largeData <- read.csv("huge-file.csv",
			header = TRUE,
			colClasses = c("factor", "integer", "character", "integer", 
				"integer", "character"))
	}

> This post is one part of [my series on dealing with large datasets](http://blog.mollietaylor.com/tag/series-large-data.html).
