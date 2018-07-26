import random

guessRangeHigh = 100
guessRangeLow = 1
firstComputerGuess = guessRangeHigh / 2
currentComputerGuess = firstComputerGuess
lowestGuess = guessRangeLow
highestGuess = guessRangeHigh



input("Please think of a number between " + str(guessRangeLow) + "-" + str(guessRangeHigh) + ". Hit enter to continue")

print("is your number: " + str(firstComputerGuess))

while True:
    random_amount = random.randint(-(highestGuess-lowestGuess), highestGuess-lowestGuess) / 5
    userResponse = input("""Type "+" for too high, Type "-" for too low, Type "=" if I am right: """)

    if userResponse is "+":
        highestGuess = currentComputerGuess
        currentComputerGuess -= round(((((highestGuess)+1) - lowestGuess) / 2) + random_amount)
        print("is your number: " + str(currentComputerGuess))
    elif userResponse is "-":
        lowestGuess = currentComputerGuess
        currentComputerGuess += round(((((highestGuess)+1) - lowestGuess) / 2) + random_amount)
        print("is your number: " + str(currentComputerGuess))
    elif userResponse is "=":
        print("I win!!")
        break
    else:

        print("Please follow directions.")


