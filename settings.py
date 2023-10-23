"""
Contains functions common to all language logic files.
Also contains vital code for audio input, concatenation, and output.

Authors: Dragos Balan & Hubert Matuszewski
"""
import librosa
import numpy as np
import pygame
import soundfile as sf
import time
import pytz
from datetime import datetime

def get_current_time(timezone_name):
    local_timezone = pytz.timezone(timezone_name)
    current_time = datetime.now(local_timezone)
    time_str = current_time.strftime("%H:%M:%S")
    split_time = time_str.split(':')
    return int(split_time[0]), int(split_time[1]), int(split_time[2])


# Function used for reading the audio
def get_audio(filename: str, path: str):
    audio, sr = librosa.load(path + filename, sr=None)
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
        audio = np.concatenate((audio, get_audio(name, lang_path)))
    return sr, audio


# Convert array of file names to resulting concatenated audio, then plays that
def play_audio(audio_names, speed_rate, volume_level,lang_path):
    sr, result_audio = concatenate_audio(audio_names, lang_path)
    # Apply time stretching only if needed
    if speed_rate != 1:
        result_audio = librosa.effects.time_stretch(result_audio,
                                                    rate=float(speed_rate))

    # Write the result as a .wav file
    sf.write('result.wav', result_audio, sr)
    # Code related to playing the audio file
    pygame.mixer.init()

    aud = pygame.mixer.Sound('result.wav')
    aud.set_volume(volume_level)
    aud.play()
    # Apply this so the audio can play without interruption
    time.sleep(aud.get_length())
    # Unload to make sure we can rewrite "result.wav" again in the same session
    pygame.mixer.music.unload()
