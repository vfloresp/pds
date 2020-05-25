#python3
import matplotlib.pyplot as plt 
from scipy.io import wavfile as wv
from skimage.io import imread
from skimage import util
from scipy.fft import fft, fft2, ifft2
import numpy as np
from cv2 import VideoWriter, VideoWriter_fourcc
from sklearn.neighbors import KNeighborsClassifier
from scipy.signal import find_peaks


def real_imag2magn_phas(real, imag):
    magn = np.sqrt(real*real + imag*imag)
    phas = np.arctan2(imag, real)
    return magn, phas

def magn_phas2real_imag(magnitude, phase):
    real = magnitude * np.cos(phase)
    imag = magnitude * np.sin(phase)
    return real, imag


#Carga el archivo .wav
fs, x = wv.read('./Dont you know.wav')

#Divide el espectrograma por ventanas
spectrum1, freqs1, t1, im1 = plt.specgram(x[:,0],NFFT = 1600,Fs=fs, sides='onesided')
spectrum2, freqs2, t2, im2 = plt.specgram(x[:,1],NFFT = 1600,Fs=fs, sides='onesided')
N = len(x)
L = len(x) / fs
print(f"Rate: {fs} Hz")
print(f"Length (n): {N}")
print(f"Length (s): {L:.2f}")

#separar en canales
ch1 = x[:, 0]
ch2 = x[:, 1]

#Define ventana
stride_size = 1472
def slice_signal(in_signal):
    return(util.view_as_windows(in_signal, window_shape=(640,), step=stride_size))

int_ch1 = slice_signal(ch1)
int_ch2 = slice_signal(ch2)
print(f"Sliced channel 1: {int_ch1.shape}")
print(f"Sliced channel 2: {int_ch2.shape}")

n_int = int_ch1.shape[0]

#Espectro audio
X_ch1 = fft(int_ch1, axis=1)
mag_ch1, phs_ch1 = real_imag2magn_phas(X_ch1.real, X_ch1.imag)

X_ch2 = fft(int_ch2, axis=1)
mag_ch2, phs_ch2 = real_imag2magn_phas(X_ch2.real, X_ch2.imag)


#Carga imagen
img = imread('./mujer.jpg')
n_rows, n_cols, n_channs = img.shape
print(f"Number of rows: {n_rows}")
print(f"Number of columns: {n_cols}")
print(f"Number of channels: {n_channs}")
print(img.min())
print(img.max())

#Espectro RGB imagen
imgE = fft2(img)
mag_imgE, phs_imgE = real_imag2magn_phas(imgE.real, imgE.imag)

X = [[440.0],[220.0],[110.0],[55.0],[880.0],[1760.0],[3520.0],[7040.0],[14080.0],[349.2],[174.6],[87.3],[43.65],[698.4],[1396.8],[2793.6],[5587.2],[11174.4],[22348.8],[370.0],[185.0],[92.5],[46.25],[740.0],[1480.0],[2960.0],[5920.0],[11840.0],[23680.0],[392.0],[196.0],[98.0],[49.0],[784.0],[1568.0],[3136.0],[6272.0],[12544.0],[25088.0],[415.3],[207.65],[103.825],[51.91],[830.6],[1661.2],[33224.4],[6644.8],[13289.6],[26579.2],[466.2],[233.1],[116.55],[58.275],[932.4],[1864.8],[3729.6],[7459.2],[14918.4],[29836.8],[493.9],[246.95],[123.48],[61.74],[987.8],[1975.6],[3951.2],[7902.4],[15804.8],[31609.6],[523.2],[261.6],[130.8],[65.4],[1046.4],[2092.8],[4185.6],[8371.2],[16742.4],[33484.8],[554.4],[277.2],[138.6],[69.3],[1108.8],[2217.6],[4435.2],[8870.4],[17740.8],[35481.6],[587.3],[293.65],[146.83],[73.41],[1174.6],[2349.2],[4689.4],[9396.8],[18793.6],[37587.2],[622.2],[311.1],[155.55],[77.78],[1244.4],[2488.8],[4977.6],[9955.2],[19910.4],[39820.8],[659.3],[329.65],[164.83],[82.41],[1318.6],[2637.2],[5274.4],[10548.8],[21097.6],[42195.2],[698.5],[349.25],[174.63],[87.31],[1397.0],[2794.0],[5588.0],[11176.0],[22352.0],[44704.0]]
y = [[255,99,0],[255,99,0],[255,99,0],[255,99,0],[255,99,0],[255,99,0],[255,99,0],[255,99,0],[255,99,0],[82,0,0],[82,0,0],[82,0,0],[82,0,0],[82,0,0],[82,0,0],[82,0,0],[82,0,0],[82,0,0],[82,0,0],[116,0,0],[116,0,0],[116,0,0],[116,0,0],[116,0,0],[116,0,0],[116,0,0],[116,0,0],[116,0,0],[116,0,0],[179,0,0],[179,0,0],[179,0,0],[179,0,0],[179,0,0],[179,0,0],[179,0,0],[179,0,0],[179,0,0],[179,0,0],[238,0,0],[238,0,0],[238,0,0],[238,0,0],[238,0,0],[238,0,0],[238,0,0],[238,0,0],[238,0,0],[238,0,0],[255,236,0],[255,236,0],[255,236,0],[255,236,0],[255,236,0],[255,236,0],[255,236,0],[255,236,0],[255,236,0],[255,236,0],[153,255,0],[153,255,0],[153,255,0],[153,255,0],[153,255,0],[153,255,0],[153,255,0],[153,255,0],[153,255,0],[153,255,0],[40,255,0],[40,255,0],[40,255,0],[40,255,0],[40,255,0],[40,255,0],[40,255,0],[40,255,0],[40,255,0],[40,255,0],[0,255,232],[0,255,232],[0,255,232],[0,255,232],[0,255,232],[0,255,232],[0,255,232],[0,255,232],[0,255,232],[0,255,232],[0,124,255],[0,124,255],[0,124,255],[0,124,255],[0,124,255],[0,124,255],[0,124,255],[0,124,255],[0,124,255],[0,124,255],[5,0,255],[5,0,255],[5,0,255],[5,0,255],[5,0,255],[5,0,255],[5,0,255],[5,0,255],[5,0,255],[5,0,255],[69,0,234],[69,0,234],[69,0,234],[69,0,234],[69,0,234],[69,0,234],[69,0,234],[69,0,234],[69,0,234],[69,0,234],[87,0,158],[87,0,158],[87,0,158],[87,0,158],[87,0,158],[87,0,158],[87,0,158],[87,0,158],[87,0,158],[87,0,158]]
neigh = KNeighborsClassifier(n_neighbors=2)
neigh.fit(X, y)

