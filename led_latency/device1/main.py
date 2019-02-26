import pycom
import led_controller
import time
from machine import UART

uart = UART(0, 115200)
commands = {
    'on': led_controller.on, 
    'off': led_controller.off
}


def dispatch(command):
    try:
        commands[command]()
    except KeyError:
        print('Command \'' + command + '\' not recognized')


def read():
    return uart.readline().decode().rstrip('\r\n')


def main():
    pycom.heartbeat(False)

    for i in range(10):
        if uart.any() > 0:
            line = read()
            print('pycom read ' + line)
            dispatch(line)
        else:
            print('pycom nothing to read')
        time.sleep(1)


if __name__ == '__main__':
    main()

