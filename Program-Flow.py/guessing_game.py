answer = 5
print("please guess no. btw 1 and 10:")
guess = int(input())

if guess < answer:
    print("please guess higher")
elif guess > answer:
    print("please guess lower")
else:
    print("Hooray you have guessed correct")