#Author - Uditangshu Aurangabadkar
import wave
import matplotlib.pyplot as plot
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

#Function to read an audio track
'''
    Params - track_name - specifies the name of the track to be read
    Return - track that has been read as an object type
'''
def readTrack(track_name):
    fs, signal = wavfile.read(track_name)
    #data, samplerate = sf.read(track_name)
    return signal

#Function to read matlab file where index is a 1
'''
    Params - file_name - matlab file
    Return - A dictionary
'''
def getMatlabFile(file_name):
    matlab_file = loadmat(file_name)
    return matlab_file

#Function to convert dictionary to array
'''
    Params - dict_name - dictionary type variable
    Return - Converted dictionary as an array
'''
def getArrayFromDict(dict_name):
    dict_list = list(dict_name.items()) 
    ret_array = np.asarray(dict_list, dtype=object)[3][1][0]
    return ret_array

#Function to get the detection index
'''
    Params - arr - input array
           - item - 1 or 0
    Return - index where the item is present in array
'''
def getIndex(arr, item):
    indices = np.where(arr == item)
    return indices

#Function to set window length for the median filter
def setWindowLength(val):
    return val

#Get track here
track = readTrack('corrupted_signal_created.wav')

#Loading matlab files here
threshold_indicator_mat = getMatlabFile('threshold_bk.mat')
indicator_indices_mat = getMatlabFile('threshold_index.mat')

#Progress Bar
#for i in tqdm(range(100), desc= "Processing audio", ncols = 75):
#   time.sleep(0.1)

#Building an indicator array from matlab
threshold_indicator = getArrayFromDict(threshold_indicator_mat)

#Getting indices where the detection array is 1
threshold_array = getIndex(threshold_indicator, 1)

#Setting window length here
window_length = setWindowLength(3)

#print(threshold_array)
#print(window_length)




