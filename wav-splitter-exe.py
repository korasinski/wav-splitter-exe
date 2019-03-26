#________________________________________
#
# WAV File splitter
# Copytright 2019 - Jakub Orasiński, KudlatyWOKRSHOP.com
#________________________________________

from scipy.io import wavfile
import os
import struct
import time

import warnings
warnings.filterwarnings("ignore")

#________________________________________
#
# Infto
#________________________________________

print("_______________________________________")
print("             WAV Splitter              ")
print("_______________________________________\n")
time.sleep(.5)

#________________________________________
#
# Paths
#________________________________________

path = os.getcwd()
#print("Actual working path:",path)

input_path = path + "/input"

if not os.path.exists(input_path):
    print("Creating input directory")
    os.makedirs(input_path)

output_path = path + "/output"

if not os.path.exists(output_path):
    print("Creating output directory")
    os.makedirs(output_path)

#________________________________________
#
# Print all .wav files in input directory
#________________________________________

if len(os.listdir(input_path) ) == 0:
    print("\nInput directory is empty")

else:
    print("Some .wav files were found in input directory:")

    for file in os.listdir(input_path):
        if file.endswith(".wav"):
            print("- " + file)
    print("\n")

    try:
        input("Press enter to begin splitting files.... \n")
    except SyntaxError:
        pass

#________________________________________
#
# Split every channel in each file in directory
#________________________________________


for file in os.listdir(input_path):
    if file.endswith(".wav"):
        source_name = os.path.splitext(file)[0]
        file_path = input_path + "/" + file
        audio_file = open(file_path,"rb") # Read wav file for information, "r flag" - read, "b flag" - binary
        fs, data = wavfile.read(file_path) # Read wav file for splitter
        print("Loading file: " + source_name)
        time.sleep(.5)

        non_important_data=audio_file.read(22)

        NumChannelsString=audio_file.read(2) # Should be 1 for mono, 2 for stereo
        NumChannels=struct.unpack("H",NumChannelsString) # 'H' unsigned 16-bit integer
        channels = int(NumChannels[0])
        audio_file.close()


        if channels > 1:

            print("Detected " + str(channels) + " channels")

            print("Splitting channels...")

            export_path = output_path + "/" + source_name

            if not os.path.exists(export_path):
                os.makedirs(export_path)

            for ch in range(channels):
                channel_number = ch + 1
                time.sleep(.5)
                p_name = export_path + "/{0}_ch_{1}.wav".format(source_name, channel_number)
                wavfile.write(p_name, fs, data[:, ch])  # saving x column which corresponds to channel x
                print(p_name)

            print("Splitting done :)")

        if channels <= 1 :
            print("Detected " + str(channels) + " channel")
            print("No more channels to split \n")



time.sleep(5)