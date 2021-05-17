from Crypto.Cipher import DES3
from time import time
from pwn import *
from secrets import token_hex
from binascii import unhexlify

key = b'0000001621174954'
secret = "7ef72a7b6e53e7878c035b3b529ae29f"
bruh = "cc83d570e4dcb2682135370abc8e1f78a670924274eba831db41e6f14b05f686"

cipher = DES3.new(key, DES3.MODE_CFB, b"00000000")
pt = cipher.decrypt(unhexlify(bruh))
print(pt)

