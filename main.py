import Adafruit_DHT
from  time import  sleep
import datetime
from os.path import exists
import csv

SENSOR = Adafruit_DHT.DHT22
PIN = 4
FIELDS = ['Date', 'Time', 'Temperature', 'Humidity']
DIRECTORY = './raspberry/results/'

while True:
    now = datetime.datetime.now()
    Date = now.strftime("%Y-%m-%d")
    Time = now.strftime("%H:%M:%S")

    humidity, temperature = Adafruit_DHT.read_retry(SENSOR, PIN)
    humidity, temperature = round(humidity, ndigits=2), round(temperature, ndigits=2)

    if humidity and temperature:
        print(f'Temperature: {temperature}C. Humidity: {humidity}%.')
        row = [Date,Time,temperature,humidity]

        if not exists(f'{DIRECTORY}{Date}.csv'):
            with open(f'{DIRECTORY}{Date}.csv', 'w', newline='') as file:
                csvfile = csv.writer(file)
                csvfile.writerow(FIELDS)

        with open(f'{DIRECTORY}{Date}.csv', 'a+', newline='') as file:
            csvfile = csv.writer(file)
            csvfile.writerow(row)
            

    else:
        print('Failed to get reading. Try again!')
    sleep(58)

