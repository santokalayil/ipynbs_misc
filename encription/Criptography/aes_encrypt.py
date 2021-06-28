#!/usr/bin/python3

try:
	from Crypto.Cipher import AES
except:
	import subprocess
	subprocess.call(['python3', '-m', 'pip','install', 'pycrypto'])
	from Crypto.Cipher import AES

from Crypto.Cipher import AES
import hashlib, os

# for creating a key of 32bit, for convenience sake we use a password and hash it
password = '8ehbraaa'
key = hashlib.sha256(password.encode()).digest()
#print(key)

mode = AES.MODE_CBC # block cypher mode for block chain

# initialization vector : need a 16 character string
IV = "santokalayilkunjumon"[:16]

cypher = AES.new(key, mode, IV)


# padding is needed to get message also 32bites
def pad_message(message):
	if isinstance(message, bytes):
		# print("Input is an instance of bytes. Therefore Decoding....")
		message = message.decode()
	else:
		#print("Input is not an instance of bytes. \nTherefore moving forwarding thinking \nthat it is a string....") 
		pass
	
	print(' FILE CONTENT - ORIGINAL '.center(75, '='))
	print(message)
	print(' END OF FILE CONTENT - ORIGINAL '.center(75, '='))

	length = len(message)%16
	if length != 0:
		padd_len = 16 - length
		padd = padd_len * "*"
		padded_message = message+ padd
		return padded_message

	else:
		return message

filename = 'test.txt'
with open(filename, 'rb') as f:
	message = f.read()


print("padding...")
padded = pad_message(message)
#print(padded)
#print(len(padded))
print("encrypting..l")
encrypted = cypher.encrypt(padded)

print(' FILE CONTENT - ENCRYPTED '.center(75, '='))
print(encrypted)
print(' END OF FILE CONTENT - ENCRYPTED '.center(75, '='))

destination = f"encrypted_{filename}"
print(f"Writing the file to {destination}")
with open(destination, 'wb') as f:
	f.write(encrypted)

print("Truncating the Original file...")
open(filename, 'w').close()
print("Deleting the Original file...")
os.remove(filename)
# f = open('file.txt', 'r+')
# f.truncate(0) # need '0' when using r+

print("Encryption Process completed!.....")