import pycom
import time


def on():
    pycom.rgbled(0x007f00) #green


def off():
    pycom.rgbled(0x000000)


commands = {
    'on': on, 
    'off': off
}


def dispatch(command):
    try:
        commands[command]()
    except KeyError:
        print('Command \'' + command + '\' not recognized')


def main():
    pycom.heartbeat(False)

    for i in range(10):
        line = input()
        print('pycom read ' + line)
        dispatch(line)


if __name__ == '__main__':
    main()
