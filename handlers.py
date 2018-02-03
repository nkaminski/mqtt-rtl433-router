import json
import util
from config import *

def handle_osv1_data(data):
    #Compute MQTT topic to publich to
    topic = MQTT_TOPIC_BASE + "/osv1/" + str(data['channel']) + "/" + str(data['sid'])
    #Discard unwanted parameters
    del data['model']
    del data['time']
    del data['channel']
    del data['sid']
    #Publish result
    util.publish_mqtt(topic, json.dumps(data))

def handle_acuritetower_data(data):
    #Compute MQTT topic to publich to
    topic = MQTT_TOPIC_BASE + "/acuritetower/" + str(data['channel']) + "/" + str(data['id'])
    #Discard unwanted parameters
    del data['model']
    del data['time']
    del data['channel']
    del data['id']
    del data['status']
    #Publish result
    util.publish_mqtt(topic, json.dumps(data))

#Mapping for models to handler functions
model_map = {'Acurite tower sensor': handle_acuritetower_data, 'OSv1 Temperature Sensor': handle_osv1_data}

def call_handler(data):
    try:
        #Call handler function to process the data
        model_map[data['model']](data)
    except KeyError:
        print("No mapping found for sensor!")
