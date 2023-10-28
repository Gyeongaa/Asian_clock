"""
This file contains basic functions for audio processing.
It covers getting current time, audio, sampling rate and hour, minute, seconds file name etc.
Also contains vital code for concatenation, and play.

Authors: Soogyeong Shin
"""

import librosa
import numpy as np
import pygame
import soundfile as sf
import time
import pytz
from datetime import datetime


def get_current_time(timezone_name):
    """
    Get current time based on the time zone that user selected
        Args:
            local_time_zone : get location
            current_time 'datetime' : get current local time
            time_str 'str' :
        Retruns:
            splited time 'int' : hour, minute, seconds
    """
    local_timezone = pytz.timezone(timezone_name)
    current_time = datetime.now(local_timezone)
    time_str = current_time.strftime("%H:%M:%S")
    split_time = time_str.split(':')
    return int(split_time[0]), int(split_time[1]), int(split_time[2])


"""
General description for get_audio/sr().
Function used for reading the audio
Args:
    audio 'ndarray' : readed audio file
    sr 'float' : sampling rate
Return:
    audio : audio file 
    or sr : sampling rate
    """
def get_audio(filename: str, path: str):
    audio, sr = librosa.load(path + filename, sr=None)
    return audio


# Returns the sampling rate of the audio file
def get_sr(filename: str, path: str):
    audio, sr = librosa.load(path + filename)
    return sr

def get_which_meridium(hr: int):
    """
    Get meridium ("AM", "PM") by getting current hour value
    Return:
        meridium audio file name 'str' : 'PM.wav' or 'AM.wav'
    """
    if hr> 12:
        return 'PM.wav'
    else:
        return 'AM.wav'


"""
General description for get_hour/minute_seconds_filename()
Each function takes each hour, minute, seconds to get audio file name(string type).
They return directory path + audio file name such as 'hours/7h.wav' as a string type.
"""
def get_hour_filename(hr: int):
    if hr > 12:
        hr = hr % 12
    path = 'hours/'
    return path+str(hr) + 'h.wav'

def get_minute_filename(m: int):
    path = 'mins/'
    return path + str(m) + 'm.wav'

def get_sec_filename(s: int):
    path = 'seconds/'
    return path + str(s) + 's.wav'



def concatenate_audio(filenames, lang_path):
    """
    Concatenate the audio files given an array of filename strings
    Returns sampling rate and audio file after concatenating.
    """
    audio = []
    sr = get_sr(filenames[0], lang_path)
    for name in filenames:
        audio = np.concatenate((audio, get_audio(name, lang_path)))
    return sr, audio



def play_audio(audio_names, speed_rate, volume_level, lang_path):
    """
    Convert array of file names to resulting concatenated audio, then plays.
    Args:
        audio_names 'list' : a list of audio file names such as ['hours/7h.wav', 'minutes/26m.wav'].
        speed_rate : speed rate from 0.25 to 2.0.
        volume_level : volume level from 0 to 1.0.
        lang_path 'str' : country audio directory path such as 'JapaneseAudios/'
    Returns:
        None
    """
    try:
        # Concatenate the audio files
        sr, result_audio = concatenate_audio(audio_names, lang_path)

        # Apply time stretching only if needed
        if speed_rate != 1:
            result_audio = librosa.effects.time_stretch(result_audio, rate=float(speed_rate))

        # Write the result as a .wav file
        sf.write('result.wav', result_audio, sr)

        # Initialize the mixer
        pygame.mixer.init()

        # Check if the mixer is already initialized
        if not pygame.mixer.get_init():
            raise Exception("Mixer not initialized")

        # Load and play the audio
        pygame.mixer.music.load('result.wav')
        pygame.mixer.music.set_volume(volume_level)
        pygame.mixer.music.play()

        # Ensure the audio plays without interruption
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)

        # Unload to make sure we can rewrite "result.wav" again in the same session
        pygame.mixer.music.stop()
        pygame.mixer.quit()

    except Exception as e:
        print("An error occurred:", e)


# stop playing audios
def stop_audio():
    pygame.mixer.music.stop()


