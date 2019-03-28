import pycom
import time
import ltr329als01

light_sensor = LTR329ALS01(integration = LTR329ALS01.ALS_INT_50, rate = LTR329ALS01.ALS_RATE_50)
light_difference_threshold = 10.0


def sense_light():
    return light_sensor.light()


def average(data_structure):
    return sum(value for value in data_structure) / len(data_structure)


def process_light(prev_light_value, light_value):
    if is_light_different(prev_light_value, light_value):
        print(light_value)


def is_light_different(prev_light_value, light_value):
    if not prev_light_value:
        return False
    return abs(light_value - prev_light_value) > light_difference_threshold


def main():
    pycom.heartbeat(False)
    
    prev_light_value = None
    try:
        for i in range(100000):
            light_value = sense_light()
            light_value = average(light_value)
            process_light(prev_light_value, light_value)

            prev_light_value = light_value
    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    main()
