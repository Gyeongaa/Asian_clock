import threading
from clock import Clock

CAPITAL_DICT = {
    "CHINA": "Asia/Shanghai",
    "JAPAN": "Asia/Tokyo",
    "KOREA": "Asia/Seoul",
    "THAILAND": "Asia/Bangkok",
    "SINGAPORE": "Asia/Singapore"}


class Button (Clock):
    def __init__(self, mainUI, buttons):
        self.mainUI = mainUI
        self.buttons = buttons

    def disable_buttons(self):
        for button in self.buttons:
            button.config(state="disabled")

    def enable_buttons(self):
        # Enable buttons
        for button in self.buttons:
            button.config(state="active")

    def t2_completed(self):
        # print("t2_completed")
        self.enable_buttons()

    def t2_worker(clock, clock_name, callback):
        # t2의 작업을 수행
        if clock_name == "kr_clock":
            clock.kr_clock()
        elif clock_name == "jp_clock":
            clock.jp_clock()
        elif clock_name == "ch_clock":
            clock.ch_clock()
        elif clock_name == "ch_natural_clock":
            clock.ch_natural_clock()
        elif clock_name == "sg_clock":
            clock.sg_clock()
        elif clock_name == "th_clock":
            clock.th_clock()

        callback()

    def china_audio(self, *args):
        selected_audio = audio_choice.get()
        if selected_audio == "China Natural":
            # Play natural Chinese audio (replace with nature with your actual audio file)
            button_callback("CHINA", 'natural')
        elif selected_audio == "China Synthetic":
            # Play synthetic Chinese audio (replace with your actual audio file)
            button_callback("CHINA", 'gtts')

    def button_callback(self, country: str, type=None):
        self.mainUI.after(500, self.disable_buttons)
        from main import show_local_time
        t1 = threading.Thread(target=show_local_time, args=(CAPITAL_DICT[country],))
        from main import speed_rate, volume_level
        clock = Clock(speed_rate.get(), volume_level.get())
        if country == "CHINA":
            if type == 'gtts':
                t2 = threading.Thread(target=self.t2_worker, args=(clock, 'ch_clock', self.t2_completed,))

            elif type == 'natural':
                t2 = threading.Thread(target=self.t2_worker, args=(clock, 'ch_natural_clock', self.t2_completed,))

        elif country == "JAPAN":
            t2 = threading.Thread(target=self.t2_worker, args=(clock, 'jp_clock', self.t2_completed,))

        elif country == "KOREA":
            t2 = threading.Thread(target=self.t2_worker, args=(clock, 'kr_clock', self.t2_completed,))

        elif country == "THAILAND":
            t2 = threading.Thread(target=self.t2_worker, args=(clock, 'th_clock', self.t2_completed,))

        elif country == "SINGAPORE":
            t2 = threading.Thread(target=self.t2_worker, args=(clock, 'sg_clock', self.t2_completed,))

        t1.start()
        t2.start()







