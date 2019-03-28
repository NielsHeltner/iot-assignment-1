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
        print('Command \'' + command + '\' dispatched')
    except KeyError:
        print('Command \'' + command + '\' not recognized')


def main():
    pycom.heartbeat(False)

    try:
        for i in range(100000):
            line = input()
            dispatch(line)
    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    main()
