import tkinter as tk
from tkinter import ttk
from datetime import datetime
import pytz
import threading
import pygame

import time
from tkinter import OptionMenu
from PIL import Image, ImageTk
from korean import kr_clock
from Japanese import jp_clock
from singapore import sg_clock
from thai import th_clock
from chinese import ch_clock
from ChineseNatural import ch_natural_clock
from tkinter import OptionMenu, StringVar
from settings import get_current_time

# Create the main window
mainUI = tk.Tk()
mainUI.title("Asian Time")
pygame.init()
pygame.mixer.init()

# Use a relative path to open the background image
background_image = Image.open("images/Asia_Map_Resized.png")
background_photo = ImageTk.PhotoImage(background_image)

# Import the night version background image
night_background_image = Image.open("images/Asia_Map_Night_Resized.png")
night_background_photo = ImageTk.PhotoImage(night_background_image)

# Set the window size to match the background image size and user can't change window size
mainUI.geometry(f"{background_image.width}x{background_image.height}")
mainUI.resizable(False, False)

# Create a Label to display the background image, using relwidth and relheight to fill the entire window
background_label = tk.Label(mainUI, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create a label for the default time text
default_time_label = tk.Label(mainUI, text="Default: Singapore time",
                              font=("Helvetica", 24, "bold"), bg="white")
default_time_label.place(x=20, y=200, anchor="w")

# Create a label for displaying the current time
current_time_label = tk.Label(mainUI, text="", font=("Helvetica", 24))
current_time_label.place(x=20, y=235, anchor="w")

def slider_sr(val):  # slider for speed rate
    new_val = min(speed_rates, key=lambda x: abs(x - float(SpeedRate.get())))
    SpeedRate.set(new_val)

def slider_vl(val):  # slider for volume level
    new_val = min(volume_level, key=lambda x: abs(x - float(VolumeLevel.get())))
    VolumeLevel.set(new_val)

#regarding to speed rate setting
speed_rates = [0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2]
SpeedRate = tk.Scale(mainUI, from_=0.25, to=2,
                     font=("Helvetica", 12, "bold"), command=slider_sr,
                     orient="horizontal", digits=3, resolution=0.25)
SpeedRate.set(1) #default value is 1
SpeedRate.place(x=20, y=600)
SpeedRate.configure(bg='white', label='Change the speed rate', troughcolor='grey', length=360)

#regarding to volume level setting
volume_level = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
VolumeLevel = tk.Scale(mainUI, from_=0, to=1,
                       font=("Helvetica", 12, "bold"), command=slider_vl,
                       orient="horizontal", digits=3, resolution=0.1)
VolumeLevel.set(1)
VolumeLevel.place(x=20, y=650)
VolumeLevel.configure(bg='white', label='Change the volume level', troughcolor='grey', length=360)


def set_background():
    hour= get_current_time("Asia/Singapore")[0]
    if hour >= 6 and hour <= 18:
            background_label.config(image=background_photo)
    else:
        background_label.config(image=night_background_photo)

def change_background(mode):
    if mode == "Light":
        background_label.config(image=background_photo)
    elif mode == "Dark":
        background_label.config(image=night_background_photo)


# Create a button to toggle between modes
mode_choice = tk.StringVar()
mode_combobox = ttk.Combobox(mainUI, textvariable=mode_choice)
mode_combobox["values"] = ("Light", "Dark")
mode_combobox.set("Light")
mode_combobox.bind("<<ComboboxSelected>>", lambda event: change_background(mode_choice.get()))
mode_combobox.configure(width=20)
mode_combobox.place(x=20, y=500)

# Function to update the Singapore time label
def update_singapore_time():
    singapore_timezone = pytz.timezone("Asia/Singapore")
    current_time = datetime.now(singapore_timezone)
    time_str = current_time.strftime("%Y-%m-%d %I:%M:%S %p")
    current_time_label.config(text=time_str)
    mainUI.after(1000, update_singapore_time)  # Update every second

# Start updating the Singapore time label
update_singapore_time()
t1 = threading.Thread(target=update_singapore_time)
t1.start()

# Function to toggle between Light Mode and Dark Mode


def show_world_time(timezone_name: str):
    local_timezone = pytz.timezone(timezone_name)
    current_time = datetime.now(local_timezone)
    time_str = current_time.strftime("%Y-%m-%d %I:%M:%S %p")
    time_str = time_str.lstrip("0").replace(" 0", " ")
    return time_str

def show_local_time(time_zone):
    time_str = show_world_time(time_zone)

    # Create a new window to display local time
    local_time_window = tk.Toplevel(mainUI)
    local_time_window.title("Local Time")
    local_time_window.geometry("300x100")
    time_label = tk.Label(local_time_window, text=time_str, font=("Helvetica", 20))
    time_label.pack(pady=20)
    time_label.config(text=time_str)

    def update_local_time():
        time_str = show_world_time(time_zone)
        time_label.config(text=time_str)
        local_time_window.after(1000, update_local_time)
    update_local_time()



def enable_buttons():
    # Enable buttons
    for button in buttons:
        button.config(state="active")


def button1_callback():
    # Disable buttons
    for button in buttons:
        button.config(state="disabled")

    # Start the show_world_time and ch_clock threads
    thread1 = threading.Thread(target=show_local_time, args=("Asia/Shanghai",))
    thread2 = threading.Thread(target=ch_clock, args=(SpeedRate.get(), VolumeLevel.get()))
    thread1.daemon = True
    thread2.daemon = True
    thread1.start()
    thread2.start()

    # enable buttons
    mainUI.after(8500, enable_buttons)


def button2_callback():
    for button in buttons:
        button.config(state="disabled")

    thread1 = threading.Thread(target=show_local_time, args=("Asia/Tokyo",))
    thread2 = threading.Thread(target=jp_clock, args=(SpeedRate.get(), VolumeLevel.get()))
    thread1.start()
    thread2.start()
    mainUI.after(8500, enable_buttons)


def button3_callback():
    for button in buttons:
        button.config(state="disabled")

    thread1 = threading.Thread(target=show_local_time, args=("Asia/Seoul",))
    thread2 = threading.Thread(target=kr_clock, args=(SpeedRate.get(), VolumeLevel.get()))
    thread1.start()
    thread2.start()
    mainUI.after(8500, enable_buttons)


def button4_callback():
    # Disable buttons

    for button in buttons:
        button.config(state="disabled")

    thread1 = threading.Thread(target=show_local_time, args=("Asia/Bangkok",))
    thread2 = threading.Thread(target=th_clock, args=(SpeedRate.get(), VolumeLevel.get()))
    thread1.start()
    thread2.start()
    mainUI.after(8500, enable_buttons)


def button5_callback():
    # Disable buttons
    for button in buttons:
        button.config(state="disabled")

    thread1 = threading.Thread(target=show_local_time, args=("Asia/Singapore",))
    thread2 = threading.Thread(target=sg_clock, args=(SpeedRate.get(), VolumeLevel.get()))
    thread1.start()
    thread2.start()
    mainUI.after(8500, enable_buttons)

def button6_callback():
    # Disable buttons
    for button in buttons:
        button.config(state="disabled")

    thread1 = threading.Thread(target=show_local_time, args=("Asia/Shanghai",))
    thread2 = threading.Thread(target=ch_natural_clock, args=(SpeedRate.get(), VolumeLevel.get()))
    thread1.start()
    thread2.start()
    mainUI.after(8500, enable_buttons)

# Function to play the selected Chinese audio, either in natural or synthetic Chinese voice
def china_audio(*args):
    selected_audio = audio_choice.get()
    if selected_audio == "China Natural":
        # Play natural Chinese audio (replace with your actual audio file)
        button6_callback()
    elif selected_audio == "China Synthetic":
        # Play synthetic Chinese audio (replace with your actual audio file)
        button1_callback()

# Create buttons for different countries

# A combobox is created to choose synthetic or natural chinese voice for button China
# Create a variable to store the selected audio choice
audio_choice = tk.StringVar()

# Create a Combobox (dropdown) with audio choices for Chinese
button1 = ttk.Combobox(mainUI, textvariable=audio_choice)
button1["values"] = ("China Natural", "China Synthetic")
button1.set("China Natural")
button1.bind("<<ComboboxSelected>>", china_audio)
button1.configure(width=10)

button2 = tk.Button(mainUI,text="JAPAN", compound=tk.TOP, command=lambda: button2_callback())
button3 = tk.Button(mainUI,text="KOREA", compound=tk.TOP, command=lambda: button3_callback())
button4 = tk.Button(mainUI, text="THAILAND", compound=tk.TOP, command=lambda: button4_callback())
button5 = tk.Button(mainUI, text="SINGAPORE", compound=tk.TOP, command=lambda: button5_callback())

buttons = [button1, button2, button3, button4, button5]

# Function to update button positions based on window size
button1.place(x=630, y=345)
button2.place(x=1020, y=300)
button3.place(x=910, y=300)
button4.place(x=620, y=540)
button5.place(x=640, y=680)



# Bind a function to the <Configure> event to update button positions
mainUI.bind("<Configure>", lambda event: set_background())

# Create a new window for setting custom alarms
custom_alarm_window = tk.Toplevel(mainUI)
custom_alarm_window.title("Set Custom Alarm")
custom_alarm_window.withdraw()

custom_alarm_window.geometry("400x600")

# Create labels for time, name, and timezone
time_label = tk.Label(custom_alarm_window, text="Set Alarm Time:")
time_label.pack()
hour_var = StringVar()
minute_var = StringVar()
ampm_var = StringVar()

# Create OptionMenus for hour, minute, and AM/PM
hour_menu = OptionMenu(custom_alarm_window, hour_var, *range(1, 13))
minute_menu = OptionMenu(custom_alarm_window, minute_var, *range(0, 60))
ampm_menu = OptionMenu(custom_alarm_window, ampm_var, "AM", "PM")

hour_menu.pack()
minute_menu.pack()
ampm_menu.pack()

# Create labels and entry widgets for name and timezone
name_label = tk.Label(custom_alarm_window, text="Enter Alarm Name:")
name_entry = tk.Entry(custom_alarm_window, font=("Helvetica", 12))
if name_label == "":
    name_entry = "Default"
name_label.pack()
name_entry.pack()

timezone_label = tk.Label(custom_alarm_window, text="Select Timezone:")
timezone_var = tk.StringVar()
timezone_var.set("Asia/Singapore")  # 默认时区
timezone_menu = tk.OptionMenu(custom_alarm_window, timezone_var, "Asia/Singapore", "Asia/Shanghai", "Asia/Tokyo",
                              "Asia/Seoul", "Asia/Bangkok")
timezone_menu.config(font=("Helvetica", 12))
timezone_label.pack()
timezone_menu.pack()

# Function to open the custom alarm window
custom_alarms = []


def open_custom_alarm_window():
    new_custom_alarm_window = tk.Toplevel(mainUI)
    new_custom_alarm_window.title("Set Custom Alarm")
    new_custom_alarm_window.geometry("400x400")

    # Create labels for time, name, and timezone
    time_label = tk.Label(new_custom_alarm_window, text="Set Alarm Time:")
    time_label.pack()

    hour_var = tk.StringVar()
    minute_var = tk.StringVar()
    ampm_var = tk.StringVar()

    # Create OptionMenus for hour, minute, and AM/PM
    hour_menu = tk.OptionMenu(new_custom_alarm_window, hour_var, *range(0, 12))
    hour_menu.configure(width=50)
    minute_menu = tk.OptionMenu(new_custom_alarm_window, minute_var, *range(0, 60))
    minute_menu.config(width=50)
    ampm_menu = tk.OptionMenu(new_custom_alarm_window, ampm_var, "AM", "PM")
    ampm_menu.config(width=50)
    hour_menu.pack()
    minute_menu.pack()
    ampm_menu.pack()

    name_label = tk.Label(new_custom_alarm_window, text="Enter Alarm Name:")
    name_entry = tk.Entry(new_custom_alarm_window, font=("Helvetica", 12))
    name_label.pack()
    name_entry.pack()

    timezone_label = tk.Label(new_custom_alarm_window, text="Select Timezone:")
    timezone_var = tk.StringVar()
    timezone_var.set("Asia/Singapore")  # Default timezone
    timezone_menu = tk.OptionMenu(new_custom_alarm_window, timezone_var, "Asia/Singapore", "Asia/Shanghai",
                                  "Asia/Tokyo", "Asia/Seoul", "Asia/Bangkok")
    timezone_menu.config(font=("Helvetica", 12))
    timezone_label.pack()
    timezone_menu.pack()

    # Create a label to display the confirmation message
    confirmation_label = tk.Label(new_custom_alarm_window, text="", font=("Helvetica", 14))
    confirmation_label.pack()

    # Function to set a custom alarm
    def set_custom_alarm(custom_alarm_window):
        hour = int(hour_var.get())
        minute = int(minute_var.get())
        ampm = ampm_var.get()
        alarm_name = name_entry.get()
        alarm_timezone = timezone_var.get()

        # Convert to 24-hour format
        if ampm == "PM":
            hour += 12

        local_timezone = pytz.timezone(alarm_timezone)
        current_time = datetime.now(local_timezone).replace(microsecond=0)

        alarm_time = current_time.replace(hour=hour, minute=minute, second=0)
        time_difference = (alarm_time - current_time).total_seconds()

        confirmation_text = f"Alarm ({alarm_name}): {alarm_time.strftime('%Y-%m-%d %I:%M:%S %p')} is set"
        confirmation_label.config(text=confirmation_text)

        # Schedule the alarm to trigger after the time difference elapses
        mainUI.after(int(time_difference * 1000), lambda: trigger_alarm(alarm_name, custom_alarm_window))

    # Function to trigger the alarm
    def trigger_alarm(alarm_name, custom_alarm_window):
        # Play the alarm sound (modify this line to use your own sound)
        alarm_sound = pygame.mixer.Sound("alarm.wav")
        alarm_sound.play()

        # Close the custom alarm window after the alarm triggers
        custom_alarm_window.destroy()

    # Create a button to set the custom alarm
    set_alarm_button = tk.Button(new_custom_alarm_window, text="Set Alarm",
                                 command=lambda: set_custom_alarm(new_custom_alarm_window))
    set_alarm_button.pack()

    # Append the new custom alarm window to the list
    custom_alarms.append(new_custom_alarm_window)



# Create a button to open the custom alarm window
open_alarm_window_button = tk.Button(mainUI, text="Set Custom Alarm", command=open_custom_alarm_window)
open_alarm_window_button.configure(width=20)
open_alarm_window_button.place(x=20, y=550)



# Start the main Tkinter event loop
mainUI.mainloop()