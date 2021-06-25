import random

import numpy as np
from termcolor import colored


matrix=[[" " for item in range(10)] for sublist in range(10)]
score=0
player_key=0
#Wall
for i in range(10):
    matrix[i][0]=matrix[0][i]=matrix[9][i]=matrix[i][9]=colored("X","green")

#Key
random_keys=[]
for count in range(30):
    for randon_int in range(2):
        rand=(random.randint(1,9))
        random_keys.append(rand)

    if matrix[random_keys[count]][random_keys[count+1]]==colored("X","green"):
        continue
    else:
        matrix[random_keys[count]][random_keys[count + 1]] = colored("K","magenta")
        break



#Chest

random_chest=[]

for count in range(30):
    for randon_int in range(2):
        rand=(random.randint(1,9))
        random_chest.append(rand)

    if matrix[random_chest[count]][random_chest[count+1]]==colored("X","green") \
            or matrix[random_chest[count]][random_chest[count+1]]==colored("K","magenta"):
        continue
    else:
        matrix[random_chest[count]][random_chest[count + 1]] = colored("C","magenta")
        break
#Player

random_player=[]

for count in range(30):
    for randon_int in range(2):
        rand=(random.randint(1,9))
        random_player.append(rand)

    if matrix[random_player[count]][random_player[count+1]]==colored("X","green") \
            or matrix[random_player[count]][random_player[count+1]]==colored("K","magenta")\
            or matrix[random_player[count]][random_player[count+1]]==colored("C","magenta"):
        continue
    else:
        matrix[random_player[count]][random_player[count + 1]] = colored("P","blue")
        break

#Traps
random_traps = []
for count in range(12):
    for randon_int in range(2):
        rand=(random.randint(1,9))
        random_traps.append(rand)

    for each_random in random_traps:
        if matrix[random_traps[count]][random_traps[count+1]]!=colored("X","green") \
            and matrix[random_traps[count]][random_traps[count+1]]!=colored("C","magenta") \
            and matrix[random_traps[count]][random_traps[count + 1]]!= colored("K","magenta")\
            and matrix[random_traps[count]][random_traps[count + 1]] != colored("P","blue"):
            matrix[random_traps[count]][random_traps[count + 1]]=colored("T","red")

#Coins
random_coins = []
for count in range(12):
    for randon_int in range(2):
        rand=(random.randint(1,9))
        random_coins.append(rand)

    for each_random in random_coins:
        if matrix[random_coins[count]][random_coins[count+1]]!=colored("X","green") \
            and matrix[random_coins[count]][random_coins[count+1]]!=colored("C","magenta") \
            and matrix[random_coins[count]][random_coins[count + 1]]!= colored("K","magenta") \
            and matrix[random_coins[count]][random_coins[count + 1]]!=colored("T","red")\
            and matrix[random_coins[count]][random_coins[count + 1]] != colored("P","blue"):
            matrix[random_coins[count]][random_coins[count+1]]=colored("O","yellow")


print(colored("X - Wall\t","green")
      + colored("C – Chest\t","magenta")
      + colored(" K – Key\t","magenta")
      + colored("O – Coin\t","yellow")
      +colored("T – Trap\t","red")
      + colored("P - Player\t","blue"))
print()


def find(l, elem):
    for row, i in enumerate(l):
        try:
            column = i.index(elem)
        except ValueError:
            continue
        return row, column
    return -1


def actual_game(next_row_of_player,next_column_of_player):
    global score,player_key
    if matrix[next_row_of_player][next_column_of_player] == colored("T", "red"):
        print(colored("game over! You've lost!! ", "red"))
        return "break",score,player_key

    elif matrix[next_row_of_player][next_column_of_player] == colored("X", "green"):
        print(colored("game over! You've lost!! ", "red"))
        return "break", score, player_key

    elif matrix[next_row_of_player][next_column_of_player] == colored("K", "magenta"):
        print(colored("Coin picked up!","green"))
        player_key=player_key+1
        score=score+1
        matrix[next_row_of_player][next_column_of_player] = colored("P", "blue")
        matrix[current_row_of_player][current_column_of_player] = " "
        return "continue", score, player_key

    elif matrix[next_row_of_player][next_column_of_player] == colored("O", "yellow"):
        score = score + 1
        matrix[next_row_of_player][next_column_of_player] = colored("P", "blue")
        matrix[current_row_of_player][current_column_of_player] = " "
        return "continue", score, player_key

    elif matrix[next_row_of_player][next_column_of_player] == colored("C", "magenta"):
        if (player_key == 1):
            print(colored("Congratulations... You won with score "+str(score),"green"))
            return "break", score, player_key
        else:
            print("You have no keys")
            return "continue", score, player_key
    else:
        matrix[next_row_of_player][next_column_of_player] = colored("P", "blue")
        matrix[current_row_of_player][current_column_of_player] = " "
        return "continue", score, player_key


while True:

    print(colored("Key - "+str(player_key)+"\t", "magenta")+ colored("Score - "+str(score), "yellow"))
    for rows in range(len(matrix)):
        for cols in range(len(matrix[rows])):
            print(matrix[rows][cols], end=" ")
        print()

    direction=input("In which direction you want to move (up, down, left, right)\n")
    current_row_of_player, current_column_of_player = find(matrix, colored("P", "blue"))

    print("row " + str(current_row_of_player) + " column " + str(current_column_of_player))
    if direction=="left":
        next_row_of_player=current_row_of_player
        next_column_of_player=current_column_of_player-1;
    elif direction=="right":
        next_row_of_player = current_row_of_player
        next_column_of_player = current_column_of_player + 1;
    elif direction=="up":
        next_row_of_player = current_row_of_player-1
        next_column_of_player = current_column_of_player;
    elif direction=="down":
        next_row_of_player = current_row_of_player+1
        next_column_of_player = current_column_of_player;
    else :
        print("please enter valid direction")

    result,score,player_key=actual_game(next_row_of_player, next_column_of_player)
    if(result=="continue"):
        continue
    else:
        break
























