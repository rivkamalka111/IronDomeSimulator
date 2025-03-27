import function
import dic
import tkinter as tk
root = tk.Tk()
root.title("Timer Window")
timer_seconds = dic.all

app = function.TimerApp(root, timer_seconds)
root.mainloop()


