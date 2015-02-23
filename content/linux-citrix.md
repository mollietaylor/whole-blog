Title: Get Citrix XenDesktop to Work on Linux
Date: 2013-02-07
Tags: Citrix, Linux, ubuntu, XenDesktop
Category: 
Slug: 2013/02/get-citrix-xendesktop-to-work-on-linux
Author: Mollie Taylor
Summary: I had some difficulty figuring out how to get Citrix XenDesktop to work properly on Linux.

I had some difficulty figuring out how to get Citrix XenDesktop to work properly on Linux.

I was having the same problem I had had on Windows — when I would try to access XenDesktop, the browser would try to download launch.ica instead of running it.

##Citrix Receiver
However, on other operating systems, I had always downloaded the Citrix Online Plug-in to fix the problem. For some reason, the Citrix Online Plug-in is not available for Linux. However, the [Citrix Receiver](http://receiver.citrix.com/?ntref=receiverdownload) is available for Linux, and seems to do the same thing.

After installing Citrix Receiver, your browser will ask for your permission to run it.

![Permission]({filename}/images/citrix-permission.png){.size-auto}

##Open Motif
You may need to install Open Motif before you can install Citrix Receiver.

If so, download Open Motif, extract it, and follow the directions in INSTALL.configure, namely:

	:::console
	cd
	./configure
	make check
	make install
	make clean

##Security Certificate

![Error]({filename}/images/citrix-error.png){.size-auto}

If you try to log on to your virtual desktop and get an error about "AddTrust External CA Root", you can just do

	:::console
	sudo cp /usr/share/ca-certificates/mozilla/*.* /opt/Citrix/ICAClient/keystore/cacerts/



##References
* <http://www.jorink.nl/2010/11/you-have-not-chosen-to-trust-addtrust-external-ca-root-the-issuer-of-the-servers-security-certificate/>