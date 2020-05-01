#Víctor Hugo Flores Pineda 155990
#Rebeca Baños García 157655
#Python 3
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
from scipy.io import wavfile as wv

#1
fs, x = wv.read('./audios/HolaMundo.wav')

#2
n = len(x)
t = np.linspace(0,np.round(n/fs),n)
plt.xlabel('tiempo')
plt.ylabel('Amplitud')
plt.plot(t,x)


#4
plt.figure()
plt.specgram(x[:,1],NFFT = 2048,Fs=fs, sides='onesided' )
plt.ylabel('Normalized Frequency')
plt.xlabel('Samples')



#5
spectrum, freqs, t, im = plt.specgram(x[:,1],NFFT = 2048,Fs=fs, sides='onesided')

#o
plt.figure()
plt.title('transiente O')
plt.xlabel('Frecuencia')
plt.ylabel('Amplitud')
plt.plot(spectrum[160])

#a
plt.figure()
plt.title('transiente A')
plt.xlabel('Frecuencia')
plt.ylabel('Amplitud')
plt.plot(spectrum[230])

#u
plt.figure()
plt.title('transiente U')
plt.xlabel('Frecuencia')
plt.ylabel('Amplitud')
plt.plot(spectrum[332])

#o
plt.figure()
plt.title('transiente O')
plt.xlabel('Frecuencia')
plt.ylabel('Amplitud')
plt.plot(spectrum[436])

plt.show()

