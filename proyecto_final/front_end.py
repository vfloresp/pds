#imports
import tkinter as tk
from tkinter import filedialog

#crear objeto de ventana
window = tk.Tk()
window.title('Voz a texto')

LA = tk.Label(window,text='Archivo: ')
LA.grid(row=0,column=0)

eA = tk.Entry(window)
eA.grid(row=0,column=1,columnspan=2)

def open_file():
    window.filename = filedialog.askopenfilename(initialdir ="./",title= "Seleccione el archivo de audio")
    eA.delete(0,tk.END)
    eA.insert(0,window.filename)

bA = tk.Button(window,text="seleccionar", command = open_file)
bA.grid(row=0,column=3)





window.mainloop()