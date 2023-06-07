from hcsr04 import HCSR04
from time import sleep
from machine import Pin
from utime import sleep_ms

# ESP8266
sensor = HCSR04(trigger_pin=5, echo_pin=4, echo_timeout_us=10000)
led = Pin(2,Pin.OUT)
led.value(0)

def blink():
    led.value(0)    
    sleep_ms(50)
    led.value(1)

while True:
    distance = sensor.distance_cm()
    print('Distance:', distance, 'cm')
    if(distance<=20): 
       blink()
    sleep(1)