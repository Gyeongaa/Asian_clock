import tkinter as tk
from datetime import datetime
import pytz
import threading
from PIL import Image, ImageTk
from korean import kr_clock
from Japanese import jp_clock
from singapore import sg_clock
from thai import th_clock
from chinese import ch_clock

# Create the main window
mainUI = tk.Tk()
mainUI.title("Asian Time")

# Use a relative path to open the background image

background_image = Image.open("images/background_map.png")
background_photo = ImageTk.PhotoImage(background_image)

# Set the window size to match the background image size
mainUI.geometry(f"{background_image.width}x{background_image.height}")

# Create a Label to display the background image, using relwidth and relheight to fill the entire window
background_label = tk.Label(mainUI, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create a label for the default time text
default_time_label = tk.Label(mainUI, text="Default: Singapore time",
                              font=("Helvetica", 24, "bold"), bg="white")
default_time_label.place(x=20, y=mainUI.winfo_screenheight() // 2 - 24, anchor="w")

# Create a label for displaying the current time
current_time_label = tk.Label(mainUI, text="", font=("Helvetica", 24))
current_time_label.place(x=20, y=mainUI.winfo_screenheight() // 2 + 24, anchor="w")

def slider_sr(val): #slider for speed rate
    new_val = min(speed_rates, key=lambda x: abs(x - float(SpeedRate.get())))
    SpeedRate.set(new_val)

def slider_vl(val): #slider for volume level
    new_val = min(volume_level, key=lambda x: abs(x - float(VolumeLevel.get())))
    VolumeLevel.set(new_val)


speed_rates = [0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2]
volume_level = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]

SpeedRate = tk.Scale(mainUI, from_=0.25, to=2,
                     font=("Helvetica", 12, "bold"), command=slider_sr,
                     orient="horizontal", digits=3, resolution=0.25)
SpeedRate.set(1)
SpeedRate.place(x=20, y=500)
SpeedRate.configure(bg='white', label='Change the speed rate', troughcolor='grey',length=360)

VolumeLevel = tk.Scale(mainUI, from_ = 0, to = 1,
                       font =("Helvetica", 12, "bold"), command = slider_vl,
                       orient = "horizontal", digits = 3, resolution = 0.1)

VolumeLevel.set(1)
VolumeLevel.place(x = 20, y = 600)
VolumeLevel.configure(bg = 'white', label = 'Change the volume level', troughcolor = 'grey', length = 360)




# Function to update the Singapore time label
def update_singapore_time():
    singapore_timezone = pytz.timezone("Asia/Singapore")
    current_time = datetime.now(singapore_timezone)
    time_str = current_time.strftime("%Y-%m-%d %I:%M:%S %p")
    current_time_label.config(text=time_str)
    mainUI.after(1000, update_singapore_time)  # Update every second


# Start updating the Singapore time label



# Function to show local time
def show_world_time(timezone_name: str):
    local_timezone = pytz.timezone(timezone_name)
    current_time = datetime.now(local_timezone)
    time_str = current_time.strftime("%Y-%m-%d %I:%M:%S %p")
    time_str = time_str.lstrip("0").replace(" 0", " ")

    # Create a new window to display local time
    local_time_window = tk.Toplevel(mainUI)
    local_time_window.title("Local Time")
    local_time_window.geometry("300x100")
    time_label = tk.Label(local_time_window, text=time_str, font=("Helvetica", 20))
    time_label.pack(pady=20)

    # Function to update the time label in this window
    def update_local_time():
        current_time = datetime.now(local_timezone)
        time_str = current_time.strftime("%Y-%m-%d %I:%M:%S %p")
        time_str = time_str.lstrip("0").replace(" 0", " ")
        time_label.config(text=time_str)
        local_time_window.after(1000, update_local_time)  # Update every second

    # Start updating the time label in this window
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
    thread1 = threading.Thread(target=show_world_time, args=("Asia/Shanghai",))
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

    thread1 = threading.Thread(target=show_world_time, args=("Asia/Tokyo",))
    thread2 = threading.Thread(target=jp_clock, args=(SpeedRate.get(), VolumeLevel.get()))
    thread1.start()
    thread2.start()
    mainUI.after(8500, enable_buttons)

def button3_callback():
    for button in buttons:
        button.config(state="disabled")

    thread1 = threading.Thread(target=show_world_time, args=("Asia/Seoul",))
    thread2 = threading.Thread(target=kr_clock, args=(SpeedRate.get(), VolumeLevel.get()))
    thread1.start()
    thread2.start()
    mainUI.after(8500, enable_buttons)

def button4_callback():
    # Disable buttons

    for button in buttons:
        button.config(state="disabled")

    thread1 = threading.Thread(target=show_world_time, args=("Asia/Bangkok",))
    thread2 = threading.Thread(target=th_clock, args=(SpeedRate.get(), VolumeLevel.get()))
    thread1.start()
    thread2.start()
    mainUI.after(8500, enable_buttons)

def button5_callback():
    # Disable buttons

    for button in buttons:
        button.config(state="disabled")

    thread1 = threading.Thread(target=show_world_time, args=("Asia/Singapore",))
    thread2 = threading.Thread(target=sg_clock, args=(SpeedRate.get(), VolumeLevel.get()))
    thread1.start()
    thread2.start()
    mainUI.after(8500, enable_buttons)

# Create buttons for different countries
button1 = tk.Button(
    mainUI,
    text="CHINA",
    compound=tk.TOP,
    command= lambda : button1_callback()
)
button2 = tk.Button(
    mainUI,
    text="JAPAN",
    compound=tk.TOP,
    command=lambda: button2_callback()
)
button3 = tk.Button(
    mainUI,
    text="KOREA",
    compound=tk.TOP,
    command=lambda: button3_callback()
)
button4 = tk.Button(
    mainUI,
    text="THAILAND",
    compound=tk.TOP,
    command=lambda: button4_callback()
)
button5 = tk.Button(
    mainUI,
    text="SINGAPORE",
    compound=tk.TOP,
    command= lambda: button5_callback()
)

buttons = [button1, button2, button3, button4, button5]
# Place the buttons
button1.pack(pady=10)
button2.pack(pady=10)
button3.pack(pady=10)
button4.pack(pady=10)
button5.pack(pady=10)


# Function to update button positions based on window size
def update_button_positions():
    button1.place(
        x=1000 * mainUI.winfo_width() / background_image.width,
        y=450 * mainUI.winfo_height() / background_image.height,
    )
    button2.place(
        x=1250 * mainUI.winfo_width() / background_image.width,
        y=400 * mainUI.winfo_height() / background_image.height,
    )
    button3.place(
        x=1120 * mainUI.winfo_width() / background_image.width,
        y=380 * mainUI.winfo_height() / background_image.height,
    )
    button4.place(
        x=800 * mainUI.winfo_width() / background_image.width,
        y=730 * mainUI.winfo_height() / background_image.height,
    )
    button5.place(
        x=790 * mainUI.winfo_width() / background_image.width,
        y=930 * mainUI.winfo_height() / background_image.height,
    )

t1 = threading.Thread(target=update_singapore_time)
t1.start()
# Bind a function to the <Configure> event to update button positions
mainUI.bind("<Configure>", lambda event: update_button_positions())

# Start the main Tkinter event loop
mainUI.mainloop()


