from w1thermsensor import W1ThermSensor
from datetime import *
from dateutil.tz import *
import time

while True:
    for sensor in W1ThermSensor.get_available_sensors():
        sensor_id = sensor.id
        temperature = sensor.get_temperature()
        now_isoformat = datetime.now(tzlocal()).isoformat()
        with open('mytemps','a') as temperature_file:
            temperature_file.write('%s,%s,%.3f\n' % (now_isoformat, sensor_id, temperature))
    time.sleep(60)
