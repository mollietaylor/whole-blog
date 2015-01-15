Title: Truncate by Delimiter in R
Date: 2013-09-19
Tags: cleaning, R, regular expressions, Series: Text to Columns, setup, sub
Category: R
Slug: 2013/09/truncate-by-delimiter-in-r.html
Author: Mollie Taylor
Summary: Sometimes, you only need to analyze part of the data stored as a vector.

Sometimes, you only need to analyze part of the data stored as a vector. In this example, there is a list of patents. Each patent has been assigned to one or more patent classes. Let's say that we want to analyze the dataset based on only the first patent class listed for each patent.

	:::r
	patents <- data.frame(
		patent = 1:30,
		class = c("405", "33/209", "549/514", "110", "540", "43", 
		"315/327", "540", "536/514", "523/522", "315", 
		"138/248/285", "24", "365", "73/116/137", "73/200", 
		"252/508", "96/261", "327/318", "426/424/512", 
		"75/423", "430", "416", "536/423/530", "381/181", "4", 
		"340/187", "423/75", "360/392/G9B", "524/106/423"))

We can use [regular expressions](http://en.wikipedia.org/wiki/Regular_expression) to truncate each element of the vector just before the first "/".

```grep```,``` grepl```,``` sub```,``` gsub```,``` regexpr```,``` gregexpr```, and ```regexec``` are all functions in the **base** package that allow you to use regular expressions within each element of a character vector. ```sub``` and ```gsub``` allow you to replace within each element of the vector. ```sub``` replaces the first match within each element, while ```gsub``` replaces all matches within each element. In this case, we want to remove everything from the first "/" on, and we want to replace it with nothing. Here's how we can use ```sub``` to do that:

	:::r
	patents$primaryClass <- sub("/.*", "", patents$class)

	> table(patents$primaryClass)

	110 138  24 252 315 327  33 340 360 365 381   4 405 416 423 426  43 430 523 524 
	  1   1   1   1   2   1   1   1   1   1   1   1   1   1   1   1   1   1   1   1 
	536 540 549  73  75  96 
	  2   2   1   2   1   1 

> This post is one part of my series on Text to Columns.

##Citations and Further Reading
* [Regular Expressions Cheat Sheet](http://www.cheatography.com/davechild/cheat-sheets/regular-expressions/)