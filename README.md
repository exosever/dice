# dice
This is a DnD style dice rolling program made by Joshua Harrison aka SeverX

-v1 is a function by function program, that reads an input based off pre-determined variables, and then asks for a value. It then runs the appropriate function to print out the dice rolls.
This version only supports single input at the moment and has a lot of code.

-v2 uses a dictionary to base Dice face keys with number of dice values. There is then a single code block that iterates over the dictionary and rolls the appropriate dice.
This version does not have user input yet, or error-correction. It will set the dictionary to 0 each loop, and user multi-input will assign values to the dictionary which will be iterated.

-v3 uses only user input for dice faces and number of dice. It supports multiple inputs in a list type string "#d#, #d#. etc" and checks the input for errors.
It then output all the dice rolled at once from a .split method.
