#DnD style dice rolling program by Joshua Harrison aka SeverX
#V2 version uses a nested loop using input to determine faces and rolls instead of multiple functions.
#This capability makes it easy to ADD or REMOVE dice from the program list.

#Modules
import random

#Add the user input to tie into dictionary here
input()
dice += input

#Dictionary for storing and altering key-pairs dice sides and values
dice = {
"D4": 1,
"D6": 0,
"D8": 0,
"D10": 0,
"D12": 3,
"D20": 0}

#For loop to take dictionary key pairs and roll the appropriate amount and type of dice
#Dice is dictionary, die is a place-held keyword (the for loop runs over the key words, D4, D6 etc.)
#Calling on die brings the key and value, allowing us to look at the value associated to the current key.
#dice[die] > 0 checks if current keypair has a value > 0, the rolls variable stores that value.
for die in dice:
  if dice[die] > 0:
    sides=int(die[1:])
    rolls=int(dice[die])
    result=[]
    for roll in range(0, rolls):
      number = random.randint(1, sides)
      result.append(number)
    results = str(result)
    print(die + ": " + f"{results[1:-1]}")
