"""
Dataset configuration file.
"""

sr  = 192000                #samplerate
f   = 997                   #frequency 
l   = 1                     #length    
fs  = 1                     #features  
dc  = 0.05                  #max dc offset higher and lower limit
sd  = 42                    #random gen seed
snr = 35                    #signal to noise ratio

bl = 10                     #block of zeros length. Comment or
#bl = "random"              #uncomment alternatively

bug_name = "BLOCK_ZEROS"    #bug name appended at the end of each sample