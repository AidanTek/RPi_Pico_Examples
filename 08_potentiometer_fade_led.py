# Potentiometer fade control

'''
Connect a potentiometer to GPIO26 (ADC0). The 'ears' of the pot should connect to 3V3 and ground
Connect an LED to GPIO15, use a 470ohm to connect the LED cathode to ground
For reference: https://datasheets.raspberrypi.org/pico/Pico-R3-A4-Pinout.pdf 
'''

from machine import ADC, PWM, Pin
import time

adc = ADC(Pin(26)) # create 'adc' object to handle the ADC input

pwm = PWM(Pin(15))

pwm.freq(10000)

while True:
    pwm.duty_u16(adc.read_u16()) # Set the PWM duty directly with the ADC reading
    
    time.sleep(0.1)