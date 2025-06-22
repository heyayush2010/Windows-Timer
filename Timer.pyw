# Required libraries
import time
import tkinter as tk 
import threading
import ctypes
from tkinter import simpledialog

# Notification alert
def show_notification():
    ctypes.windll.user32.MessageBoxW(0, "Your set time is up", "Timer", 0x40 | 0x1)

# Timer
def start_timer(seconds):
    def countdown():
        remaining = seconds
        status_label.config(text="COUNTING DOWN")
        while remaining > 0:
            mins, secs = divmod(remaining, 60)
            timer_text = f"{mins:02}:{secs:02}"
            status_label.config(text=f"COUNTING DOWN\n{timer_text}")
            root.update()
            time.sleep(1)
            remaining -= 1
        status_label.config(text="TIME'S UP")
        show_notification()
    threading.Thread(target=countdown).start()

def set_timer(unit):
    prompt = f"Enter time in {unit.lower()}:"
    try:
        input_value = simpledialog.askinteger("Set Timer", prompt)
        if input_value is not None:
            if unit == "SECONDS":
                total_seconds = input_value
            elif unit == "MINUTES":
                total_seconds = input_value * 60
            elif unit == "HOURS":
                total_seconds = input_value * 3600
            start_timer(total_seconds)
    except Exception as e:
        status_label.config(text="Invalid input")

# GUI user-interface
root = tk.Tk()
root.title("Timer")
root.geometry("400x300")
root.configure(bg="white")

button_frame = tk.Frame(root, bg="white")
button_frame.pack(pady=30)

btn_minutes = tk.Button(button_frame, text="SET TIMER IN MINUTES", command=lambda: set_timer("MINUTES"), bg="grey", fg="white", width=25)
btn_minutes.pack(pady=5)

btn_seconds = tk.Button(button_frame, text="SET TIMER IN SECONDS", command=lambda: set_timer("SECONDS"), bg="grey", fg="white", width=25)
btn_seconds.pack(pady=5)

btn_hours = tk.Button(button_frame, text="SET TIMER IN HOURS", command=lambda: set_timer("HOURS"), bg="grey", fg="white", width=25)
btn_hours.pack(pady=5)

status_label = tk.Label(root, text="", bg="white", fg="black", font=("Arial", 14))
status_label.pack(pady=20)

root.mainloop()