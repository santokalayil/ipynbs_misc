#! /usr/bin/python3

import optparse
from socket import (gethostbyname, gethostbyaddr, setdefaulttimeout,
                   socket,AF_INET, SOCK_STREAM)
from threading import Thread
from termcolor import colored

def connScan(tgtHost, tgtPort):
    try:
        sock = socket(AF_INET, SOCK_STREAM)
        sock.connect((tgtHost, tgtPort))
        print(colored(f'[+] {tgtPort} TCP Open', 'red'))
    except:
        print(colored(f'[-] {tgtPort} TCP Closed','green'))
    finally:
        sock.close()

def portScan(tgtHost, tgtPorts):
    try:
        tgtIP = gethostbyname(tgtHost)
        print(f'Target IP is {tgtIP} ({tgtHost})')
    except:
        print(f'Unknown Host {tgtHost}')
        # if error hhere. how to exit?
    
    try:
        tgtName = gethostbyaddr(tgtIP)
        print(f'[+] Scan Results for: {tgtName[0]}')
    except:
        print(f'[+] Scan Results for: {tgtIP}')
        
    setdefaulttimeout(1)
    
    for tgtPort in tgtPorts:
        t = Thread(target = connScan, args=(tgtHost, int(tgtPort)))
        t.start()

def main():
	parser = optparse.OptionParser('Usage of Program: ' + '-H <target host> -p <target port>')
	parser.add_option('-H', dest='tgtHost', type='string', help = 'Specify target host')
	parser.add_option('-p', dest='tgtPorts', type='string', help = 'Specify target ports seperated by comma')
	(options, args) = parser.parse_args()
	tgtHost = options.tgtHost
	tgtPorts = str(options.tgtPorts).split(',')
	if (tgtHost == None) | (tgtPorts == None):
		print(parser.usage)
		exit(0)
	#print("starting PortScan Function")
	portScan(tgtHost, tgtPorts)

if __name__ == '__main__':
	main()