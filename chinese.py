from settings import play_audio, get_current_time, get_which_meridium, get_hour_filename, get_minute_filename

#These below function can be changed depends on the way you saved your file.
def ch_clock(speed_rate=1, volume_level=1):
    hour, minute, second = get_current_time("Asia/Shanghai")

    if minute != 0:
        audio_names = ['hello.wav','current_time.wav', get_which_meridium(hour), get_hour_filename(hour),
                       get_minute_filename(minute)]
    else:
        audio_names = ['hello.wav', 'current_time.wav', get_which_meridium(hour), get_hour_filename(hour)]

    play_audio(audio_names, speed_rate, volume_level, 'MandarinAudios/')
