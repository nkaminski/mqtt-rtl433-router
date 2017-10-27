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

#Mapping for models to handler functions
model_map = {'OSv1 Temperature Sensor': handle_osv1_data}

def call_handler(data):
    try:
        #Call handler function to process the data
        model_map[data['model']](data)
    except KeyError:
        print("No mapping found for sensor!")
