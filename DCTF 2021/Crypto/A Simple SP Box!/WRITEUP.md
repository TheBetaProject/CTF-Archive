# A Simple SP Box
### `Submmited by SpiderPig`

from https://en.wikipedia.org/wiki/Substitution%E2%80%93permutation_network
```
In cryptography, an SP-network, or substitution–permutation network (SPN), is a series of linked mathematical operations used in block cipher algorithms such as AES (Rijndael), 3-Way, Kalyna, Kuznyechik, PRESENT, SAFER, SHARK, and Square.

Such a network takes a block of the plaintext and the key as inputs, and applies several alternating "rounds" or "layers" of substitution boxes (S-boxes) and permutation boxes (P-boxes) to produce the ciphertext block
```

so in simple words an SP just subsituetes one character with another and changes that char poistion in the string. it does that for many rounds to preduce the ciphertext.

lets see how its implemented in the code:

```python
from string import ascii_letters, digits
from random import SystemRandom
from math import ceil, log
from signal import signal, alarm, SIGALRM
from secret import flag

random = SystemRandom()
ALPHABET = ascii_letters + digits + "_!@#$%.'\"+:;<=}{"
shuffled = list(ALPHABET)

random.shuffle(shuffled) 
S_box = {k : v for k, v in zip(ALPHABET, shuffled)} 

def encrypt(message):
    if len(message) % 2:
        message += "_"

    message = list(message)
    rounds = int(2 * ceil(log(len(message), 2))) 

    for round in range(rounds):
        message = [S_box[c] for c in message]
        if round < (rounds-1):
            message =  [message[i] for i in range(len(message)) if i%2 == 1] + [message[i] for i in range(len(message)) if i%2 == 0]
    return ''.join(message)

def play():
    print("Here's the flag, please decrypt it for me:")
    print(encrypt(flag))

    for _ in range(150):
        guess = input("> ").strip()
        assert 0 < len(guess) <= 10000

        if guess == flag:
            print("Well done. The flag is:")
            print(flag)
            break

        else:
            print("That doesn't look right, it encrypts to this:")
            print(encrypt(guess))

def timeout(a, b):
    print("\nOut of time. Exiting...")
    exit()

signal(SIGALRM, timeout) 
alarm(5 * 60) 

play()
```

If we would look at the `play()` function we can see the flag is being envrypted somehow and we have 150 tries to guess what the flag is. if we guess wrong we get our guess encrypted and printed to us. but how the flag is encrypted?

so the first thing the code does is creating a randomy shuffled dictionary of our alphabet (letters, digits and some symbols) for example {'a' : 'e', 'b' : '%', 'c':'k'...}:
```python
random = SystemRandom()
ALPHABET = ascii_letters + digits + "_!@#$%.'\"+:;<=}{"
shuffled = list(ALPHABET)

random.shuffle(shuffled) 
S_box = {k : v for k, v in zip(ALPHABET, shuffled)} 
```
then with our created SP box we can now encrypt some text with the `encrypt` function. in the encrypt function we first of all pad the inputed text with `"_"` so the length of the text would be even (so the CT either the same len as the pt or longer by 1). and then we pass the text through the SP box for `rounds` times equalls `log2(length_of_text)`.

