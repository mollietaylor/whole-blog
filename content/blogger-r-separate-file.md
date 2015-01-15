Title: Storing a Function in a Separate File in R
Date: 2013-01-24
Tags: dget, function, R, source
Category: R
Slug: 2013/01/storing-function-in-separate-file-in-r.html
Author: Mollie Taylor
Summary: If you're going to be using a function across several different R files, you might want to store the function in its own file.

If you're going to be using a function across several different R files, you might want to store the function in its own file.

###If you want to name the function in its own file

This is probably the best option in general, if only because you may want to put more than one function in a single file.

Next, let's make our function in the file ```fun.R```:
	:::r
	mult <- function(x, y) {
	    x*y
	}

If you get the warning message "In readLines(file) : incomplete final line found on 'fun.R'", just insert a line break at the end of the fun.R file.

###If you want to name the function in the file running it

First let's make the same function (but this time unnamed) in the file times.R:
	
	:::r
	function(x, y) {
		x*y
	}

###Calling the functions

And finally we'll make a file file.R to call our functions:

	:::r
	times <- dget("times.R")
	times(-4:4, 2)

	source("fun.R")
	mult(-4:4, 2)


Note: if you are used to using source to run your R code, note that in this case we are using the ```source``` command *within* a file.


All files are available as a [gist](https://gist.github.com/4472146).