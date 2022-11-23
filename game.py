#!/bin/python3

#MY FIRST PYTHON GAME SOFTWARE
#it's just a Simple Game about geussing, that's all.. hahah
#


# MY FIRST PYTHON CHALLENGE


import random


def promptUser():
    """This Function Prompt user to enter a number,and Returns that number"""
    try:
        n = input("Enter a Level number(Numeric): ")
    except:
        print("Please enter a valid Numeric Number...")
    return (n)

def generator(n):
    """This Function takes an integer and randomly generate a number between 1 and n.
    Returns the generated number"""
    genrtdNumber = random.randrange(1, int(n) + 1)
    return (genrtdNumber)


if __name__ == '__main__':
    x = 0
    while x <= 0:
        rightAnswer = 0
        inputNumber = promptUser()
        generatedNum = generator(inputNumber)
        generatedNum = int(generatedNum)
        guessdNum = int(input("Guess The Random Number Generated Between between 1 and the Level you enterd : "))
        if guessdNum == generatedNum:
            print("Congratulations ! Congratulations !! Congratulations!!! "
                  "\nThe Number Generated is {} \n YOU WON!!!".format(generatedNum))
            rightAnswer += 1
        elif guessdNum < generatedNum:
            print("Too small!!! The Number Generated is {} \n Try again!!!".format(generatedNum))
        else:
            print("Too Large!!! The Number Generated is {} \n Try again!!!!".format(generatedNum))

        if rightAnswer > 0:
            x += 1





