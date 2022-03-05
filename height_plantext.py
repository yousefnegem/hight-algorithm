import csv
import os
import simon

#------------------------------------------------------------------------------   
#Read the plaintext For High Algorithm from the csv file
def read_high_plaintext():
    plaintext = []
    with open(str(os.path.dirname(__file__)) + "/temperature.csv") as file:
        reader = csv.reader(file)
        for row in reader:
            for i in range (0, 8):
                plaintext.append(complate((format(int(row[i], 16), "b"))))
    cipherresult = "0x"
    for i in  range(0, len(plaintext)):
        cipherresult += str(hex(int(plaintext[i],2)))[2:]
    plaintext = int(cipherresult, 16)       
    return plaintext

#Read the plaintext For Simon Algorithm from the csv file
def read_simon_plaintext():
    simon_plaintext1 = []
    simon_value = 0
    with open(str(os.path.dirname(__file__)) + "/temperature.csv") as file:
        reader = csv.reader(file)
        for row in reader:
            for i in range (8, 16):
                simon_plaintext1.append(complate((format(int(row[i], 16), "b"))))
    cipherresult = "0x"
    for i in  range(0, len(simon_plaintext1)):
        cipherresult += str(hex(int(simon_plaintext1[i],2)))[2:]
    simon_value = int(cipherresult, 16)
    return simon_value

#------------------------------------------------------------------------------                
#The generation of whitening keys is defined as follows
#Read the keys from the csv file
keys = {}
def read_keys():
    countsk = 0 
    countwk = 0
    with open(str(os.path.dirname(__file__)) + "/keys.csv") as file:
        reader = csv.reader(file)
        for row in reader:
            start = 0 
            end = 7
            for i in range (0, len(row)):
                tempStr =  ((format(int(row[i], 16), "b")))
                if(len(keys) == 0 or countsk >= 31):
                    for i in range(0 , 4):
                        #The read of whitening keys is defined as follows: 
                        keys['WK' + str(countwk) ] = complate(tempStr[start: end])
                        start = end + 1 
                        end = end + 8
                        countwk += 1
                else :
                    for i in range(0 , 4): 
                        #The read of subkeys is defined as follows:
                        keys['SK' + str(countsk) ] = complate(tempStr[start: end])
                        start = end + 1 
                        end = end + 8
                        countsk += 1

#------------------------------------------------------------------------------
# Round function 0 (F0)   
def f0(x):
    m = ""
    if(len(x) < 8):
        for i in range(0, 8-len(x)):
            x = "0" + x
    result = xor_fun(x[1:8] + x[0:1], x[2:8] + x[0:2])
    result = xor_fun(result, x[7:8] + x[0:7])
    return result

#------------------------------------------------------------------------------
# Round function 1 (F1)
def f1(x):
    m = ""
    if(len(x) < 8):
        for i in range(0, 8-len(x)):
            x = "0" + x
    result = xor_fun(x[3:8] + x[0:3], x[4:8] + x[0:4])
    result = xor_fun(result, x[6:8] + x[0:6])
    return result

#------------------------------------------------------------------------------
# function bitwise XOR  
def xor_fun(num1, num2):
    x = "" 
    n1 = complate(num1)
    n2 = complate(num2)
    for i in range(0, 8):
        x += str(int(n1[i]) ^ int(n2[i]))
    return x

#------------------------------------------------------------------------------
# function addition in modular (2**8)  
def or_fun(num1, num2):
    x = "" 
    n1 = complate(num1)
    n2 = complate(num2)
    for i in range(0, 8):
        x += str((int(n1[i]) + int(n2[i])) % 2)
    return x

#------------------------------------------------------------------------------
# function subtraction in modular (2**8)
def min_fun(num1, num2):
    x = "" 
    n1 = complate(num1)
    n2 = complate(num2)
    for i in range(0, 8):
        x += str((int(n1[i]) - int(n2[i])) % 2)
    return x 

#-------------------------------------------------------------------------------   
#Complete Two byte zeros
def complate(binary):
    if(len(binary) < 8):
        for i in range(0, 8-len(binary)):
            binary = "0" + binary
    return binary

#-------------------------------------------------------------------------------
#Complate Sinagle byte Zeros 
def comp(binary):
    if(len(binary) < 4):
        for i in range(0, 4-len(binary)):
            binary = "0" + binary
    return binary