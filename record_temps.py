from w1thermsensor import W1ThermSensor
import time

while True:
    for sensor in W1ThermSensor.get_available_sensors():
        f = open('mytemps','a')
        f.write('%s:%.2f\n' % (sensor.id, sensor.get_temperature()))
        f.close()
    time.sleep(60)
