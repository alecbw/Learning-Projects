""" so basically this calculates the area of a circle or a triangle (that is selected via the console)"""
from math import pi 
# this imports the value pi from the math library
from time import sleep
import time 
#this imports code that is used to simulate a thinking calculator (?)
#it specified we use 'from time import sleep' but it only worked after adding 'import time' as a sepearte line 
from datetime import datetime
#this imports the date and time to print at the beginning of the program 
now = datetime.now()
print "It's on"
print '%s/%s/%s %s:%s' % (now.month, now.day, now.year, now.hour, now.minute)
time.sleep(1)
hint = "Don't forget to include the correct units! \nExiting..."
#the \n prints it on a seperate line 
option = raw_input("What shape do you want to analyze? Pick C for Circle and T for Triangle.").upper()
if option == "C":
	radius = float(raw_input ("What Length Radius?"))
  	area = pi*(radius**2)
    	print "the pie is baking..."
      	time.sleep(1)
        print str("%.2f" % area)
        print hint
elif option == "T":
	base = float(raw_input ("What Length Base?"))
	height = float(raw_input ("What Length Height?"))
  	area = 0.5*base*height
    	print "Uni Bi Tri..."
      	time.sleep(1)
        print str("%.2f" % area)
        print hint
else:
	print "beep boop boop error code: Letters-R-Hard"
  	
"""oh man so much going on here
so basically, the time.sleep causes the program to 'think' for one second
the option = ensures if they enter C or T it is recorded, always in uppwer case
then the giant if/else calculates the area of the circle by asking for a radius length
and printing that to two decimal points (%.2f (floating point) as well as the hint)"""