#globalMax1 = max(map(max,mag_ch1))
#globalMax2 = max(map(max,mag_ch2))

globalMax1 = max(map(sum,mag_ch1))
globalMax2 = max(map(sum,mag_ch2))


#modulacion del audio a imagen
def modulate(IMG, modulator1,modulator2,f1,f2):
    global globalMax1, globalMax2
    peaks1 = find_peaks(f1, height=1)
    peaks2 = find_peaks(f2, height=1)
    
    total1 = sum(peaks1[1]['peak_heights'])
    total2 = sum(peaks2[1]['peak_heights'])

    proportion1 = []
    for val1 in peaks1[1]['peak_heights']:
        proportion1.append(val1/total1)
    
    proportion2 = []
    for val2 in peaks2[1]['peak_heights']:
        proportion2.append(val2/total2)
            
    color1 = []
    for ind1 in peaks1[0]:
        color1.append(neigh.predict([[freqs1[int(ind1)]]])[0])

    color2 = []
    for ind2 in peaks2[0]:
        color2.append(neigh.predict([[freqs2[int(ind2)]]])[0])

    for i in range(0,n_rows,8):
        for j in range(0,int((n_cols/2)-1),8):
            if ((sum(modulator1)/globalMax1))>np.random.rand():
                if (modulator1[i]/max(modulator1))>np.random.rand():
                    try:
                        col = color1[np.random.choice(range(0,len(color1)),p=proportion1)]
                        if i>640-4:
                            i = i-3
                        if j>480-4:
                            j = j-3
                        IMG[i,j] = col
                        IMG[i,j+1] = col
                        IMG[i,j+2] = col
                        IMG[i,j+3] = col
                        IMG[i+1,j] = col
                        IMG[i+1,j+1] = col
                        IMG[i+1,j+2] = col
                        IMG[i+1,j+3] = col
                        IMG[i+2,j] = col
                        IMG[i+2,j+1] = col
                        IMG[i+2,j+2] = col
                        IMG[i+2,j+3] = col
                        IMG[i+3,j] = col
                        IMG[i+3,j+1] = col
                        IMG[i+3,j+2] = col
                        IMG[i+3,j+3] = col
                    except:
                        print('no color')

    for i in range(0,n_rows,8):
        for j in range(int((n_cols/2)-1),n_cols,8):
            if ((sum(modulator1)/globalMax1))>np.random.rand():
                if (modulator2[i]/max(modulator2))>np.random.rand():
                    try:
                        col = color2[np.random.choice(range(0,len(color2)),p=proportion2)]
                        if i>640-4:
                            i = i-3
                        if j>480-4:
                            j = j-3
                        IMG[i,j] = col
                        IMG[i,j+1] = col
                        IMG[i,j+2] = col
                        IMG[i,j+3] = col
                        IMG[i+1,j] = col
                        IMG[i+1,j+1] = col
                        IMG[i+1,j+2] = col
                        IMG[i+1,j+3] = col
                        IMG[i+2,j] = col
                        IMG[i+2,j+1] = col
                        IMG[i+2,j+2] = col
                        IMG[i+2,j+3] = col
                        IMG[i+3,j] = col
                        IMG[i+3,j+1] = col
                        IMG[i+3,j+2] = col
                        IMG[i+3,j+3] = col
                    except:
                        print('no color')

    return(IMG)

# Genera cada frame del nuevo video
out_images = []
for ind_interval in range(3000,3600):
    freq1 = []
    for val in spectrum1:
        freq1.append(val[ind_interval]*1000000)
    
    freq2 = []
    for val in spectrum2:
        freq2.append(val[ind_interval]*1000000)


    img_mod =  modulate(img, mag_ch1[ind_interval, :], mag_ch2[ind_interval, :],freq1,freq2)
    #img_mod = ifft2(img_mod)
    img_mod = np.round(255 * img_mod).astype('uint8') # Formato para guardar en disco
    out_images.append(img_mod)
    print(ind_interval)

# Save sequence of frames to disk
out = VideoWriter('frame_seq_fast4.mp4', VideoWriter_fourcc(*'MP4V'), 30, (480, 640))
for im in out_images:
    out.write(im)
out.release()




