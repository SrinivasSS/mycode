#!/usr/bin/env python3

import urllib.request
import json

#Trace the ISS
majortom = 'http://api.open-notify.org/astros.json'

#Call the web service
groundctrl = urllib.request.urlopen(majortom)

#Pul fileobject into helmet
helmet = groundctrl.read()
print(type(helmet))

#Decode json into python object
helmetjson = json.loads(helmet.decode('utf-8'))

print("\nConverted python data")
print(helmetjson)

print("People in space:", helmetjson['number'])
people = helmetjson['people']
print(type(people))

for x in people:
    print(x['name'], "is on the", x['craft'])

