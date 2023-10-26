from settings import play_audio, get_current_time, get_which_meridium, get_hour_filename, get_minute_filename
from pydub import AudioSegment
from pydub.playback import play
from pydub.utils import ratio_to_db


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

        # Adjust  speed rate
        if speed_rate !=1:
            audio = audio.speedup(playback_speed=speed_rate)

        # Adjust volume by multiplying by volume_level (percentage) using dB conversion
        db = ratio_to_db(volume_level)
        audio = audio.apply_gain(db)

        audio_segments.append(audio)

    # Concatenate the audio segments
    combined_audio = sum(audio_segments)

    # Play the concatenated audio
    play(combined_audio)

