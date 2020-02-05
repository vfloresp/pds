#Víctor Hugo Flores Pineda 155990
#Rebeca Baños García 157655
#Python 3

import numpy as np 
import matplotlib.pyplot as plt

t = np.linspace(0,1000,1000) / 1000
fs = 4
y = np.cos(2*np.pi*fs*t)

plt.subplot(611)
plt.title("Señal original")
plt.plot(t,y)


plt.subplot(612)

t = np.linspace(0,1000,1000) / 1000
y = np.cos(2*np.pi*fs*t)
plt.plot(t,y)
plt.title("16 muestras por periodo")
t = np.linspace(1,1000,48) / 1000
y = np.cos(2*np.pi*fs*t)
plt.stem(t,y)

t = np.linspace(1,1000,24) / 1000
y = np.cos(2*np.pi*fs*t)
plt.subplot(613)
plt.title("8 muestras por periodo")
plt.stem(t,y)

t = np.linspace(1,1000,12) / 1000
y = np.cos(2*np.pi*fs*t)
plt.subplot(614)
plt.title("4 muestras por periodo")
plt.stem(t,y)

t = np.linspace(1,1000,6) / 1000
y = np.cos(2*np.pi*fs*t)
plt.subplot(615)
plt.title("2 muestras por periodo")
plt.stem(t,y)

t = np.linspace(1,1000,3) / 1000
y = np.cos(2*np.pi*fs*t)
plt.subplot(616)
plt.title("1 muestras por periodo")
plt.stem(t,y)



plt.show()
