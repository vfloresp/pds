#imports
import os
import matplotlib.pyplot as plt
import numpy as np
import scipy.signal
from scipy.io import wavfile as wv
import librosa.core as lc
from pydub import AudioSegment
from pydub.silence import split_on_silence

#variables
X = []
Y = []

def calcFormantes(directorio,asignacion):
    #plt.figure()
    #plt.title(directorio)
    for filename in os.listdir(directorio):
        global X
        global Y
        plt.figure()
        plt.title(filename)
        fs, x = wv.read(directorio+'/'+filename)
        n = len(x)
        ham = scipy.signal.hamming(n)
        mult = ham*x[:,1]
        y = scipy.signal.lfilter([1],[1,0.63],mult)
        a = lc.lpc(y,12)
        w, h = scipy.signal.freqz([0] + -1*a[1:], [1],n)
        plt.plot(w,h)
        aux = 0
        i = 0
        max = 0
        tupla = [0,0]
        while(aux<2 and i<len(h)):
            if(h[i]>max):
                max = h[i]
            else:
                tupla[aux] = np.real(h[i]*10000)
                aux = aux+1
                X.append(tupla)
                Y.append(asignacion)
            i = i+1
    

calcFormantes('./audios/A','A')
print(X)
print(Y)
#calcFormantes('./audios/E')
#calcFormantes('./audios/I')
#calcFormantes('./audios/O')
#calcFormantes('./audios/U')
plt.show()