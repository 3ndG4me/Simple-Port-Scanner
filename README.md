# Simple-Port-Scanner

A Simple Port Scanner in python3

## Purpose
Sometimes firewalls are tough and you need the most basic stupid portscanner there is to just test for open ports.

## Features
- Can scan single IPs and single ports Example: `portscanner.py 192.168.0.1 22`
- Can parse CIDR range and scan multiple ips Example: `portscanner.py 192.168.0.1/24 22`
- Can parse port ranges and scan multiple ports Example: `portscanner.py 192.168.0.1 1-1024`
- Any combiniation of the above 3


## TODO:
- Add the option to parse a list of ports i.e. `portscanner.py <IP> 22, 23, 445`
- Add the option to parse a list of IPs i.e. `portscanner.py 192.168.0.1, 192.168.0.2, 192.168.0.3 <port(s)>`
- Add timeout flag to change the length of timeouts between scans


## Usage:
- `python3 portscanner.py <IP> <port>`
- Example: `python3 portscanner.py 192.168.0.1/24 1-1024`



