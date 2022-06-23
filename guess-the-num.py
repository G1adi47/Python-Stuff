#!/bin/python3

import random
import os
#----------------------------------------------------#
print("""

╔═╗┬ ┬┌─┐┌─┐┌─┐    ╔╦╗┬ ┬┌─┐    ╔╗╔┬ ┬┌┬┐┌┐ ┌─┐┬─┐  
║ ╦│ │├┤ └─┐└─┐     ║ ├─┤├┤     ║║║│ ││││├┴┐├┤ ├┬┘  
╚═╝└─┘└─┘└─┘└─┘     ╩ ┴ ┴└─┘    ╝╚╝└─┘┴ ┴└─┘└─┘┴└─  
─┼─┼─                                          ─┼─┼─
─┼─┼────────────────────────────────────────────┼─┼─

	""")

#----------------------------------------------------#
d1 = "Going too much deep mortal its hot down there"
d2 = "How pathetic! upgrade your morals kid"
d3 = "WTF you doin down there"
num = random.randrange(1,50)
no = [1,2,3]
sh = random.choice(no)
# print(num)
#----------------------------------------------------#
if sh == 1:
	ss = d1
elif sh == 2:
	ss = d2
else:
	ss = d3
#----------------------------------------------------#

a = input("Hallo Mortal! Try to Guess the number if ya can \n 1-50: ")
try:
	int(a)
except:
	print("STFU mortal dont try to shit here")
	os._exit(os.EX_OK)

if int(a) == int(num) :
	print("You impress me Mortal \n Congrats mate!")
elif int(a) > num :
	print(ss)
elif int(a) < num : 
	print("You are gonna get stuck in the ground mate!")
else :
	print("STFU kiddo")
#----------------------------------------------------#