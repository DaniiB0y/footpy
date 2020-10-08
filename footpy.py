import requests
from bs4 import BeautifulSoup as bs
from string import *
import os
from socket import *
import re
from pyfiglet import Figlet
import platform
#
ports = [20, 23, 21, 25, 80, 8080, 22, 443, 4444, 110, 53, 119, 161]
ports = sorted(ports)
ni = len(ports)
i = -1
#
input("I am not responsible for any actions you take using the program, and you will be subject to any penalty for the actions you take. type any key if you agree")
if platform.system() == 'Linux':
    os.system('clear')
else:
    os.system('c')
f = Figlet(font='slant')
print(f.renderText('Footpy'))
x = int(input('Whois: 1\nPortscan: 2\nVerify Pwned Email: 3\nEnum: 4\n ~>'))

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
    #Agradecimento a mentebinaria.com.br, código deles
    endereco = input('type the dns: ')

    whois_arin = "whois.arin.net"

    servidores_whois_tdl = {'.br': 'whois.registro.br', '.org': 'whois.pir.org', '.com': 'whois.verisign-grs.com', '.pt': 'whois.dns.pt'}

    padrao_expressao_regular = re.compile(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")

    def requisicao_whois(servidor_whois, endereco_host, padrao):
        objeto_socket = socket(AF_INET, SOCK_STREAM)
        conexao = objeto_socket.connect_ex((servidor_whois, 43))
        if conexao == 0:
            if padrao == True:
                objeto_socket.send('n + {}\r\n'.format(endereco_host).encode())
                while True:
                    dados = objeto_socket.recv(65500)
                    if not dados:
                        break
                    print(dados.decode('latin-1'))
            elif padrao == False:
                objeto_socket.send('{}\r\n'.format(endereco_host).encode())
                while True:
                    dados = objeto_socket.recv(65500)
                    if not dados:
                        break
                    print(dados.decode('latin-1'))

    if padrao_expressao_regular.match(endereco):
        requisicao_whois(whois_arin, endereco, padrao = True)
    else:
        for TLD in servidores_whois_tdl.keys():
            if endereco.endswith(TLD):
                requisicao_whois(servidores_whois_tdl[TLD], endereco, padrao = False)



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
