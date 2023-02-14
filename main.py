import Adafruit_DHT as Dht
from time import sleep
import datetime
from os.path import exists
import csv
from liquidcrystal_i2c import LiquidCrystal_I2C as Lc

LC_COLS, LC_ROWS = 16, 2
LCD = Lc(0x3f, 1, numlines=LC_ROWS)

SENSOR = Dht.DHT22
PIN = 4
FIELDS = ['Date', 'Time', 'Temperature', 'Humidity']
DIRECTORY = './results/'


def show_temp(temp, humid, light=0):
    if light == 1:
        LCD.backlight()
    else:
        LCD.noBacklight()
    LCD.printline(0, f'Temp:  {temp}C')
    LCD.printline(1, f'Humid: {humid}%')


while True:
    now = datetime.datetime.now()
    Date = now.strftime("%Y-%m-%d")
    Time = now.strftime("%H:%M:%S")

    humidity, temperature = Dht.read_retry(SENSOR, PIN)
    humidity, temperature = round(humidity, ndigits=2), round(temperature, ndigits=2)

    if humidity and temperature:

        # print(f'Temperature: {temperature}C. Humidity: {humidity}%.')
        if 8 < int(now.strftime("%H")) < 18:
            show_temp(temperature, humidity, 1)
        else:
            show_temp(temperature, humidity)
        row = [Date, Time, temperature, humidity]

        if not exists(f'{DIRECTORY}{Date}.csv'):
            with open(f'{DIRECTORY}{Date}.csv', 'w', newline='') as file:
                csvfile = csv.writer(file)
                csvfile.writerow(FIELDS)

        with open(f'{DIRECTORY}{Date}.csv', 'a+', newline='') as file:
            csvfile = csv.writer(file)
            csvfile.writerow(row)

    # else:
    #     print('Failed to get reading. Try again!')
    sleep(58)
