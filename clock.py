"""
This file contains 5 languages clock functions.
There are chinese(recording, gtts version), japanese, korean, thai and english.
Except for chinese, all audio files are made by gtts.
Also, for recorded chinese audio file, we use seperate audio library (pydub)
"""



from settings import play_audio, get_current_time, get_which_meridium, get_hour_filename, get_minute_filename
from pydub import AudioSegment
import audio_effects as ae
from pydub.playback import play
from pydub.utils import ratio_to_db


def ch_clock(speed_rate=1, volume_level=1):
    hour, minute, second = get_current_time("Asia/Shanghai")

    if minute != 0:
        audio_names = ['hello.wav','current_time.wav', get_which_meridium(hour), get_hour_filename(hour),
                       get_minute_filename(minute)]
    else:
        audio_names = ['hello.wav', 'current_time.wav', get_which_meridium(hour), get_hour_filename(hour)]

    play_audio(audio_names, speed_rate, volume_level, 'MandarinAudios/')


def jp_clock(speed_rate=1, volume_level = 1):
    hour, minute, second = get_current_time("Asia/Tokyo")

    if minute != 0:
        audio_names = ['Hello.wav', 'current_time_is.wav', get_which_meridium(hour), get_hour_filename(hour),
                       get_minute_filename(minute), 'ending_sentence.wav']
    else:
        audio_names = ['Hello.wav', 'current_time_is.wav', get_which_meridium(hour), get_hour_filename(hour),
                       'ending_sentence.wav']

    play_audio(audio_names, speed_rate, volume_level, 'JapaneseAudios/')

def kr_clock(speed_rate=1, volume_level = 1):
    hour, minute, second = get_current_time("Asia/Seoul")

    if minute!= 0:
        audio_names = ['Hello.wav','current_time_is.wav', get_which_meridium(hour), get_hour_filename(hour),
                       get_minute_filename(minute), 'ending_sentence.wav']
    else:
        audio_names = ['Hello.wav', 'current_time_is.wav', get_which_meridium(hour), get_hour_filename(hour),
                       'ending_sentence.wav']

    play_audio(audio_names, speed_rate, volume_level, 'KoreanAudios/')
    print('korea')

def sg_clock(speed_rate=1, volume_level=1):
    hour, minute, second = get_current_time("Asia/Singapore")
    # Check if it's an even hour
    if minute == 0:
        audio_names = ['Hello.wav', 'Its.wav', get_hour_filename(hour), 'Oclock.wav', get_which_meridium(hour)]
    elif minute == 30:
        audio_names = ['Hello.wav','Its.wav', 'half.wav','past.wav',get_hour_filename(hour), get_which_meridium(hour)]
    elif minute == 15:
        audio_names = ['Hello.wav','Its.wav','quarter.wav','past.wav',get_hour_filename(hour),get_which_meridium(hour)]
    elif minute == 45:
        audio_names = ['Hello.wav','Its.wav','quarter.wav','to.wav',get_hour_filename(hour+1),get_which_meridium(hour)]
    else:
        audio_names = ['Hello.wav', 'Its.wav', get_hour_filename(hour), get_minute_filename(minute), get_which_meridium(hour)]

    play_audio(audio_names, speed_rate, volume_level, 'EnglishAudios/')


def hour_audios(hr):
    """The hour_audios function plays audio when it's on the hour.
    The time system used in Thailand is the 6-hour clock, and the word for "am" and "pm" differs."""

    # Initialize the list of audio names
    audio_names = ["hello.wav", "the current time is.wav"]

    if hr <= 5 and hr >= 1:
        # When it's 1-5am, the format is "am" (for 1-5) + the number of the hour
        audio_names += ["am_1_5.wav", get_hour_filename(hr)]

    elif hr <= 11 and hr >= 6:
        # When it's 6-11am, the format is the number of the hour + "o'clock" in Thai + "am" (for 6-11)
        audio_names += [get_hour_filename(hr), "o'clock.wav", "am_6_11.wav"]

    elif hr == 12:
        # A specific word for 12pm
        audio_names += ["midday.wav"]

    elif hr <= 17 and hr >= 13:
        # When it's 1-5pm, the format is "pm" (for 1-5) + the number of the hour + "o'clock" in Thai
        audio_names += ["pm_1_5.wav", get_hour_filename(hr), "o'clock.wav"]

    elif hr <= 23 and hr >= 18:
        # When it's 6-11pm, the format is the number of the hour + "pm" (for 6-11)
        audio_names += [get_hour_filename(hr), "pm_6_11.wav"]

    elif hr == 0:
        # A specific word for 12am
        audio_names += ["midnight.wav"]
    return audio_names


def minute_audios(hr, m):
    """the minute_audios function plays video when the minute is not at 0.
It presents hour information first then minute information"""

    # add the file names of hour
    audio_names = hour_audios(hr)
    # add the file name of minute number
    audio_names += [get_minute_filename(m)]
    # add the file name of word "minutes" in Thai

    return audio_names


def th_clock(speed_rate=1, volume_level=1):
    """this function plays video according to present the current time in Thaiand in Thai in complete sentences."""

    hour, minute, second = get_current_time("Asia/Bangkok")

    if minute == 0:
        audio_names = hour_audios(hour)
    else:
        audio_names = minute_audios(hour, minute)

    play_audio(audio_names, speed_rate, volume_level, 'ThaiAudios/')

def ch_natural_clock(speed_rate=1, volume_level=1):
    hour, minute, second = get_current_time("Asia/Shanghai")

    if minute != 0:
        audio_names = ['hello.wav', 'current_time.wav', get_which_meridium(hour), get_hour_filename(hour),
                       get_minute_filename(minute)]
    else:
        audio_names = ['hello.wav', 'current_time.wav', get_which_meridium(hour), get_hour_filename(hour)]

    # Generate file paths for all the audios involved
    wav_file_paths = audio_names

    # Define a list to store the audio segments
    audio_segments = []

    # Load and append the WAV files to the audio_segments list
    for wav_file_path in wav_file_paths:
        audio = AudioSegment.from_file(f"MandarinRecordings/{wav_file_path}")


        # Adjust speed rate
        if speed_rate > 1:
            audio = audio.speedup(playback_speed=speed_rate)
        elif speed_rate <1:
            audio = ae.speed_down(audio, speed_rate)


        # Adjust volume by multiplying by volume_level (percentage) using dB conversion
        db = ratio_to_db(volume_level)
        audio = audio.apply_gain(db)

        audio_segments.append(audio)

    # Concatenate the audio segments
    combined_audio = sum(audio_segments)

    # Play the concatenated audio
    play(combined_audio)
