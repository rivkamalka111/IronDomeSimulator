import tkinter as tk
import video
import dic
class TimerApp:
    def __init__(self, root, timer_seconds):
        self.root = root
        self.timer_seconds = timer_seconds
        self.remaining_time = timer_seconds
        self.label = tk.Label(root, text="", font=("Helvetica", 250))
        self.label.pack(pady=20)
        self.update_timer()

    def update_timer(self):
        # חישוב הזמן הנותר בפורמט דקות ושניות
        minutes, seconds = divmod(self.remaining_time, 60)
        self.label.config(text=f"\n      {minutes:02}:{seconds:02}       \n")
        if self.remaining_time > 0:
            self.remaining_time -= 1
            self.root.after(1000, self.update_timer)  # עדכון כל שנייה
        else:
            self.on_timer_complete()

    def on_timer_complete(self):
        video.play_music()
        self.label.config(text=dic.cityIs+"   \n          אזעקה💥        \n "+dic.nameEnemy+" :ממדינת"+"\n"+dic.Missile +" :סוג הטיל", font=("Helvetica", 130))
        print("The city from which the Iron Dome is operated is : "+dic.cityIronDome)
        #self.root.after((dic.all40000), self.root.destroy)  # סוגר את החלון לאחר 3 שניות