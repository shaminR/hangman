import random
#import randint

wrong = 6
index = 0
yuh = " "

def difficulty():
    print("Pick a difficulty: 1 easiest, 3 hardest")
    x = input("Please enter a difficulty: ")
    a = "diff" + x + ".txt"
    x = int(x)
    if x > 3 or x < 1:
        print("invalid difficulty entered")
        exit(True)
    file = open(a, "r")
    word = file.readline(randint(1, 5))
    i = 0
    while i < len(word):
        yuh[i] = "_"
        i += 1
    return word


def program():
    print("Welcome to Hangman Deluxe®")
    print("*-------------------------*")
    word = difficulty()
    while True:
        a = checker(word)
        if wrong == 0:
            print("you've been hanged :(")
        if a != 0:
            printer(index, a)


def checker(word):
    letter = input("Enter a letter: ")
    letter.strip()
    i = 0
    correct = False
    while i < len(word):
        if word[i] == letter and i > index:
            index = i
            correct = True
        i += 1
    if correct == False:
        print("ya guessed wrong fool")
        wrong -= 1
        return 0
    else:
        print("guessed right")
        return letter


def printer(index, a):
