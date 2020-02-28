#Víctor Hugo Flores Pineda 155990
#Rebeca Baños
#Python 3
import numpy as np 
import matplotlib.pyplot as plt
import control
from scipy.fftpack import fft, ifft
from scipy import signal



#Encontrar la fucnion de transferencia
#Usar signal.tf2zpk para encontrar polos y zeros de cada función


def TranformadaZ(titutlo,num,den):
    h1 = control.TransferFunction(num,den)
    [zeros,poles,gain] = signal.tf2zpk(num,den)
    print(titutlo)
    print("zeros")
    print(zeros)
    print("polos ")
    print(poles)
    print("\n")

    control.pzmap(h1, Plot=True, grid=False, title=titutlo)
    [t,y] = signal.impulse( (num,den) )
    plt.figure()
    plt.suptitle(titutlo)
    plt.plot(t, y)
    plt.title('Respuesta al impulso')    

#A
num = [4,-5]
den = [2,-5,2]
TranformadaZ("A",num,den)


#B
num = [2]
den = [1,0,-1]
TranformadaZ("B",num,den)


#C
num = [2]
den = [1,-3/4,1/8]
TranformadaZ("C",num,den)

#D
num = [4,3]
den = [4,-3,2,-1]
TranformadaZ("D",num,den)

#E
num = [1]
den = [1,0,-1j]
TranformadaZ("E",num,den)

#F
num = [2,1]
den = [1,-2,3]
TranformadaZ("F",num,den)


plt.show()