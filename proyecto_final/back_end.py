#imports
import matplotlib.pyplot as plt
import numpy as np
from sklearn.neighbors import RadiusNeighborsClassifier
from scipy import signal
from scipy.io import wavfile as wv
from pydub import AudioSegment
from pydub.silence import split_on_silence
import os, shutil
from scipy.io import wavfile as wv
from scikit_param import X, Y

#separa la frase en palabras
def frase_palabras(filePath):
    #Borra los archivos en el directorio
    folder = './audios/split_audios/'
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        os.unlink(file_path)
    #Genera un nuevo archivo por palabra
    sound_file = AudioSegment.from_wav(filePath)
    audio_chunks = split_on_silence(sound_file, min_silence_len=300, silence_thresh=-32)
    for i, chunk in enumerate(audio_chunks):
        out_file = "./audios/split_audios/chunk{0}.wav".format(i)
        print ("exporting " + out_file)
        chunk.export(out_file, format="wav")
    res = palabra(folder)
    return res.lstrip()

#analiza cada palabra
def palabra(directorio):
    global X,Y
    words = ''
    neigh = RadiusNeighborsClassifier(radius=1.0)
    neigh.fit(X, Y)
    for filename in os.listdir(directorio):
        word = ' '
        fs, x = wv.read(directorio+'/'+filename)
        n = len(x)
        if((n/fs)>0.5):
            spectrum, freqs, t, im = plt.specgram(x[:,1],NFFT = 1024,Fs=fs, sides='onesided')
            for i in range(len(spectrum)):
                point = findForm(np.linspace(0,2.4,len(spectrum[i])),spectrum[i])
                if point[0]!= 0 and point[1] != 0:
                    try:
                        print(point)
                        val = neigh.predict([point])
                        char = valores(val[0])
                        if word[-1] != char:
                            word = word + char
                    except:
                        print('No neighbors found for the given radius')
        words = words + ' ' + word
    return words

def valores(val):
    if val == 0:
        return 'a'
    elif val == 1:
        return 'e'
    elif val == 2:
        return 'i'
    elif val == 3:
        return 'o'
    elif val == 4:
        return 'u'
    else:
        return -1

def findForm(freq,signal):
    aux = 0
    MaxMin = 0
    i = 0
    max = 0
    tupla = [0,0]
    maxVal = 0.5*np.max(signal) 
    if np.real(signal[i+1]) < np.real(signal[i]):
        MaxMin = 1
    while(aux<2 and i<len(signal)):
        if MaxMin==0:
            if(np.real(signal[i])>max):
                max = np.real(signal[i])
            else:
                if(np.real(signal[i])>maxVal):
                    tupla[aux] = freq[i]
                    aux = aux+1
                MaxMin = 1
        else:
            if max < np.real(signal[i]):
                MaxMin=0
            max = np.real(signal[i])
        i = i+1
    return tupla
    

#analiza la frase completa y gráfica tanto en el tiempo como espectrograma
def frase(filePath):
    fs, x = wv.read(filePath)

    plt.figure()
    n = len(x)
    t = np.linspace(0,np.round(n/fs),n)
    plt.xlabel('tiempo')
    plt.ylabel('Amplitud')
    plt.plot(t,x)
    nameT = './imgs/tiempo.png'
    plt.savefig(nameT)

    plt.figure()
    plt.specgram(x[:,1],NFFT = 1024,Fs=fs, sides='onesided' )
    plt.ylabel('Normalized Frequency')
    plt.xlabel('Samples')
    nameE = './imgs/espectrograma.png'
    plt.savefig(nameE)

    return [nameT,nameE]

    