import sys
def decipher(input,keys,outfile):
	with open(input) as input:
		string=input.read().strip()
	with open(keys) as keys:
		keys=keys.read().strip()
	output='';
	for i in range(len(string)):
		if(string[i]>='A' and string[i]<='Z'):
			k=ord(string[i])-ord('A')
			output=output[:i]+keys[k]+output[i+1:]
		else:
			output=output[:i]+string[i]+output[i+1:]
	with open(outfile,"w") as outfile:
		outfile.write(output)
		print 'things done'
decipher(sys.argv[1],sys.argv[2],sys.argv[3])
