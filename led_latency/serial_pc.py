import serial
import time
from datetime import datetime


def write_to_device1():
	with serial.Serial("COM3", 115200, timeout=None) as ser:
		start = datetime.now()
		print('Writing to device 1 (time: ' + str(start) + ')')
		ser.write('on\n'.encode())
		
		return start

		#print('Device 1 response: ' + ser.readline().decode())


def read_from_device2(start):
	with serial.Serial("port of second device", 115200, timeout=None) as ser:
		print('Waiting for device 2')
		line = ser.readline().decode()
		#print(line)
		end = datetime.now()
		print('Device 2 response at time: ' + end)
		difference = end - start
		print('Latency: ' + difference)


def main():
	start = write_to_device1()
	read_from_device2(start)

if __name__ == '__main__':
	main()
