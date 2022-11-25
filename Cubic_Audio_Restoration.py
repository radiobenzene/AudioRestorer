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

#The current functions returns the y value for the cubic interpolation
def getValues():
    pass
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

clicked_data = track

track_length = len(track)

track_range = np.arange(track_length)

popped_range = np.delete(track_range, threshold_array)

popped_data = np.delete(clicked_data, threshold_array)

print(popped_range)
print(popped_data)
cubic_spline = CubicSpline(popped_range, popped_data, bc_type="natural")

for i in range(max_bound):
    popped_data[threshold_array[i]] = cubic_spline(threshold_array)[i]

plotGraph(popped_data, 44100)
