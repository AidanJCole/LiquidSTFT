# First we need to make a spectrogram, then we need to make the dynamic programming for it,
# then we run seam carving on it, and then once we run seam carving we have to figure out how to cut those parts of the stft out,
# then we have to run the inverse stft on those results and hopefully it results in something we can listen to. Who knows tho

from scipy.signal import stft, istft
from PIL import Image
from Lib import wave

file = wave.open("MLKDream.wav", "rb")

print(f"Channels: {file.getnchannels()}\nByte width: {file.getsampwidth()}\nFramerate:{file.getframerate()}\n")
