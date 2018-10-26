import sys
from Crypto.Cipher import AES
import binascii
def decipher(input):
	with open(input) as input:
		string=input.read().strip()
		string=binascii.unhexlify(string)
	for i in range(32):
		if(i<16):
			keys='000000000000000000000000000000000000000000000000000000000000000'+hex(i)[2:]
		else:
			keys='00000000000000000000000000000000000000000000000000000000000000'+hex(i)[2:]
		transkey=binascii.unhexlify(keys)
		iv='00000000000000000000000000000000'
		iv=binascii.unhexlify(iv)
		cryptor=AES.new(transkey,AES.MODE_CBC,iv)
		plaintext=cryptor.decrypt(string)
		print keys
		print plaintext
decipher(sys.argv[1])
