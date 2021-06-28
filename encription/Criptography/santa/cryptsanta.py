#!/usr/bin/python3

try:from Crypto.Cipher import AES
except:
	import subprocess
	subprocess.call(['python3', '-m', 'pip','install', 'pycrypto'])

from Crypto.Cipher import AES
import hashlib, os

def trunc_rm(filename):
	open(filename, 'w').close()
	os.remove(filename)

def aes_encrypt(filename, password = '8ehbraaa', init_vect = "santokalayilkunjumon", trunc = True):
	with open(filename, 'rb') as f:
		message = f.read()

	# padding is needed to get message also 32bites
	def pad_message(message, pad = '*'):
		message = message.decode() if isinstance(message, bytes) else message
		length = len(message)%16
		if length != 0:
			padd_len = 16 - length
			padd = padd_len * pad
			padded_message = message+ padd
			return padded_message

		else:
			return message

	padded = pad_message(message)

	key = hashlib.sha256(password.encode()).digest()
	mode = AES.MODE_CBC
	IV = init_vect[:16]
	cypher = AES.new(key, mode, IV)
	encrypted = cypher.encrypt(padded)
	destination = f"encrypted_{filename}"
	with open(destination, 'wb') as f:
		f.write(encrypted)


	if trunc:
		trunc_rm(filename)


def aes_decrypt(filename, password = '8ehbraaa', init_vect = "santokalayilkunjumon", trunc = False):
	
	with open(filename, 'rb') as f:message = f.read()

	key = hashlib.sha256(password.encode()).digest()
	mode = AES.MODE_CBC
	IV = init_vect[:16]
	cypher = AES.new(key, mode, IV)

	decrypted = cypher.decrypt(message)
	destination = f"decrypted_{filename}"

	def depad_message(message,  pad="*"):
		message = message.decode() if isinstance(message, bytes) else message
		de_padded_message = message.rstrip(pad) if message.endswith(pad) else message
		return de_padded_message

	depadded_message = depad_message(decrypted)

	destination = 'decrypted_'+filename
	with open(destination, 'wb') as f:f.write(depadded_message.encode())

	if trunc:trunc_rm(filename)

	print(f"Decryption Process completed for file '{filename}'")


if __name__ == '__main__':
	print("Running Script Directly... Please import it to another script to run it..")