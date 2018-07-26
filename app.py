import requests
import config
import time
import _thread
import sched

# Alarms and Timers can be handled differently, so we create two variables to keep track of it
sniffed_alarms = []
sniffed_timers = []


# simple function to send get request to google hoome and get alarm and timer
def get_info():
    try:
        resp = requests.get(config.google_home_url + "/setup/assistant/alarms")
        resp = resp.json()
        return resp
    except Exception as e:
        return e


# simple function that parses response from google home
def parse_response(info):

    # simple list to store the current state of google home mini
    alarms = []
    timers = []
    # parse through alarm and update list
    for item in info["alarm"]:
        fire_time = item["fire_time"]
        alarms.append(fire_time)
        # parse through timer and update list
    for item in info["timer"]:
        fire_time = item["fire_time"]
        timers.append(fire_time)
        # update the global variables that other function uses to trigger events
    global sniffed_alarms
    global sniffed_timers

    sniffed_alarms = alarms
    sniffed_timers = timers


# Runs the two above functions , this is the one we will call to have our global variable lists for sniffed_alarms and sniffed_timers updated
def update_alarms():
    # get response from google home device
    info = get_info()
    # if its normal response parse it
    if type(info) != Exception:
        parse_response(info)
        # if not let user know whats going on
    else:
        print("Exception Occured: ", str(e))


# This if the function that will call home assistant
def hass_trigger(trigger):
    if trigger == "alarm":
        print("Alarm event fired!")
        url = config.hass_alarm_url
        data = config.data_alarm
    else:
        print("Timer event fired!")
        url = config.hass_timer_url
        data = config.data_timer

    try:
        requests.post(url, json=data, headers={"Content-Type": "application/json"})
    except Exception as e:
        print(e)
    time.sleep(1.5)


# This is the function that will monitor the global variables and check if any alarm is about to fire with a 2 second accuracy, this can be tuned if needed
def monitor():
    global sniffed_alarms
    global sniffed_timersi

    while True:
        # get current time
        now = time.time() * 1000

        # check if alarm is almost triggered
        for item in sniffed_alarms:
            if item - now < 2000:
                hass_trigger("alarm")
                # check if timer is almost triggered
        for item in sniffed_timers:
            if item - now < 2000:
                hass_trigger("timer")
                # eat sleep and repat
        time.sleep(0.1)


# Initialize the thread that monitors the global lists and accordingly calls home assistant triggering timer or alarm events
_thread.start_new_thread(monitor, ())

# Initialize the function to update global variables
while True:
    update_alarms()
    print("Alarms: ", sniffed_alarms)
    print("Timers: ", sniffed_timers)
    time.sleep(2)
