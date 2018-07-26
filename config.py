
# The internal ip address of your google home device
google_home_url = "http://192.168.1.122:8008"

# The URL you want to call to fire hass ALARM script
hass_alarm_url = (
    "https://hass.duckdns.org/api/services/script/alarm_blink?api_password=mypassword"
)
# any data you wish to pass through
data_alarm = {}

# The URL you want to call to fire hass ALARM script
hass_timer_url = (
    "https://hass.duckdns.org/api/services/script/timer_blink?api_password=mypassword"
)
# any data you wish to pass through
data_timer = {}
