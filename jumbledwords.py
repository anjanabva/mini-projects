import random as r
def choose():
	words = [
    	"apple", "ball", "cat", "dog", "elephant", "fish", "goat", "hat", "ice", "jump",
    	"kite", "lion", "monkey", "nest", "orange", "parrot", "queen", "rabbit", "sun", "tree",
    	"umbrella", "van", "water", "x-ray", "yarn", "zebra", "ant", "bird", "car", "desk",
    	"egg", "fan", "grape", "house", "insect", "jug", "key", "leaf", "moon", "nose",
    	"ocean", "pencil", "quilt", "rain", "star", "table", "under", "vase", "window", "box",
    	"yellow", "zoo", "cloud", "flower", "garden", "hill", "island", "jelly", "kangaroo",
    	"lamp", "mountain", "net", "octopus", "penguin", "quiet", "river", "school", "tiger"
    	]
	pick = r.choice(words)
	return pick
def jumble(word):
	x = "".join(r.sample(word,len(word)))
	return x
	
def play():
        p1 = input("Enter your name player 1 : ")
        p2 = input("Enter your name player 2 : ")
        p1points = 0
        p2points = 0
        turn = 0
        while(1):
                word = choose()
                jumbled_word = jumble(word)
                if(turn%2==0):
                        print(p1,", Your turn!")
                        print("Here is the jumpled word :", jumbled_word)
                        a = input("Your answer : ")
                        if(a ==word):
                                print(p1,"You're right!!")
                                p1points += 1
                        else:
                                print("The word was",word,"Better luck next time!!")
                        print("Wanna conintue playing? \0Enter 1 to continue\nEnter 0 to exit")
                        c = input()
                        c = int(c)
                        if(c!=1):
                                break
                        turn+=1
                else:
                        print(p2,", Your turn!")
                        print("Here is the jumpled word :", jumbled_word)
                        a = input("Your answer : ")
                        if(a ==word):
                                print(p2,"You're right!!")
                                p2points += 1
                        else:
                                print("The word was",word,"Better luck next time!!")
                        print("Wanna conintue playing? \0Enter 1 to continue\nEnter 0 to exit")
                        c = input()
                        c = int(c)
                        if(c!=1):
                                break
                        turn+=1
        print("Scores :")
        print(p1,":",p1points," | ",p2,":",p2points)
        if(p1points>p2points):
                print(p1,"wins!!!!! with",p1points,"points")
        elif(p2points>p1points):
                print(p2,"wins!!!!! with",p2points,"points")
        else:
                print("Its a tie with",p1points,"each bye byee~")
play()
