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
from scipy.interpolate import *
import sys, getopt

def main():
    #Get track here
    fs, track = readTrack('new_degraded.wav')

    #Loading matlab files here
    threshold_indicator_mat = getMatlabFile('threshold_bk.mat')
        
    #Building an indicator array from matlab
    threshold_indicator = getArrayFromDict(threshold_indicator_mat, 'thress')

    #Specify x value for spline function
    threshold_array = getIndex(threshold_indicator, 1)

    #Setting the max bounds for the loop
    max_bound = len(threshold_array)

    #Initializing a new track
    clicked_data = initializeNewTrack(track)

    #Getting track length here
    track_length = len(track)

    #Getting range of track length, [0, len(track)]
    track_range = np.arange(track_length)

    #Deleting indices where a click exists
    updated_index_block = np.delete(track_range, threshold_array)

    #Deleteing data points where a click exists
    updated_data_block = np.delete(clicked_data, threshold_array)

    #Using the CubicSpline function
    cubic_spline = CubicSpline(updated_index_block, updated_data_block, bc_type="natural")

    #Interpolating at every point where there are clicks
    for i in range(max_bound):
        updated_data_block[threshold_array[i]] = cubic_spline(threshold_array)[i]

    #Creating a new restored track
    restored_track = initializeNewTrack(updated_data_block)

    #Writing a new file
    wavfile.write("clean_cubic.wav", fs, restored_track)

if __name__ == "__main__":

    #Getting the argument list here
    fs_degraded, degraded_track = readTrack("new_degraded.wav")
    #fs_median_clean, median_clean_track = readTrack("clean_median.wav")
    fs_cubic_clean, cubic_clean_track = readTrack("clean_cubic.wav")

    argument_list = sys.argv[1:]

    #Condensed options
    options = "hmrpd"
    #Creating a dictionary of options
    long_options = ["help", "mse", "run", "plot", "diff"]

    try:
        # Parsing argument
        arguments, values = getopt.getopt(argument_list, options, long_options)

        for currentArgument, currentValue in arguments:
 
            if currentArgument in ("-h", "--help"):
                print ("Displaying Help")
                showHelpForMedian()
                break
                
            elif currentArgument in ("-m", "--mse"):
                print ("Displaying MSE error")
                #MSE = getMSE(clean_track, degraded_track)
                #print(MSE)
            
            elif currentArgument in ("-d", "--diff"):
                print ("Displaying the MSE error difference between the two restored tracks")
               # MSE = getMSE(clean_track, degraded_track)
                #print(MSE)
            
            elif currentArgument in ("-p", "--plot"):
                print("Plotting graph for the degraded track")
                plotGraph(degraded_track, fs_degraded)
                
                print("Plotting graph for the restored track")
                plotGraph(cubic_clean_track, fs_cubic_clean)
                
            elif currentArgument in ("-r", "--run"):
                for i in tqdm(range(100), desc= "Restoring Audio using cubic interpolation", ncols = 100):   
                    main()
                    time.sleep(0.05)
                print("Done!")  

    except getopt.err as error:
        err = "Invalid Option"
        print(str(err))


