import time

#Timer logic
class PomodoroTimer:
    def __init__(self, work_duration, short_break, long_break, cycles):
        self.work_duration = work_duration
        self.short_break = short_break
        self.long_break = long_break
        self.cycles = cycles
        self.interrupt = False # Initialize the interrupt flag
        
    def countdown(self, duration_in_seconds):
        while duration_in_seconds > 0:
            if self.interrupt: # Check the interrupt flag
                print(f"\n Timer interrupted.")
                break
            minutes = duration_in_seconds / 60.0
            seconds = duration_in_seconds % 60.0
            print(f"{minutes:.1f} minutes :{seconds:.1f} seconds", end='\r')
            time.sleep(1)
            duration_in_seconds -=1
        if not self.interrupt:
            print("Time's Up")
    
    def start(self):
        for i in range(self.cycles):
            if self.interrupt:
                break
            print("Work session")
            self.countdown(self.work_duration)
            
            if self.interrupt:
                break
            
            if i < self.cycles - 1:
                print("Short break")
                self.countdown(self.short_break)
            else:
                print("Long break")
                self.countdown(self.long_break)
                
    def stop(self):
        self.interrupt = True # Set the interrupt