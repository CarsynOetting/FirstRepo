import logic_TwoZero

if __name__ == '__main__':
    mat = logic_TwoZero.start_game()

while(True):
    x = input("Press the command:")
    if(x == 'W' or x== "w"):
        mat, flag = logic_TwoZero.move_up(mat)
        status = logic_TwoZero.get_current_state(mat)
        print(status)

        if(status == 'GAME NOT OVER'):
            logic_TwoZero.add_new_2(mat)
        else:
            break

    elif(x == 'S' or x == 's'):
        mat, flag = logic_TwoZero.move_down(mat)
        status = logic_TwoZero.get_current_state(mat)
        print(status)

        if(status == 'GAME NOT OVER'):
            logic_TwoZero.add_new_2(mat)
        else:
            break

    elif(x == 'A' or x == 'a'):
        mat, flag = logic_TwoZero.move_left(mat)
        status = logic_TwoZero.get_current_state(mat)
        print(status)

        if(status == 'GAME NOT OVER'):
            logic_TwoZero.add_new_2(mat)
        else:
            break

    elif(x == 'D' or x == 'd'):
        mat, flag = logic_TwoZero.move_right(mat)
        status = logic_TwoZero.get_current_state(mat)
        print(status)

        if(status == 'GAME NOT OVER'):
            logic_TwoZero.add_new_2(mat)
        else:
            break
    else:
        print("INVALID KEY ENETRED")

    print(mat)
