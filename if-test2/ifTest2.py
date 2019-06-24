#!/usr/bin/env python3

import ipaddress
ipchk = input('Apply an ip address: ')

try:
    ipaddress.ip_address(ipchk)
    if ipchk:
        print('IP address provided: ' +ipchk)
    else:
        print('No IP given')

except:
    print("Not valid IP!")
