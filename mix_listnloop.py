#!/usr/bin/env python3

def main():
    networklist = [['ios','10.0.0.1'],['ios','10.0.55.1'],['ios-xr','10.0.3.1'],['juno','10.0.10.1'],['eos','10.0.14.1']]

    for driverandip in networklist:
        print('SSH to ' +driverandip[1] + ' using driver ' +driverandip[0])

main()
