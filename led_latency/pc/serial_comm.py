import serial
import time

file_location = 'data.txt'


def write_to_device1():
	with serial.Serial("COM3", 115200, timeout=None) as ser:
		start = time.time()
		print('Writing to device 1 (time: ' + str(start) + ')')
		ser.write('on\n'.encode())
		
		return start

		#print('Device 1 response: ' + ser.readline().decode())


def read_from_device2(start):
	with serial.Serial("port of second device", 115200, timeout=None) as ser:
		print('Waiting for device 2')
		light = ser.readline().decode().rstrip('\r\n')
		end = time.time()
		print(light)
		print('Device 2 response at time: ' + str(end))

		return end, light


def log_to_file(*args):
	text = '\t'.join(map(str, args))
	with open(file_location, 'w+') as data_file:
		data_file.write(text)


def main():
	start = write_to_device1()
	end, light = read_from_device2(start)

	difference = abs(start - end)

	log_to_file(start, end, difference, light)


if __name__ == '__main__':
	main()
