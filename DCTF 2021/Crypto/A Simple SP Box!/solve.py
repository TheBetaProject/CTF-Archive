from string import ascii_letters, digits
from pwn import *

context.log_level = "debug"

r = remote("dctf1-chall-sp-box.westeurope.azurecontainer.io" ,8888)

flag_len = 42

pt_to_c_indexes = {0: 7, 1: 15, 2: 23, 3: 31, 4: 39, 5: 4, 6: 12, 7: 20, 8: 28, 9: 36, 10: 1, 11: 9, 12: 17, 13: 25, 14: 33, 15: 41, 16: 6, 17: 14, 18: 22, 19: 30, 20: 38, 21: 3, 22: 11, 23: 19, 24: 27, 25: 35, 26: 0, 27: 8, 28: 16, 29: 24, 30: 32, 31: 40, 32: 5, 33: 13, 34: 21, 35: 29, 36: 37, 37: 2, 38: 10, 39: 18, 40: 26, 41: 34}

ALPHABET = ascii_letters + digits + "_!@#$%.'\"+:;<=}{"

tests = []


def decodeman(dictman,cipher,indexes):
    clear_text = ""
    for i in range(len(cipher)-1):
        clear_text += dictman[cipher[indexes[i]]]
        print(clear_text)
    
    return clear_text


for letter in ALPHABET:
    test = list("A" * flag_len)
    test[0] = letter
    test = "".join(test)
    tests.append(test)

r.recvline()
cipher = r.recvline()
decipher_dict = {}
for i in range(len(tests)):
    r.sendline(tests[i])
    r.recvline()
    crypted_test = r.recvline()
    decipher_dict[crypted_test[pt_to_c_indexes[0]]] = tests[i][0]
print(decipher_dict)
decoded_text = decodeman(decipher_dict,cipher,pt_to_c_indexes)
info.log("Got Flag!: " + decoded_text)
r.sendline(decoded_text)

r.interactive()




