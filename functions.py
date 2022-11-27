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
import unittest
from playsound import playsound
import pandas as pd
from pymatreader import read_mat
from time import gmtime, strftime
from functions import *
import unittest
import sys
import scipy
import random

'''
    The current file contains all the functions
    used in the main() function for median filtering
    and cubic interpolation
'''
#Defining error code for window with even length
WINDOW_LEN_EVEN = -1

#Function to read an audio track
'''
    Params - track_name - specifies the name of the track to be read
    Return - track that has been read as an object type
'''
def readTrack(track_name):
    fs, signal = wavfile.read(track_name)
    #data, samplerate = sf.read(track_name)
    return fs, signal

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
def getArrayFromDict(dict_name, val):
    ret_val = dict_name[val]
    return ret_val

#Function to get the detection index
'''
    Params - arr - input array
           - item - 1 or 0
    Return - index where the item is present in array
'''
def getIndex(arr, item):
    indices = np.where(arr == item)
    indices = indices[1]
    indices = indices[1:661500]
    return indices

#Function to set window length for the median filter
def setWindowLength(val):
    return val

#Function to set block length for cubic spline interpolation
def setBlockLength(val):
    return val
    
# Function to check if the filter length is odd
'''
    Params - filter_len - length of the filter
    Return - odd_flag - boolean variable if filter length is odd = true, else false
'''
def isOddLength(filter_len):

    if (filter_len % 2 == 1):
        is_odd_flag = True

    else:
        is_odd_flag = False
        print("Window size is even")
        
    return is_odd_flag

# Function for zero padding of the list
'''
    Params - data_list - input list
           - window_len - window length
    Return - A padded list with 0s determined by the window length and input list
'''
def zeroPadding(data_list, window_len):
    padded_list = data_list

    N_filter = window_len
    N_new = int((N_filter - 1) / 2)

    is_odd_flag = isOddLength(window_len)

    if (is_odd_flag == True):
        padded_list = np.pad(padded_list, (N_new, N_new),
                             'constant', constant_values=(0, 0))

    else:
        padded_list = data_list


    return padded_list

# Function for Median filtering
'''
    Params - data_list - input list
           - window_len - window length
    Return - A new filter after being median filtered
'''
def medianFilter(data_list, window_len):
    new_array = []

    #Case when the length of list is less than window length
    if (isOddLength(window_len) == False):
        return WINDOW_LEN_EVEN

    if len(data_list) < window_len:
        return data_list

    for i in range(len(data_list) - window_len + 1):
        #Sorting the windowed elements
        sorted_list = np.sort(data_list[i: i + window_len])

        #Getting the middle element
        middle_index = int((window_len - 1) / 2)

        #Getting elements from the sorted list
        middle_elem = sorted_list[middle_index]

        #Creating a new array of only middle elements
        new_array.append(middle_elem)

    return np.array(new_array)

#Function to modify median filter such that window size and list are same
def modifyList(data_list, window_len):
    ret_list = data_list
    pass

#Function to plot the graph
'''
    Params - track - audio track
           - fs - sampling rate
    Return - a plotted graph
'''
def plotGraph(track, fs):
    length = track.shape[0] / fs
    time = np.linspace(0., length, track.shape[0])
    plt.plot(time, track)
    plt.show()

#Function to plot multiple graphs
def plotMultipleGraphs(track_1, track_2, fs):
    length_track_1 = track_1.shape[0] / fs
    length_track_2 = track_2.shape[0] / fs

    time_track_1 = np.linspace(0., length_track_1, length_track_1.shape[0])
    time_track_2 = np.linspace(0., length_track_2, length_track_2.shape[0])

    plt.subplot(2, 1, 1)
    plt.plot(time_track_1, length_track_1)
    plt.show();

    plt.subplot(2, 1, 2)
    plt.plot(time_track_2, length_track_2)
    plt.show()

#Function to get Mean Squared Error for 2 tracks
def getMSE(clean_track, degraded_track):
    diff = np.subtract(clean_track, degraded_track)
    squared = np.square(diff)
    output = squared.mean()
    return output

