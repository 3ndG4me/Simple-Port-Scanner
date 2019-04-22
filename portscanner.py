#!/usr/bin/python3

import socket
from netaddr import IPNetwork
import sys


if len(sys.argv) < 3:
    print("Usage: portscanner.py <IP or IP Range> <port or port range>")
    print("Example: portscannery.py 192.168.2.3 1-1024")
else:
    port = sys.argv[2]
    port = port.replace('-', ' ').split(' ')
    if (len(port) > 1):
        range_start = int(port[0])
        range_end = int(port[1]) + 1
        port_range = range(range_start, range_end)
    else:
        range_start = int(port[0])
        range_end = int(port[0]) + 1
        port_range = range(range_start, range_end)
    
    
    for ip in IPNetwork(sys.argv[1]):
        for port in port_range:
            s = socket.socket()
            s.settimeout(1) # Speeds things up, change this to a higher value if you're on a slower connection.
            try:
                s.connect((str(ip), port))
                print("Port %d is open on %s" % (port, str(ip)))
                s.close()
            except Exception as e:
                print("Port %d not open on %s" % (port, str(ip)))
                s.close()
