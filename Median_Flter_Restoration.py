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

#Function to plot an audio track frequency
'''
    Params - track - object
    Return - A plot of the audio track
'''
def plotTrack(track):
    pass

#Function to read matlab ones and zeros
'''
    Params - file_name - matlab file
    Return - A dictionary of 0s and 1s
'''
def getIndicator(file_name):
    matlab_file = loadmat(file_name)
    return matlab_file

#Function to read matlab file where index is a 1
'''
    Params - file_name - matlab file
    Return - A dictionary of indices where detection vector is 1
'''
def getIndex(file_name):
    matlab_file = loadmat(file_name)
    return matlab_file

#Function to convert dictionary to array
'''
    Params - dict_name - dictionary type variable
    Return - Converted dictionary as an array
'''
def getArrayFromDict(dict_name):
    dict_list = list(dict_name.items()) 
    ret_array = np.asarray(dict_list)[3][1][0]
    return ret_array


#Get track here
track = readTrack('corrupted_signal_created.wav')

#Loading matlab files here
threshold_indicator = getIndicator('threshold_bk.mat')
indicator_indices = getIndex('threshold_index.mat')

#Progress Bar
#for i in tqdm(range(100), desc= "Processing audio", ncols = 75):
#   time.sleep(0.1)

#Getting indicator array here
threshold_indicator_list = list(threshold_indicator.items())
threshold_indicator_array = np.asarray(threshold_indicator_list)[3][1][0]

#Building an indicator array
temp_arr = getArrayFromDict(threshold_indicator)
print(temp_arr)
#print(np.where(threshold_indicator_array == 1))




