#Author - Uditangshu Aurangabadkar
import wave
import matplotlib.pyplot as plot
from tqdm import tqdm
import time
from scipy.io import loadmat
import pandas as pd
from mat4py import loadmat
import numpy as np
#Function to read an audio track
'''
    Params - track_name - specifies the name of the track to be read
    Return - track that has been read as an object type
'''
def readTrack(track_name):
    obj = wave.open(track_name, 'r')
    return obj

#Function to plot an audio track frequency
'''
    Params - track - object
    Return - A plot of the audio track
'''
def plotTrack(track):
    pass

#Function to read matlab ones and zeros
def readIndicator(file_name):
    matlab_file = loadmat(file_name)
    return matlab_file


track = readTrack('corrupted_signal_created.wav')
signal = track.readframes(-1)
signal = np.frombuffer(signal, dtype ="int16")

frame_rate = track.getframerate()
track_frames = track.getnframes()
indicator = readIndicator('threshold_bk.mat')

#Progress Bar
#for i in tqdm(range(100), desc= "Processing audio", ncols = 75):
#   time.sleep(0.1)


threshold_indicator = loadmat('threshold_bk.mat')
indicator_list = list(threshold_indicator.items())
indicator_array = np.asarray(indicator_list)
print(type(indicator_array))
#print(track.getfp())

