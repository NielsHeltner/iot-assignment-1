import pycom
import time
from machine import UART
import ltr329als01

uart = UART(0, 115200)
light_sensor = ltr329als01.LTR329ALS01()


def write(message):
    uart.write(str(message) + '\n')


def average(_tuple):
    return sum(value for value in _tuple) / len(_tuple)


def main():
    pycom.heartbeat(False)
    
    for i in range(10):
        light = light_sensor.light()
        light = average(light)
        write(light)
        time.sleep(1)


if __name__ == '__main__':
    main()

