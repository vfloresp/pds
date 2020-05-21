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
        #plt.figure()
        #plt.title(filename)
        fs, x = wv.read(directorio+'/'+filename)
        n = len(x)
        ham = scipy.signal.hamming(n)
        mult = ham*x[:,1]
        y = scipy.signal.lfilter([1],[1,0.63],mult)
        a = lc.lpc(y,12)
        w, h = scipy.signal.freqz([0] + -1*a[1:], [1],n)
        tupla = findForm(w,h)
        if tupla[0]!=0 and tupla[1]!=0:    
            X.append(tupla)
            Y.append(asignacion)

def findForm(freq,signal):
    aux = 0
    MaxMin = 0
    i = 25000
    max = 0
    tupla = [0,0]
    if signal[i+1] < signal[i]:
        MaxMin = 1
    while(aux<2 and i<len(signal)):
        if MaxMin==0:
            if(signal[i]>max):
                max = signal[i]
            else:
                tupla[aux] = np.real(freq[i])
                aux = aux+1
                MaxMin = 1
        else:
            if max < signal[i]:
                MaxMin=0
            max = signal[i]
        i = i+1
    return tupla
    

calcFormantes('./audios/A',0)
calcFormantes('./audios/E',1)
calcFormantes('./audios/I',2)
calcFormantes('./audios/O',3)
calcFormantes('./audios/U',4)
#plt.show()

f = open("scikit_param.py","w+")
f.write("#Python 3 \n")
f.write("#Valores calculados de la base de datos en formato para scikit \n")
f.write("X = "+str(X)+"\n")
f.write("Y = "+str(Y)+"\n")