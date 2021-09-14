# Internal LED example

# The machine module includes the hardware commands for the Pico
from machine import Pin 

# 'led' is a new object, it is setup to control the LED on GPIO25
led = Pin(25, Pin.OUT) 

# Try typing led.value(1) and led.value(0) in the REPL to turn the LED on and off
# Try typing led.toggle()

