""" This is a very lightweight calendar
It supports the following functionality
*Viewing of the calendar
Adding events to the calendar
Updating events on the calendar
Deleting existing events """

from time import sleep, strftime 

print "Hello, this is your calendar speaking"

NAME = raw_input("What is your name? ")

calendar = {}

def welcome():
  print "Welcome " + NAME 
  print "Well, the calendar is opening now"
  sleep(1)
  print strftime("%A %B %d, %Y")
  # prints Weekday-Full-Name Month Day, Year
  print strftime("%I:%M:%S")
  sleep(1)
  print "What would you like to do?"
  
def start_calendar():
  welcome()
  start = True
  while start == True:
    user_choice = raw_input("A to Add, U to Update, V to View, D to Delete, or X to Exit: ")
    user_choice = user_choice.upper()
    if user_choice == "V":
      # first, it checks if the calendar is empty by examining the length of the keys  
      if len(calendar.keys()) == 0:
        print "Welp, the calendar is empty"
        try_again = raw_input("Guess you gotta pick something else now, huh? Y/N? \n")
        try_again = try_again.upper()
        if try_again == "Y":
        	continue
        else:
            start = False
      else:
        print calendar
        # that's just a line break
        print ""

    elif user_choice == "U":
    	date = raw_input("Ok, which date would you like to update? ")
    	update = raw_input("Ok, what do you want to do with it? ")
    	calendar[date] = update
    	print "Well, I guess that's that"
    	try_again = raw_input("Guess you gotta pick something else now, huh? Y/N? ")
    	try_again = try_again.upper()
    	if try_again == "Y":
      		continue
    	else:
     		start = False
    elif user_choice == "A":
      event = raw_input("Go ahead and enter an event: ")
      date = raw_input("Go ahead and pick a day for it (MM/DD/YYYY): ")
      # note: the format MM/DD/YYYY contains ten characters with the slashes 
      if len(date) != 10:
        print "Goodness, you had one job. "
        try_again = raw_input("Would you like to try using this fabulously complicated product again? Y for Yes, N for No: ")
        try_again = try_again.upper()
        if try_again == "Y":
        	date = raw_input("Pick a day, but this time formatted right (MM/DD/YYYY): ")
        	continue
        else:
            start = False
      elif int(date[6:]) < int(strftime("%Y")):
      	print "Unfortunately, this is not a time-traveling calendar"
        try_again = raw_input("Would you like to try using this fabulously complicated product again? Y for Yes, N for No: ")
        try_again = try_again.upper()
        if try_again == "Y":
        	date = raw_input("Pick a date in the future (MM/DD/YYYY): ")
        	continue
        else: 
          start = False 
      else: 
      	calendar[date] = event
        print "Hey we successfully added " + event + "!"
        print "Next? \n"
        continue
        
    elif user_choice == "D":
    	if len(calendar.keys()) == 0:
      		print "Can't delete no events, pal"
        	print "Try again. \n"
    	else: 
      		event = raw_input("What event? ")
      	for date in calendar.keys():
          if event == calendar[date]:
            del calendar[date]
            print "We have successfully destroyed it"
            print calendar 
          else: 
            print "Well it looks like you don't even know what you want to delete. I'm disappointed in both of us."
            continue
    elif user_choice == "X":
    	start = False 
    else:
    	print "Guy, you had one job. Just one."
    	start = False 
        
start_calendar()
    
  
