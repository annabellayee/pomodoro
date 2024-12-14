import time 
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("pomodoro timer")
root.geometry("250x110")
root.configure(bg="white")
blank_image = tk.PhotoImage(width=1, height=1)

def start_timer():

    work_duration = 25
    short_break_duration = 5
    long_break_duration = 15
    work_cycles = 4

    for i in range(work_cycles):
        countdown(work_duration * 60, f"work cycle {i+1}") 
        if i < work_cycles - 1: # prevent extra short break after last cycle
            countdown(short_break_duration * 60, "short break")

    countdown(long_break_duration * 60, "long break")
    messagebox.showinfo("pomodoro timer", f"Well done! You've completed {work_cycles} pomodoro cycles!")


def countdown(seconds, message):
    while seconds > 0:
        minutes = seconds // 60
        remaining_seconds = seconds % 60

        timer_label.config(text=f"{message} \n {minutes:02}:{remaining_seconds:02}")
        root.update()

        time.sleep(1) # wait for 1 sec
        seconds -= 1 # decrease by 1 sec

start_button = tk.Button(root, text="start timer", command=start_timer, font=("Segoe UI", 10, "bold"), bg="grey", fg="white", relief="flat")
start_button.pack(pady=10)

timer_label = tk.Label(root, text="ready", font=("Segoe UI", 10), bg="white", fg="grey")
timer_label.pack(pady=5)


root.mainloop()

