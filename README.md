# wav-splitter-exe
### A lightweight Windows for WAV files processing
This is a Windows executable file for splitting each channel on WAV audio file into separate files. Written in Python, exported to exe by [PyInstaller](https://www.pyinstaller.org). 

------------------------------

![Screenshoot](https://i.imgur.com/Af5qw2E.png)

------------------------------
### Usage

Place your multichannel wav files in folder input. Script will print all files that are eligible to do splitting. Press enter to start the procedure. Output files will be placed in output folder with subfolders (named as input files) and with individual filename ('input_file_name'_'ch'_'channel_number'.wav).  

```
_______________________________________
             WAV Splitter
_______________________________________

Some .wav files were found in input directory:
- 4ch.wav

Press enter to begin splitting files....

Loading file: 4ch
Detected 4 channels
Splitting channels...
C:\wav-splitter-exe/output/4ch/4ch_ch_1.wav
C:\wav-splitter-exe/output/4ch/4ch_ch_2.wav
C:\wav-splitter-exe/output/4ch/4ch_ch_3.wav
C:\wav-splitter-exe/output/4ch/4ch_ch_4.wav
Splitting done :)
```

-------------------------------

### Examples

Example WAV files from: http://www-mmsp.ece.mcgill.ca/Documents/AudioFormats/WAVE/Samples.html

-------------------------------
