from machine import ADC
import time

sensor = ADC(0)
while True:
    result = sensor.read_u16()
    print(result)
    time.sleep(1)