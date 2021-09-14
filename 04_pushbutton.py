# Pushbutton 

'''
Connect an LED to GPIO15, use a 470ohm to connect the LED cathode to ground
Connect a toggle switch / push button to GPIO14 with the other side connected to ground
For reference: https://datasheets.raspberrypi.org/pico/Pico-R3-A4-Pinout.pdf 
'''

from machine import Pin
from time import sleep

led = Pin(15, Pin.OUT)
button = Pin(14, Pin.IN, Pin.PULL_UP) # Pin 14 is an input, with the internal pull-up active

while True:
    led.value(not button.value()) # LED is set directly with the state of the button
    print(button.value()) # The print command will output text to the REPL
    sleep(0.1) # short sleep to avoid overloading the REPL