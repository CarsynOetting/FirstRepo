import random

##START GAME FUNCTION##
def start_game():
    mat =[]
    for i in range(4):
        mat.append([0] * 4)
    print("Commands are as follows : ")
    print("'W' or 'w' : Move Up")
    print("'S' or 's' : Move Down")
    print("'A' or 'a' : Move Left")
    print("'D' or 'd' : Move Right")

    add_new_2(mat)
    return mat
##END START GAME FUNCTION##

##END START GAME FUNCTION##
def add_new_2(mat):
    r = random.randint(0,3)
    c = random.randint(0,3)

    while(mat[r] != 0):
        r = random.randint(0,3)
        c = random.randint(0,3)

    mat[r] = 2
##END START GAME FUNCTION##

##CURRENT STATE FUNCTION##
def get_current_state(mat):
    for i in range(4):
        for j in range(4):
            if(mat[i][j] == 2048):
                return 'WON'

    for i in range(3):
        for j in range(3):
            if(mat[i][j]==mat[i + 1][j] or mat[i][j]==mat[i][j+1]):
                return 'GAME NOT OVER'

    for j in range(3):
        if(mat[3][j]== mat[3][j + 1]):
            return 'GAME NOT OVER'

    for i in range(3):
        if(mat[i][3]== mat[i + 1][3]):
            return 'GAME NOT OVER'

    return 'LOST'
##END CURRENT STATE FUNCTION##


def compress():
    changed = False
    new_mat = []

    for i in range(4):
        new_mat.append([0]*4)

    for i in range(4):
        pos = 0
        for j in range(4):
            if (mat[i][j] != 0):
                new_mat[i][pos] = mat[i][j]

                if(j != pos):
                    changed = True
                pos += 1
    return new_mat, changed
