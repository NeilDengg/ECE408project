import urllib
import sys
from pymd5 import md5,padding
def decipher(query,command,outfile ):
	with open(query) as query:
		query=query.read().strip()
	with open(command) as command:
		command=command.read().strip()
	token=(query.split("&")[0]).split("=")[1]
	user="user="+(query.split("&")[1]).split("=")[1]
	token=md5(state=token.decode('hex'),count=512)
	token.update(command)
	print token.hexdigest()
	string="token="+token.hexdigest()+"&"+user+urllib.quote(padding(len(user)*8))+command
	with open(outfile,"w") as outfile:
		outfile.write(string)

decipher(sys.argv[1],sys.argv[2],sys.argv[3])