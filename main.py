import tkinter as tk
from tkinter import ttk
from datetime import datetime
import pytz
import threading
import pygame
from PIL import Image, ImageTk
from settings import get_current_time
from alarm import Alarm
from clock import *

# Create the main window
mainUI = tk.Tk()
mainUI.title("Asian Time")
#pygame.init()
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
default_time_label = tk.Label(mainUI, text="Singapore time (Default)",
                              font=("Helvetica", 24, "bold","italic"), bg="white")
default_time_label.configure(width=20)
default_time_label.place(x=500, y=50, anchor="w")

# Create a label for displaying the current time
current_time_label = tk.Label(mainUI, text="", font=("Helvetica", 24),bg="white")
current_time_label.place(x=500, y=83, anchor="w")
current_time_label.configure(width=20)

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

#set background image following current time, this will be executed when mainroop starts
current_mode = ''
def set_background():
    global current_mode
    hour= get_current_time("Asia/Singapore")[0]
    if hour >= 6 and hour <= 18:
            background_label.config(image=background_photo)
            current_mode = 'Light Mode'
    else:
        background_label.config(image=night_background_photo)
        current_mode = 'Dark Mode'

#Following user input, user can change background mode

def change_background(mode):
    global current_mode
    if mode == "Light Mode":
        background_label.config(image=background_photo)
        current_mode = 'Light Mode'

    elif mode == "Dark Mode":
        background_label.config(image=night_background_photo)
        current_mode = "Dark Mode"

set_background()
bg_choice = tk.StringVar()
mode_combobox = ttk.Combobox(mainUI, textvariable=bg_choice)
mode_combobox["values"] = ("Light Mode", "Dark Mode")
mode_combobox.set(current_mode)

mode_combobox.bind("<<ComboboxSelected>>", lambda event: change_background(bg_choice.get()))
mode_combobox.configure(width=20)
mode_combobox.place(x=20, y=540)

# Function to update the Singapore time label
def update_singapore_time():
    singapore_timezone = pytz.timezone("Asia/Singapore")
    current_time = datetime.now(singapore_timezone)
    time_str = current_time.strftime("%Y-%m-%d %I:%M:%S %p")
    current_time_label.config(text=time_str)
    mainUI.after(1000, update_singapore_time)  # Update every second

# Start updating the Singapore time label
update_singapore_time()


#get world time
def get_world_time(timezone_name: str):
    local_timezone = pytz.timezone(timezone_name)
    current_time = datetime.now(local_timezone)
    time_str = current_time.strftime("%Y-%m-%d %I:%M:%S %p")
    time_str = time_str.lstrip("0").replace(" 0", " ")
    return time_str

def show_local_time(time_zone):
    time_str = get_world_time(time_zone)
    # Create a new window to display local time
    local_time_window = tk.Toplevel(mainUI)
    local_time_window.title("Local Time")
    local_time_window.geometry("300x100")
    time_label = tk.Label(local_time_window, text=time_str, font=("Helvetica", 20))
    time_label.pack(pady=20)
    time_label.config(text=time_str)

    def update_local_time():
        time_str = get_world_time(time_zone)
        time_label.config(text=time_str)
        local_time_window.after(1000, update_local_time)
    update_local_time()


capital_dict = {
    "CHINA": "Asia/Shanghai",
    "JAPAN": "Asia/Tokyo",
    "KOREA": "Asia/Seoul",
    "THAILAND": "Asia/Bangkok",
    "SINGAPORE": "Asia/Singapore"}

def disable_buttons():
    for button in buttons:
        button.config(state="disabled")

def enable_buttons():
    # Enable buttons
    for button in buttons:
        button.config(state="active")

def button_callback(country: str, type=None):
    mainUI.after(500, disable_buttons)
    t1 = threading.Thread(target=show_local_time, args=(capital_dict[country],))

    if country == "CHINA":
        if type == 'gtts':
            t2 = threading.Thread(target=ch_clock, args=(SpeedRate.get(), VolumeLevel.get()))
        elif type == 'natural':
            t2 = threading.Thread(target=ch_natural_clock, args=(SpeedRate.get(), VolumeLevel.get()))

    elif country == "JAPAN":
        t2 = threading.Thread(target=jp_clock, args=(SpeedRate.get(), VolumeLevel.get()))

    elif country == "KOREA":
        t2 = threading.Thread(target=kr_clock, args=(SpeedRate.get(), VolumeLevel.get()))

    elif country == "THAILAND":
        t2 = threading.Thread(target=th_clock, args=(SpeedRate.get(), VolumeLevel.get()))

    elif country == "SINGAPORE":
        t2 = threading.Thread(target=sg_clock, args=(SpeedRate.get(), VolumeLevel.get()))

    t1.start()
    t2.start()

    mainUI.after(8500, enable_buttons)


# Function to play the selected Chinese audio, either in natural or synthetic Chinese voice
def china_audio(*args):
    selected_audio = audio_choice.get()
    if selected_audio == "China Natural":
        # Play natural Chinese audio (replnaturalace with your actual audio file)
        button_callback("CHINA", 'natural')
    elif selected_audio == "China Synthetic":
        # Play synthetic Chinese audio (replace with your actual audio file)
        button_callback("CHINA", 'gtts')

# Create buttons for different countries

# A combobox is created to choose synthetic or natural chinese voice for button China
# Create a variable to store the selected audio choice
audio_choice = tk.StringVar()

# Create a Combobox (dropdown) with audio choices for Chinese
button1 = ttk.Combobox(mainUI, textvariable=audio_choice)
button1["values"] = ("China Natural", "China Synthetic")
button1.set("China Natural")
button1.bind("<<ComboboxSelected>>",china_audio)
button1.configure(width= 12)

button2 = tk.Button(mainUI,text="JAPAN", compound=tk.TOP, command=lambda: button_callback("JAPAN"), width=9)
button3 = tk.Button(mainUI,text="KOREA", compound=tk.TOP, command=lambda: button_callback("KOREA"), width=9)
button4 = tk.Button(mainUI, text="THAILAND", compound=tk.TOP, command=lambda: button_callback("THAILAND"), width=9)
button5 = tk.Button(mainUI, text="SINGAPORE", compound=tk.TOP, command=lambda: button_callback("SINGAPORE"), width=9)

buttons = [button1, button2, button3, button4, button5]

# Function to update button positions based on window size
button1.place(x=620, y=345)
button2.place(x=1000, y=300)
button3.place(x=870, y=300)
button4.place(x=620, y=540)
button5.place(x=640, y=680)

# Bind a function to the <Configure> event to update button positions
mainUI.bind("<Configure>", lambda event: set_background())


alarm = Alarm(mainUI)
# Create a button to open the custom alarm window using open_alarm_window
open_alarm_window_button = tk.Button(mainUI, text="Set Custom Alarm", command=lambda: alarm.open_alarm_window())
open_alarm_window_button.configure(width=20)
open_alarm_window_button.place(x=20, y=500)

# Start the main Tkinter event loop
mainUI.mainloop()