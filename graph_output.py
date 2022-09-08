"""
Create a zero value sample add glitch dataset. 
Or use its functions for other stuff.
"""

from random import seed
import time
from matplotlib import offsetbox
import numpy as np
import matplotlib.pyplot as plt
import cfg

from scipy.io import wavfile
from datetime import date


samplerate  = cfg.sr
frequency   = cfg.f
length      = cfg.l        # In seconds
features    = cfg.fs       # dataset size
dc_offset   = cfg.dc       # 
seed        = cfg.sd
sine_SNR_db = cfg.snr
########################################################

samples = samplerate * length
block_zeros = np.zeros(samplerate * length, dtype=int)
np.random.seed(seed)       # Initialise the random gen

ring_a = 2000
ring_b = 2000

# global settings
global add_noise
add_noise = "n"
global offset_onoff
offset_onoff = "n" 

avui = str(date.today())

format_key = '''
Naming of the files follows:
date_frequency_phase_glitchlocation_samplerate_blocklength_seed_BUG_TYPE.csv
'''
########################################################

def plot_glitch(y, r):
    
    #print(y[r-5:r+5])
    plt.figure(figsize=(4, 4)) 
    plt.suptitle("Glitch Vicinity")
    plt.grid(True, 'both')
    plt.plot(y[(r - 100):(r + 100)])
    plt.ylim(-1.2,1.2)
    
def plot_start(y):
    
    #print(y[r-5:r+5])
    plt.figure(figsize=(4, 4)) 
    plt.suptitle("First 400 Samples")
    plt.grid(True, 'both')
    plt.plot(y[0:400])
    plt.ylim(-1.2,1.2)

def plot_runtime(r, runtime):

    plt.figure(figsize=(20, 4))
    plt.subplot(133)
    plt.suptitle("Runtime per feature")
    plt.grid(True, 'both')
    plt.ylabel("Runtime (s)")
    plt.xlabel("Glitched sample")
    plt.plot(r, runtime, '.b', )

def write_wav(y):
    wavfile.write('Sine.wav', samplerate, y)

def main():

    
    #offset_onoff = input("add random offset to the signal? (y/n): ")
    
    """print(format_key)
    start_time = time.time()
    new_dataset(length, 44100, frequency, features)
    np.random.seed(seed + 1)
    new_dataset(length, 48000, frequency, features)
    np.random.seed(seed + 2)
    new_dataset(length, 88200, frequency, features)
    np.random.seed(seed + 3)
    new_dataset(length, 96000, frequency, features)
    np.random.seed(seed + 4)
    new_dataset(length, 176400, frequency, features)
    np.random.seed(seed + 5)
    new_dataset(length, 192000, frequency, features)
    total_runtime = time.time() - start_time
    print(total_runtime)"""
    #phase = 0#rand_phase()
    #y, r, runtime = glitch(new_sine(length, samplerate, frequency))
    #plot_start(y)
    #plot_glitch(y, r)
    #print("DC offset is:", offset)
    #print("Starting phase is:", phase)
    #plt.figure(figsize=(20, 4))
    #plt.subplot(132)
    #plt.plot(gungan)
    #plt.show()

main()

#plot_graph(y, r)
#plot_runtime(r, runtime)

#print("Iteration took", runtime, "seconds")
#print("Glitch at", r)