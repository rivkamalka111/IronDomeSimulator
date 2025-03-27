import tkinter as tk
from pygame import mixer
try:
    mixer.init()
    play_music=lambda :(mixer.music.load("alarms.mp3"),mixer.music.play())
except:
    "השמע שהכנסת הוא לא מסוג mp3"