from pomodoro_timer.timer import PomodoroTimer
import numpy as np

# Collect user inputs

try:
    work_minutes = float(input("Enter work duration in minutes: "))
    short_break_minutes = float(input("Enter short break duration in minutes: "))
    long_break_minutes = float(input("Enter long break duration in minutes: "))
    cycles = int(input("Enter the number of cycles: "))
    
    # Convert minutes to seconds
    work_duration = work_minutes * 60.0
    short_break = short_break_minutes * 60.0
    long_break = long_break_minutes * 60.0
    
    # Initialize and start the timer
    pomodoro = PomodoroTimer(work_duration, short_break, long_break, cycles)
    
    try:
        pomodoro.start()
    except KeyboardInterrupt:
        pomodoro.stop()
        print(f"\n Timer stopped by user.")
     
except ValueError:
    print("Please enter valid numbers for duration and number of cycles")