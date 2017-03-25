[![Build Status](https://travis-ci.org/justinharringa/pi-temp-monitor.svg?branch=master)](https://travis-ci.org/justinharringa/pi-temp-monitor)
[![Code Climate](https://codeclimate.com/github/justinharringa/pi-temp-monitor/badges/gpa.svg)](https://codeclimate.com/github/justinharringa/pi-temp-monitor)

# pi-temp-monitor

Temperature monitor that runs on a [Raspberry Pi](http://amzn.to/1HToEf5) using a [DS18B20 waterproof temperature sensor](http://amzn.to/1lMVMe2). 
Prints temperature and sends the data to DynamoDB.

## Dependencies
To install dependencies, use pip:

```pip install -r requirements.txt```

## Thanks!
Thanks to Timo Furrer for the [w1thermsensor module](https://github.com/timofurrer/w1thermsensor) that he put together!
