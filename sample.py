"""
Create a zero value sample add glitch dataset.
"""

import time
import numpy as np
import matplotlib.pyplot as plt
import cfg
import graph_output as go

samplerate  = cfg.sr
frequency   = cfg.f
length      = cfg.l        # In seconds
features    = cfg.fs       # dataset size
dc_offset   = cfg.dc       # 

########################################################

samples = samplerate * length
block_zeros = np.zeros(samplerate * length, dtype=int)
np.random.seed(55)           # Initialise the random gen
sine_SNR_db = 35
ring_a = 2000
ring_b = 2000

def rand_phase():
    
    phase = np.random.uniform(0, 360)
    
    return phase

def rand_offset(limit):
    
    offset = np.random.uniform(-limit, limit)
    print("DC offset is: ", offset)
    return offset

def new_sine(length, samplerate, frequency):

    t = np.linspace(0, length, samplerate * length)                 # Create time                                                      # equidistants entre 0 i length
    y = np.sin((frequency * 2 * np.pi * t) + (rand_phase() * (np.pi/180)))   # Fill with sine
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
    
def ring(x, a, b):
    
    sign = 1
    
    return (np.exp(-a*x)*np.sin(2*np.pi*b*x))*(sign)    #known overflow bug
    
def glitch(y):
    
    start_time = time.time()
    
    noise_array, s_watts = gen_noise(y)
    r = np.random.randint(0, samplerate * length - 1)   
    block_length = np.random.randint(0, samples-r)
    
    del_mask = np.linspace(samples-1, samples+block_length-1, block_length, dtype=int)     
    
    y = np.insert(y, r+1, block_zeros[0:block_length])
    y = np.delete(y, del_mask)
    y[r:samples] += ring(y[r:samples], ring_a, ring_b)  #known overflow bug
    y += noise_array

    runtime = time.time() - start_time
    
    print("runtime was:", runtime)
    return y, r, runtime                        #add runtime to a list so I can plot it when looping

########################################################

def main():

    phase = rand_phase()
    y, r, runtime = glitch(new_sine(length, samplerate, frequency))
    go.plot_start(y)
    go.plot_glitch(y, r)
    go.plot_runtime(r, runtime)
    print("Starting phase is:", phase)
    plt.show()

#main()