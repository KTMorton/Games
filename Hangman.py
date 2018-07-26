guessList = []
guessesList = []
guesses = 0
numberAllowedWrong = 5
words = ["hello", "one", "two", "three", "goodbye", "test", "work", "idea", "code"]
wordFound = False


def RepresentsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

import random

input1 = input("Type 1 for random and 0 for user selected word: ")

if RepresentsInt(input1):
    if int(input1) is 1:
        selectedWord = words[random.randint(0, 8)]
    else:
        input1 = input("Type word for user to guess: ")
        selectedWord = input1




for char in selectedWord:
    guessList.append("~")

numberOfChances = len(guessList) + numberAllowedWrong

print("".join(guessList))

while True:

    userInput = input("Guess a letter: ")
    inputLen = len(userInput)
    print(inputLen)
    while int(inputLen) != 1 or RepresentsInt(userInput):
        print("Input one letter plz!")
        userInput = input("Guess a letter: ")
        inputLen = len(userInput)
        print(inputLen)

    posOfLetter = []


    if userInput in selectedWord:
        posOfLetter = [i for i, char in enumerate(selectedWord) if char == userInput]
        for pos in posOfLetter:
            guessList[pos] = userInput
            guesses += 1

        if "".join(guessList) == selectedWord:
            wordFound = True

    else:
        if userInput not in guessesList:
            print("sorry not in word")
            guesses += 1

        if guesses >= numberOfChances and wordFound == False:
            print("You Lose!")
            break
    if userInput in guessesList:
        print("Already guessed this letter")
        guesses -= 1

    if wordFound:
        print("You Win!!")
        break
    print("".join(guessList))
    guessesList.append(userInput)
    print("Guessed Already: " + ", ".join(list(set(guessesList))))
    print("You have guessed "+ str(guesses) + " times." "\nYou Have " + str(numberOfChances - guesses) + " guesses left.")

