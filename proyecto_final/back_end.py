#imports
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
from scipy.io import wavfile as wv
from pydub import AudioSegment
from pydub.silence import split_on_silence
import os, shutil
from scipy.io import wavfile as wv

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
    return res

#analiza cada palabra
def palabra(directorio):
    for filename in os.listdir(directorio):
        plt.figure()
        fs, x = wv.read(directorio+'/'+filename)
        n = len(x)
        if((n/fs)>0.5):
            spectrum, freqs, t, im = plt.specgram(x[:,1],NFFT = 1024,Fs=fs, sides='onesided')
            plt.plot(spectrum[213])
    plt.show()

#analiza la frase completa y gráfica tanto en el tiempo como espectrograma
def frase(filePath):
    fs, x = wv.read(filePath)

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

    