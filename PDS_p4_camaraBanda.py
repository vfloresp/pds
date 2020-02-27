#Víctor Hugo Flores Pineda 155990
#Rebeca Baños García 157655
#Python 3
import sounddevice as sd 
import matplotlib.pyplot as plt
import numpy as np
from scipy.io.wavfile import write
from scipy.io import wavfile as wv
from scipy.fftpack import fft,fftfreq

#Parámetros y metolología usada para obtener las grabaciones
#fs = 44100
#seconds = 2

#my_recording = sd.rec(int(seconds * fs), samplerate = fs, channels = 2)
#sd.wait()
#write('camaraU.wav',fs,my_recording)

fs, data = wv.read('./camaraA.wav')

#print(fs)
#print(data)
#y = np.fft.fft(data,256)
datafft = fft(data)
#Get the absolute value of real and complex component:
fftabs = abs(datafft)
plt.plot(fftabs)
plt.figure()
plt.plot(data)
plt.show()
