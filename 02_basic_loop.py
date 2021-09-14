# Basic program loop Example

from machine import Pin
# The time module has commands that allow you to add timing features to your program
from time import sleep

led = Pin(25, Pin.OUT)

while True:
    led.toggle()
    sleep(1) # Sleep for 1 second