# Function to use inbuilt median function
'''
    Params - data_list - list of numbers on which a median filter must be applied
           - window_len - window_length
    Return - Filtered list using Median filter
'''
def checkerFunction(data_list, window_len):
    out = scipy.signal.medfilt(data_list, kernel_size = window_len)
    return out

#Function to generate random number list of total_len size
def generateList(total_len):
    random_list = []
    for i in range(0, total_len):
        n = random.randint(1,30)
        random_list.append(n)
    return random_list

#Function  to test individual functions
'''
    The current function is for individual unit tests
'''
def individualUnitTest():
    pass_counter = 0
    fail_counter = 0

    total_tests = 5

    #Generating first test and then checking
    raw_list_1 = generateList(10)
    window_1 = 3
    list_1 = zeroPadding(raw_list_1, window_1)
    if(np.array_equal(np.array(medianFilter(list_1, window_1)), checkerFunction(raw_list_1, window_1))):
        pass_counter = pass_counter + 1
        print("OK")
    else:
        fail_counter = fail_counter + 1
        print("NOT OK")

    raw_list_2 = generateList(12)
    window_2 = 5
    list_2 = zeroPadding(raw_list_2, window_2)
    if(np.array_equal(np.array(medianFilter(list_2, window_2)), checkerFunction(raw_list_2, window_2))):
        pass_counter = pass_counter + 1
        print("OK")
    else:
        fail_counter = fail_counter + 1
        print("NOT OK")

    raw_list_3 = generateList(22)
    window_3 = 7
    list_3 = zeroPadding(raw_list_3, window_3)
    if(np.array_equal(np.array(medianFilter(list_3, window_3)), checkerFunction(raw_list_3, window_3))):
        pass_counter = pass_counter + 1
        print("OK")
    else:
        fail_counter = fail_counter + 1
        print("NOT OK")

    raw_list_4 = generateList(1052)
    window_4 = 5
    list_4 = zeroPadding(raw_list_4, window_4)
    if(np.array_equal(np.array(medianFilter(list_4, window_4)), checkerFunction(raw_list_4, window_4))):
        pass_counter = pass_counter + 1
        print("OK")
    else:
        fail_counter = fail_counter + 1
        print("NOT OK")

    raw_list_4 = generateList(20052)
    window_4 = 11
    list_4 = zeroPadding(raw_list_4, window_4)
    if(np.array_equal(np.array(medianFilter(list_4, window_4)), checkerFunction(raw_list_4, window_4))):
        pass_counter = pass_counter + 1
        print("OK")
    else:
        fail_counter = fail_counter + 1
        print("NOT OK")

    #Displaying the passed tests 
    print("Total tests passed:", pass_counter, "/", total_tests)
    print("Total tests failed:", fail_counter, "/", total_tests)


#Function to initialize a new track
def initializeNewTrack(track):
    new_track = track
    return new_track

#Function to show help for median filtering
def showHelpForMedian():
    print("This is an audio restoration project which uses Median Filtering to restore a track\n")
    print("python3 <file_name> -h displays the Help Menu")
    print("python3 <file_name> -r runs the program")
    print("python3 <file_name> -m gives the MSE error between the audio tracks")
    print("python3 <file_name> -s changes the loader theme")
    print("python3 <file_name> -p plots the graphs of the degraded and restored tracks")
    print("python3 <file_name> -t to change the loader theme")
    print("python3 <file_name> --diff gives the difference between the MSE of the restored tracks created by either ways")
    print("To get the MSE, you must first run the file")

#Function to show help for cubic filtering
def showHelpForCubic():
    print("This is an audio restoration project which uses Cubic Filtering to restore a track\n")
    print("python3 <file_name> -h displays the Help Menu")
    print("python3 <file_name> -r runs the program")
    print("python3 <file_name> -s changes the loader theme")
    print("python3 <file_name> -m gives the MSE error between the audio tracks")
    print("python3 <file_name> -p plots the graphs of the degraded and restored tracks")
    print("python3 <file_name> -t to change loader theme")
    print("python3 <file_name> --diff gives the difference between the MSE of the restored tracks created by either ways")
    print("python3 <file_name> --diff gives the difference between the MSE of the restored tracks created by either ways")
    print("To get the MSE, you must first run the file")