Title: Word Clouds in R
Date: 2012-09-13
Tags: R, visualization, wordcloud
Category: R
Slug: 2012/09/word-clouds-in-r
Author: Mollie Taylor
Summary: Thanks to the wordcloud package, it's super easy to make a word cloud or tag cloud in R.

Thanks to the **wordcloud** package, it's super easy to make a word cloud or tag cloud in R.

In this case, the words have been counted already. If you are starting with plain text, you can use the text mining package **tm** to obtain the counts. [Other bloggers](http://onertipaday.blogspot.com/2011/07/word-cloud-in-r.html) have provided good examples of this. I'll just be covering the simple case where we already have the frequencies.

Let's look at some commonly used words during the National Conventions this year. [The New York Times produced a cool infographic](http://www.nytimes.com/interactive/2012/09/06/us/politics/convention-word-counts.html) that we'll use as our data source. The data in csv format (and the R code too) are available in a [gist](https://gist.github.com/3671518).

First we need to load up the packages and our data:

	:::r
	library(wordcloud)
	library(RColorBrewer)

	conventions <- read.table("conventions.csv",
		header = TRUE,
		sep = ",")

And then we can get to using the **wordcloud** library to produce our clouds in R:

	:::r
png("dnc.png")
	wordcloud(conventions$wordper25k, # words
		conventions$democrats, # frequencies
		scale = c(4,1), # size of largest and smallest words
		colors = brewer.pal(9,"Blues"), # number of colors, palette
		rot.per = 0) # proportion of words to rotate 90 degrees
	dev.off()

	png("rnc.png")
	wordcloud(conventions$wordper25k,
		conventions$republicans,
		scale = c(4,1),
		colors = brewer.pal(9,"Reds"),
		rot.per = 0)
	dev.off()

![DNC word cloud]({filename}images/r-word-cloud-dnc.png)

![RNC word cloud]({filename}images/r-word-cloud-rnc.png)

The default word cloud has some words rotated 90 degrees, but I prefer to use rot.per = 0 to make them all horizontal for readability.

You can easily change to just one color if you prefer that since the size already denotes the frequency of the word, by changing color to "red3", for example:

![RNC single color]({filename}images/r-word-cloud-rnc-alt.png)

	:::r
	png("rncalt.png")
	wordcloud(conventions$wordper25k,
		conventions$republicans,
		scale = c(4,1),
		colors = "red3",
		rot.per = 0)
	dev.off()

![DNC single color]({filename}images/r-word-cloud-dnc-alt.png)

And there you have it, a simple way to generate a word count from frequency data using R.