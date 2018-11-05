import sys
from math import *
from Crypto.PublicKey import RSA
from fractions import gcd

def producttree(X):
	result=[X]
	while len(X)>1:
		X=[reduce(lambda x,y:x*y, X[i*2:(i+1)*2]) for i in range(len(X)+1)/2]
		result.append(X)
	return result
def remaindertree(n,T):
	mid=[n]
	for t in reversed(T):
		print(mid,t)
		mid=[mid[floor(i/2)]%t[i] for i in range(len(t))]
		print(mid,t)
	result=[]
	for i in range(len(mid)):
		for j in range(len(mid[i])):
			result.append(mid[i][j]**2)
	return result
def egcd(a,b):
	if a==0:
		return(b,0,1)
	else:
		g,y,x=egcd(b%a,a)
		return (g,x-(b//a)*y,y)
def modinv(a,m):
	g,x,y=egcd(a,m)
	if g!=1:
		raise Exception('modular inverse dose not exist')
	else:
		return x%m
def decipher(moduli,ciphertext,outfile):
	raw=[]
	with open(moduli) as moduli:
		for line in moduli:
			raw.append(int(line,16))
	with open(ciphertext) as ciphertext:
		ciphertext=ciphertext.read()
	e=long(65537)
	(P,ptree)=producttree(raw)
	gcds=remaindertree(P,ptree)
	for i in range(len(gcds)):
		if gcds[i] !=1:
			p=gcds[i]
			q=raw[i]/p
			d=modinv(e,(p-1)*(q-1))
			try:
				key=RSA.construct((p*q,e,d))
				plaintext=pbp.decrypt(key,ciphertext)
				print ciphertext
			except ValueError:
				continue
decipher(sys.argv[1],sys.argv[2],sys.argv[3])
