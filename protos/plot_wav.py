from os import listdir, rename, mkdir
from os.path import isfile, join, dirname, basename
from scipy.io import wavfile 

import matplotlib.pyplot as plt

wav_path = input("Path: ")

wavs = [f for f in listdir(wav_path) if isfile(join(wav_path, f)) and f[-3:] == "wav"]

for w in wavs:
    print(wavs.index(w),".", w)

filename = int(input("Choose a file to read: "))
samplerate, sample = wavfile.read(wavs[filename])

print(wavs[filename], "at", samplerate, "samplerate")
input("Press any key to see the waveform")

plt.plot(sample)
plt.show()



