Pi-Switch
=========

Access Raspberry Pi GPIO pins from a Django WebPage
------------------------------------------------------

**NOTE:** to use this project you need to have a Raspberry Pi set up that can host a django project.

I followed "http://blog.mattwoodward.com/2013/01/setting-up-django-on-raspberry-pi.html" on how to set up the raspberry pi as a django server. 

Following Mike Hibberts YouTube series using python2.7 is where I learned the ins and outs of django (http://www.youtube.com/watch?v=oT1A1KKf0SI).
From following the tutorials I started making a blog first that is why the one file is named article.

After I was comfortable with django I switched up the models and some other things like ajax and jquery to fit my needs. I added twitter bootstrap as the final touch to beautify my project. 

**NOTE:** Make sure before using the runserver command you edit the settings.py and update any file paths etc. Also I deleted my sqlite database for the time being so you will need to create your own

**NOTE:** to make the python scripts run using subprocesses you need to edit the sudoers page so the command sudo /usr/bin/python"YourVersionHere" can be called and you will not be prompted for a password. 

An example of what the end of my sudoers page looks like is 

> \#includedir /etc/sudoers.d
>
>pi ALL=(ALL) NOPASSWD: /usr/bin/python2.7

This way it asks for my password every time except for when I call /usr/bin/python2.7
