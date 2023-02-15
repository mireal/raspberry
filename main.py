from time import sleep
from datetime import datetime
from csvwriter import csvwriter
from lcd import show_temp
from dht_sensor import get_data

DIRECTORY = './results/'
HEADERS = ['Date', 'Time', 'Temperature', 'Humidity']

last_minute = int(datetime.now().strftime('%M'))

while True:
    now = datetime.now()
    Date = now.strftime("%Y-%m-%d")
    Time = now.strftime("%H:%M:%S")
    Minute = int(now.strftime("%M"))

    humidity, temperature = get_data()

    if humidity and temperature:

        if 8 < int(now.strftime("%H")) < 18:
            show_temp(temperature, humidity)
        else:
            show_temp(temperature, humidity, False)

        row = [Date, Time, temperature, humidity]
        filename = f'{DIRECTORY}{Date}.csv'

        if Minute != last_minute:
            csvwriter(HEADERS, filename, row)
            last_minute = Minute

    sleep(5)
