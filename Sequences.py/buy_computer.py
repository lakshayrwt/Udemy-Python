available_parts = ["monitor",
                    "CPU",
                    "keyboard",
                    "mouse",
                    "mouse pad",
                    "HDMI cable"
                    ]
current_choice = "-"
computer_parts = []

valid_choices = []
for i in range(1,len(available_parts) + 1):
    valid_choices.append(str(i))
print(valid_choices)

while current_choice != "0":
    if current_choice in valid_choices:
        print("adding {}".format(current_choice))
        index = int(current_choice) - 1
        chosen_part = available_parts[index]
        if chosen_part in computer_parts:
            print("removing {}".format(current_choice))
            computer_parts.remove(chosen_part)
        else:
            print("adding {}".format(current_choice))
            computer_parts.append(chosen_part)
        print("your list now contains: {}".format(computer_parts))
        
    else:
        print("select from the following options")
        for number, part in enumerate(available_parts):
            print("{0}: {1}".format(number+ 1 , part))
    current_choice = input()
print(computer_parts)