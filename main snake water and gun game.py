'''We all have played snake, water gun game in our childhood. If you haven’t, google the
rules of this game and write a python program capable of playing this game with the
user.'''


import random

computer = random.choice([-1,0,1])
youstr = input (" Enter the choose : ")
youDict = {"s":1,"w":-1, "g":0}
youreverse = {1 : "SNAKE" ,-1:"WATER", 0: "GUN"}
you = youDict[youstr]
print (f"The computer choose :{youreverse[computer]}\nYour choice is :{ youreverse[you]} " )
if (computer== you ):
        print ("Its draw!")
else:
    if(computer ==-1 and you == 1): 
        print("You win!")

    elif(computer ==-1 and you == 0):
            print("You Lose!")

    elif(computer == 1 and you == -1):
            print("You lose!")

    elif(computer ==1 and you == 0):
            print("You Win!")

    elif(computer ==0 and you == -1):
            print("You Win!")

    elif(computer == 0 and you == 1):
            print("You Lose!")
    else :
           print("Some thing want wrong")



