#!/usr/bin/env python3
#import time module
import time
# define the function countdown timer
def timer(c):
	while c:
		m,s=divmod(c,60)
		timer='{:02d}:{:02d}'.format(m,s)
		print(timer,end="\r")
		time.sleep(1)
		c-=1
	print("Time is up")
# User input of time
c=input("Enter time in seconds:")
# Call the function timer
timer(int(c))
