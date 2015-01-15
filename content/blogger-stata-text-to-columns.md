Title: Text to Columns in Stata
Date: 2012-09-06
Tags: cleaning, setup, split, Stata
Category: 
Slug: 2012/09/text-to-columns-in-stata.html
Author: Mollie Taylor
Summary: Take one column of data and separate it into multiple columns using delimiters

If you've ever used Excel's text to columns feature, you know how valuable it can be. If you haven't ever used text to columns, it allows you to take one column of data and separate it into multiple columns using delimiters that you provide. One time this is helpful is when converting data from other formats.

If you're learning Stata, you may wonder how you can gain this useful functionality. There are a few different ways, but for now we'll be discussing ```split```.

For the following example, I have imported some patent data where the four most relevant primary patent classes for each observation are listed in a single column. These are delimited by a "/" as can be seen below.

![Data before transformation]({filename}images/stata-before.png)

I would like each of these classes to be included in its own column. To do this, I give Stata the following command:

```split class, parse(/) generate(class)```

![Stata command and feedback]({filename}images/stata-command-line.png)

In this command, the first ```class``` is the name of the variable I want to transform, ```/``` is the delimiter, and ```generate(class)``` lets Stata to know that I would like the names of the new variables to each be class followed by an integer. In the example, the most ```/```'s there were in ```class``` was two, so three ```class[n]``` variables are created.

![Data after transformation]({filename}images/stata-after.png)

I can then ```drop class``` if I want to remove the original class variable.

I could have also used the option ```destring``` if I wanted to treat the patent classes as numbers.

![Stata documentation excerpt]({filename}images/stata-docs.png)

More use cases are shown in the [split documentation](http://www.stata.com/help.cgi?split). One example they provide allows you to use multiple delimiters. In this instance showing how to separate the names of court cases even if some are delimited by "v." and some by "vs."

For more complex situations, you can also use [regular expressions](http://www.ats.ucla.edu/stat/Stata/faq/regex.htm).