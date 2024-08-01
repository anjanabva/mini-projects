import random as rd
userPoints = 0
computerPoints = 0
max = input("Enter number of points required to win.. ")
max = int(max)
def rockps(userPoints, computerPoints):
    if userPoints<=max and computerPoints<=max:
        user = input("rock(r), paper(p), scissor(s) shoot.. ")
        computer = rd.choice(['r','p','s'])
        print(f"computer plays {computer}")
        #r>s,s>p,p>r
        if user==computer:
           print("tie!!")
        elif (user == 's') and (computer == 'r'):
           print("+1 point to computer")
           computerPoints+=1
        elif (user == 's') and (computer == 'p'):
           print("+1 point to user")
           userPoints += 1
        elif (user == 'r') and (computer == 'p'):
          print("+1 point to computer")
          computerPoints += 1
        elif (user == 'r') and (computer == 's'):
           print("+1 point to user")
           userPoints += 1
        elif (user == 'p') and (computer == 'r'):
            print("+1 point to user")
            userPoints += 1
        elif (user == 'p') and (computer == 's'):
            print("+1 point to computer")
            computerPoints += 1
        print(f"Scores:\nComputer : {computerPoints}\nUser : {userPoints}")
        if computerPoints==max:
             print("the computer won!!")
        elif userPoints==max:
           print("you won!!")
        else:
            rockps(userPoints,computerPoints)
rockps(0,0)