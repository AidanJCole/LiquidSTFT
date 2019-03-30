# First we need to make a spectrogram, then we need to make the dynamic programming for it,
# then we run seam carving on it, and then once we run seam carving we have to figure out how to cut those parts of the stft out,
# then we have to run the inverse stft on those results and hopefully it results in something we can listen to. Who knows tho

from scipy.signal import stft, istft
from PIL import Image
from Lib import wave
from math import sin, pi, atan2, sqrt

def sinebow(t):
    r = 128*sin(2*pi*t)+128
    g = 128*sin(2*pi*t+2*pi/3)+128
    b = 128*sin(2*pi*t+4*pi/3)+128

    return (r,g,b)

targetHertz = 100

file = wave.open("MLKDream.wav", "rb")

print(f"Channels: {file.getnchannels()}\nByte width: {file.getsampwidth()}\nFramerate:{file.getframerate()}\n")

test = list(memoryview(file.readframes(file.getnframes())).cast("h"))

temp = stft(test, window="hann", nperseg=256)




