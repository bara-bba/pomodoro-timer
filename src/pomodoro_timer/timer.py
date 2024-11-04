import time

#Timer logic
class PomodoroTimer:
    def __init__(self, work_duration, short_break, long_break, cycles):
        self.work_duration = work_duration
        self.short_break = short_break
        self.long_break = long_break
        self.cycles = cycles
        
    def countdown(self, duration_in_seconds):
        while duration_in_seconds > 0:
            minutes = duration_in_seconds // 60
            seconds = duration_in_seconds % 60
            print(f"{minutes:02d}:{seconds:02d}", end='\r')
            time.sleep(1)
            duration_in_seconds-=1
        print("Time's Up")
    
    def start(self):
        for i in range(self.cycles):
            print("Work session")
            self.countdown(self.work_duration)
            
            if i < self.cycles - 1:
                print("Short break")
                self.countdown(self.short_break)
            else:
                print("Long break")
                self.countdown(self.long_break)