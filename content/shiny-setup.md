Title: How to Set Up Your App on Shiny Beta Hosting
Date: 2013-10-03
Tags: Linux, shiny, ssh, R
Category: R
Slug: 2013/10/how-to-set-up-your-app-on-shiny-beta
Author: Mollie Taylor
Summary: This is a short tutorial on how to create a web version of a Shiny app you've built once you've received access to the shiny hosting beta.

This is a short tutorial on how to create a web version of a [Shiny](http://www.rstudio.com/shiny/) app you've built once you've received [access to the shiny hosting beta](https://rstudio.wufoo.com/forms/shiny-server-beta-program/).

##SSH: Setting Up Directories
To connect to your account, input this line into a terminal (obviously input your own username instead of "username"):

	:::console
	ssh username@spark.rstudio.com

It will prompt you for your password. Enter the password you received in the email.

Next, create a folder to put your first app in. Like the email says, you want to put this at ```~/ShinyApps/myapp/```. The "myapp" folder can be named whatever you want, but the "ShinyApps" folder needs to have that name.

	:::console
	mkdir ShinyApps
	mkdir ShinyApps/myapp

##SSH: Installing R Packages
Next, you can go ahead and install R packages, if you know which ones your application will need.

First, open R just like you would on your own computer:

	:::console
	R

Next, install a package (e.g. "maps"):

	:::console
	install.packages("maps", dependencies = TRUE)

It will ask you the following questions:

	:::console
	Would you like to use a personal library instead?  (y/n)
	Would you like to create a personal library 
	~/R/library 
	to install packages into?  (y/n)

You can answer "y" to both of these. Your applications will be able to use packages installed here.

Then you can follow the standard procedure for installing R packages.

You can now quit R and exit ssh:

	:::console
	q()
	exit

##Copying Files
On your own computer, navigate to the directory your Shiny application's folder is in, e.g.:

	:::console
	cd Shiny

Once you're there, you can copy the application folder to the server:

	:::console
	scp -r myapp/ username@spark.rstudio.com:ShinyApps/

Or if you don't want to copy all the files, you can move them one at a time:

	:::console
	scp myapp/ui.R username@spark.rstudio.com:ShinyApps/myapp/ui.R

##Try It Out
Now you should be able to access your application at http://spark.rstudio.com/username/myapp/

You can now send it to all your friends or leave a link in the comments!