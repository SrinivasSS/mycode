#!/usr/bin/env python3

import requests

def main():
    neourl = 'https://api.nasa.gov/neo/rest/v1/feed?'
    startdate = 'start_date=2018-06-01'
    enddate = '&end_date=END_DATE'
    mykey = '&api_key=fThjtoWz3LSzkFG7afxkFT4rRDUvg9an81AeQaOa'

    neourl = neourl + startdate + mykey

    neojson = (requests.get(neourl)).json()

    print('\nConverted python data')
    print(neojson)

main()
