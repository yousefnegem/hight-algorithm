import os
from height_plantext import *

#---------------------------------------Start HIGHT Encryption ----------------------------------------
X = []
ciphertext = []
def encrypt(plain):
    X = []

    # Convert Int To Byte List
    h = hex(plain)
    # print(f"plain {h}")
    plaintext = []
    for i in range (2, len(h), 2):
        plaintext.append(comp(format(int(h[i], 16), "b")) + comp(format(int(h[i+1], 16), "b")))

# initial round
    X1 = []   
    X1.append(or_fun(plaintext[0], keys['WK0']))
    X1.append(complate(plaintext[1]))
    X1.append(xor_fun(plaintext[2], keys['WK1']))
    X1.append(plaintext[3])
    X1.append(or_fun(plaintext[4] , keys['WK2']))
    X1.append(plaintext[5])
    X1.append(xor_fun(plaintext[6], keys['WK3']))
    X1.append(plaintext[7])
    X.append(X1)
# middle round
    for i in range(0, 7): 
        X1 = []
        X1.append(xor_fun(X[i][7], or_fun(f0(X[i][6]) , keys["SK" + str(4*i+3)])))
        X1.append(X[i][0])
        X1.append(or_fun(X[i][1], xor_fun(f1(X[i][0]) , keys["SK" + str(4*i)])))
        X1.append(X[i][2])
        X1.append(xor_fun( X[i][3],  or_fun(f0(X[i][2]) , keys["SK" + str(4*i+1)])))
        X1.append(X[i][4])
        X1.append(or_fun( X[i][5],  xor_fun(f1(X[i][4]) , keys["SK" + str(4*i+2)])))
        X1.append(X[i][6])
        X.append(X1)
# final round
    X1 = []
    X1.append(xor_fun(X[7][7], or_fun(f0(X[7][6]) , keys["SK" + str(4*7+3)])))
    X1.append(X[7][0])
    X1.append(or_fun(X[7][1], xor_fun(f1(X[7][0]) , keys["SK" + str(4*7)])))
    X1.append(X[7][2])
    X1.append(xor_fun( X[7][3],  or_fun(f0(X[7][2]) , keys["SK" + str(4*7+1)])))
    X1.append(X[7][4])
    X1.append(or_fun( X[7][5],  xor_fun(f1(X[7][4]) , keys["SK" + str(4*7+2)])))
    X1.append(X[7][6])
    X.append(X1)
# result cipher
    ciphertext = []
    ciphertext.append(or_fun(X[8][0], keys["WK4"] ))
    ciphertext.append(X[8][1])
    ciphertext.append(xor_fun(X[8][2], keys["WK5"] ))
    ciphertext.append(X[8][3])
    ciphertext.append(or_fun(X[8][4], keys["WK6"] ))
    ciphertext.append(X[8][5])
    ciphertext.append(xor_fun(X[8][6], keys["WK7"] ))
    ciphertext.append(X[8][7])

    # Convert Result Byte List To the Fianl Hex Result
    cipherresult = "0x"
    for i in  range(0, len(ciphertext)):
        cipherresult += str(hex(int(ciphertext[i],2)))[2:]
    return cipherresult
#---------------------------------------End HIGHT Encryption ----------------------------------------   