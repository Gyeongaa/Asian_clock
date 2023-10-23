from settings import play_audio, get_current_time


#These below function can be changed depends on the way you saved your file.

def get_which_meridium(hr: int):
    if hr> 12: #does the requirements need 12 hours formant?
        return 'PM.wav'
    else:
        return 'AM.wav'

def get_hour_filename(hr: int):
    if hr > 12:
        hr = hr%12
    path = 'hours/'
    return path+str(hr) + 'h.wav'


def get_minute_filename(m: int):
    path = 'mins/'
    return path + str(m) + 'm.wav'

def get_sec_filename(s: int):
    path = 'seconds/'
    return path + str(s) + 's.wav'

def ch_clock(speed_rate=1, volume_level=1):
    hour, minute, second = get_current_time("Asia/Shanghai")

    if minute != 0 and second !=0:
        audio_names = ['hello.wav','current_time.wav', get_which_meridium(hour), get_hour_filename(hour),
                       get_minute_filename(minute), get_sec_filename(second)]
    elif minute == 0 and second !=0:
        audio_names = ['hello.wav', 'current_time.wav', get_which_meridium(hour), get_hour_filename(hour),
                       get_sec_filename(second)]
    elif minute != 0 and second == 0:
        audio_names = ['hello.wav', 'current_time.wav', get_which_meridium(hour), get_hour_filename(hour),
                       get_minute_filename(minute)]
    else:
        audio_names = ['hello.wav', 'current_time.wav', get_which_meridium(hour),
                       get_hour_filename(hour)]

    play_audio(audio_names, speed_rate, volume_level, 'MandarinAudios/')
