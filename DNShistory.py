#! /usr/bin/env python3
import sys
import requests
import re
import socket

print( ' ')    
print("Author: Warren Vos <info@redmoonsecurity.com>")
print("GitHub: https://github.com/RedMoon-Security/DNShistory")

print("\nThis script displays all historical IP addresses related to a given domain")
print("You can use this info to try bypass WAFs like Cloudflare etc")
print("as you might be able to get the origin server IP address\n")

domain = input("Enter domain: ")
if len(domain) < 2:
    print("Usage: Enter a domain name\nExample: google.com")
    sys.exit(1)

print("\n")
print("Discovering Historical IP Addresses for " + domain)
print('-' * 55)

req = requests.get("https://securitytrails.com/domain/" + domain + "/history/a")
source = str(req.content)
ip = re.findall(r'[0-9]+(?:\.[0-9]+){3}', source)
unique_list = list(set(ip))
sorted_ip = sorted(unique_list, key=lambda item: socket.inet_aton(item[0]))

print(*sorted_ip, sep="\n")
print('-' * 55)
