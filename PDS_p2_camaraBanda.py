#Víctor Hugo Flores Pineda 155990
#Rebeca Baños García 157655
#Python 3
import numpy as np 
import matplotlib.pyplot as plt
import huffman as hf

#1
x = np.random.randint(1,6,20)
print(x)

#2
xB = np.zeros(20)
for i in range(0,20):
    xB[i] = np.binary_repr(x[i],3)
print(xB)

longT = 0
for i in range(0,20):
    longT = longT + len(str(xB[i])) -2
print("Longitud total de cadena bianria: " + str(longT))
longP = longT/20
print("Longitud pormedio por simbolo: " + str(longP))

#4
#Seis bits

#4
def prob(vec):
    p = np.zeros(5)
    for i in range(0,20):
        if vec[i] == 1:
            p[0] = p[0] + 1
        elif vec[i] == 2:
            p[1] = p[1] +1
        elif vec[i] == 3:
            p[2] = p[2] +1
        elif vec[i] == 4:
            p[3] = p[3] + 1
        else:
            p[4] = p[4] +1
    for i in range(0,5):
        p[i] = p[i]/20
    return p

probabilidad = prob(x)
print(probabilidad)

#5 
huffVec = ([('1',probabilidad[0]*20), ('2',probabilidad[1]*20), ('3',probabilidad[2]*20), ('4',probabilidad[3]*20),('5',probabilidad[4]*20)])
xH = hf.codebook(huffVec)
print(xH)
longT = len(xH['1']) + len(xH['2']) + len(xH['3']) + len(xH['4']) + len(xH['5'])
print("Longitud total de cadena Huffman: " + str(longT))
longP = longT/5
print("Longitud pormedio por simbolo: " + str(longP))