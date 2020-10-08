import requests
import socket
from bs4 import BeautifulSoup as bs
from string import *
import os
#
ports = [20, 23, 21, 25, 80, 8080, 22, 443, 4444, 110, 53, 119, 161]
ports = sorted(ports)
ni = len(ports)
i = -1
#
x = int(input('Whois: 1\nPortscan: 2\nVerify Pwned Email: 3\n Enum: 4\n ~>'))

def enum():
    ip = input('Ip or dns: ~>')
    os.system(f'host {ip}')
def pwned():
    print("Soon")
    #email = str(input('email: without @ like johndoe.1, we gonna set domain soon'))
    #domain = str(input('domain, like @gmail.com'))
    #page = requests.get(f'https://haveibeenpwned.com/unifiedsearch/https://haveibeenpwned.com/unifiedsearch/{email}%40{domain}')
    #soup = bs(page.content, 'html.parser')
    #print(soup)
def whois():
    url = str(input('Type the url without "www" like google.com \n ~>'))
    #
    page = requests.get(f'https://who.is/whois/{url}')
    soup = bs(page.content, 'html.parser')
    whois = soup.find('pre')
    whois = whois.get_text()
    print(whois)

def portscan():
    global ports
    global i
    ip = input('ip: ~>')
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(0.1)
    choice = str(input('Verify only most common ports? y/n: ~>'))
    choice = choice.lower()

    if choice == "y" or "yes":
        while i <= ni:
            i += 1
            code = client.connect_ex((ip, ports[0]))
            if code == 0:
                print(ports[i], "OPEN")
            else:
                print(ports[i], "CLOSED")
    elif choice == "n" or "no":
        for i in range(1, 100):
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.settimeout(0.1)
            code = client.connect_ex((ip, i))
            if code == 0:
                print(port, "OPEN")
            else:
                print(port, "CLOSED")

if x == 1:
    whois()

if x == 2:
    portscan()

if x == 3:
    pwned()

if x == 4:
    enum()
