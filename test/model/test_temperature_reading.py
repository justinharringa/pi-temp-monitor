import unittest

from decimal import Decimal

from model.temperature_reading import TemperatureReading


class TemperatureReadingTestCase(unittest.TestCase):
    def test_temperature_short_reading(self):
        date = '2015-12-13T11:00:00.000-3:00'
        sensor_id = '8675309'
        temperature = Decimal(str(0.000))
        reading = TemperatureReading(date, sensor_id, temperature)
        expected_format = {TemperatureReading.DATE: date,
                           TemperatureReading.SENSOR_ID: sensor_id,
                           TemperatureReading.TEMPERATURE: temperature}
        self.assertEqual(expected_format, reading.get_dict())

    def test_temperature_long_reading(self):
        date = '2015-12-13T11:00:00.000-3:00'
        sensor_id = '8675309'
        temperature = Decimal(str(9.999))
        reading = TemperatureReading(date, sensor_id, temperature)
        expected_format = {TemperatureReading.DATE: date,
                           TemperatureReading.SENSOR_ID: sensor_id,
                           TemperatureReading.TEMPERATURE: temperature}
        self.assertEqual(expected_format, reading.get_dict())
