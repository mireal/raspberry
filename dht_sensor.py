import Adafruit_DHT as Dht

SENSOR = Dht.DHT22
PIN = 4


def get_data():
    """returns humidity and temperature from DHT sensor"""
    humidity, temperature = Dht.read_retry(SENSOR, PIN)
    humidity, temperature = round(humidity, ndigits=1), round(temperature, ndigits=1)
    return temperature, humidity

if __name__ == '__main__':
    print(get_data())