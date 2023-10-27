"""
This file contains alarm class
Create alarm window, set and trigger alarm.
User can choose the time zone for setting alarm.
"""

import tkinter as tk
import pytz
from datetime import datetime
import pygame
from threading import Timer

class Alarm:
    """
    This class serves as alarm function.

    Methods:
        create_alarm_window(): Create alarm window following user input(press alarm button in main ui).
        set_custom_alarm() : Set custom alarm. It has hour, minute, time zone variables.
        trigger_alarm() : Play alarm sound on the time user set.
    """
    def __init__(self, mainUI):
        self.custom_alarms = []
        self.mainUI = mainUI
        self.name_entry = None
        self.confirmation_label = None

    def create_alarm_window(self):
        new_alarm_window = tk.Toplevel(self.mainUI)
        new_alarm_window.title("Set Custom Alarm")
        new_alarm_window.geometry("400x400")

        time_label = tk.Label(new_alarm_window, text="Set Alarm Time:")
        time_label.pack()
        self.hour_var = tk.StringVar()
        self.minute_var = tk.StringVar()
        self.ampm_var = tk.StringVar()

        hour_menu = tk.OptionMenu(new_alarm_window, self.hour_var, *range(0, 12))
        hour_menu.configure(width=5)
        minute_menu = tk.OptionMenu(new_alarm_window, self.minute_var, *range(0, 60))
        minute_menu.config(width=5)
        ampm_menu = tk.OptionMenu(new_alarm_window, self.ampm_var, "AM", "PM")
        ampm_menu.config(width=2)
        hour_menu.pack()
        minute_menu.pack()
        ampm_menu.pack()

        name_label = tk.Label(new_alarm_window, text="Enter Alarm Name:")
        self.name_entry = tk.Entry(new_alarm_window, font=("Helvetica", 12))
        name_label.pack()
        self.name_entry.pack()

        timezone_label = tk.Label(new_alarm_window, text="Select Timezone:")
        self.timezone_var = tk.StringVar()
        self.timezone_var.set("Singapore")  # Default timezone
        timezone_menu = tk.OptionMenu(new_alarm_window, self.timezone_var, "Singapore", "Shanghai",
                                      "Tokyo", "Seoul", "Bangkok")
        timezone_menu.config(font=("Helvetica", 12))
        timezone_label.pack()
        timezone_menu.pack()

        # Create a label to display the confirmation message
        self.confirmation_label = tk.Label(new_alarm_window, text="", font=("Helvetica", 14))  # Define confirmation_label here
        self.confirmation_label.pack()

        # Create a button to set the custom alarm
        set_alarm_button = tk.Button(new_alarm_window, text="Set Alarm", command=self.set_custom_alarm)
        set_alarm_button.pack()

        # Append the new custom alarm window to the list
        self.custom_alarms.append(new_alarm_window)

    def set_custom_alarm(self):
        hour = int(self.hour_var.get())
        minute = int(self.minute_var.get())
        ampm = self.ampm_var.get()
        alarm_name = self.name_entry.get()
        alarm_timezone ='Asia/'+self.timezone_var.get()
        try:
            if alarm_name == '':
                raise TypeError('You need to add an alarm name')
        except TypeError as e:
            confirmation_text = str(e)
            self.confirmation_label.config(text=confirmation_text)
        else:
        # Convert to 24-hour format
            if ampm == "PM":
                hour = hour + 12

            local_timezone = pytz.timezone(alarm_timezone)
            current_time = datetime.now(local_timezone).replace(microsecond=0)

            alarm_time = current_time.replace(hour=hour, minute=minute, second=0)
            time_difference = (alarm_time - current_time).total_seconds()

            if time_difference < 0:
                confirmation_text = f"Alarm ({alarm_name}):\n{alarm_time.strftime('%Y-%m-%d %I:%M:%S %p')} is past!"
                self.confirmation_label.config(text=confirmation_text)
            else:
                confirmation_text = f"Alarm ({alarm_name}):\n{alarm_time.strftime('%Y-%m-%d %I:%M:%S %p')} is set"
                self.confirmation_label.config(text=confirmation_text)  # Use self.confirmation_label

                # Schedule the alarm to trigger after the time difference elapses
                t = Timer(time_difference, self.trigger_alarm)
                t.start()

    def trigger_alarm(self):
        # Play the alarm sound (modify this line to use your own sound)
        alarm_sound = pygame.mixer.Sound("alarm.wav")
        alarm_sound.play()

        # Close the custom alarm window after the alarm triggers
        self.custom_alarms[-1].destroy()


