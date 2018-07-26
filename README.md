# Home Assistant Custom Actions for Google Home Alarms & Timers 


## Introduction 

In order to trigger automation based on alarms at home, I found that I was stuck to using tasker and my mobile phone, however this wasn't the method I wanted to use since my main alarm platform was the google home mini. After some digging around online I found that the google home has a local API that you can call from within the network to get its alarm and timer details, thus its possible to build a smarter system which can distinguish between timers and alarms and trigger different events on home assistant. (The program could be modified to trigger any API call)

More information on google home mini API: https://rithvikvibhu.github.io/GHLocalApi/

## What You Will Need 


Basically this script can be run on any system. Currently its just a simple python program so you could run it on your pi or any computer at home. This script will need to be running 24x7 so if you are running home assistant on a virtual python environment like me you can simply ssh in and run this script. 

## HASSIO 

I haven't come across any add-ons for this functionality and it should be pretty easy to port to hassio, if there is interest please let me know, I can work on porting this as an add-on. 

## Installaion

1) Most of the modules used are inbuilt into python3 , but you may need the requests library if not already installed, simply run ```pip3 install requests ```

2) Before we run this program, we will set up two different scripts on Home Assistant, one that is the action when timer is fired and the other one for the alarm. You can have a look at my attached scripts.yaml file and copy paste this configuartion which toggles the light once. I choose a different light for the timer and a different one for the alarm, however you can feel free to do anything, like maybe you want to trigger spotify to play when your alarm goes off. 

3) Once you have the scripts set-up go into the config.py file and set the ip address of your google home device followed by the port number, usually 8008. 

4) Now set up your home assistant urls for both the alarm and timer script and also any of the required data, in my case i did not need to provide any data since my scripts handle that. 

5) You are ready to go, simply fire the program by running ```python3 app.py ```, this should start running and print a your alarms and timers every few seconds. 

6) Now you can try talking to your google home and see your home get smarter and react to alarms and timers! 



