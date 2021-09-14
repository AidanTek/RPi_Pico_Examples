# Pushbutton toggle

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

lastswitch = 0 # variable storage for button transition 

while True:
    switch = button.value() # store the current value of the button
    
    if switch != lastswitch:
        # If the button state has changed:
        lastswitch = switch # Update the transition
        
        if switch == 0:
            led.toggle() # Only change the LED state when the switch is pressed
        
        sleep(0.1) # Small sleep to prevent button 'bounce'
    
    