#!/usr/bin/env python3

import urllib.request
import json
import webbrowser

apodurl = 'https://api.nasa.gov/planetary/apod?date='
date = input('\nEnter date of pic in YYYY-MM-DD: ')
mykey = 'api_key=fThjtoWz3LSzkFG7afxkFT4rRDUvg9an81AeQaOa'
apodurlobj = urllib.request.urlopen(apodurl+date+'&'+mykey)

apodread = apodurlobj.read()

decodeapod = json.loads(apodread)#.decode('utf-8'))

print("\nConverted python data")
print(decodeapod)

input('\nPress ENTER to open NASA picture')

webbrowser.open(decodeapod['url'])
