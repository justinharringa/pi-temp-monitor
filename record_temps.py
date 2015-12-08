from w1thermsensor import W1ThermSensor
from datetime import *
from dateutil.tz import *

for sensor in W1ThermSensor.get_available_sensors():
    sensor_id = sensor.id
    temperature = sensor.get_temperature()
    now_isoformat = datetime.now(tzlocal()).isoformat()
    print('%s,%s,%.3f\n' % (now_isoformat, sensor_id, temperature))
