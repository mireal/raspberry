import paho.mqtt.client as mqtt
from config import MQTT_BROKER, MQTT_PORT, MQTT_TOPIC


class MqttGetMessage:
    def __init__(self):
        self.client = mqtt.Client()
        self.client.on_message = self.on_message
        self.received_message = 0

    def on_message(self, client, userdata, message):
        self.received_message = str(message.payload.decode('utf-8')).split(',')

    def get_message(self):
        self.client.connect(MQTT_BROKER, MQTT_PORT)
        self.client.subscribe(MQTT_TOPIC)
        self.client.loop_start()
        while True:
            if self.received_message:
                return self.received_message


if __name__ == '__main__':
    get_mqtt = MqttGetMessage()
    print(get_mqtt.get_message())
