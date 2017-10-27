import sys
import json
import handlers
import time

#Main routine
if __name__ == '__main__':
    for line in sys.stdin:
        try:
            #Read a JSON line
            js = json.loads(line)
            #Call handler function to process the data
            handlers.call_handler(js)
        except json.JSONDecodeError as e:
            print(e.msg)
        except ConnectionError:
            print("Connection failed when publishing! Delaying 5 sec.")
            time.sleep(5.0)

