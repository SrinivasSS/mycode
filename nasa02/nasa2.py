#!/usr/bin/env python3

import urllib.request
import json

neourl = 'https://api.nasa.gov/neo/rest/v1/feed?'
startdate = 'start_date=2018-06-01'
enddate = '&end_date=END_DATE'
mykey = '&api_key=fThjtoWz3LSzkFG7afxkFT4rRDUvg9an81AeQaOa'

neourl = neourl + startdate + mykey

neourlobj = urllib.request.urlopen(neourl)

neoread = neourlobj.read()

decodeneo = json.loads(neoread.decode('utf-8'))

print('\nConverted python data')
print(decodeneo)
