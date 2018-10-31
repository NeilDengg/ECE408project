import sys
import math
import binascii
def decipher(input,keys,modulo,outfile):
	with open(input) as input:
		string=input.read().strip()
	with open(keys) as keys:
		keys=keys.read().strip()
	with open(modulo) as modulo:
		modulo=modulo.read().strip()
	ans=pow(int(string,16),int(keys,16),int(modulo,16))
	ans=str(hex(ans))[2:-1]
	with open(outfile,"w") as outfile:
		outfile.write(ans)
decipher(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])
