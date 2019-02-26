import pycom


def on():
    pycom.rgbled(0x007f00) #green


def off():
    pycom.rgbled(0x000000)

