import socket 
from IPy import IP 

targets = input('[+] Input IP addresses or domain name !(EXMP(127.0.0.1,192.169.9.1)): ')

class PortScanner:
    def portscan(ipadd,port):
        try:
            sock = socket.socket()
            sock.settimeout(0.5);sock.connect((''.join(ipadd.split()), int(port)))
            print(f'[+] Port {port} is open!')
        except Exception as e:pass
    
    def ipaddscan(ipadd):
        try:
            IP(ipadd)
            return ipadd 
        except ValueError:
            return socket.gethostbyname(ipadd)

    def scan(ipadd):
        print(PortScanner.ipaddscan(ipadd))
        print('[+]IP Scanned!')
        for port in range(1,250):PortScanner.portscan(ipadd, port)

if ',' in targets:
    for ipadd in targets.split(','):PortScanner.scan(ipadd)
else:PortScanner.scan(targets)
