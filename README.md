## Test sinewave dataset creator 

A script that generates a dataset of commonly found glitches in realtime digital audio transceiving and conversion. The samples in the dataset are fully featured renders of a sinewave in the analog domain (as if recorded by AD converter) with configurable SNR, DC offset, ringing (WIP), samplerate, seed, frequency and length.

Currently can quickly render:
* Single sample add: adds a zero value sample, simulating dropout at the DUT microcontroller´s high speed clock followed by immediate resuming of playback.
* Block of zeros: similar to single sample add but longer, modelling complete playback dropout of unspecified cause followed by resuming playback.
* Playback dropout: complete interruption of the sinewave until the end of the sample.

### Use

1. Edit the settings in `cfg.py` to suit your dataset needs.
2. Navigate to the root on terminal and run `python dataset_gen.py`.
3. The csv files will be created directly in the root folder.
