# simple debounced button interface for raspberry pi pico w.

import machine
import time

# connect the button legs to GP2 and the other one to 3v3.
button = machine.Pin(2, machine.Pin.IN, machine.Pin.PULL_DOWN)
button_pressed = False

while True:
    # while the button state is on, the button is pressed.
    if button.value():
        if not button_pressed:
            print("Button pressed")
            button_pressed = True
    else:
        button_pressed = False

    time.sleep(0.1)