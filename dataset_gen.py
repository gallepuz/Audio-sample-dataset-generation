"""
Create a zero value sample add glitch dataset. 
Or use its functions for other stuff.
"""

from random import seed
import time
import numpy as np
import cfg
import sample_gen as sg
import graph_output as go   #do not remove

from datetime import date

samplerate  = cfg.sr
frequency   = cfg.f
length      = cfg.l        # In seconds
features    = cfg.fs       # dataset size
dc_offset   = cfg.dc       # 
seed        = cfg.sd
sine_SNR_db = cfg.snr
block_length = cfg.bl
append      = cfg.bug_name

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

def new_dataset(length, samplerate, frequency, features):
    start_time = time.time()
    runtimes = []
    glitches = []
    print("Generating dataset...")
    for _ in range(features):
        phase = sg.rand_phase()
        y, r, runtime, block_length = sg.glitch(sg.new_sine(length, samplerate, frequency, phase))
        runtimes.append(runtime)
        glitches.append(r)
        name = f"{avui}_{frequency}_{phase:.2f}_{r}_{samplerate}_{block_length}_{seed}_{append}.csv" 
        with open(name, "w") as f:
            f.write(",".join([format(x, ".9f") for x in y]))
        
        
    total_runtime = time.time() - start_time

    #go.plot_glitch(y, r)
    #go.plot_start(y)
    #plt.show()
    
    print("Number of features:", features)
    print("Generating the dataset took", total_runtime, "seconds.")

def main():

    #input("Have you turned off plotting? Press any key to continue or ctrl+c to exit")
    new_dataset(length, samplerate, frequency, features)

main()
