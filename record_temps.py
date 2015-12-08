from w1thermsensor import W1ThermSensor

for sensor in W1ThermSensor.get_available_sensors():
    f = open('mytemps','w')
    f.write('%s:%.2f\n' % (sensor.id, sensor.get_temperature()))
    f.close()
