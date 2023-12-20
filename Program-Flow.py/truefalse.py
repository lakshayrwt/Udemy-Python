day = "Saturday"
temperature = 30
raining = False

if (day == "Saturday" and temperature > 30) or not raining:
    print("go play basketball")
else:
    print("learn Python")

if 0:
    print("true")
else:
    print("false")

name = input("please enter your name? ")
if name:
    print("hello, {0}".format(name))
else:
    print("are you the man with no name")