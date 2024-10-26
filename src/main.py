from pomodoro_timer.timer import PomodoroTimer

# Collect user inputs

try:
    work_minutes = int(input("Enter work duration in minutes: "))
    short_break_minutes = int(input("Enter short break duration in minutes: "))
    long_break_minutes = int(input("Enter long break duration in minutes: "))
    cycles = int(input("Enter the number of cycles: "))
    
    # Convert minutes to seconds
    work_duration = work_minutes * 60
    short_break = short_break_minutes * 60
    long_break = long_break_minutes * 60
    
    # Initialize and start the timer
    pomodoro = PomodoroTimer(work_duration, short_break, long_break, cycles)
    pomodoro.start()
     
except ValueError:
    print("Please enter valid numbers for duration and number of cycles")