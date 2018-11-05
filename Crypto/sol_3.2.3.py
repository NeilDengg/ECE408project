import urllib2
import sys
import binascii
def get_status(u):
	req=urllib2.Request(u)
	try:
		f=urllib2.urlopen(req)
		print f.read().strip()
		return f.code
	except urllib2.HTTPError,e:
		print e.read().strip()
		print e.code
		return e.code
def decipher(input,outfile):
	with open(input) as input:
		string=input.read().strip().decode('hex')
	BLOCK_SIZE=16
	hexstring=bytearray(string)
	l=len(hexstring)
	num_blocks=l/BLOCK_SIZE
	plaintext=bytearray(l-BLOCK_SIZE)

	for num in range(num_blocks-2,-1,-1):
		padding=bytearray(BLOCK_SIZE)
		iv_p=bytearray(BLOCK_SIZE)
		for m in range(15+num*BLOCK_SIZE,num*BLOCK_SIZE-1,-1):
			offset=0x10
			idx=BLOCK_SIZE-1-m%BLOCK_SIZE
			for i in range(BLOCK_SIZE-1-idx,BLOCK_SIZE):
				padding[i]=offset
				offset-=1
			for b in range(0,256):
				iv_p[BLOCK_SIZE-1-idx]=b
				cipherblock=hexstring[num*BLOCK_SIZE:(num+1)*BLOCK_SIZE]
				for j in range(BLOCK_SIZE):
					cipherblock[j]=cipherblock[j]^iv_p[j]^padding[j]				
				ciphertext=binascii.hexlify(hexstring[0:num*BLOCK_SIZE])+binascii.hexlify(cipherblock)+binascii.hexlify(hexstring[(num+1)*BLOCK_SIZE:(num+2)*BLOCK_SIZE])
				if get_status('http://72.36.89.198:8081/mp3/younand2/?'+ciphertext)!=500:
					print "plaintext:"+str(b)
					plaintext[m]=b
					break
	plaintext=''.join(chr(p) for p in plaintext)
	print plaintext
	with open(outfile,"w") as outfile:
		outfile.write(plaintext)

decipher(sys.argv[1],sys.argv[2])