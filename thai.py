from settings import play_audio, get_current_time, get_which_meridium, get_hour_filename, get_minute_filename

# define 3 functions to return the file name for the current hour, minute, second in Thai pronunciation.
# define some functions to get file names of the involved audios, including hour, minute, second audios,
# to play the videos to present time in a complete sentence.

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
    print(audio_names)
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
        print(audio_names)

    play_audio(audio_names, speed_rate, volume_level, 'ThaiAudios/')

