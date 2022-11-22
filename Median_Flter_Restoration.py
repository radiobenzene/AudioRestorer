#Author - Uditangshu Aurangabadkar
import wave
import matplotlib.pyplot as plot
from tqdm import tqdm
import time
from scipy.io import loadmat
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
frame_rate = track.getframerate()
track_frames = track.getnframes()
indicator = readIndicator('threshold_bk.mat')

#Progress Bar
#for i in tqdm(range(100), desc= "Processing audio", ncols = 75):
#   time.sleep(0.1)

con_list = [[element for element in upperElement] for upperElement in indicator['thress']]

print(track_frames)
print()