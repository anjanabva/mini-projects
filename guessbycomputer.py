import random as rd
def guess(y,x):
    print(f"choose a number from {y} to {x} for the computer to guess")
    randomNum = rd.randint(y, x)
    print(randomNum)
    response = input("is the number high or low or correct ?.. ")
    if response == 'correct':
        print("the guess was right!!")
    elif response == 'high':
        guess(y,randomNum-1)
    else :
        guess(randomNum+1,x)

guess(1,20)