import unittest

from formatter.csv_formatter import CsvFormatter


class CsvFormatterTestCase(unittest.TestCase):
    def test_csv_format(self):
        date = '2015-12-13T11:00:00.000-3:00'
        sensor_id = '8675309'
        temperature = 0.000
        formatter = CsvFormatter(date, sensor_id, temperature)
        self.assertEqual(formatter.format(), date + ',' + sensor_id + ',%.3f' % temperature)
