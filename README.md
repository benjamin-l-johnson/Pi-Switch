Pi-Switch
=========

Access Raspberry Pi GPIO pins from a Django WebPage
------------------------------------------------------

**NOTE:** to use this project you need to have a Raspberry Pi set up that can host a django project.

I followed "http://blog.mattwoodward.com/2013/01/setting-up-django-on-raspberry-pi.html" on how to set up the raspberry pi as a django server. 

Following Mike Hibberts YouTube series using python2.7 is where I learned the ins and outs of django (http://www.youtube.com/watch?v=oT1A1KKf0SI).


After I was comfortable with django I switched up the models and some other things like ajax and jquery to fit my needs. I added twitter bootstrap as the final touch to beautify my project. 

**NOTE:** Make sure before using the runserver command you edit the settings.py and update any file paths etc. Also I deleted my sqlite database for the time being so you will need to create your own

**NOTE:** Although you do need root access to turn the pins on and off, you DO NOT need to set it up so python can be called as root (which is a huge security risk and what I had before). A better and more secure way to do this would be to make a simple bash script that had permissions for execute only and append the sudoers file that way. So my sudoers page now looks like this. 
```
#includedir /etc/sudoers.d

pi ALL=(ALL) NOPASSWD:/home/pi/on.sh,/home/pi/off.sh
```

This simply means that sudo /home/pi/on.sh and sudo /home/pi/off.sh will not prompt you for a password when you execute those commands.
Now you would create the scripts on.sh, off.sh (they can be found in this projects root directory so I will not go over how to create them)
Next we need to change file permissions on the two scripts we just created.(and since we are here we might as well get the python scripts also). From the terminal type

```
sudo chown root off.sh on.sh lightOn.py lightOff.py
```
This is to change ownership of the files to root.

Now type in the terminal  
```
sudo chmod 710 off.sh on.sh lightOn.py lightOff.py
```
This makes the scripts readable, writable, and executable for the root user, and ONLY executable for users in the that group (the sudoers group I believe). 


Some commands I find useful to start the site up, since I don't always have this site up and running.
```
sudo service nginx start
sudo service supervisor start

# or if you want to debug
python manage.py run_gunicorn
```
