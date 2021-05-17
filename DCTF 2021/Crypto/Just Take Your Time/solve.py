from Crypto.Cipher import DES3
import time
from pwn import *
from binascii import unhexlify

context.log_level = "debug"

key = str(int(time.time())).zfill(16).encode("utf-8")
cipher = DES3.new(key, DES3.MODE_CFB, b"00000000")
r = remote("dctf-chall-just-take-your-time.westeurope.azurecontainer.io" ,9999)

r.recvline()
a,b = r.recvline()[:-4].replace(' ', '').split('*')
log.info("Sending a * b!")
r.sendline(str(int(a) * int(b)))
r.recvuntil("yours!\n")
encrypted = r.recvline()[:-1]
for i in range(3):
    key = str(int(time.time())+i).zfill(16).encode("utf-8")
    cipher = DES3.new(key, DES3.MODE_CFB, b"00000000")
    decrypted = cipher.decrypt(unhexlify(encrypted))
    print("BRUHHHHH  ",decrypted)
    r.sendline(decrypted)
r.interactive()