#Víctor Hugo Flores Pineda 155990
#Rebeca Baños García 157655
#Python 3
import numpy as np 
import matplotlib.pyplot as plt
import scipy.signal as sg


def tranformadaFourier(f,fs):
    plt.figure()
    t = np.linspace(0,100,5000)/fs
    y = np.sin(2*np.pi*t*f)
    plt.subplot(211)
    plt.title('Señal sinusoidal con f= ' + str(f) + ' fs = '+str(fs) )
    plt.plot(t,y)

    y = np.fft.fft(y,2048)
    x = np.linspace(0,fs,2048)
    plt.subplot(212)
    plt.title('fft con f= ' + str(f) + ' fs = '+str(fs) )
    plt.plot(x,abs(y))

    plt.figure()
    y = sg.square(2*np.pi*f*t)
    plt.subplot(211)
    plt.title('Señal cuadrada con f= ' + str(f) + ' fs = '+str(fs) )
    plt.plot(t,y)

    y = np.fft.fft(y,2048)
    x = np.linspace(0,fs,2048)
    plt.subplot(212)
    plt.title('fft con f= ' + str(f) + ' fs = '+str(fs) )
    plt.plot(x,abs(y))

tranformadaFourier(5,100)
tranformadaFourier(10,100)
tranformadaFourier(5,50)
tranformadaFourier(10,50)

plt.show()