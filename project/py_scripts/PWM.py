from machine import Pin, ADC, PWM
from time import sleep

# Wait for USB to become ready
sleep(0.1)

# store desired output pin in a variable
led_pin = 25
led2_pin = 15
data_pin = 13
analog_data_pin = 26

# configure GPIO Pin as an output pin and create and led object for Pin class
led = PWM(Pin(led_pin))
led2 = PWM(Pin(led2_pin))

# set the PWM frequnecy for LED's
led.freq(1000)
led2.freq(1000)

# configure GPIO Pin as an input pin and create a data object for Pin class
data = Pin(data_pin, Pin.IN)

# configure GPIO Pin as an ADC pin and create a data object for ADC class that is a composition of the Pin class
analog_data = ADC(Pin(analog_data_pin))

while True:
    adc_value = analog_data.read_u16()  # 0-65535
    if data.value() == 1:
        led.duty_u16(adc_value)
        led2.duty_u16(adc_value)
    else:
        led.duty_u16(0)
        led2.duty_u16(0)
    print(f"Digital: {data.value()} , Analog: {adc_value}")
    sleep(0.1)
