from settings import play_audio, get_current_time

def get_which_meridium(hr: int):
    if hr >= 12:
        return 'PM.wav'
    else:
        return 'AM.wav'

def get_hour_filename(hr: int):
    if hr > 12:
        hr = hr % 12
    path = 'hours/'
    return path + str(hr) + 'h.wav'

def get_minute_filename(m: int):
    path = 'mins/'
    return path + str(m) + 'm.wav'

def get_sec_filename(s: int):
    path = 'seconds/'
    return path + str(s) + 's.wav'

def sg_clock(speed_rate=1):
    hour, minute, second = get_current_time("Asia/Singapore")

    audio_names = ['Hello.wav', 'Its.wav']

    if hour % 2 == 0:
        audio_names.append('Oclock.wav')

    audio_names.append(get_hour_filename(hour))
    audio_names.append(get_minute_filename(minute))
    audio_names.append(get_sec_filename(second))
    audio_names.append(get_which_meridium(hour))

    play_audio(audio_names, speed_rate, 'EnglishAudios/')
