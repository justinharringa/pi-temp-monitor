from w1thermsensor import W1ThermSensor
from datetime import datetime
import dateutil.tz

from formatter.csv_formatter import CsvFormatter
from model.temperature_reading import TemperatureReading
from sender.dynamodb_sender import DynamoDbSender

TEMP_READING_TABLE = 'temperature_readings'


def send_data(iso_formatted_date, sensor_id, temperature):
    formatter = CsvFormatter(iso_formatted_date, sensor_id, temperature)
    print(formatter.format())


for sensor in W1ThermSensor.get_available_sensors():
    sensor_id = sensor.id
    temperature = sensor.get_temperature()
    now_isoformat = datetime.now(dateutil.tz.tzlocal()).isoformat()
    send_data(now_isoformat, sensor_id, temperature)
    temp_reading = TemperatureReading(now_isoformat, sensor_id, temperature)
    sender = DynamoDbSender(TEMP_READING_TABLE)
    sender.send(temp_reading)
