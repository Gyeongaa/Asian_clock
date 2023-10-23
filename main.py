import tkinter as tk
from datetime import datetime
import pytz

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
default_time_label = tk.Label(
    mainUI, text="Default: Singapore time", font=("Helvetica", 24, "bold"), bg="white"
)
default_time_label.place(x=20, y=mainUI.winfo_screenheight() // 2 - 24, anchor="w")

# Create a label for displaying the current time
current_time_label = tk.Label(mainUI, text="", font=("Helvetica", 24))
current_time_label.place(x=20, y=mainUI.winfo_screenheight() // 2 + 24, anchor="w")

def slider_func(val):
    new_val = min(play_rates, key=lambda x: abs(x - float(SpeedRate.get())))
    SpeedRate.set(new_val)

play_rates = [0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2]

SpeedRate = tk.Scale(mainUI, from_=0.5, to=2,
                     font=("Helvetica", 12, "bold"), command=slider_func,
                     orient="horizontal", digits=3, resolution=0.25)
SpeedRate.set(1)
SpeedRate.place(x=20, y=500)
SpeedRate.configure(bg='white', label='Change the speed rate', troughcolor='grey',length=360)


# Function to update the Singapore time label
def update_singapore_time():
    singapore_timezone = pytz.timezone("Asia/Singapore")
    current_time = datetime.now(singapore_timezone)
    time_str = current_time.strftime("%Y-%m-%d %I:%M:%S %p")
    current_time_label.config(text=time_str)
    mainUI.after(1000, update_singapore_time)  # Update every second


# Start updating the Singapore time label
update_singapore_time()


# Function to show local time
def show_world_time(timezone_name):
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

# Create buttons for different countries
button1 = tk.Button(
    mainUI,
    text="CHINA",
    compound=tk.TOP,
    command=lambda: [show_world_time("Asia/Shanghai"),ch_clock()]
)
button2 = tk.Button(
    mainUI,
    text="JAPAN",
    compound=tk.TOP,
    command=lambda: [show_world_time("Asia/Tokyo"), jp_clock()]
)

button3 = tk.Button(
    mainUI,
    text="KOREA",
    compound=tk.TOP,
    command=lambda: [show_world_time("Asia/Seoul"), kr_clock()],
)
button4 = tk.Button(
    mainUI,
    text="THAILAND",
    compound=tk.TOP,
    command=lambda: [show_world_time("Asia/Bangkok"),th_clock()]
)
button5 = tk.Button(
    mainUI,
    text="SINGAPORE",
    compound=tk.TOP,
    command=lambda: [show_world_time("Asia/Singapore"),sg_clock()],
)

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


# Bind a function to the <Configure> event to update button positions
mainUI.bind("<Configure>", lambda event: update_button_positions())

# Start the main Tkinter event loop
mainUI.mainloop()
