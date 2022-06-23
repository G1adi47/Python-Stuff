#!/usr/bin/python3

import random
import os

ra = random.randrange(1,3)

print('''
#----------------------------------------------------------------------------------------------#

.---. .----..---..-.,-.  .---..---..---..---..---.   .---..---..-..---..---..----..---. .---.
| |-< | || || |  | . <   | |-'| | || |-'| |- | |-<    \ \ | |  | | \ \  \ \ | || || |-<  \ \ 
`-'`-'`----'`---'`-'`-'  `-'  `-^-'`-'  `---'`-'`-'  `---'`---'`-'`---'`---'`----'`-'`-'`---'
                                                                                             
#----------------------------------------------------------------------------------------------#

''')

inp = input("Hallo mortal you're here weow.\n now choose from \n1>Rock\n2>Paper\n3>Scissors\n>")

if (inp.lower() == 'rock') or (inp.lower() == 'paper') or (inp.lower() == 'scissors'):
	pass
elif (inp.lower() == '1337'):
	print("Not too shaby")
	os._exit(os.EX_OK)
else:
	print("Not too quick mortal")
	os._exit(os.EX_OK)


def win(x, y):
	if (x == 'rock' and y == 1) or (x == 'paper' and y == 2) or (x == 'scissors' and y == 3):
		print("Its a Tie!!")
		pass
	elif (x == 'rock' and y == 3 ) or (x == 'paper' and y == 1 ) or (x == 'scissors' and y == 2):
		print("You've won mortal, enjoy")
	else:
		print("You Lost mortal")

if ra == 1:
	print("\nPC chose ROCK")
elif ra == 2:
	print("\nPC chose PAPER")
else:
	print("\nPC chose Scissors")

print(f"\nYou chose {inp.upper()}")

win(inp, ra)