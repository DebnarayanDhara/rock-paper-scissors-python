import random

'''
1 is for rock                   
-1 for paper                               
0 for scissors                                 
'''

computer = random.choice([1, -1, 0])   # computer chose number randomly
userStr = input("Enter your choice(R for Rock, P for Paper, S for scissors): ")   #chosed by user

userDict = {
    "R" : 1,
    "P" : -1,
    "S" : 0
}

reverseDict = {
    1 : "Rock",
    -1 : "Paper",
    0 : "scissors"
}

user = userDict[userStr]

# By now we have two numbers (Variables), you and computer

print(f"You chose {reverseDict[user]} \nComputer chose {reverseDict[computer]}")

if(computer == user):
    print("It is a draw")
else:
    if (computer == -1 and user == 1):
        print("You Lose!")

    elif (computer == -1 and user == 0):
        print("You Win!")

    elif (computer == 1 and user == -1):
        print("You Win!")

    elif (computer == 1 and user == 0):
        print("You Lose!")

    elif (computer == 0 and user == 1):
        print("You Win!")

    elif (computer == 0 and user == -1):
        print("You Lose!")

    else :
        print("Something Went Wrong")

