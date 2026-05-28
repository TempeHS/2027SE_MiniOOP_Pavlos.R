from machine import Pin
from time import sleep


class Led_Light(Pin):
    def __init__(self, pin, flashing=False, debug=False):
        super().__init__(pin, Pin.OUT)
        self.__debug = debug
        self.__pin = pin
        self.__flashing = flashing
        self.led_light_state

    @property
    def led_light_state(self):
        return self.value()

    @led_light_state.setter
    def led_light_state(self, value):
        if value == 0:
            self.off()
        elif value == 1:
            self.on()

    def on(self):
        self.high()
        if self.__debug:
            print(f"LED connected to Pin {self.__pin} is high")

    def off(self):
        self.low()
        if self.__debug:
            print(f"LED connected to Pin {self.__pin} is low")

    def toggle(self):
        if self.value() == 0:
            self.on()

        elif self.value() == 1:
            self.off()


red_light = Led_Light(3, False, True)
green_light = Led_Light(6, False, True)

while True:
    print(red_light.led_light_state)
    red_light.led_light_state = 1
    sleep(1)
    print(red_light.led_light_state)
    red_light.led_light_state = 0
    sleep(1)
