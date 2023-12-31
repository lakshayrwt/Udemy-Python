low = 1
high = 1000

print("Please think of a number between {} and {}".format(low , high))
input("Please ENTER to start")

guesses = 1
while low != high:
    # print("\t guess in the range of {} and {}".format(low, high))
    guess = low + (high - low) // 2
    high_low = input("My guess is {}. should i guess higher or lower? Enter h or l, or c if my guess is correct ".format(guess)).casefold()

    if high_low == "h":
        low = guess + 1
    elif high_low == "l":
        high = guess - 1
    elif high_low == "c":
        print("i got it in {} guesses".format(guesses))
        break
    else:
        print("Please enter h , l or c")


    guesses += 1
else:
    print("you guessed of number {}".format(low))
    print("I got it in {} guesses".format(guesses))
    