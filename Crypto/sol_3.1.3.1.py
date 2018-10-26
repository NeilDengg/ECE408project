import sys
from Crypto.Hash import SHA256
def decipher(input,perturbed,outfile):
	with open(input) as input:
		input=input.read().strip()
	with open(perturbed) as perturbed:
		perturbed=perturbed.read().strip()
	inhash=SHA256.new(input).hexdigest()
	inhash=bin(int(inhash,16))[2:]
	perhash=SHA256.new(perturbed).hexdigest()
	perhash=bin(int(perhash,16))[2:]
	idx=min(len(inhash),len(perhash))
	ans=0
	for i in range (0,idx):
		if(inhash[i]!=perhash[i]):
			ans+=1
	ans+=max(len(inhash),len(perhash))-min(len(inhash),len(perhash))
	with open(outfile,"w") as outfile:
		outfile.write(str(hex(ans)[2:]))
	
decipher(sys.argv[1],sys.argv[2],sys.argv[3])
