# Simple button interface using Raspberry Pi Pico W Microcontroller
# Github: yuan-miranda

import machine # From MicroPython library
import time

#   GP2---[ button ]---3v3
# Note: 3v3 is used instead of GND so no external resistor is needed
button = machine.Pin(2, machine.Pin.IN, machine.Pin.PULL_DOWN)

while True:
    if button.value(): # returns 1(ON) when clicked
        print("Button pressed")
        time.sleep(1)  # 1 second click debounce