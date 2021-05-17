from string import ascii_letters, digits
from random import SystemRandom
from math import ceil, log
# from signal import signal, alarm, SIGALRM
# from secret import flag
flag = "dctf{cyber_yay_i_just_love_it_so_much_lol}"
random = SystemRandom()
ALPHABET = ascii_letters + digits + "_!@#$%.'\"+:;<=}{"
shuffled = list(ALPHABET)

random.shuffle(shuffled) 
S_box = {k : v for k, v in zip(ALPHABET, shuffled)} 
S_box = {'a': '=', 'b': "'", 'c': 'h', 'd': 'M', 'e': 'Y', 'f': '4', 'g': '8', 'h': 'p', 'i': 'f', 'j': 'j', 'k': 'y', 'l': 'X', 'm': 'o', 'n': 'F', 'o': 'b', 'p': '$', 'q': 's', 'r': 't', 's': 'Q', 't': 'H', 'u': 'O', 'v': 'N', 'w': 'L', 'x': 'm', 'y': 'R', 'z': 'd', 'A': 'g', 'B': 'K', 'C': 'B', 'D': 'J', 'E': 'D', 'F': '1', 'G': 'z', 'H': 'W', 'I': '0', 'J': '2', 'K': '.', 'L': 'I', 'M': 'v', 'N': 'U', 'O': ';', 'P': 'V', 'Q': '5', 'R': '6', 'S': 'e', 'T': 'A', 'U': 'G', 'V': '@', 'W': 'r', 'X': '#', 'Y': 'E', 'Z': 'Z', '0': '!', '1': '9', '2': ':', '3': 'c', '4': '}', '5': 'i', '6': 'w', '7': 'C', '8': '3', '9': 'l', '_': '"', '!': '<', '@': '%', '#': 'q', '$': 'S', '%': '7', '.': 'T', "'": 'a', '"': '{', '+': 'P', ':': '_', ';': 'x', '<': '+', '=': 'n', '}': 'k', '{': 'u'}

def encrypt(message):
    if len(message) % 2: # pad so always will be even
        message += "_"

    message = list(message)
    rounds = int(2 * ceil(log(len(message), 2))) 

    for round in range(rounds):
        message = [S_box[c] for c in message]
        if round < (rounds-1): # for each round except last take all odd index items and put them before all the even index items [1,2,3,4] -> [2,4,1,3]
            message =  [message[i] for i in range(len(message)) if i%2 == 1] + [message[i] for i in range(len(message)) if i%2 == 0]
            ####print(f'round: {round} and message is: {message}')
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

# signal(SIGALRM, timeout) 
# alarm(5 * 60) 

# play()
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