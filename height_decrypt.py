import os
from height_plantext import *

#---------------------------------------HIGHT Decryption ---------------------------------------------

Y = []
def decrypt(plain):
    Y = []
    # Convert Int To Byte List
    h = hex(plain)
    ciphertext = []
    for i in range (2, len(h), 2):
        ciphertext.append(comp(format(int(h[i], 16), "b")) + comp(format(int(h[i+1], 16), "b")))
  
# initial round
    X1 = []
    X1.append(min_fun(ciphertext[0], keys["WK4"]))
    X1.append(ciphertext[1])
    X1.append(xor_fun(ciphertext[2], keys["WK5"]))
    X1.append(ciphertext[3])
    X1.append(min_fun(ciphertext[4], keys["WK6"]))
    X1.append(ciphertext[5])
    X1.append(xor_fun(ciphertext[6], keys["WK7"]))
    X1.append(ciphertext[7])
    Y.append(X1)
# middle round
    SKCount = 31
    for i in range(0,7):
        X1 = []      
        X1.append(Y[i][1])
        X1.append(min_fun(Y[i][2], xor_fun(f1(Y[i][1]) , keys["SK" + str(SKCount-3)])))
        X1.append(Y[i][3])
        X1.append(xor_fun(Y[i][4], or_fun(f0(Y[i][3]) , keys["SK" + str(SKCount-2)])))
        X1.append(Y[i][5])
        X1.append(min_fun( Y[i][6],  xor_fun(f1(Y[i][5]) , keys["SK" + str(SKCount-1)])))
        X1.append(Y[i][7])
        X1.append(xor_fun(Y[i][0],  or_fun(f0(Y[i][7]) , keys["SK" + str(SKCount)])))
        Y.append(X1)
        SKCount = SKCount - 4
# final round
    X1 = []      
    X1.append(Y[7][1])
    X1.append(min_fun(Y[7][2], xor_fun(f1(Y[7][1]) , keys["SK" + str(SKCount-3)])))
    X1.append(Y[7][3])
    X1.append(xor_fun(Y[7][4], or_fun(f0(Y[7][3]) , keys["SK" + str(SKCount-2)])))
    X1.append(Y[7][5])
    X1.append(min_fun( Y[7][6],  xor_fun(f1(Y[7][5]) , keys["SK" + str(SKCount-1)])))
    X1.append(Y[7][7])
    X1.append(xor_fun(Y[7][0],  or_fun(f0(Y[7][7]) , keys["SK" + str(SKCount)])))
    Y.append(X1)
    SKCount = SKCount - 4
# result cipher
    plain = []
    plain.append(min_fun(Y[8][0], keys["WK0"]))
    plain.append(Y[8][1])
    plain.append(xor_fun(Y[8][2], keys["WK1"]))
    plain.append(Y[8][3])
    plain.append(min_fun(Y[8][4], keys["WK2"]))
    plain.append(Y[8][5])
    plain.append(xor_fun(Y[8][6], keys["WK3"]))
    plain.append(Y[8][7])

    # Convert Result Byte List To the Fianl Hex Result
    cipherresult = "0x"
    for i in  range(0, len(plain)):
        cipherresult += str(hex(int(plain[i],2)))[2:] 
    simon_plaintext = int(cipherresult, 16) 
    return hex(simon_plaintext)

#---------------------------------------End HIGHT Decryption ----------------------------------------