print ("Welcome to Treasure Island\n")
print("Your mission is to find the treasure!\n")

an1 = input("You arrive at a stop on the road. Go to the river or back to the highway (river or highway)?\n")
if an1 == 'highway':
    print("You got back in your car and went home. Game over.\n")
elif an1 == 'river':
    an2 = input("You arrive at a river, swim across or wait for a boat(swim or wait)?\n")
    if an2 == 'swim':
        print("You drowned. Game over")
    elif an2 == 'wait':
        an3 = input("You travel by boat to an island. before youe are three doors, red, green, and yellow, Pick one\n")
        if an3 == 'red':
            print ("Burning. Game over\n")
        elif an3 == 'green':
            print ("Posion. Game over\n")
        elif an3 == 'yellow':
            print ("Gold. You win!\n")
        else:
            print ("Please submit a valid input\n")
    else:
        print ("Please submit a valid input\n")
else:
    print ("Please submit a valid input\n")