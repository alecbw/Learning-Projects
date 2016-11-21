"""this rolls a pair of dice, asks the user for input on what they think the sum is, and calculates who the winner is based off if the predicted sum or the actual sum was higher"""

from random import randint
from time import sleep

def get_user_guess():
		user_guess = input("What do you guess the sum is? ")
		return user_guess

number_of_sides = int(raw_input("How many sides should the die have? "))
  
def roll_dice(number_of_sides):
	first_roll = randint(1, number_of_sides)
	second_roll = randint(1, number_of_sides)
	max_val = number_of_sides*2  
	total_roll = first_roll + second_roll
	print "The maximum value is " + str(max_val) + "."
	sleep(1)
	user_guess = get_user_guess()
	if user_guess > max_val:
		print "Guess a more reasonable number."
		return
	else:
		print "Rolling..."
   	sleep(2)
    	print "The first dice returns %d." % first_roll
    	sleep(1)
    	print "The second dice returns %d." % second_roll
	if user_guess > total_roll: 
			print "You won!"
			return
	else: 
  		print "Well, you lost."
		return
		   
roll_dice(number_of_sides)


  
  

