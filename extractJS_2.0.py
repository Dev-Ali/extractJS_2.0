#!/bin/python3
#This program is built by Dev_Ali.
#The purpose of this program is to extract all the JavaScript links from a Web page.
#The program comes handy when people like developers and hackers etc want to extract Javascript file links from source codes for performing further operation. 

import re
import sys
import socket
from datetime import datetime
import urllib.request, urllib.parse, urllib.error


def request_regex(url,port): # added this so we can call it in both the prompt and argument ways of launching
    #Establish a connection
    try:
        regex = r"(/.*)"
        path = re.findall(regex, url)
        path = ''.join(str(e) for e in path)
        regex = r"(.*?)/"
        host = re.findall(regex, url)[0]
        full_url = host + str(":") + str(port) + path
        url = host
    except:
        host = url
        full_url = url + ":" + str(port) + "/"
    if port == 80:
        full_url = "http://" + full_url
    else:
        full_url = "https://" + full_url
        pass
    print(full_url)
    if re.search("^http", url):
        ext = str(re.findall("/\S([^ ]*?)/", url))
        ext2 = ext[0]
        connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("-" * 50)
        print("[+] Time started:", datetime.now())
        print("[+] Hostname:", url)
        print("-" * 50)
        try:
            request = connection.connect_ex((full_url))
            print("[+] Connected to the Webserver")
            print("[+] Extracting JavaScript URLs")
            print("-" * 50)
        except:
            print("[+] Connection to the host can't be establish")
            print("[+] Exiting! (exempt 1)")
            sys.exit()
    else:
        connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("-" * 50)
        print("[+] Time started:", datetime.now())
        print("[+] URL:", full_url)
        print("-" * 50)
        try:
            request = connection.connect_ex((url, port))
            print("[+] Connected to the Webserver")
            print("[+] Extracting JavaScript URLs")
            print("-" * 50)
        except:
            print("[+] Connection to the host can't be establish")
            print("[+] Exiting! (Exempt 1)")
            sys.exit()  

    #Request the web source code and extract JS links
    try:        
        js_links = list()
        if re.search("^http", url):
            connect = urllib.request.urlopen(url)
        else:
            connect = urllib.request.urlopen(full_url)
        for line in connect:
            var = (line.decode().strip())
            search = re.findall("https://\S+js", var)
            if len(search) < 1:
                continue
            else:
                for link in search:
                    js_links.append(link)
        count = 0
        print("Full path links (EX: https://google.com/js/javascript.js)")
        for value in js_links:
            count = count + 1
            print(count, "-", value)
        function(url,count)
#        for value in js_links:
#            count = count + 1
#            print(count, "-", value)
#        print("The total number of extracted links is", count)
        
    except:
        KeyboardInterrupt()
        print("\nExiting program.")
        sys.exit()
    pass

def argument_checker():
    arg = sys.argv[1:]#gathers all arguments into a list
    num = 0

    for var in arg:#cycles through argument list
        num = num + 1#adds 1 to indicate moving to the next argument
        #The following checks for certain variables by matching values found in the argument list
        if var == "-url" or var == "--url" or var == "-u" or var == "--u" :
            url = num + 1#adds 1 for the user defined elemt after the argument
            url = sys.argv[url]#here we assign the argument and we have the number due to the above calculations
        elif var == "-port" or var == "--port" or var == "-p" or var == "--p":#repeat notes from if part of statement
            port = num + 1
            port = int(sys.argv[port])
        elif var == "-h" or var == "--h" or var == "-help" or var == "--help":#repeat notes from if part of statement
            print("Thank you for using the script!!!\n\n-url/-u           This is for defining the host to scan (EX: -url google.com)\n\n-port/-p           This is for defining the port to scan (80 for http, 443 for https) (EX: -p 443)\n\n-h/-help           Displays this help menu. (EX: -h)\n\n\nExamples:\n\n(Scan https://yahoo.com for javascript files): python3 extractJS_2.0 -url yahoo.com -port 443\n\n(Help): python3 extractJS_2.0 -h")
            sys.exit("\n\nNow that you know how... Go scan some files!!!")
        pass
    pass
    request_regex(url,port)

def function(url,count):
    local_js_links = list()
    regex = r'<script src="(.*)"></script>'
    connect = urllib.request.urlopen("https://" + url)
    for line in connect:
        x = (line.decode().strip())
        search = re.findall(regex, x)
        if len(search) < 1:
            continue
        else:
            for link in search:
                if link[0:1] == "/":
                    local_js_links.append("https://" + url + link)
                else:
                    pass
    print("Local site links (EX: /js/javascript.js")
    for value in local_js_links:
        count = count + 1
        print(count, "-", value)
    pass
    print("The total number of extracted links is", count)




if len(sys.argv) < 2:# This checks if theres any input if not then it defaults to original script 
    #Syntax
    print("Syntax: host: xyz.com Port: 80/443") 
    #Hostname and Port Number
    url = input("Enter a host to connect to: ")
    port = int(input("Enter a port number (80/443): ")) 
    request_regex(url,port)
else:# if there is input it goes to an argument checker
    argument_checker()#Checks for arguments
    pass