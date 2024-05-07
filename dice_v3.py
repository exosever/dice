#DnD style dice rolling program by Joshua Harrison aka SeverX
#V3 version solely uses user input for any size and number of dice.

#Modules
import random

#Banner
print()
print("---------------------------------------------------")
print("Dice rolling program by Joshua Harrison aka SeverX.")
print("---------------------------------------------------")
print()

#Error
def error():
  print("---------------------------------------------------------------------------")
  print("Error: Please check your input and use the #d# format seperated by a comma.")
  print("---------------------------------------------------------------------------")
  print()

#Function to check input validity - Clean it up?
def valid(dice):
  if dice.count('d') == 1:
    dice_split=dice.split('d')
    if int(dice_split[0].isnumeric()) and int(dice_split[1].isnumeric()) > 0:  
      return True
    else:
      error()
  else:
    error()

#Nested loops to run through listed user input.
while True:
  while True:
    print("Which dice do you wish to roll?")
    dice=input("Example: 3d12, 5d15, 7d26 - Each set must be seperated by a comma.\n").lower()
    print()
    dice_list=dice.split(',')
    for dice in dice_list:
      if valid(dice):
        dice_split=dice.split('d')
        roll = []
        for die in range(0, int(dice_split[0])):
          roll.append(random.randint(1, int(dice_split[1])))
        print(f"D{dice_split[1]}: {', '.join(str(die) for die in roll)}")
      print()
      break
