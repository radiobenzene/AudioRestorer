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
    
    clean_cubic = readTrack("clean_cubic.wav")
    original_clean = readTrack("myclean.wav")

