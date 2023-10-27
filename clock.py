"""
This file contains 5 languages clock functions.
There are chinese(recording, gtts version), japanese, korean, thai and english.
Except for chinese, all audio files are made by gtts.
Also, for recorded chinese audio file, we use separate audio library (pydub)
"""

from audio_setting import play_audio, get_current_time, get_which_meridium, get_hour_filename, get_minute_filename
from pydub import AudioSegment
import audio_effects as ae
from pydub.playback import play
from pydub.utils import ratio_to_db

class Clock:
    def __init__(self, speed_rate=1, volume_level=1):
        self.speed_rate = speed_rate
        self.volume_level = volume_level

    def get_audio_names(self, hour, minute, second):
        """
        This function is made to improve code reusability since Japanese and Korean have same grammar.
        They have "S + O + V" grammar format, while English has "S + V + O" sequence.
        Therefore, it must be at the end to finish the sentence
        Return:
            audio_names 'list' : return audio file name as list type
        """
        if minute != 0:
            audio_names = ['Hello.wav', 'current_time_is.wav',
                           get_which_meridium(hour), get_hour_filename(hour),
                           get_minute_filename(minute), 'ending_sentence.wav']
        else:
            audio_names = ['Hello.wav', 'current_time_is.wav',
                           get_which_meridium(hour), get_hour_filename(hour),
                           'ending_sentence.wav']
        return audio_names

    def get_ch_audio_names(self, hour, minute, second):
        """
        It has same function as get_audio_name(),
        but it is made for only chinese language(natural/gtts type)
        Returns audio_names as list type
        """

        if minute != 0:
            audio_names = ['hello.wav', 'current_time.wav',
                           get_which_meridium(hour), get_hour_filename(hour),
                           get_minute_filename(minute)]
        else:
            audio_names = ['hello.wav', 'current_time.wav',
                           get_which_meridium(hour), get_hour_filename(hour)]

        return audio_names
    def ch_clock(self):
        hour, minute, second = get_current_time("Asia/Shanghai")
        audio_names = self.get_ch_audio_names(hour, minute, second)
        play_audio(audio_names, self.speed_rate, self.volume_level, 'MandarinAudios/')

    def ch_natural_clock(self):
        hour, minute, second = get_current_time("Asia/Shanghai")
        audio_names = self.get_ch_audio_names(hour, minute, second)

        # Generate file paths for all the audios involved
        wav_file_paths = audio_names

        # Define a list to store the audio segments
        audio_segments = []
        # Load and append the WAV files to the audio_segments list
        for wav_file_path in wav_file_paths:
            audio = AudioSegment.from_file(f"MandarinRecordings/{wav_file_path}")

            # Adjust speed rate
            if self.speed_rate > 1:
                audio = audio.speedup(playback_speed=self.speed_rate)
            elif self.speed_rate < 1:
                audio = ae.speed_down(audio, self.speed_rate)

            # Adjust volume by multiplying by volume_level (percentage) using dB conversion
            db = ratio_to_db(self.volume_level)
            audio = audio.apply_gain(db)
            audio_segments.append(audio)

        # Concatenate the audio segments
        combined_audio = sum(audio_segments)

        # Play the concatenated audio
        play(combined_audio)

    def jp_clock(self):
        hour, minute, second = get_current_time("Asia/Tokyo")
        audio_names = self.get_audio_names(hour, minute, second)
        play_audio(audio_names, self.speed_rate, self.volume_level, 'JapaneseAudios/')

    def kr_clock(self):
        hour, minute, second = get_current_time("Asia/Seoul")
        audio_names = self.get_audio_names(hour, minute, second)
        play_audio(audio_names, self.speed_rate, self.volume_level, 'KoreanAudios/')

    def sg_clock(self):
        hour, minute, second = get_current_time("Asia/Singapore")
        # Check if it's an even hour
        if minute == 0:
            audio_names = ['Hello.wav', 'Its.wav', get_hour_filename(hour),
                           'Oclock.wav', get_which_meridium(hour)]
        elif minute == 30:
            audio_names = ['Hello.wav', 'Its.wav',
                           'half.wav', 'past.wav', get_hour_filename(hour),
                           get_which_meridium(hour)]
        elif minute == 15:
            audio_names = ['Hello.wav', 'Its.wav',
                           'quarter.wav', 'past.wav', get_hour_filename(hour),
                           get_which_meridium(hour)]
        elif minute == 45:
            audio_names = ['Hello.wav', 'Its.wav', 'quarter.wav', 'to.wav',
                           get_hour_filename(hour + 1), get_which_meridium(hour)]
        else:
            audio_names = ['Hello.wav', 'Its.wav', get_hour_filename(hour),
                           get_minute_filename(minute), get_which_meridium(hour)]

        play_audio(audio_names, self.speed_rate, self.volume_level, 'EnglishAudios/')

    def get_th_audio_names(self, hr, m):
        """This function is made to get thai audio file names and thai has complex time grammar,
        therefore, we disassemble this function from th_clock as codes are long to process.
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

        if m != 0:
            audio_names += [get_minute_filename(m)]

        return audio_names

    def th_clock(self):
        """this function plays video according to present
        the current time in Thaiand in Thai in complete sentences."""

        hour, minute, second = get_current_time("Asia/Bangkok")
        audio_names = self.get_th_audio_names(hour, minute)
        play_audio(audio_names, self.speed_rate, self.volume_level, 'ThaiAudios/')

