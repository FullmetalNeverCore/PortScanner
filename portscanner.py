import socket 
from IPy import IP 

targets = input('[+] Input IP addresses or domain name !(EXMP(127.0.0.1,192.169.9.1)): ')
ports = input('[+] Input ports that u want to scan or leave this field empty!(EXMP 80,256,1024): ')

class PortScanner:
    def portscan(ipadd,port):
        try:
            sock = socket.socket()
            sock.settimeout(0.5);sock.connect((''.join(ipadd.split()), int(port)))
            try:
                bnnr = PortScanner.check_banner(sock)
                print(f'[+] Port {port} is open! ::  Banner - {bnnr.decode()}')
            except Exception:
                print(f'[+] Port {port} is open!')
        except Exception as e:pass #DEBUG print(f'{port} closed')
    
    def check_banner(sock):
        return sock.recv(1024)

    def ipaddscan(ipadd):
        try:
            IP(ipadd)
            return ipadd 
        except ValueError:
            return socket.gethostbyname(ipadd)

    def scan(ipadd):
        print(PortScanner.ipaddscan(ipadd))
        print('[+]IP Scanned!')
        if ',' in ports:
            for x in range(len(ports.split(','))):PortScanner.portscan(ipadd,ports.split(',')[x-1])
        else:   
            if not ports: 
                for port in range(1,250):PortScanner.portscan(ipadd, port) 
            else:PortScanner.portscan(ipadd,ports)

if ',' in targets:
    for ipadd in targets.split(','):PortScanner.scan(ipadd)
else:PortScanner.scan(targets)
