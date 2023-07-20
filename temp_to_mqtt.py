from mqtt_client import MqttClient
from dht_sensor import get_data

if __name__ == '__main__':
    from time import sleep

    mqtt = MqttClient()

    while True:
        t, h = get_data()
        text = f'{t}C, {h}%'
        mqtt.publish_message(text)
        sleep(5)
