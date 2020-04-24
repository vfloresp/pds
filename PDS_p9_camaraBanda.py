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
plt.plot(t,x)

#4
plt.figure()
plt.specgram(x[:,1],NFFT = 1024,Fs=fs, sides='onesided' )
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
#plt.show()


#5
f, t, Sxx = signal.spectrogram(x, fs,window=('hamming',1024),return_onesided=True)


#print(f)
#print(t)
#print(Sxx)



