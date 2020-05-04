#Víctor Hugo Flores Pineda 155990
#Rebeca Baños García 157655
#Python 3
import matplotlib.pyplot as plt
import numpy as np
import scipy.signal
from scipy.io import wavfile as wv
import librosa.core


fs, x = wv.read('./audios/camaraA.wav')
n = len(x)
ham = scipy.signal.hamming(n)
mult = ham*x[:,1]
y = scipy.signal.lfilter([1],[1,0.63],mult)
a = librosa.core.lpc(y,10)
h, w = scipy.signal.freqz([1],a,n)

raices = np.roots(a)



Ftransform = np.fft.fft(x)
plt.figure()
plt.plot(Ftransform)

plt.show()