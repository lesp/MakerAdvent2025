import network
from time import sleep
from secrets import *
from machine import Pin
import urequests as requests
#Get Online
wlan = network.WLAN()
wlan.active(True)
wlan.scan()
wlan.connect(SSID,PASS)
sleep(5)
wlan.isconnected()
print(wlan.ipconfig("addr4"))
#Setup Button
# Configure GPIO3 as input with internal pull-up
button = Pin(3, Pin.IN, Pin.PULL_UP)

while True:
    if button.value() == 0:   # Button pressed
        print("Button pressed")
        requests.post("https://ntfy.sh/bigles-doorbell",
                     data="Answer the door",
                     headers={
                         "Title": "Doorbell",
                         "Priority": "5",
                         "Tags": "bell",
                         })
        sleep(0.5)       # Simple debounce
    else:
        print("Button released")
    sleep(0.2)

