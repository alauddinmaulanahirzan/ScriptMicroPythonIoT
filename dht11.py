from machine import Pin
from time import sleep
import dht
from utime import sleep_ms

sensor = dht.DHT11(Pin(5))
led = Pin(2,Pin.OUT)
led.value(0)

def blink():
    led.value(0)    
    sleep_ms(50)
    led.value(1)

while True:
  try:
    sleep(2)
    sensor.measure()
    temp = sensor.temperature()
    hum = sensor.humidity()
    if(temp > 24.0 or hum > 49.0):
        blink()
    print('Temperature: %3.1f C' %temp)
    print('Humidity: %3.1f %%' %hum)
    print("")
  except OSError as e:
    print('Failed to read sensor.')