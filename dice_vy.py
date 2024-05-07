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

#Nested loops to run through listed user input.
#For repeated use
while True:
  #To loop back if a ValueError occurs
  while True:
    print("Which dice do you wish to roll?")
    dice=input("Example: 3d12, 5d15, 7d26 - Each set must be seperated by a comma.\n").lower()
    print()
    #Split the input a list
    dice_list=dice.split(',')
    for dice in dice_list:
      #Split the elements in list on 'd' to use the left and right integers
      dice_split=dice.split('d')
      roll = []
      try:
        #Uses left split integer for number of dice 
        for die in range(0, int(dice_split[0])):
          #Uses right split integer for number of dice faces
          roll.append(random.randint(1, int(dice_split[1])))
        print(f"D{dice_split[1]}: {', '.join(str(die) for die in roll)}")
      #If a ValueError occurs in the integer elements, will loop back to input. ie; anything other than #d#  
      except ValueError:
        print("---------------------------------------------------------------------------")
        print("Error: Please check your input and use the #d# format seperated by a comma.")
        print("---------------------------------------------------------------------------")
        print()
    print()
