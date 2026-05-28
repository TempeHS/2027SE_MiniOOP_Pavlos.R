from lib.led_light import Led_Light
from time import sleep

red_light = Led_Light(3, True, True)

while True:
    red_light.flash()
    print(1)
    sleep(0.1)
