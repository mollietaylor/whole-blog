Title: Date Formats in R
Date: 2013-08-22
Tags: as.Date, format, R, setup, Sys.Date
Category: R
Slug: 2013/08/date-formats-in-r.html
Author: Mollie Taylor
Summary: Dealing with date formats in R

##Importing Dates
Dates can be imported from character, numeric, POSIXlt, and POSIXct formats using the ```as.Date``` function from the **base** package.

If your data were exported from Excel, they will possibly be in numeric format. Otherwise, they will most likely be stored in character format.

###Importing Dates from Character Format
If your dates are stored as characters, you simply need to provide ```as.Date``` with your vector of dates and the format they are currently stored in. The possible date segment formats are listed in a table below. 

For example,

"05/27/84" is in the format %m/%d/%y, while "May 27 1984" is in the format %B %d %Y.

To import those dates, you would simply provide your dates and their format (if not specified, it tries %Y-%m-%d and then %Y/%m/%d):

	:::r
	dates <- c("05/27/84", "07/07/05")
	betterDates <- as.Date(dates,
		format = "%m/%d/%y")
	> betterDates
	[1] "1984-05-27" "2005-07-07"

This outputs the dates in the ISO 8601 international standard format %Y-%m-%d. If you would like to use dates in a different format, read "Changing Date Formats" below.

###Importing Dates from Numeric Format
If you are importing data from Excel, you may have dates that are in a numeric format. We can still use as.Date to import these, we simply need to know the origin date that Excel starts counting from, and provide that to as.Date.

For Excel on Windows, the origin date is December 30, 1899 for dates after 1900. (Excel's designer thought 1900 was a leap year, but it was not.) For Excel on Mac, the origin date is January 1, 1904.

	:::r
	# from Windows Excel:
		dates <- c(30829, 38540)
		betterDates <- as.Date(dates,
			origin = "1899-12-30")

	>   betterDates
	[1] "1984-05-27" "2005-07-07"

	# from Mac Excel:
		dates <- c(29367, 37078)
		betterDates <- as.Date(dates,
			origin = "1904-01-01")

	>   betterDates
	[1] "1984-05-27" "2005-07-07"

This outputs the dates in the ISO 8601 international standard format %Y-%m-%d. If you would like to use dates in a different format, read the next step:

##Changing Date Formats
If you would like to use dates in a format other than the standard %Y-%m-%d, you can do that using the ```format``` function from the **base** package.

For example,

	:::r
	format(betterDates,
		"%a %b %d")

	[1] "Sun May 27" "Thu Jul 07"

##Correct Centuries
If you are importing data with only two digits for the years, you will find that it assumes that years 69 to 99 are 1969-1999, while years 00 to 68 are 2000--2068 (subject to change in future versions of R).

Often, this is not what you intend to have happen. [This page](http://stackoverflow.com/questions/9508747/r-adding-century-to-year) gives a good explanation of several ways to fix this depending on your preference of centuries. One solution it provides is to assume all dates R is placing in the future are really from the previous century. That solution is as follows:

	:::r
	dates <- c("05/27/84", "07/07/05", "08/17/20")
	betterDates <- as.Date(dates, "%m/%d/%y")

	> betterDates
	[1] "1984-05-27" "2005-07-07" "2020-08-17"

	correctCentury <- as.Date(ifelse(betterDates > Sys.Date(), 
		format(betterDates, "19%y-%m-%d"), 
		format(betterDates)))

	> correctCentury
	[1] "1984-05-27" "2005-07-07" "1920-08-17"

##Purpose of Proper Formatting
Having your dates in the proper format allows R to know that they are dates, and as such knows what calculations it should and should not perform on them. For one example, see my [post on plotting weekly or monthly totals]({filename}blogger-r-weekly-totals.md). Here are a few more examples:

	:::r
	>   mean(betterDates)
	[1] "1994-12-16"

	>   max(betterDates)
	[1] "2005-07-07"

	>   min(betterDates)
	[1] "1984-05-27"

The code is available in a [gist](https://gist.github.com/mollietaylor/6258459).

##Date Formats
| Conversion specification | Description | Example |
| --- | --- | --- |
| %a | Abbreviated weekday | Sun, Thu |
| %A | Full weekday | Sunday, Thursday |
| %b or %h | Abbreviated month | May, Jul |
| %B | Full month | May, July |
| %d | Day of the month | 27, 07 |
| | 01-31 | |
| %j | Day of the year | 148, 188 |
| | 001-366 | |
| %m | Month | 05, 07 |
| | 01-12 | |
| %U | Week | 22, 27 |
| | 01-53 | |
| | with Sunday as first day of the week | |
| %w | Weekday | 0, 4 |
| | 0-6 | |
| | Sunday is 0 | |
| %W | Week | 21, 27 |
| | 00-53 | | 
| | with Monday as first day of the week | | 
| %x | Date, locale-specific |  |
| %y | Year without century | 84, 05 |
| | 00-99 | |
| %Y | Year with century | 1984, 2005 |
| | on input: | |
| | 00 to 68 prefixed by 20 | |
| | 69 to 99 prefixed by 19 | |
| %C | Century | 19, 20 |
| %D | Date formatted %m/%d/%y | 05/27/84, 07/07/05 |
| %u | Weekday | 7, 4 |
| | 1-7 | |
| | Monday is 1 | |
| %n | Newline on output or | |
| | Arbitrary whitespace on input |  |
| %t | Tab on output or | |
| | Arbitrary whitespace on input | |

##References
* help(as.Date)
* help(strptime)
* <http://stackoverflow.com/questions/9508747/r-adding-century-to-year>

