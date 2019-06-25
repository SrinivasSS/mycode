#!/usr/bin/env python3

import urllib.request
import json
import webbrowser

apodurl = 'https://api.nasa.gov/planetary/apod?date=2017-01-03&'
mykey = 'api_key=fThjtoWz3LSzkFG7afxkFT4rRDUvg9an81AeQaOa'
apodurlobj = urllib.request.urlopen(apodurl+mykey)

apodread = apodurlobj.read()

decodeapod = json.loads(apodread)#.decode('utf-8'))

print("\nConverted python data")
print(decodeapod)

input('\nPress ENTER to open NASA picture')

webbrowser.open(decodeapod['url'])
