answer = 5
print("please guess no. btw 1 and 10:")
guess = int(input())

if guess < answer:
    print("please guess higher")
    guess = int(input())
    if guess == answer:
        print("you finally guessed it")
    else:
        print("sorry, you have not guessed correctly")
elif guess > answer:
    print("please guess lower")
    guess = int(input())
    if guess == answer:
        print("you finally guessed it")
    else:
        print("sorry, you have not guessed correctly")
else:
    print("Hooray you have guessed correct")

x = 5
y = 7

if x > y:
    print("x is greater than y")
elif x < y:
    print("x is smaller than y")
elif x == y:
    print("x equals y")

tree1 = "Adam"
tree2 = "Eve"

if tree1 == tree2 :
    print("The trees are the same")
else:
    print("The trees are different")