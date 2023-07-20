import paho.mqtt.client as mqtt
from config import MQTT_BROKER, MQTT_PORT, MQTT_TOPIC


class MqttClient:
    def __init__(self):
        self.client = mqtt.Client()
        self.client.on_message = self.on_message
        self.received_message = None

    def on_message(self, client, userdata, message):
        self.received_message = str(message.payload.decode('utf-8'))

    def publish_message(self,message,topic=MQTT_TOPIC):
        self.client.connect(MQTT_BROKER, MQTT_PORT)
        self.client.publish(topic,message)

    def get_message(self):
        self.client.connect(MQTT_BROKER, MQTT_PORT)
        self.client.subscribe(MQTT_TOPIC)
        self.client.loop_start()
        while True:
            if self.received_message:
                return self.received_message



if __name__ == '__main__':
    mqtt_client = MqttClient()
    mqtt_client.publish_message('hey')
    print(mqtt_client.get_message())
