# Import standard library modules
import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from threading import Timer

# Import external libraries
import pygame
import pytz

class Alarm:
    def __init__(self, mainUI):
        self.custom_alarms = []
        self.mainUI = mainUI
        self.name_entry = None
        self.confirmation_label = None

    """
    General description for create_alarm_window()
    get the alarm time that user input through the option menu.
    There are 4 variables: hour, minute, am/pm, timezone.
    """

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
        timezone_menu = tk.OptionMenu(new_alarm_window, self.timezone_var, "Singapore",
                                      "Shanghai", "Tokyo", "Seoul", "Bangkok")
        timezone_menu.config(font=("Helvetica", 12))
        timezone_label.pack()
        timezone_menu.pack()

        # Create a label to display the confirmation message
        self.confirmation_label = tk.Label(new_alarm_window, \
                                           text="", font=("Helvetica", 14))
        self.confirmation_label.pack()

        # Create a button to set the custom alarm
        set_alarm_button = tk.Button(new_alarm_window, \
                                     text="Set Alarm", command=self.set_custom_alarm)
        set_alarm_button.pack()

        # Append the new custom alarm window to the list
        self.custom_alarms.append(new_alarm_window)

    """
    store the four variables that user's input,
    error handling: message box, if any input was missing, it will pump out to notify users.
    also compare the alarm time to current time, get the time difference to trigger alarm.
    """
    def set_custom_alarm(self):
        try:
            hour_str = self.hour_var.get()
            minute_str = self.minute_var.get()
            ampm = self.ampm_var.get()
            alarm_name = self.name_entry.get()
            alarm_timezone = 'Asia/' + self.timezone_var.get()

            # Check if the hour, minute, am/pm is not chosen, and if the alarm name is not set
            if not hour_str:
                raise ValueError('Please select a valid hour for the alarm.')

            if not minute_str:
                raise ValueError('Please select a valid minute for the alarm.')

            if not ampm:
                raise ValueError('Please select am or pm for the alarm.')

            if not alarm_name:
                raise ValueError('Please enter an alarm name.')

            hour = int(hour_str)
            minute = int(minute_str)

            # Convert to 24-hour format
            if ampm == "PM":
                hour = hour + 12

            local_timezone = pytz.timezone(alarm_timezone)
            current_time = datetime.now(local_timezone).replace(microsecond=0)

            alarm_time = current_time.replace(hour=hour, minute=minute, second=0)
            time_difference = (alarm_time - current_time).total_seconds()

            if time_difference < 0:
                raise ValueError(f"Alarm ({alarm_name}):\
                \n{alarm_time.strftime('%Y-%m-%d %I:%M:%S %p')} is past!")

            confirmation_text = f"Alarm ({alarm_name}):\
            \n{alarm_time.strftime('%Y-%m-%d %I:%M:%S %p')} is set"
            self.confirmation_label.config(text=confirmation_text)

            # Schedule the alarm to trigger after the time difference elapses
            t = Timer(time_difference, self.trigger_alarm)
            t.start()
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    """
    activate the alarm, play the alarm music.
    """
    def trigger_alarm(self):
        # Play the alarm sound (modify this line to use your own sound)
        alarm_sound = pygame.mixer.Sound("alarm.wav")
        alarm_sound.play()

        # Close the custom alarm window after the alarm triggers
        self.custom_alarms[-1].destroy()