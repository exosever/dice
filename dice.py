#DnD style dice rolling program by Joshua Harrison aka SeverX

import random

#Dice rolling functions
def D4(dice):
  x=0
  while x < dice:
    print(random.randint(1,4))
    x +=1
def D6(dice):
  x=0
  while x < dice:
    print(random.randint(1,6))
    x +=1
def D8(dice):
  x=0
  while x < dice:
    print(random.randint(1,8))
    x +=1
def D10(dice):
  x=0
  while x < dice:
    print(random.randint(1,10))
    x +=1
def D12(dice):
  x=0
  while x < dice:
    print(random.randint(1,12))
    x +=1
def D20(dice):
  x=0
  while x < dice:
    print(random.randint(1,20))
    x +=1
def D100(dice):
  x=0
  while x < dice:
    print(random.randint(1,100))
    x +=1

#Input
while True:
  print()
  print("---------------------------------------------------")
  print("Dice rolling program by Joshua Harrison aka SeverX.")
  print("---------------------------------------------------")
  print()
  print("Which dice do you wish to roll?")
  dice=input("D4, D6, D8, D10, D12, D20, or D100: ")
  if dice == "D4":
    d4dice=input("How many D4? ")
    d4dice = int(d4dice)
    D4(d4dice)
  elif dice == "D6":
    d6dice=input("How many D6? ")
    d6dice = int(d6dice)
    D6(d6dice)
  elif dice == "D8":
    d8dice=input("How many D8? ")
    d8dice = int(d8dice)
    D8(d8dice)
  elif dice == "D10":
    d10dice=input("How many D10? ")
    d10dice = int(d10dice)
    D10(d10dice)
  elif dice == "D12":
    d12dice=input("How many D12? ")
    d12dice = int(d12dice)
    D12(d12dice)
  elif dice == "D20":
    d20dice=input("How many D20? ")
    d20dice = int(d20dice)
    D20(d20dice)
  elif dice == "D100":
    d100dice=input("How many D100? ")
    d100dice = int(d100dice)
    D100(d100dice)
  else:
    print("Sorry, you have entered an incorrect dice type.")
  print()
  if input("Repeat the program? (Y/N)") != 'Y':
        break


#Possibly clear some data, so the console isn't full of numbers after?
#If multiple dice, seperate and annotate them neatly
#How to arrange numbers differently, so it doesn't post in a series of line?
