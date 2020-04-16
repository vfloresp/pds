#Víctor Hugo Flores Pineda 155990
#Rebeca Baños García 157655
#Python 3
import matplotlib.pyplot as plt
import numpy as np
import scipy.signal
from scipy.io import wavfile as wv
import librosa.core


fs, data = wv.read('./camaraA.wav')
n = len(data)
ham = scipy.signal.hamming(n)
mult = ham*data[:,1]
y = scipy.signal.lfilter([1],[1,0.63],mult)
a = librosa.core.lpc(y,10)
h, w = scipy.signal.freqz([1],a,n)

plt.plot(abs(h))
plt.figure()
plt.plot(abs(w))

plt.show()