```python
for round in range(rounds):
        message = [S_box[c] for c in message]
        if round < (rounds-1):
            message =  [message[i] for i in range(len(message)) if i%2 == 1] + [message[i] for i in range(len(message)) if i%2 == 0]
    return ''.join(message)
```
as we can see the SP box substitutes one letter of the alphabet with another `rounds` times and permutates the text by taking all the odd indexed items and puts them before the even indexed items:
```
>>> message = 'ababab'
>>> message =  [message[i] for i in range(len(message)) if i%2 == 1] + [message[i] for i in range(len(message)) if i%2 == 0]
>>> message
['b', 'b', 'b', 'a', 'a', 'a']
```
the problem with this SP box is that even after all the substitutions and the permutaions each each letter and its index is mapped to the same substitued letter and permutated index. 
lets run the following example with a made up flag the same length as the real flag (which is len(ct) or len(ct-1)):
```python
pt_to_c_indexes = {}
cipher = encrypt(flag)
print(f"OG CIPHER: {cipher}")
for i in range(len(flag)):
    test = list("A" * len(flag))
    test[i] = "B"
    test = "".join(test)
    test_cipher = encrypt(test)
    print("TEST: " + test + "     " + test_cipher)
    pt_to_c_indexes[test.index("B")] = test_cipher.index("S")

print(pt_to_c_indexes)
print(len(ALPHABET))
```
which preduces the following output:
```
➜  A Simple SP Box! python3 sp_box_modified.py
OG CIPHER: ====_==G!@yy@#j_t5qqs11t=@yd;_L<L=P;r"tFq!
TEST: BAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA     DDDDDDDSDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD
TEST: ABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA     DDDDDDDDDDDDDDDSDDDDDDDDDDDDDDDDDDDDDDDDDD
TEST: AABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA     DDDDDDDDDDDDDDDDDDDDDDDSDDDDDDDDDDDDDDDDDD
TEST: AAABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA     DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDSDDDDDDDDDD
TEST: AAAABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA     DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDSDD
TEST: AAAAABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA     DDDDSDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD
TEST: AAAAAABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA     DDDDDDDDDDDDSDDDDDDDDDDDDDDDDDDDDDDDDDDDDD
TEST: AAAAAAABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA     DDDDDDDDDDDDDDDDDDDDSDDDDDDDDDDDDDDDDDDDDD
TEST: AAAAAAAABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA     DDDDDDDDDDDDDDDDDDDDDDDDDDDDSDDDDDDDDDDDDD
TEST: AAAAAAAAABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA     DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDSDDDDD
TEST: AAAAAAAAAABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA     DSDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD
TEST: AAAAAAAAAAABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA     DDDDDDDDDSDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD
TEST: AAAAAAAAAAAABAAAAAAAAAAAAAAAAAAAAAAAAAAAAA     DDDDDDDDDDDDDDDDDSDDDDDDDDDDDDDDDDDDDDDDDD
TEST: AAAAAAAAAAAAABAAAAAAAAAAAAAAAAAAAAAAAAAAAA     DDDDDDDDDDDDDDDDDDDDDDDDDSDDDDDDDDDDDDDDDD
TEST: AAAAAAAAAAAAAABAAAAAAAAAAAAAAAAAAAAAAAAAAA     DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDSDDDDDDDD
TEST: AAAAAAAAAAAAAAABAAAAAAAAAAAAAAAAAAAAAAAAAA     DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDS
TEST: AAAAAAAAAAAAAAAABAAAAAAAAAAAAAAAAAAAAAAAAA     DDDDDDSDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD
TEST: AAAAAAAAAAAAAAAAABAAAAAAAAAAAAAAAAAAAAAAAA     DDDDDDDDDDDDDDSDDDDDDDDDDDDDDDDDDDDDDDDDDD
TEST: AAAAAAAAAAAAAAAAAABAAAAAAAAAAAAAAAAAAAAAAA     DDDDDDDDDDDDDDDDDDDDDDSDDDDDDDDDDDDDDDDDDD
TEST: AAAAAAAAAAAAAAAAAAABAAAAAAAAAAAAAAAAAAAAAA     DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDSDDDDDDDDDDD
TEST: AAAAAAAAAAAAAAAAAAAABAAAAAAAAAAAAAAAAAAAAA     DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDSDDD
TEST: AAAAAAAAAAAAAAAAAAAAABAAAAAAAAAAAAAAAAAAAA     DDDSDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD
TEST: AAAAAAAAAAAAAAAAAAAAAABAAAAAAAAAAAAAAAAAAA     DDDDDDDDDDDSDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD
TEST: AAAAAAAAAAAAAAAAAAAAAAABAAAAAAAAAAAAAAAAAA     DDDDDDDDDDDDDDDDDDDSDDDDDDDDDDDDDDDDDDDDDD
TEST: AAAAAAAAAAAAAAAAAAAAAAAABAAAAAAAAAAAAAAAAA     DDDDDDDDDDDDDDDDDDDDDDDDDDDSDDDDDDDDDDDDDD
TEST: AAAAAAAAAAAAAAAAAAAAAAAAABAAAAAAAAAAAAAAAA     DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDSDDDDDD
TEST: AAAAAAAAAAAAAAAAAAAAAAAAAABAAAAAAAAAAAAAAA     SDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD
TEST: AAAAAAAAAAAAAAAAAAAAAAAAAAABAAAAAAAAAAAAAA     DDDDDDDDSDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD
TEST: AAAAAAAAAAAAAAAAAAAAAAAAAAAABAAAAAAAAAAAAA     DDDDDDDDDDDDDDDDSDDDDDDDDDDDDDDDDDDDDDDDDD
TEST: AAAAAAAAAAAAAAAAAAAAAAAAAAAAABAAAAAAAAAAAA     DDDDDDDDDDDDDDDDDDDDDDDDSDDDDDDDDDDDDDDDDD
TEST: AAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAAAAAAAAAAA     DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDSDDDDDDDDD
TEST: AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAAAAAAAAAA     DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDSD
TEST: AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAAAAAAAAA     DDDDDSDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD
TEST: AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAAAAAAAA     DDDDDDDDDDDDDSDDDDDDDDDDDDDDDDDDDDDDDDDDDD
TEST: AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAAAAAAA     DDDDDDDDDDDDDDDDDDDDDSDDDDDDDDDDDDDDDDDDDD
TEST: AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAAAAAA     DDDDDDDDDDDDDDDDDDDDDDDDDDDDDSDDDDDDDDDDDD
TEST: AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAAAAA     DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDSDDDD
TEST: AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAAAA     DDSDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD
TEST: AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAAA     DDDDDDDDDDSDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD
TEST: AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAA     DDDDDDDDDDDDDDDDDDSDDDDDDDDDDDDDDDDDDDDDDD
TEST: AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABA     DDDDDDDDDDDDDDDDDDDDDDDDDDSDDDDDDDDDDDDDDD
TEST: AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAB     DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDSDDDDDDD
{0: 7, 1: 15, 2: 23, 3: 31, 4: 39, 5: 4, 6: 12, 7: 20, 8: 28, 9: 36, 10: 1, 11: 9, 12: 17, 13: 25, 14: 33, 15: 41, 16: 6, 17: 14, 18: 22, 19: 30, 20: 38, 21: 3, 22: 11, 23: 19, 24: 27, 25: 35, 26: 0, 27: 8, 28: 16, 29: 24, 30: 32, 31: 40, 32: 5, 33: 13, 34: 21, 35: 29, 36: 37, 37: 2, 38: 10, 39: 18, 40: 26, 41: 34
```

so as we can see in our example pt `'A'` is always mapped to  ct `'D'` and pt `'B'` is always mapped to ct `'S'`.
so we can reverse that proccess (ct `'D'` is in pt `'A'`)
aswell as the indexes are always mapped to the same location we can create a dictionary `{pt_index:ct_index}` to help us reverse the encryption:
```python
{0: 7, 1: 15, 2: 23, 3: 31, 4: 39, 5: 4, 6: 12, 7: 20, 8: 28, 9: 36, 10: 1, 11: 9, 12: 17, 13: 25, 14: 33, 15: 41, 16: 6, 17: 14, 18: 22, 19: 30, 20: 38, 21: 3, 22: 11, 23: 19, 24: 27, 25: 35, 26: 0, 27: 8, 28: 16, 29: 24, 30: 32, 31: 40, 32: 5, 33: 13, 34: 21, 35: 29, 36: 37, 37: 2, 38: 10, 39: 18, 40: 26, 41: 34}
```

now that we have our indexes we need to just run over all the pt alphabet to see which letter in preduces as ct and we can reverse the flag:

```python
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
```

## dctf{S0_y0u_f0und_th3_cycl3s_in_th3_s_b0x}