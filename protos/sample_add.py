import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt

sampleRate = 44100
frequency = 997
length = 5

figure, axis = plt.subplots(1,2)

t = np.linspace(0, length, sampleRate * length)  #  Produces a 5 second Audio-File
#print(t[(sampleRate * length - 10):(sampleRate * length)])

y = np.sin(frequency * 2 * np.pi * t)
axis[0].plot(y[(sampleRate * length - 50):(sampleRate * length)], )


y[(sampleRate * length - 30)] = 0
axis[1].plot(y[(sampleRate * length - 50):(sampleRate * length)])

plt.show()

#wavfile.write('Sine.wav', sampleRate, y)