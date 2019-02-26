import pycom
import time
from machine import UART
import ltr329als01

uart = UART(0, 115200)
light_sensor = ltr329als01.LTR329ALS01()
light_difference_threshold = 10.0


def write(message):
    uart.write(str(message) + '\n')


def sense_light():
    return light_sensor.light()


def average(_tuple):
    return sum(value for value in _tuple) / len(_tuple)


def process_light(prev_light_value, light_value):
    if is_light_different(prev_light_value, light_value):
        write('light diff noticed')


def is_light_different(prev_light_value, light_value):
    if not prev_light_value:
        return False
    return abs(light_value - prev_light_value) > light_difference_threshold


def main():
    pycom.heartbeat(False)
    
    prev_light_value = None
    for i in range(10):
        light_value = sense_light()
        light_value = average(light_value)
        process_light(prev_light_value, light_value)

        prev_light_value = light_value
        time.sleep(1)


if __name__ == '__main__':
    main()
