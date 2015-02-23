Title: Check if a Variable Exists in R
Date: 2013-12-05
Tags: any, attach, colnames, exists, in, names, R
Category: R
Slug: 2013/12/check-if-variable-exists-in-r
Author: Mollie Taylor
Summary: Check to see if a variable exists in R

If you use ```attach```, it is easy to tell if a variable exists. You can simply use ```exists``` to check:

	:::r
	>attach(df)

	>exists("varName")
	[1] TRUE

However, if you don't use ```attach``` (and I find you generally don't want to), this simple solution doesn't work.

	:::r
	> detach(df)
	> exists("df$varName")
	[1] FALSE

Instead of using ```exists```, you can use ```in``` or ```any``` from the **base** package to determine if a variable is defined in a data frame:

	:::r
	> "varName" %in% names(df)
	[1] TRUE
	> any(names(df) == "varName")
	[1] TRUE

Or to determine if a variable is defined in a matrix:

	:::r
	> "varName" %in% colnames(df)
	[1] TRUE
	> any(colnames(df) == "varName")
	[1] TRUE

##References
* <https://stat.ethz.ch/pipermail/r-help/2009-June/202178.html>
* <https://stat.ethz.ch/pipermail/r-help/2011-February/267518.html>
