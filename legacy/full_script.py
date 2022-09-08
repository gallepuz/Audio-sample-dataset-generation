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

def rand_phase():
    
    phase = np.random.uniform(0, 360)
    
    return phase

def find(target, after, y, t_e5=1):
    '''find the index at which value is target after a point in the array
    within tolerance'''
    found = False
    i = 0
    t = t_e5 * 10 ** -5
    while found != True:
        if target-t < y[after+i] < target+t:
            found = True
        else:
            i += 1
    return after+i

def rand_offset(limit):

    if offset_onoff == "y":
        offset = np.random.uniform(-limit, limit)
    else:
        offset = 0
    #print("DC offset is: ", offset)
    return offset

def new_sine(length, samplerate, frequency, phase):

    t = np.linspace(0., length, samplerate * length)                 # Create time                                                      # equidistants entre 0 i length
    y = np.sin((frequency * 2. * np.pi * t) + (phase * (np.pi/180)))   ####### added phase as an arg
    y += rand_offset(dc_offset)
        
    return y

def gen_noise(source, start=None, end=None):
    """Generates a noise array and applies it
    to the source. Source must be array-like"""
        
    s_watts = source[start:end]**2
    s_db = 10*np.log10(s_watts)
    
    avg_watts = np.mean(s_watts)
    avg_db = 10*np.log10(avg_watts)
    
    noise_db = avg_db - sine_SNR_db
    noise_watts = 10**(noise_db/10)
    
    noise_array = np.random.normal(0, np.sqrt(noise_watts), len(s_watts))   #repassar sqrt
    
    return noise_array, s_watts

def noise(y , z):
    return y + z        #this is stupid

def ring(x, a, b):
    
    sign = 1
    
    return (np.exp(-a*x)*np.sin(2*np.pi*b*x))*(sign) #known overflow bug



def glitch(y):
    
    start_time = time.time()

    #if add_noise == "y":
    #    noise_array, s_watts = gen_noise(y)
    noise_array, s_watts = gen_noise(y)
    r = np.random.randint(0, samplerate * length - 1)   
    #block_length = np.random.randint(0, samples-r)
    block_length = 1
    
    del_mask = np.linspace(samples-1, samples+block_length-1, block_length, dtype=int)     
    
    y = np.insert(y, r+1, block_zeros[0:block_length])
    y = np.delete(y, del_mask)
    #y[r:samples] += ring(y[r:samples], ring_a, ring_b)  #known bug
    
    #if add_noise == "y":
    #    y += noise_array
    y += noise_array

    runtime = time.time() - start_time
    
    #print("runtime was:", runtime)
    return y, r, runtime, block_length                       #add runtime to a list so I can plot it when looping

def new_dataset(length, samplerate, frequency, features):
    start_time = time.time()
    runtimes = []
    glitches = []
    print("Generating dataset...")
    for _ in range(features):
        phase = rand_phase()
        y, r, runtime, block_length = glitch(new_sine(length, samplerate, frequency, phase))
        runtimes.append(runtime)
        glitches.append(r)
        #plot_glitch(y, r)
        #plot_start(y)
        name = f"{avui}_{frequency}_{phase:.2f}_{r}_{samplerate}_{block_length}_{seed}_SAMPLE_DROP.csv"
        with open(name, "w") as f:
            f.write(",".join([format(x, ".9f") for x in y]))
        
        
    total_runtime = time.time() - start_time
    #plot_runtime(glitches, runtimes)
    #plt.show()
    print("Number of features:", features)
    print("Generating the dataset took", total_runtime, "seconds.")

# Output methods

def plot_glitch(y, r):
    
    #print(y[r-5:r+5])
    plt.figure(figsize=(20, 4)) 
    plt.subplot(131)
    plt.suptitle("Glitch Vicinity")
    plt.grid(True, 'both')
    plt.plot(y[(r - 1000):(r + 1000)])
    
def plot_start(y):
    
    #print(y[r-5:r+5])
    plt.figure(figsize=(20, 4)) 
    plt.subplot(132)
    plt.suptitle("First 400 Samples")
    plt.grid(True, 'both')
    plt.plot(y[0:400])

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