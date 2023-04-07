#!/usr/bin/env python3
# import time module 
# import playsound module's playsound to play beep sound
import time
# from pygame import mixer
from playsound import playsound
# define the function countdown timer
def timer(c):
	while c:
		m,s=divmod(c,60)
		timer='{:02d}:{:02d}'.format(m,s)
		print(timer,end="\r")
		time.sleep(1)
		c-=1
	print("Time is up")
# Playing beep sound on completion
	playsound("beep.mp3")
	playsound("beep.mp3")
	playsound("beep.mp3")
"""
	mixer.init()
	beep=mixer.Sound("beep.mp3")
	beep.play()
"""
# User input of time
c=input("Enter time in seconds:")
# Call the function timer
timer(int(c))

