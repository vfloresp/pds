#Víctor Hugo Flores Pineda 155990
#Rebeca Baños García 157655
#Python 3
import numpy as np 
import matplotlib.pyplot as plt

ts = np.linspace(0,1000,1000) / 1000
fs = 4
ys = np.cos(2*np.pi*fs*ts)

plt.subplot(611)
plt.title("Señal original")
plt.plot(ts,ys)

#Ejercicio 1

plt.subplot(612)
plt.title("16 muestras por periodo")
plt.plot(ts,ys)
t = np.linspace(0,1000,65) / 1000
y = np.cos(2*np.pi*fs*t)
plt.stem(t,y)

plt.subplot(613)
plt.title("8 muestras por periodo")
plt.plot(ts,ys)
t = np.linspace(0,1000,33) / 1000
y = np.cos(2*np.pi*fs*t)
plt.stem(t,y)

plt.subplot(614)
plt.title("4 muestras por periodo")
plt.plot(ts,ys)
t = np.linspace(0,1000,17) / 1000
y = np.cos(2*np.pi*fs*t)
plt.stem(t,y)

plt.subplot(615)
plt.title("2 muestras por periodo")
plt.plot(ts,ys)
t = np.linspace(0,1000,9) / 1000
y = np.cos(2*np.pi*fs*t)
plt.stem(t,y)

plt.subplot(616)
plt.title("1 muestras por periodo")
plt.plot(ts,ys)
t = np.linspace(0,1000,5) / 1000
y = np.cos(2*np.pi*fs*t)
plt.stem(t,y)


#Ejercicio 2
plt.figure()

plt.subplot(611)
plt.title("Señal original analógica")
plt.plot(ts,ys)

plt.subplot(612)
plt.title("Señal discreta")
t = np.linspace(0,1000,150) / 1000
y = 5*np.cos(2*np.pi*fs*t)
plt.stem(t,y)

plt.subplot(613)
plt.title("Señal discreta y cuantificada")
yRound = np.round(5*np.cos(2*np.pi*fs*t))
plt.stem(t,yRound)

plt.subplot(614)
plt.title("Error de cuantificación usando round")
yErrR = yRound - y
plt.stem(t,yErrR)

plt.subplot(615)
plt.title("Error de cuantificación usando floor")
yFloor = np.floor(5*np.cos(2*np.pi*fs*t))
yErrR = yFloor - y
plt.stem(t,yErrR)

plt.subplot(616)
plt.title("Error de cuantificación usando ceil")
yCeil = np.ceil(5*np.cos(2*np.pi*fs*t))
yErrR = yCeil - y
plt.stem(t,yErrR)


plt.show()
