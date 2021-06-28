#!/bin/python3

import sys
import socket
from datetime import datetime

# define our target
if len(sys.argv) == 2:
	#print(sys.argv)
	target = socket.gethostbyname(sys.argv[1]) # translate hostname to ipv4

else:
	print("One Argument is needed, make use that is a hostname like google.com")
	sys.exit()

print(" SCANNER ".center(100, '='))
print(f"Scanning Target: {target}")
print(f" Time: {datetime.now()} ".center(100, '-'))
print(100*'*')

try:
	for port in range(1,100):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1) # is a float
		result = s.connect_ex((target, port)) # return error indicator 0 if no error.. if nonzero, error
		print(f"Checking port {port} ...")
		if result == 0:
			print(f"Port {port} is open.")
		s.close()

except KeyboardInterrupt:
	print("\nExiting the Program")
	sys.exit()

except socket.gaierror:
	print("Hostname could not be resolved..")
	sys.exit()

except socket.error:
	print("Could not connect to server...")
	sys.exit()
