# SPDX-FileCopyrightText: 2021 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""
CircuitPython single MP3 playback example for Raspberry Pi Pico.
Plays a single MP3 once.
"""
import board
import digitalio
import audiomp3
import audiopwmio

switch = digitalio.DigitalInOut(board.GP15)
switch.direction = digitalio.Direction.INPUT
switch.pull = digitalio.Pull.UP
audio = audiopwmio.PWMAudioOut(board.GP18)

decoder = audiomp3.MP3Decoder(open("Christmas-low.mp3", "rb"))
while True:
    if switch.value == True:
        audio.play(decoder)
        while audio.playing:
            pass
    else:
        pass

print("Done playing!")
