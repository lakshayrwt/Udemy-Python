available_exits = ["north","south","ease","west"]
chosen_exits = ""
while chosen_exits not in available_exits:
    chosen_exits = input("So,which way do you want to go,Pal:")

print("aren't you glad we didn't chose the other ways")