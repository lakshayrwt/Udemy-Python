parrot = "Norwegian Blue"
for character in parrot:
    print(character)

number = input("Please enter a value of your choise:")
seperators = ""
for char in number:
    if not char.isnumeric():
        seperators = seperators + char
print(seperators)