current_choice = "-"
computer_parts = []

while current_choice != "0":
    if current_choice in "1,2,3,4,5,6":
        print("adding {}".format(current_choice))
        if current_choice == '1':
            computer_parts.append("monitor")
        elif current_choice == '2':
            computer_parts.append("CPU")
        elif current_choice == '3':
            computer_parts.append("keyboard")
        elif current_choice == '4':
            computer_parts.append("mouse")
        elif current_choice == '5':
            computer_parts.append("mouse pad")
        elif current_choice == '6':
            computer_parts.append("HDMI cable")

    else:
        print("select from the following options")
        print("1: Monitor")
        print("2: CPU")
        print("3: keyboard")
        print("4: mouse")
        print("5: mouse pad")
        print("6: HDMI cable")
        print("0: to finish")

    current_choice = input()
print(computer_parts)