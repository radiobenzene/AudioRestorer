# Audio Restoration Project

## Brief Overview

Audio restoration has become an integral part of digit age and it's tasks range from restoring old recordings to reducing noise in modern audio tracks. An important task of audio restoration algorithms is to remove random clicks in an audio signal which can be done using several methods, namely, AR Method, Cubic Interpolation and Median Filtering. The current project demonstrates two kinds of "click" removal mechanisms:
1. Median Filtering
2. Cubic Interpolation

The current project uses an original audio track which is then degraded by adding high amplitudes at random points. The file
`new_clean.wav`
is an original audio track which does not have any degradations or "clicks". Henceforth, the term "clicks" will be used to denote degradations in the tracks. 
The file `new_degraded.wav` is the degraded track in which distinct clicks can be heard at random points. `cubic_clean.wav` is the audio track that was restored using cubic interpolation. `clean_median.wav` is the audio track that was restored using median filtering.

## Getting started
The project is divided into 3 main files:
1. Median_Flter_Restoration.py
2. Cubic_Audio_Restoration.py
3. unit_test.py

To run any of the files, please check whether your machine has the following dependencies:
1. wave
2. tqdm
3. matplotlib
4. pandas
5. scipy
6. playsound
7. pymatreader
8. alive_progress
9. sys
10. subprocess

The following dependencies can be installed on a local machine using the following command - `pip install <dependency_name>`

### Cloning the Project
The project can be cloned to a local machine via a terminal window using the command:
```
git clone https://github.com/radiobenzene/Audio_Restoration.git
```

## Median Filtering
Let us detail the algorithm for median filtering:
1. Read input track - `new_degraded.wav`
2. Read .mat file (Matlab) `threshold_bk.mat` that contains a list of points where clicks exist. For convenience, we shall denote them as "indicators".
3. Convert the .mat file to an array. As a Matlab file is read as a "Dictionary" type, we must convert it into an "Array"
4. Get the indices of those points where the .mat file has clicks, i.e. the indicator gets a value of 1
5. Set a window length for the median filtering
6. Define a certain constant length, i.e. delta, which is an offset of window length. This value will help us apply the median filtering only around the specified window
7. Apply the median filter, i.e Sorting the points which lie within the window range and calculating the median value.
8. Substitue those values which have been filtered back into the track
9. Write the track to a new file - `clean_median.wav`

### Implementation specifics
The following command must be typed in to run the median filtering algorithm on a local machine:
```
python3 Median_Flter_Restoration.py --run
```
or
```
python3 Median_Flter_Restoration.py -r
```
