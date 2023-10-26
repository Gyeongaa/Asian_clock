from settings import play_audio, get_current_time, get_which_meridium, get_hour_filename, get_minute_filename

def jp_clock(speed_rate=1, volume_level = 1):
    hour, minute, second = get_current_time("Asia/Tokyo")

    if minute != 0:
        audio_names = ['Hello.wav', 'current_time_is.wav', get_which_meridium(hour), get_hour_filename(hour),
                       get_minute_filename(minute), 'ending_sentence.wav']
    else:
        audio_names = ['Hello.wav', 'current_time_is.wav', get_which_meridium(hour), get_hour_filename(hour),
                       'ending_sentence.wav']

    play_audio(audio_names, speed_rate, volume_level, 'JapaneseAudios/')
