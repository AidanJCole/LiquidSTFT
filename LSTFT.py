# First we need to make a spectrogram, then we need to make the dynamic programming for it,
# then we run seam carving on it, and then once we run seam carving we have to figure out how to cut those parts of the stft out,
# then we have to run the inverse stft on those results and hopefully it results in something we can listen to. Who knows tho

from scipy.signal import stft, istft
from PIL import Image
from Lib import wave
from math import sin, pi, atan2, sqrt, log10

def sinebow(t):
    r = 127.5*sin(2*pi*t)+127.5
    g = 127.5*sin(2*pi*t+2*pi/3)+127.5
    b = 127.5*sin(2*pi*t+4*pi/3)+127.5


    return (int(r),int(g),int(b))

targetHertz = 100

file = wave.open("MLKDream.wav", "rb")

print(f"Channels: {file.getnchannels()}\nByte width: {file.getsampwidth()}\nFramerate:{file.getframerate()}\n")

test = list(memoryview(file.readframes(file.getnframes())).cast("h"))

f, n, Zxx = stft(test, window="hann", nperseg=512)

graphC = Image.new('RGB', Zxx.shape, 0)
graph = graphC.load()
max = 0
min = 5000000000
for x in range(Zxx.shape[0]):
    for y in range(Zxx.shape[1]):
        colorPhase = sinebow((atan2(Zxx[x,y].real, Zxx[x,y].imag)+pi/2)/pi)
        # maximum/min amp: 5363.286519380089 0.0
        magnitude = sqrt(Zxx[x,y].real**2 + Zxx[x,y].imag**2)
        temp = magnitude/32767
        db = 0
        if magnitude > 3.2767:
            db = 20 * log10(temp)
        else:
            db = -80

        val = (db+80)/80
        #color = (int(colorPhase[0]*val),int(colorPhase[1]*val),int(colorPhase[2]*val))
        color = (int(255 * val), int(255 * val), int(255 * val))
        graph[x,y] = color

graphC.save("test.png", "PNG")

print(max, min)
