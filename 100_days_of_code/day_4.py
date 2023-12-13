import random

#Get the computer's decision on what to play
play_optn = ['rock','paper','scissors']
comp_des = play_optn[random.randint(0,2)]

#Get the player's decision on what to play
plyr_des = input("What do you play?\n")

if comp_des == plyr_des:
    print(f"The computer has also played {comp_des}. Draw!")
elif plyr_des == 'paper':
    if comp_des == 'rock':
        print("The computer has played rock. You win!")
    else:
        print("The computer has played sicssors. You Lose!")
elif plyr_des == 'rock':
    if comp_des == 'scissors':
        print("The computer has played scissors. You win!")
    else:
        print("The computer has played paper. You Lose!")
elif plyr_des == 'scissors':
    if comp_des == 'rock':
        print("The computer has played paper. You win!")
    else:
        print("The computer has played rock. You Lose!")
else:
    print("Invalid input. Try again.")
