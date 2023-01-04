from matplotlib.pyplot import table
from case import Case
import random

plateau = [
    [" ", " ", " ", " "],
    [" ", " ", " ", " "],
    [" ", " ", " ", " "],
    [" ", " ", " ", " "]
]

plateau[0][0] = Case("Vide").get_status()

for i in range(4):
    for j in range(4):
        plateau[i][j] = Case("Numb")

for mines in range(4):
    i = random.randint(0,3)
    j = random.randint(0,3)
    plateau[i][j] = Case("Mine")
        

def count_mines(plateau):
    mines_around = 0
    for i in range(4):
        for j in range(4):
            if(plateau[i][j].get_status() == "Numb"):
                if(i==0):
                    if(plateau[i+1][j].get_status() == "Mine"):
                        mines_around += 1
                    elif(plateau[i][j+1].get_status() == "Mine"):
                        mines_around += 1
                    elif(plateau[i][j-1].get_status() == "Mine"):
                        mines_around += 1
                elif(i==3):
                    if(plateau[i-1][j].get_status() == "Mine"):
                        mines_around += 1
                    elif(plateau[i][j+1].get_status() == "Mine"):
                        mines_around += 1
                    elif(plateau[i][j-1].get_status() == "Mine"):
                        mines_around += 1
                elif(j==0):
                    if(plateau[i+1][j].get_status() == "Mine"):
                        mines_around += 1
                    elif(plateau[i-1][j].get_status() == "Mine"):
                        mines_around += 1
                    elif(plateau[i][j+1].get_status() == "Mine"):
                        mines_around += 1
                elif(j==3):
                    if(plateau[i+1][j].get_status() == "Mine"):
                        mines_around += 1
                    elif(plateau[i-1][j].get_status() == "Mine"):
                        mines_around += 1
                    elif(plateau[i][j-1].get_status() == "Mine"):
                        mines_around += 1
                else:
                    if(plateau[i+1][j].get_status() == "Mine"):
                        mines_around += 1
                    elif(plateau[i-1][j].get_status() == "Mine"):
                        mines_around += 1
                    elif(plateau[i][j+1].get_status() == "Mine"):
                        mines_around += 1
                    elif(plateau[i][j-1].get_status() == "Mine"):
                        mines_around += 1 
                plateau[i][j].set_status(mines_around)

#count_mines(plateau)

for i in range(4):
    print("")
    for j in range(4):
        print(plateau[i][j].get_status(), end=" ")