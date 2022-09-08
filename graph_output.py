"""
Create a zero value sample add glitch dataset.
"""

import matplotlib.pyplot as plt
from cfg import sr
from scipy.io import wavfile

samplerate = sr

########################################################

def plot_glitch(y, r):
    
    plt.figure(figsize=(4, 4)) 
    plt.suptitle("Glitch Vicinity")
    plt.grid(True, 'both')
    plt.plot(y[(r - 100):(r + 100)])
    plt.ylim(-1.2, 1.2)

    
def plot_start(y):
    
    plt.figure(figsize=(4, 4)) 
    plt.suptitle("First 400 Samples")
    plt.grid(True, 'both')
    plt.plot(y[0:400])
    plt.ylim(-1.2, 1.2)

def plot_runtime(r, runtime):

    plt.figure(figsize=(4, 4))
    plt.suptitle("Runtime per feature")
    plt.grid(True, 'both')
    plt.ylabel("Runtime (s)")
    plt.xlabel("Glitched sample")
    plt.plot(r, runtime, '.b', )

def write_wav():
    
    wavfile.write('Sine.wav', samplerate, y)
