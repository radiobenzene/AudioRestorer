import unittest
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
from alive_progress import alive_bar

#The current file is for unit testing

raw_list_1 = generateList(10)
window_1 = 3
list_1 = zeroPadding(raw_list_1, window_1)

raw_list_2 = generateList(100000)
window_2 = 3
list_2 = zeroPadding(raw_list_2, window_2)

class MedianTest(unittest.TestCase):
    def test_medianFilter1(self):
        user_filter = medianFilter(list_1, window_1)
        python_filter = checkerFunction(raw_list_1, window_1)
        self.assertEqual(np.array(user_filter).all(), np.array(python_filter).all())

    def test_medianFilter2(self):
        user_filter = medianFilter(list_2, window_2)
        python_filter = checkerFunction(raw_list_2, window_2)
        self.assertEqual(np.array(user_filter).all(), np.array(python_filter).all())

if __name__ == "__main__":
    unittest.main()