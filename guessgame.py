import random as rd
def guess(x):
    x = input("Enter your guess.. ")
    x = int(x)
    if x>randomNum :
        print("Go lower!")
        guess(x)
    elif x==randomNum :
        print("You did it!!The number is " + str(randomNum) )
    else :
        print("Go higher!")
        guess(x)
randomNum = rd.randint(1,100)
guess(100)