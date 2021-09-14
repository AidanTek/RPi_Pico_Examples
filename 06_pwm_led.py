from machine import Pin, PWM # PWM allows you to use commands to control a PWM channel on the pico
from time import sleep

'''
Connect an LED to GPIO15, use a 470ohm to connect the LED cathode to ground
For reference: https://datasheets.raspberrypi.org/pico/Pico-R3-A4-Pinout.pdf 
'''

pwm = PWM(Pin(15))

pwm.freq(10000) # set the PWM oscillator frequency

while True:
    for duty in range(65025): # this will loop 65025 times, counting from 0 up
        pwm.duty_u16(duty) # Set the duty cycle of the pwm oscillator 
        sleep(0.0001) # Sleep for 100 microseconds
    for duty in range(65025, 0, -1): # this will loop 65025 times, counting from 65025 down
        pwm.duty_u16(duty)
        sleep(0.0001)