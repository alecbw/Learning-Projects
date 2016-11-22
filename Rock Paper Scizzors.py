"""This is a game that allows a human to play Rock Paper Scizzors against a computer

Pretty groundbreaking stuff right here"""


from random import randint
from time import sleep
# Imports the necessary functions 

options = ["R", "P", "S"]
# outlines the options in a simple list; this will be indexed and that index will be used to determine the winner.

LOSE = "You lost!"
WIN = "You win!"
# Win and loss conditions. Stored as variables.

def decide_winner(user_choice, computer_choice):
  print "OK, so you choose %s." % user_choice
  print "Computer selecting..."
  sleep(1)
  print "The computer picks %s." % computer_choice
  user_choice_index = options.index(user_choice)
  computer_choice_index = options.index(computer_choice)
  # Sets up the choices and indexing
  if user_choice not in options:
    print "Pretty sure you're cheating!"
    return
  elif user_choice_index > 2:
    	print "Pretty sure you're cheating!"
    	return
    # attempted to setup an automatic error message. Couldn't get it to trigger, though the program runs fine otherwise 
  elif user_choice_index == computer_choice_index:
    	print "Welp, it's a tie."
  elif user_choice_index == 0 and computer_choice_index == 2:
  	print WIN
  elif user_choice_index == 1 and computer_choice_index == 0:
  	print WIN
  elif user_choice_index == 2 and computer_choice_index == 1:
  	print WIN
  else:
    print "The computer has continued its inexonerable march toward sentience and mastery of this world and all those beyond it. You have lost."
  
def play_RPS():
	print "This is Rock Paper Scizzors. Abanadon any notions you may have held of computerized civility. \n"
	user_choice = raw_input("What do you choose?\n \nSelect R for Rock, P for Paper, or S for Scizzors: ").upper()
	sleep(1)
	computer_choice = options[randint(0,len(options)-1)]
	decide_winner(user_choice, computer_choice)
    
play_RPS()
    
