# -*- coding: utf-8 -*-

import string
import itach
import devices.nexa as nexa
import devices.multibrackets as multibrackets
import devices.yamaha_rx350 as yamaha
from bottle import route, run

def send(command):
    print ">", command
    result = itach.send_command(command)
    print "<", result

@route('/')
def hello():
    return "PyTach Web Server is running!"

@route('/device/<device:path>')
def device(device):
    print device
    device = device.split('/')
    if device[0] == 'nexa':
        print 'nexa'
        if len(device) == 3:
            sub_command = nexa.build_command(device[1], device[2])
            command = itach.build_command(1, 1, sub_command)
            send(command)
        else:
            print 'Incorrect parameters'
    elif device[0] == 'multibrackets':
        if len(device) == 2:
            sub_command = multibrackets.get_command(device[1])
            command = itach.build_command(1, 1, sub_command)
            send(command)
        else:
            print 'Incorrect parameters'
    elif device[0] == 'yamaha':
        print 'yamaha'
        if len(device) == 2:
            sub_command = yamaha.get_command(device[1])
            command = itach.build_command(1, 3, sub_command)
            send(command)
        else:
            print 'Incorrect parameters'
    else:
        print 'Unknown device'

run(host='localhost', port=8080, debug=True)