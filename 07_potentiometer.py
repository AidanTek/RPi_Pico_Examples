# Potentiometer Analogue Input

'''
Connect a potentiometer to GPIO26 (ADC0). The 'ears' of the pot should connect to 3V3 and ground
For reference: https://datasheets.raspberrypi.org/pico/Pico-R3-A4-Pinout.pdf 
'''

from machine import ADC, Pin # ADC allows the use of the built in ADC
import time

adc = ADC(Pin(26)) # Set up 'adc' object to handle ADC input

while True:
    print(adc.read_u16()) # Print the reading from the ADC input
    time.sleep(0.1)