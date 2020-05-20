#imports
import tkinter as tk
from tkinter import filedialog
import sounddevice as sd
from scipy.io.wavfile import write
from PIL import Image, ImageTk
from back_end import frase, palabra, frase_palabras


#variables
audio = ''

#crear objeto de ventana
window = tk.Tk()
window.geometry('850x800')
window.title('Voz a texto')


LA = tk.Label(window,text='Archivo: ')
LA.grid(row=0,column=0,padx=20,pady=20,columnspan=2)

eA = tk.Entry(window)
eA.grid(row=0,column=2,columnspan=4,padx=10,pady=20)
eA.config(width=70)

#seleccionar audio del explorador de archivos
def open_file():
    window.filename = filedialog.askopenfilename(initialdir ="./",title= "Seleccione el archivo de audio")
    eA.delete(0,tk.END)
    eA.insert(0,window.filename)
    global audio 
    audio = window.filename
 
bA = tk.Button(window,text="seleccionar", command = open_file)
bA.grid(row=0,column=7,padx=10,pady=10)

#crear grabacion de audio
def record_file():
    fs = 44100  # Sample rate
    seconds = 10  # Duration of recording
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()  # Wait until recording is finished
    write('./audios/recorded.wav', fs, myrecording)  # Save as WAV file
    eA.delete(0,tk.END)
    eA.insert(0,'./audios/recorded.wav')
    global audio
    audio =  './audios/recorded.wav'

def popUp():
    pop = tk.Toplevel()
    lG = tk.Label(pop,text="Grabando...")
    lG.grid(row=3,column=3,padx=30,pady=30)
    record_file()

bG = tk.Button(window,text="Grabar", command = popUp)
bG.grid(row=1,column=7,padx=10,pady=0)

#convertir audio a texto (ver back end)
def convertir():
    nameT,nameE = frase(audio)

    global imgT
    original = Image.open(nameT)
    resized = original.resize((330, 330),Image.ANTIALIAS)
    imgT = ImageTk.PhotoImage(resized)
    LIT['image']=imgT
    global imgE
    original = Image.open(nameE)
    resized = original.resize((330, 330),Image.ANTIALIAS)
    imgE = ImageTk.PhotoImage(resized)
    LIE['image']=imgE

    frase_palabras(audio)

bI = tk.Button(window,text='Convertir', command=convertir)
bI.grid(row=3,column=7,padx=20,pady=35)

LR = tk.Label(window,text="Resultado:")
LR.grid(row=4,column=0,padx=20,pady=10)

L1 = tk.Listbox(window,heigh=5,width=85)
L1.grid(row=5,column=0,columnspan=5,padx=20)

LT = tk.Label(window,text="Tiempo")
LT.grid(row=6,column=0,padx=10,pady=20)

LE = tk.Label(window,text="Espectrograma")
LE.grid(row=6,column=3,padx=15,pady=20)

LIT = tk.Label(window)
LIT.grid(row=7,column=0,columnspan=3, padx=20,pady=10)

LIE = tk.Label(window)
LIE.grid(row=7,column=3,columnspan=3, padx=10,pady=10)



window.mainloop()