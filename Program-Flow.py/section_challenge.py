choise = "-"
while choise != "6":
    if choise in "12345":
        print("You chose {}".format(choise))
    else:
        print("Please chose from the options below")
        print("1:\t Doctor")
        print("2:\t Engineer")
        print("3:\t Pilot")
        print("4:\t Marine")
        print("5:\t Influencer")
        print("6:\tQuit")

    choise = input()