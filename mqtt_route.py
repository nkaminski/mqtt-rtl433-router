import sys
import json
import handlers


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

