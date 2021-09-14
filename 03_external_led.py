# External LED

'''
Connect an LED to GPIO15, use a 470ohm to connect the LED cathode to ground
For reference: https://datasheets.raspberrypi.org/pico/Pico-R3-A4-Pinout.pdf 
'''

from machine import Pin
from time import sleep

led = Pin(15, Pin.OUT)

while True:
    led.toggle()
    sleep(1) # Sleep for 1 second