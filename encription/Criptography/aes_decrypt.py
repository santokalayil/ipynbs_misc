#!/usr/bin/python3

try:
	from Crypto.Cipher import AES
except:
	import subprocess
	subprocess.call(['python3', '-m', 'pip','install', 'pycrypto'])
	from Crypto.Cipher import AES

from Crypto.Cipher import AES
import hashlib, os




def depad_message(message):
	if isinstance(message, bytes):
		# print("Input is an instance of bytes. Therefore Decoding....")
		message = message.decode()
	else:
		#print("Input is not an instance of bytes. \nTherefore moving forwarding thinking \nthat it is a string....") 
		pass

	if message.endswith("*"):
		de_padded_message = message.rstrip('*')
		return de_padded_message

	else:
		return message

filename = 'encrypted_test.txt'
with open(filename, 'rb') as f:
	message = f.read()

print("Decrypting..l")

password = '8ehbraaa'
key = hashlib.sha256(password.encode()).digest()
mode = AES.MODE_CBC # block cypher mode for block chain
IV = "santokalayilkunjumon"[:16]
cypher = AES.new(key, mode, IV)

decrypted = cypher.decrypt(message)

print("Depadding...")
depadded_message = depad_message(decrypted)

print(' FILE CONTENT - DECRYPTED '.center(75, '='))
print(depadded_message)
print(' END OF FILE CONTENT - DECRYPTED '.center(75, '='))

destination = 'decrypted_'+filename
print(f"Writing the file to {destination}")
with open(destination, 'wb') as f:
	f.write(depadded_message.encode())

print("Decryption Process completed!.....")