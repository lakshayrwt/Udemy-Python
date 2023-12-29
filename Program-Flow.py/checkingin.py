parrot = "Norwegian Blue"

letter = input("please enter a letter: ")
if letter in parrot:
    print("{} is in {}".format(letter,parrot))
else:
    print("please enter a different letter")