parrot = "Norwegian Blue"
for character in parrot:
    print(character)

number = input("Please enter a value of your choise:")
seperators = ""
for char in number:
    if not char.isnumeric():
        seperators = seperators + char
print(seperators)

Extraction ="Alright, but apart from the Sanitation, the Medicine, Education,Wine,Public Order,Irrigation,Roads,the Fresh-Water System, and Public Health,what have the Romans ever done for us?"
Capital = ""
for char in Extraction:
    if char.isupper():
        Capital = Capital + char
print(Capital)