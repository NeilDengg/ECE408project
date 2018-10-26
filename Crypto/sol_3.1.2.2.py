import sys
from Crypto.Cipher import AES
import binascii
def decipher(input,keys,iv,outfile):
	with open(input) as input:
		string=input.read().strip()
		string=binascii.unhexlify(string)
	with open(keys) as keys:
		keys=keys.read().strip()
		keys=binascii.unhexlify(keys)
	with open(iv) as iv:
		iv=iv.read().strip()	
		iv=binascii.unhexlify(iv)
	cryptor=AES.new(keys,AES.MODE_CBC,iv)
	plaintext=cryptor.decrypt(string)
	with open(outfile,"w") as outfile:
		outfile.write(plaintext)
		print 'things done'+plaintext
decipher(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])
