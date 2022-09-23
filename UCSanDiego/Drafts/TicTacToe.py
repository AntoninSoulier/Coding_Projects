plateau = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

def check(plateau, caractere):
    res = False
    #check rows
    for i in range(len(plateau)):
        if(plateau[i][0] == caractere and plateau[i][1] == caractere and plateau[i][2] == caractere):
                res = True
    #check col
    for j in range(len(plateau)):
        if(plateau[0][j] == caractere and plateau[1][j] == caractere and plateau[2][j] == caractere):
            res = True
    #check desc diag
    if(plateau[0][0] == caractere and plateau[1][1] == caractere and plateau[2][2] == caractere):
        res = True 
    #check asc diag 
    if(plateau[2][0]==caractere and plateau[1][1]==caractere and plateau[0][2]==caractere):
        res = True

    return res

def jouer(plateau):
    joueur1 = "+"
    joueur2 = "0" 
    res = joueur1
    play = False
    while(play == False):
        pos_x = int(input("Veuillez entrer la coordonnée x: "))
        pos_y = int(input("Veuillez entrer la coordonnée y: "))
        while((pos_x < 0 or pos_x > 2) or (pos_y < 0 or pos_y > 2)) :
            pos_x = int(input("Veuillez entrer la coordonnée x: "))
            pos_y = int(input("Veuillez entrer la coordonnée y: "))

        plateau[pos_x][pos_y] = res
        play = check(plateau, res)

        if(play == False):
            if(res == joueur1):
                res = joueur2 
            elif(res == joueur2):
                res = joueur1

        #display the plateau
        for i in range(len(plateau)):
            print(plateau[i])

    if(play == True):
        print("Joueur " + res + " a gagné !")
    else:
        print("Draw")
jouer(plateau)