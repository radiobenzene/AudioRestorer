#Author - Uditangshu Aurangabadkar
import wave
import matplotlib.pyplot as plot
from tqdm import tqdm
import time
from scipy.io import loadmat
import pandas as pd
from mat4py import loadmat
import numpy as np
import scipy.io.wavfile as wav
from scipy.io import wavfile
import soundfile as sf
from playsound import playsound
import pandas as pd
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
def getIndicator(file_name):
    matlab_file = loadmat(file_name)
    return matlab_file

#Function to read matlab file where index is a 1
def getIndex(file_name):
    matlab_file = loadmat(file_name)
    return matlab_file

#Get track here
track = readTrack('corrupted_signal_created.wav')

indicator = getIndicator('threshold_bk.mat')
indicator_indices = getIndex('threshold_index.mat')
#Progress Bar
#for i in tqdm(range(100), desc= "Processing audio", ncols = 75):
#   time.sleep(0.1)

#Loading the 
threshold_indicator = loadmat('threshold_bk.mat')

#con_list = [[element for element in upperElement] for upperElement in threshold_indicator['thress']]


indicator_list = list(threshold_indicator.items())
indicator_array = np.asarray(indicator_list, dtype = object)
print(indicator)
#print(type(indicator_array))
#print(track.getfp())
#playsound("corrupted_signal_created.wav")
#print(type(threshold_indicator))
#print(type(indicator_array))
#print(indicator_array)
print(np.where(indicator_array == 0))




