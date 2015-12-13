class CsvFormatter:
    def __init__(self, iso_formatted_date, sensor_id, temperature):
        self.iso_formatted_date = iso_formatted_date
        self.sensor_id = sensor_id
        self.temperature = temperature

    def format(self):
        return '%s,%s,%.3f' % \
               (self.iso_formatted_date, self.sensor_id, self.temperature)
