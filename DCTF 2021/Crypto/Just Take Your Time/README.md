# Just Take Your Time
### Submitted by SpiderPig

The problem with this challange is that they use epoch time as the key to the cipher:

from https://en.wikipedia.org/wiki/Epoch_(computing)
```
In computing, an epoch is a date and time from which a computer measures system time. Most computer systems determine time as a number representing the seconds removed from particular arbitrary date and time. For instance, Unix and POSIX measure time as the number of seconds that have passed since 1 January 1970 00:00:00 UT, a point in time known as the Unix epoch. The NT time epoch on Windows NT and later refers to the Windows NT system time in (10^-7)s intervals from 0h 1 January 1601.[1]

Computing epochs are nearly always specified as midnight Universal Time on some particular date.
```

```python
key = str(int(time())).zfill(16).encode("utf-8")
secret = token_hex(16)
cipher = DES3.new(key, DES3.MODE_CFB, b"00000000")
encrypted = cipher.encrypt(secret.encode("utf-8"))
print("You have proven yourself to be capable of taking on the final task. Decrypt this and the flag shall be yours!")
print(encrypted.hex())
```

so we get a key in the format of:
`0000001621254177`
and since we know the CTF is on UTC time we can just know what the key is by running `time()` when connecting to the challange (and worst case add or sub seconds). 
after that we can create the same cipher with the same key and IV (the b"00000000")
and just decrypt the flag:

```python
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
```
## flag: dctf{1t_0n1y_t0Ok_2_d4y5...}
=======

>>>>>>> 6f318d3f929f43ea5b6ff1301e3811924212136d
