for i in range(1,12):
    print("No. {} squared is {} and cubed is {:4}".format(i, i ** 2, i ** 3))
    print("*" * 80)

name = input("Please enter your name:")
age = int(input("What's your age, {0} ".format(name)))
print(age)

# if age >= 18:
#     print("you are eligible to vote")
#     print("Please put an X in the box")
# else:
#     print("You are uneligible to vote, please come back in {0} years".format(18 - age))

if age < 18:
    print("please come back in {0} years".format(18 - age))
elif age == 900:
    print("sorry Yoda, you died in return of jedi")
else:
    print("you are eligible to vote")
    print("please put an X in the box")