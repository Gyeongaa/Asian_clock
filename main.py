import tkinter as tk
from datetime import datetime
import pytz
from PIL import Image, ImageTk

# Create the main window
root = tk.Tk()
root.title("Asian Time")

# Use a relative path to open the background image
background_image = Image.open("Asia Map with Flag Icons.png")
background_image = background_image.resize(
    (root.winfo_screenwidth(), root.winfo_screenheight())
)
background_photo = ImageTk.PhotoImage(background_image)

# Set the window size to match the background image size
root.geometry(f"{background_image.width}x{background_image.height}")

# Create a Label to display the background image, using relwidth and relheight to fill the entire window
background_label = tk.Label(root, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create a label for the default time text
default_time_label = tk.Label(
    root, text="Default: Singapore time", font=("Helvetica", 24, "bold"), bg="white"
)
default_time_label.place(x=20, y=root.winfo_screenheight() // 2 - 24, anchor="w")

# Create a label for displaying the current time
current_time_label = tk.Label(root, text="", font=("Helvetica", 24))
current_time_label.place(x=20, y=root.winfo_screenheight() // 2 + 24, anchor="w")


# Function to update the Singapore time label
def update_singapore_time():
    singapore_timezone = pytz.timezone("Asia/Singapore")
    current_time = datetime.now(singapore_timezone)
    time_str = current_time.strftime("%Y-%m-%d %I:%M:%S %p")
    current_time_label.config(text=time_str)
    root.after(1000, update_singapore_time)  # Update every second


# Start updating the Singapore time label
update_singapore_time()


# Function to show local time
def show_world_time(timezone_name):
    local_timezone = pytz.timezone(timezone_name)
    current_time = datetime.now(local_timezone)
    time_str = current_time.strftime("%Y-%m-%d %I:%M:%S %p")
    time_str = time_str.lstrip("0").replace(" 0", " ")

    # Create a new window to display local time
    local_time_window = tk.Toplevel(root)
    local_time_window.title("Local Time")
    local_time_window.geometry("300x100")
    time_label = tk.Label(local_time_window, text=time_str, font=("Helvetica", 20))
    time_label.pack(pady=20)


# Create buttons for different countries
button1 = tk.Button(
    root,
    text="CHINA",
    compound=tk.TOP,
    command=lambda: show_world_time("Asia/Shanghai"),
)
button2 = tk.Button(
    root,
    text="JAPAN",
    compound=tk.TOP,
    command=lambda: show_world_time("Asia/Tokyo"),
)
button3 = tk.Button(
    root,
    text="KOREA",
    compound=tk.TOP,
    command=lambda: show_world_time("Asia/Seoul"),
)
button4 = tk.Button(
    root,
    text="THAILAND",
    compound=tk.TOP,
    command=lambda: show_world_time("Asia/Bangkok"),
)
button5 = tk.Button(
    root,
    text="SINGAPORE",
    compound=tk.TOP,
    command=lambda: show_world_time("Asia/Singapore"),
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
        x=830 * root.winfo_width() / background_image.width,
        y=430 * root.winfo_height() / background_image.height,
    )
    button2.place(
        x=1250 * root.winfo_width() / background_image.width,
        y=400 * root.winfo_height() / background_image.height,
    )
    button3.place(
        x=1120 * root.winfo_width() / background_image.width,
        y=380 * root.winfo_height() / background_image.height,
    )
    button4.place(
        x=800 * root.winfo_width() / background_image.width,
        y=730 * root.winfo_height() / background_image.height,
    )
    button5.place(
        x=790 * root.winfo_width() / background_image.width,
        y=930 * root.winfo_height() / background_image.height,
    )


# Bind a function to the <Configure> event to update button positions
root.bind("<Configure>", lambda event: update_button_positions())

# Start the main Tkinter event loop
root.mainloop()
