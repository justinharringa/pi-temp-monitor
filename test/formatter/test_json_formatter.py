import unittest

from formatter.json_formatter import JsonFormatter


class JsonFormatterTestCase(unittest.TestCase):
    def test_json_format_short_temp(self):
        date = '2015-12-13T11:00:00.000-3:00'
        sensor_id = '8675309'
        temperature = 0.000
        formatter = JsonFormatter(date, sensor_id, temperature)
        expected_format = '{"%s": "%s", "%s": "%s", "%s": %.1f}' % \
                          (JsonFormatter.DATE, date,
                           JsonFormatter.SENSOR_ID, sensor_id,
                           JsonFormatter.TEMPERATURE, temperature)
        self.assertEqual(expected_format, formatter.format(sort_keys=True))

    def test_json_format_long_temp(self):
        date = '2015-12-13T11:00:00.000-3:00'
        sensor_id = '8675309'
        temperature = 9.999
        formatter = JsonFormatter(date, sensor_id, temperature)
        expected_format = '{"%s": "%s", "%s": "%s", "%s": %.3f}' % \
                          (JsonFormatter.DATE, date,
                           JsonFormatter.SENSOR_ID, sensor_id,
                           JsonFormatter.TEMPERATURE, temperature)
        self.assertEqual(expected_format, formatter.format(sort_keys=True))
