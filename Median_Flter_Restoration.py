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
from alive_progress import alive_bar
import subprocess


def main():
    
    #Get track here
    fs, track = readTrack('new_degraded.wav')
    track = track

    #Loading matlab files here
    threshold_indicator_mat = getMatlabFile('threshold_bk.mat')
    
    #Building an indicator array from matlab
    threshold_indicator = getArrayFromDict(threshold_indicator_mat, 'thress')

    #Getting indices where the detection array is 1
    threshold_array = getIndex(threshold_indicator, 1)

    #Setting window length here
    window_length = setWindowLength(3) #This was 3

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
    wavfile.write("clean_median.wav", fs, restored_track)
    
if __name__ == "__main__":

    #Getting the argument list here
    #fs_degraded, degraded_track = readTrack("new_degraded.wav")
   # fs_median_clean, median_clean_track = readTrack("clean_median.wav")
    #fs_original_clean, original_clean_track = readTrack("new_clean.wav")

    argument_list = sys.argv[1:]

    #Condensed options
    options = "hmrpdtsu"
    #Creating a dictionary of options
    long_options = ["help", "mse", "run", "plot", "diff", "theme", "sound", "unit"]

    try:
        # Parsing argument
        arguments, values = getopt.getopt(argument_list, options, long_options)

        for currentArgument, currentValue in arguments:

            if currentArgument in ("-h", "--help"):
                print ("Displaying Help")
                showHelpForMedian()
                break
                
            elif currentArgument in ("-m", "--mse"):
                fs_median_clean, median_clean_track = readTrack("clean_median.wav")
                fs_original_clean, original_clean_track = readTrack("new_clean.wav")

                print ("Displaying MSE error")
                MSE_Median = getMSE(median_clean_track, original_clean_track)
                print(MSE_Median)
            
            elif currentArgument in ("-s", "--sound"):
                print ("Playing degraded audio tracks")
                degraded_song = "new_degraded.wav"
                

            elif currentArgument in ("-u", "--unit"):
                individualUnitTest()

            elif currentArgument in ("-d", "--diff"):
                print ("Displaying the MSE error difference between the two restored tracks")
                fs_median_clean, median_clean_track = readTrack("clean_median.wav")
                fs_original_clean, original_clean_track = readTrack("new_clean.wav")

                MSE_Median = getMSE(median_clean_track, original_clean_track)
                #MSE = getMSE(clean_track, degraded_track)
                #print(MSE)
            
            elif currentArgument in ("-p", "--plot"):

                fs_degraded, degraded_track = readTrack("new_degraded.wav")
                fs_median_clean, median_clean_track = readTrack("clean_median.wav")
                fs_original_clean, original_clean_track = readTrack("new_clean.wav")

                print("Plotting graph for the degraded track")
                plotGraph(degraded_track, fs_degraded, "Degraded Signal")
                
                print("Plotting graph for the restored track")
                plotGraph(median_clean_track, fs_median_clean, "Restored Signal")

                print("Plotting graph for the original track")
                plotGraph(original_clean_track, fs_original_clean, "Original Track")


            elif currentArgument in ("-r", "--run"):
                #Starting timer here
                start_time = time.time()
                for i in tqdm(range(100), desc= "Restoring Audio using median filtering", ncols = 100):   
                    main()
                    time.sleep(0.05)
                
                print("Done!")  

                #Calculating the elapsed time here
                end_time = time.time()
                elapsed_time = end_time - start_time
                print("The elapsed time is", round(elapsed_time, 4), "seconds")
            
            #Changing the loader there
            elif currentArgument in ("-t", "--theme"):
                with alive_bar(100, bar = 'notes', spinner = 'notes2') as bar:  
                    for i in range(100):
                        main()
                        time.sleep(0.01)
                        bar()
                print("Done!")

    except getopt.err as error:
        err = "Invalid Option"
        print(str(err))

    
    
        




