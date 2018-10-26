import sys
from Crypto.Hash import SHA256
def decipher(input,outfile):
	with open(input) as input:
		input=input.read().strip()
	Mask=0x3FFFFFFF
	outHash=0
	for byte in input:
		byte=ord(byte)
		intermediate_value=((byte^0XCC)<<24)|((byte^0x33)<<16)|((byte^0xAA)<<8)|(byte^0x55)
		outHash=(outHash & Mask) +(intermediate_value & Mask)
	with open(outfile,"w") as outfile:
		outfile.write(hex(outHash))
decipher(sys.argv[1],sys.argv[2])
