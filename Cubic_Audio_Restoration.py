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

#Get track here
fs, track = readTrack('new_degraded.wav')

#Read Matlab file here
degraded_data_mat = getMatlabFile('zeroed_sig.mat')

#Building an indicator array from matlab
degraded_data = getArrayFromDict(degraded_data_mat, 'd_signal')

#Specify x value for spline function
x_val = getIndex(degraded_data, 0)#np.where(degraded_data == 0)

#Setting the max bounds for the loop
max_bound = len(x_val)

#Setting block length
block = setBlockLength(3)

#Initializing restored track here
restored_track = track
#print(max_bound)