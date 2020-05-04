#Víctor Hugo Flores Pineda 155990
#Rebeca Baños García 157655
#Python 3
import matplotlib.pyplot as plt
import numpy as np
import scipy.signal
from scipy.io import wavfile as wv
import librosa.core as lc


fs, x = wv.read('./audios/camaraA.wav')
n = len(x)
ham = scipy.signal.hamming(n)
mult = ham*x[:,1]
y = scipy.signal.lfilter([1],[1,0.63],mult)
a = lc.lpc(y,10)
y_hat = scipy.signal.lfilter([0] + -1*a[1:], [1], y)
plt.plot(y)
plt.plot(y_hat,'g--')

w, h = scipy.signal.freqz([0] + -1*a[1:], [1],n)
FFT = scipy.fftpack.fft(x)
plt.figure()
plt.plot(w,h,'C1')
plt.plot(w,FFT,'g')




plt.show()