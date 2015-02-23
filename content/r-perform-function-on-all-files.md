Title: Perform a Function on Each File in R
Date: 2013-09-26
Tags: analysis, data.frame, for, paste, R, sub, Sys.glob, write.table
Category: R
Slug: 2013/09/perform-function-on-each-file-in-r
Author: Mollie Taylor
Summary: Sometimes you might have several data files and want to use R to perform the same function across all of them. Or maybe you have multiple files and want to systematically combine them into one file without having to open each file and manually copy the data out.

Sometimes you might have several data files and want to use R to perform the same function across all of them. Or maybe you have multiple files and want to systematically combine them into one file without having to open each file and manually copy the data out.

Fortunately, it's not complicated to use R to systematically iterate across files.
##Finding or Choosing the Names of Data Files
There are multiple ways to find or choose the names of the files you want to analyze.

You can explicitly state the file names or you can get R to find any files with a particular extension.
###Explicitly Stating File Names

	:::r
	fileNames <- c("sample1.csv", "sample2.csv")

###Finding Files with a Specific Extension
In this case, we use ```Sys.glob``` from the **base** package to find all files including the wildcard "*.csv".

	:::r
	fileNames <- Sys.glob("*.csv")

##Iterating Across All Files
We'll start with a loop and then we can add whatever functions we want to the inside of the loop:

	:::r
	for (fileName in fileNames) {

		# read data:
		sample <- read.csv(fileName,
			header = TRUE,
			sep = ",")

		# add more stuff here

	}

For example, we could add one to every "Widget" value in each file and overwrite the old data with the new data:

	:::r
	for (fileName in fileNames) {

		# read old data:
		sample <- read.csv(fileName,
			header = TRUE,
			sep = ",")

		# add one to every widget value in every file:
		sample$Widgets <- sample$Widgets + 1
		
		# overwrite old data with new data:
		write.table(sample, 
			fileName,
			append = FALSE,
			quote = FALSE,
			sep = ",",
			row.names = FALSE,
			col.names = TRUE)

	}

Or we could do the same thing, but create a new copy of each file:

	:::r
	extension <- "csv"

	fileNames <- Sys.glob(paste("*.", extension, sep = ""))

	fileNumbers <- seq(fileNames)

	for (fileNumber in fileNumbers) {

		newFileName <-  paste("new-", 
			sub(paste("\\.", extension, sep = ""), "", fileNames[fileNumber]), 
			".", extension, sep = "")

		# read old data:
		sample <- read.csv(fileNames[fileNumber],
			header = TRUE,
			sep = ",")

		# add one to every widget value in every file:
		sample$Widgets <- sample$Widgets + 1
		
		# write old data to new files:
		write.table(sample, 
			newFileName,
			append = FALSE,
			quote = FALSE,
			sep = ",",
			row.names = FALSE,
			col.names = TRUE)

	}

In the above example, we used the ```paste``` and ```sub``` functions from the **base** package to automatically create new file names based on the old file names.

Or we could instead use each dataset to create an entirely new dataset, where each row is based on data from one file:

	:::r
	fileNames <- Sys.glob("*.csv")

	for (fileName in fileNames) {

		# read original data:
		sample <- read.csv(fileName,
			header = TRUE,
			sep = ",")

		# create new data based on contents of original file:
		allWidgets <- data.frame(
			File = fileName,
			Widgets = sum(sample$Widgets))
		
		# write new data to separate file:
		write.table(allWidgets, 
			"Output/sample-allSamples.csv",
			append = TRUE,
			sep = ",",
			row.names = FALSE,
			col.names = FALSE)

	}

In the above example, ```data.frame``` is used to create a new data row based on each data file. Then the append option of ```write.table``` is set to ```TRUE``` so that row can be added to the other rows created from other data files.

Those are just a few examples of how you can use R to perform the same function(s) on a large number of files without having to manually run each one. I'm sure you can think of more uses.

All the files are available [on GitHub](https://github.com/mollietaylor/iterate-across-files). You can see how eachFile.R, eachfile-newNames.R, and eachFile-append.R each do something different to the sample datasets.

> [An anonymous commenter pointed out](http://mollietaylor.blogspot.com/2013/09/perform-function-on-each-file-in-r.html?showComment=1380279750603#c4308191719639677502) that for big data files, he/she often uses:
	:::r
	setwd("my_working_directory_path")
	dat <- lapply(dir(pattern=".csv"), function(file) {
	dat.i <- read.csv(file)
	# ... data formating, subsetting, ... 
	return(dat.i)
	} 
	dat <- do.call("rbind", dat)
I haven't tested it, but it is likely this is more efficient than using ```for``` loops in R.
