from settings import play_audio, get_current_time, get_which_meridium, get_hour_filename, get_minute_filename

def sg_clock(speed_rate=1, volume_level=1):
    hour, minute, second = get_current_time("Asia/Singapore")

    # Check if it's an even hour
    if minute == 0:
        audio_names = ['Hello.wav', 'Its.wav', get_hour_filename(hour), 'Oclock.wav', get_which_meridium(hour)]
    else:
        audio_names = ['Hello.wav', 'Its.wav', get_hour_filename(hour), get_minute_filename(minute), get_which_meridium(hour)]

    play_audio(audio_names, speed_rate, volume_level, 'EnglishAudios/')
