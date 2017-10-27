import paho.mqtt.publish as publish
from config import *

def publish_mqtt(topic, payload):
    #publish.single(topic, payload, hostname=MQTT_HOST, auth={'username': MQTT_USER, 'password': MQTT_PASS})
    print("%s -> %s" % (topic,payload))


