"""
Contains functions common to all language logic files.
Also contains vital code for audio input, concatenation, and output.

Authors: Dragos Balan & Hubert Matuszewski
"""
import librosa
import numpy as np
import pygame
import soundfile as sf
from scipy.io import wavfile
import time


# Function used to get the time that we will process to get the correct
# audio files
def get_current_time():
    current_time = time.strftime('%H:%M')
    split_time = current_time.split(':')
    return int(split_time[0]), int(split_time[1])


# Function used to cut the silence at the beginning and end of an audio signal
def cut_silence(signal,sr=16000,threshold=0.09,padding=40):
    # Max amplitude
    max_signal = max(signal)
    # Determine the threshold as %age of max amplitude
    _threshold = threshold * max_signal
    # Based on the sampling rate, we determine the length of the padding
    # (converted to seconds)
    len_padding = (padding / 1000) * sr
    # Indices of our beginning and end stage.
    cutoff = np.where(signal > _threshold)
    # Extract the actual array
    _cutoff = cutoff[0]
    # Take the first element and go back by the amount of samples stipulated
    # in the padding
    first_cutoff = int(_cutoff[0] - len_padding)
    # Take the last element and go forwards by the amount of samples stipulated
    # in the padding
    last_cutoff = int(_cutoff[-1] + len_padding)
    if first_cutoff < 0:
        # In case someone passes a padding which is too large,
        # to avoid negative indices
        first_cutoff = 0
    if last_cutoff > len(signal):
        # In case someone passes a padding which is too large,
        # to avoid going out of range of array
        last_cutoff = len(signal)
    # Trim our signal according to our calculated endpoints
    _signal = signal[first_cutoff:last_cutoff]
    signal = _signal
    return signal


# Function used for reading the audio
def read_audio(filename: str, path: str):
    audio, sr = librosa.load(path + filename, sr=None)
    #sr, audio = wavfile.read(path + filename)
    # Audio in Romanian has already been manually processed, thus no extra
    # processing is required
    if path != './RomanianAudio/':
        audio = cut_silence(audio,sr=sr)
    return audio


# Returns the sample rate of the audio file
def get_sr(filename: str, path: str):
    audio, sr = librosa.load(path + filename)
    return sr


# Determines if we return the equivalent of "past" or "to" in English
#def with_or_without(m: int):
#    return 'to.wav' if m > 30 else 'and.wav'


# Concatenate the audio files given an array of filename strings
def concatenate_audio(filenames, lang_path):
    audio = []
    sr = get_sr(filenames[0], lang_path)
    for name in filenames:
        audio = np.concatenate((audio, read_audio(name, lang_path)))
    return sr, audio


# Convert array of file names to resulting concatenated audio, then plays that
def play_audio(audio_names, speed_rate, lang_path):
    sr, result_audio = concatenate_audio(audio_names, lang_path)
    # Apply time stretching only if needed
    if speed_rate != 1:
        result_audio = librosa.effects.time_stretch(result_audio,
                                                    rate=float(speed_rate))

    # Convert to 16-bit integer format so the audio player understands it
    #result_audio = np.array(result_audio, dtype=np.int16)
    # Write the result as a .wav file
    print(sr, result_audio)
    sf.write('result.wav', result_audio, sr)
    # Code related to playing the audio file
    pygame.mixer.init()
    aud = pygame.mixer.Sound('result.wav')
    aud.play()
    # Apply this so the audio can play without interruption
    time.sleep(aud.get_length())
    # Unload to make sure we can rewrite "result.wav" again in the same session
    pygame.mixer.music.unload()
