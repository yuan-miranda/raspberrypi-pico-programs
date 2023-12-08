# simple button interface for raspberry pi pico w.

import machine

# connect the button legs to GP2 and the other one to 3v3.
button = machine.Pin(2, machine.Pin.IN, machine.Pin.PULL_DOWN)

while True:
    # this will continuously print the output, use the debounced_button.py instead
    # to prevent the bouncing effect.
    if button.value():
        print("Button pressed")