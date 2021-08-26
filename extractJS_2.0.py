#!/bin/python3
#This program is built by Dev_Ali.
#The purpose of this program is to extract all the JavaScript links from a Web page.
#The program comes handy when people like developers and hackers etc want to extract Javascript file links from source codes for performing further operation. 

import re
import sys
import socket
from datetime import datetime
import urllib.request, urllib.parse, urllib.error


#Syntax
print("Syntax: host: xyz.com Port: 80/443")

#Hostname and Port Number
host = input("Enter a host to connect to: ")
port = int(input("Enter a port number (80/443): "))

#Establish a connection
if re.search("^http", host):
    ext = re.findall("/\S([^ ]*?)/", host)
    ext2 = ext[0]
    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("-" * 50)
    print("[+] Time started:", datetime.now())
    print("[+] Hostname:", host)
    print("-" * 50)
    try:
        request = connection.connect_ex((ext2, port))
        print("[+] Connected to the Webserver")
        print("[+] Extracting JavaScript URLs")
        print("-" * 50)
    except:
        print("[+] Connection to the host can't be establish")
        print("[+] Exiting!")
        sys.exit()
else:
    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("-" * 50)
    print("[+] Time started:", datetime.now())
    print("[+] Hostname:", host)
    print("-" * 50)
    try:
        request = connection.connect_ex((host, port))
        print("[+] Connected to the Webserver")
        print("[+] Extracting JavaScript URLs")
        print("-" * 50)
    except:
        print("[+] Connection to the host can't be establish")
        print("[+] Exiting!")
        sys.exit()

#Request the web source code and extract JS links
try:        
    js_links = list()
    if re.search("^http", host):
        connect = urllib.request.urlopen(host)
    else:
        connect = urllib.request.urlopen("https://" + host)
    for line in connect:
        var = (line.decode().strip())
        search = re.findall("https://\S+js", var)
        if len(search) < 1:
            continue
        else:
            for link in search:
                js_links.append(link)
    count = 0
    for value in js_links:
        count = count + 1
        print(count, "-", value)
    print("The total number of extracted links is", count)
    
except:
    KeyboardInterrupt()
    print("\nExiting program.")
    sys.exit()
        