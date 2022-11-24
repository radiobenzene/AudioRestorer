#Author - Uditangshu Aurangabadkar
import wave
import matplotlib.pyplot as plt
from tqdm import tqdm
import time
from scipy.io import loadmat
import pandas as pd
import numpy as np
import scipy.io.wavfile as wav
from scipy.io import wavfile
import soundfile as sf
from playsound import playsound
import pandas as pd
from pymatreader import read_mat
from time import gmtime, strftime
from functions import *
import sys, getopt

def main():
    
    #Get track here
    fs, track = readTrack('new_degraded.wav')
    track = track

    #Loading matlab files here
    threshold_indicator_mat = getMatlabFile('threshold_bk.mat')
    
    #Building an indicator array from matlab
    threshold_indicator = getArrayFromDict(threshold_indicator_mat)

    #Getting indices where the detection array is 1
    threshold_array = getIndex(threshold_indicator, 1)

    #Setting window length here
    window_length = setWindowLength(3)

    #Initializing the restored track
    restored_track = track
    for i in range(len(threshold_array)):
        
        #Delta is the frame depending on the window length
        delta = (window_length - 1) / 2

        #Determing the block bounds here
        left_bound = threshold_array[i] - delta
        right_bound = threshold_array[i] + delta
        
        #Determing the data block with which we have to work with
        data_block = restored_track[int(left_bound) : int(right_bound + 1)]

        #Padding the block
        padded_data = zeroPadding(data_block, window_length)

        #Applying the median filter
        filtered_data = medianFilter(padded_data, window_length)

        #Getting the restored track here
        restored_track[int(left_bound) : int(right_bound + 1)] = filtered_data

    #Writing the restored .wav file and saving it as "clean.wav"
    wavfile.write("clean.wav", fs, restored_track)
    

if __name__ == "__main__":

    #Getting the argument list here
    degraded_track = readTrack("new_degraded.wav")
    clean_track = readTrack("new_degraded.wav")

    argument_list = sys.argv[1:]

    #Condensed options
    options = "hmr"
    #Creating a dictionary of options
    long_options = ["Help", "MSE_metric", "Run"]

    try:
        # Parsing argument
        arguments, values = getopt.getopt(argument_list, options, long_options)

        for currentArgument, currentValue in arguments:
 
            if currentArgument in ("-h", "--Help"):
                print ("Displaying Help")
                showHelp()
                break;
                
            elif currentArgument in ("-m", "--MSE_Metric"):
                print ("Displaying MSE error")
                MSE = getMSE(clean_track, degraded_track)
                print(MSE)
                
            elif currentArgument in ("-r", "--Run"):
                for i in tqdm(range(100), desc= "Processing audio", ncols = 100):   
                    main()
                    time.sleep(0.05)
                print("Done!")  

    except getopt.err as error:
        print(str(err))

    
    
        




