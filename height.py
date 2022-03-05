import os
from simon import SimonCipher
from height_plantext import *
from height_encrpyt import *
from height_decrypt import * 

#-------------------------Run HIGHT Algorithm -------------------------------
    
#Read plaintext from file.CSV And Display It
high_plaintext = read_high_plaintext()
simon_plaintext = read_simon_plaintext()
print(f"The Original High Text  {hex(high_plaintext)}")
print(f"The Original Simon Text {hex(simon_plaintext)}")
print("=========================================")

# #Read whitening keys and  subkeys from file.CSV
read_keys()

def myfill(mystr):
    mystr = str(mystr)
    n = 20 - len(mystr) 
    if (n >= 1):
        for i in range(0, n):
            mystr += "0" 
    return mystr

# Encrpyt Useing Simon Algorithm
def simon_encrpyt(simon_value):
    my_simon = SimonCipher(0xABBAABBAABBAABBA,   block_size=64)
    simon_ciphertext = my_simon.encrypt(simon_value)
    return simon_ciphertext

# Decrypt Useing Simon Algorithm
def simon_decrypt(simon_value):
    my_simon = SimonCipher(0xABBAABBAABBAABBA,   block_size=64)
    simon_plaintext = my_simon.decrypt(simon_value)
    return  simon_plaintext

# Encrpyt Useing High Algorithm
def high_encrypt(myPlainText1):
    encryptext = encrypt(myPlainText1)
    return int(encryptext, 16)

# Decrypt Useing High Algorithm
def high_decrypt(myPlainText1):
    decryptext = decrypt(myPlainText1)
    return int(decryptext, 16)



# high_plaintext = high_encrypt(high_plaintext)
# print(hex(high_plaintext))

# simon_plaintext = simon_encrpyt(high_plaintext)
# print(hex(simon_plaintext))

# simon_plaintext = simon_decrypt(simon_plaintext)
# print(hex(simon_plaintext))

# high_plaintext = high_decrypt(simon_plaintext)
# print(hex(high_plaintext))

def high_to_simon(high_plaintext):
    high_plaintext = high_encrypt(high_plaintext)
    simon_plaintext = simon_encrpyt(high_plaintext)
    simon_plaintext = simon_decrypt(simon_plaintext)
    high_plaintext = high_decrypt(simon_plaintext)
    return hex(high_plaintext)

def e(high_plaintext):
    for i in range(0, 6):
        high_plaintext = simon_encrpyt(high_encrypt(high_plaintext))
    return high_plaintext

def d(high_plaintext):
    high_plaintext = simon_decrypt(high_decrypt(high_plaintext))
    return high_plaintext


# Display The Encrypt And The Decrypt 
# simon_plaintext = simon_encrpyt(simon_plaintext)
# print(f"simon en {hex(simon_plaintext)}")
# simon_plaintext = simon_decrypt(simon_plaintext)
# print((f"simon de {hex(simon_plaintext)}"))
# print("=========================================")
# high_plaintext = high_encrypt(high_plaintext)
# print(f"high en {hex(high_plaintext)}")
# high_plaintext = high_decrypt(high_plaintext)
# print(f"high de {hex(high_plaintext)}")