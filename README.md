# MakerAdvent2025
All of the code for the days of MakerAdvent 2025

## Day 14 ESP32 C3 Super Mini IoT Doorbell
Building on the introduction of the £6 trio of ESP32 C3s, day 14 puts one of them to use as an Internet connected doorbell. Using MicroPython and [ntfy.sh](http://ntfy.sh) we build a simple button circuit and use that to trigger a notifications via ntfy.

The circuit looks like this
![Image of the circuit made in Fritzing](https://raw.githubusercontent.com/lesp/MakerAdvent2025/refs/heads/main/Day%2014%20-%20ESP32%20C3%20Super%20Mini%20IoT%20Doorbell/esp32c3-doorbell.jpg)

And these should be the only files in the root filesystem of your ESP32
![Image of the ESP32 filesystem shoiwng three files, boot.py, doorbell.py and secrets.py](https://raw.githubusercontent.com/lesp/MakerAdvent2025/refs/heads/main/Day%2014%20-%20ESP32%20C3%20Super%20Mini%20IoT%20Doorbell/ESP32%20Files.jpg)