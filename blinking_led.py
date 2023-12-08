# simple blinking led for raspberry pi pico w.

import machine
import time

# use the built-in LED.
led = machine.Pin("LED", machine.Pin.OUT)

while True:
    led.value(1) # turn on
    time.sleep(1)
    
    led.value(0) # turn off
    time.sleep(1)
