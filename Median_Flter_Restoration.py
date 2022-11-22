#Author - Uditangshu Aurangabadkar
import wave
import matplotlib.pyplot as plot

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
    Params - The audio track
    Return - A plot of the audio track
'''
def plotTrack(track, fig):
    pass
track = readTrack('corrupted_signal_created.wav')
frame_rate = track.getframerate()
track_frames = track.getnframes()

print(track_frames)