from height_plantext import *


def shfit1(x):
    x = complate(x)
    result = x[7:8] + x[0:1]  + x[1:7] 
    return result



def shfit2(x):
    x = complate(x)
    result = x[6:8] + x[0:1]  + x[1:6] 
    return result


# def shfit4(x):
#     x = complate(x)
#     result = x[4:8] + x[0:1]  + x[1:6] 
    # return result


# y ="01111110" 
# print(shfit2(y))



def simon_encrypt(plain):
    h = plain
    plaintext = []
    for i in range (0, len(h), 2):
        plaintext.append(comp(format(int(h[i], 16), "b")) + comp(format(int(h[i+1], 16), "b")))
    Left = plaintext[0:4]
    right = plaintext[4:8]

    # print(Left)
    # print(right)

    # for i in range (1, 10):
    #     f(1)

    # for i in range(1, 10):
    #     f = 

simon_encrypt("1f12c070f01210f0")



skey = []
def key():
    with open(str(os.path.dirname(__file__)) + "/keys.csv") as file:
        reader = csv.reader(file)
        for row in reader:
            skey.append(format(int(row[0], 16), "b"))
    print(skey)


# key()