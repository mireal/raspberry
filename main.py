from time import sleep
from datetime import datetime
from csvwriter import csvwriter
from lcd import lcd_print, light_mode
# from dht_sensor import get_data
from mqtt_client import MqttGetMessage
DIRECTORY = './results/'
HEADERS = ['Date', 'Time', 'Temperature', 'Humidity']

last_minute = int(datetime.now().strftime('%M'))

get_mqtt = MqttGetMessage()

while True:
    now = datetime.now()
    Date = now.strftime("%Y-%m-%d")
    Time = now.strftime("%H:%M:%S")
    Minute = int(now.strftime("%M"))

    # humidity, temperature = get_data()
    temperature, humidity = get_mqtt.get_message()

    if humidity and temperature:

        if 8 < int(now.strftime("%H")) < 18:  # Turn display light off from 6pm to 8am
            lcd_print(f'Temp:  {temperature}', f'Humid: {humidity}%')
        else:
            light_mode(False)
            lcd_print(f'Temp:  {temperature}', f'Humid: {humidity}%')

        row = [Date, Time, temperature, humidity]
        filename = f'{DIRECTORY}{Date}'

        if Minute != last_minute:
            csvwriter(HEADERS, filename, row)
            last_minute = Minute

    sleep(5)
