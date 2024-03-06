from player import position_snake
import keyboard
import time

map = []
size = 10
def next_position(position):
    if look =="w":
        print(position)

        for ind in range(1, len(position)):
            position[-ind] = position[-ind-1]

        position[0][0] = position[0][0]-1

    elif look =="s":

        for ind in range(1, len(position)):
            position[-ind] = position[-ind-1]
        position[0][0] = position[0][0]+1
    elif look =="a":

        for ind in range(1, len(position)):
            position[-ind] = position[-ind-1]
        position[0][1] = position[0][1]-1
    elif look =="d":

        for ind in range(1, len(position)):
            position[-ind] = position[-ind-1]
        position[0][1] = position[0][1]+1
while True:
    for line in range(0, size):
        map1 = []
        for stolb in range(0, size):
            if line == 0 or line == size - 1:
                map1.append("-")
            elif stolb == 0 or stolb == size - 1:
                map1.append("|")
            else:
                map1.append(" ")
        map.append(map1)

    for poss in position_snake[1:]:
        map[position_snake[0][0]][position_snake[0][1]] = "o"
        map[poss[0]][poss[1]] = "#"


    for line in range(0, size):
        for stolb in range(0, size):
            print(map[line][stolb], end = " ")
            if stolb == size - 1:
                print()
    look = input('look')
    next_position(position_snake)
    print(position_snake)
    time.sleep(1)