import numpy as np
import matplotlib.pyplot as plt

samplerate = 192000
length = 2
frequency = 997
sine_SNR_db = 45
plotd_vals = samplerate * length

t = np.linspace(0, length, samplerate * length)                 # Create time    
y = np.sin((frequency * 2 * np.pi * t)+(0 * (np.pi/180)))
zeros = np.zeros(int((3*samplerate)/4), dtype=int)
ones = np.ones(samplerate, dtype=int)
param = np.linspace(0, 1, num=int(samplerate/4))
param = param**4
#c = np.linspace(0, 1, samplerate * length)
c = np.append(zeros, param)
c = np.append(c, ones)

def smoothstep(threshold, edge_a, edge_b, x):
    length = len(x)
    output = [None]*length 
    i = 0
    for p in x:
        if p <= edge_a:
            output[i] = 1
        elif p >= edge_b:
            output[i] = 0
        else:
            output[i] = -((p**2)*(3-2*p))+1
        i += 1
    return output 

def ring(x, a, b):
    
    sign = 1
    
    return (np.exp(-a*x)*np.sin(2*np.pi*b*x))*(sign)

y = ring(t, 3, 20)#-c*(y)


plt.figure(figsize=(20, 4)) 
plt.subplot(132)
plt.suptitle(plotd_vals)
plt.grid(True, 'both')
plt.plot(y[0:plotd_vals])
plt.plot(param[0:plotd_vals])
plt.plot(zeros[0:plotd_vals])
plt.plot(c[0:plotd_vals])

plt.show()
print(y[400:420])