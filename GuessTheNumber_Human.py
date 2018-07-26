import random

randomNum = random.randint(1, 50)
while True:


    userInput = input("Guess a number between 1 and 50: ")

    try:
        int(userInput)
    except ValueError:
        # Handle the exception
        print('Please enter an integer')
        break

    diff = abs(int(userInput) - randomNum)

    if diff is 0:
        print("You Win!!!")
        break
    elif diff > 50:
        print("Input Too Large/Small")
    else:
        print("You are off by " + str(diff) + " of the number")



