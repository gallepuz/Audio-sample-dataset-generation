from random import sample
import time
import numpy as np
import matplotlib.pyplot as plt
import cfg
import sample_gen as sg


from scipy.io import wavfile
from datetime import date

samplerate  = cfg.sr
frequency   = cfg.f
length      = cfg.l        # In seconds
features    = cfg.fs       # dataset size
dc_offset   = cfg.dc       # 

#settings
phases = [0, 45, 90, 135, 180]
phase_at_glitch = [0, 0.25, 0.5, 0.75, 1]
print(phases.index(180))
j=0
avui = str(date.today())
for i in phases:
    name = avui + '_' + str(frequency) + '_' + str(phases[j])
    print(name)
    print(type(name))
    print("j is", j)
    #y = audio_gen.new_sine(length, samplerate, frequency, phases[0+j])
    t = np.linspace(0., 1., samplerate)
    amp = np.iinfo(np.int16).max
    y = amp * np.sin(2. * np.pi * frequency * t)
    w = sg.find(phase_at_glitch[j], 19940, y, 100)
    y[w:] = 0
    print(w)
    plt.plot(y[10000:60300])
    j+=1
    wavfile.write(name, samplerate, y)


#plt.subplot(132)
#plt.plot(z[w-50:w+50])
#plt.plot(y[19900:20100])
#plt.xlim([19900,20300])
plt.show()

