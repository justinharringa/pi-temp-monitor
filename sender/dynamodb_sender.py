import boto3
import botocore
from model.temperature_reading import TemperatureReading


class DynamoDbSender:
    def __init__(self, table):
        self.table_name = table
        dynamodb = boto3.resource('dynamodb')
        self.table = dynamodb.Table(self.table_name)

    def send(self, temperature_reading: TemperatureReading):
        try:
            self.table.put_item(temperature_reading.get_dict())
        except botocore.exceptions.ClientError as e:
            print("Unexpected error: %s" % e)
