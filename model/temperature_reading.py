class TemperatureReading:
    DATE = 'iso_formatted_date'
    SENSOR_ID = 'sensor_id'
    TEMPERATURE = 'temperature'

    def __init__(self, iso_formatted_date, sensor_id, temperature):
        self.iso_formatted_date = iso_formatted_date
        self.sensor_id = sensor_id
        self.temperature = temperature

    def get_dict(self):
        return {self.DATE: self.iso_formatted_date,
                self.SENSOR_ID: self.sensor_id,
                self.TEMPERATURE: self.temperature}
