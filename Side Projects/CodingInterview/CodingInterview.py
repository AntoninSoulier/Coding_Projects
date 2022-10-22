from cmath import sqrt
from tkinter import Grid


def Convert(suite):
    if(len(suite) == 0):
        return " "
    else:
        lst_char = []
        occurence = []
        return_string = ""

        for lettre in suite:
            if(lettre not in lst_char):
                lst_char.append(lettre)

        for element in lst_char:
            occ = suite.count(element)
            occurence.append(occ)

        for i in range(len(lst_char)):
            return_string+=str(occurence[i])+ "" + lst_char[i]
        
        return return_string

suite = "aaaabbccc"
res = Convert(suite)
print(res)

def performOperations(arr, operations):
    for op in operations:
        x1 = op[0]
        x2 = op[1]
        rev = []
        left = []
        right = []
        for i in range(0,x1):
            left.append(arr[i])
        for i in range(x2+1, len(arr)):
            right.append(arr[i])
        for i in range(x2,x1-1,-1):
            rev.append(arr[i])
        arr = left + rev + right
    return arr

arr = [9,8,7,6,5,4,3,2,1,0]
op = [[0,9],[0,1]]
print(performOperations(arr,op))

def mostCommon(paragraph,ban_list):
    tmp = paragraph.split()
    list_of_word = [x.lower() for x in tmp]
    dico = {}
    checked_list = []
    print(list_of_word)
    for element in list_of_word:
        if(element not in checked_list and element not in ban_list):
            dico[element] = list_of_word.count(element)
            checked_list.append(element)
    max_element = max(dico,key=dico.get)
    print(max_element)
        
paragraph = "Bob FAR hit a ball , the Far hit BALL flew far after it was hit"
banned = ["hit"]

mostCommon(paragraph,banned)

def MaxSubArray(arr):
    dic = {}
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            s = 0
            for k in range(i,j+1):
                s+=arr[k]
                index = (i,j)
                dic[index] = s
    max_somme = max(dic,key=dic.get)
    print(arr[max_somme[0]:max_somme[1]+1])

tab = [-2,1,-3,4,-1,2,1,-5,4]
MaxSubArray(tab)

def TypeSearch(products,search_word):
    products.sort()
    final = []
    i=0
    while(i<len(search_word)):
        sw = search_word[0:i+1]
        proposed_products = []
        for product in products:
            if(product.startswith(sw)):
                proposed_products.append(product)
        if(len(proposed_products)>3):
            final.append(proposed_products[0:3])
        else:
            final.append(proposed_products)
        i+=1
    print(final)

products = ["mobile","mouse","moneypot","monitor","mousepad"]
search_word = "mouse"
TypeSearch(products,search_word)

import math

def closestPoint(points,k):
    dic = {}
    res = []
    for point in points:
        distance = math.sqrt(math.pow(point[0],2) + math.pow(point[1],2))
        point = tuple(point)
        dic[point] = distance

    for i in range(k):
        min_point = min(dic,key=dic.get)
        del(dic[min_point])
        min_point = list(min_point)
        res.append(min_point)
    print(res)

points =  [[1,3],[-2,2]]
k = 1
closestPoint(points,k)

logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]

def Reorder(logs):
    letter_logs = []
    digit_logs = []
    dic = {}
    to_sort = []
    for log in logs:
        log = log.split()
        if(log[1].isdigit()):
            digit_logs.append(log)
        else:
            letter_logs.append(log)

    for log in letter_logs:
        dic[log[0]] = log[1:len(log)]
        to_sort.append(log[1:len(log)])
    to_sort.sort()
    for element in to_sort:
        for k, val in dic.items():
            if(element == val):
                key = k
        element.insert(0,key)
    to_sort = [' '.join(ele) for ele in to_sort]
    digit_logs = [' '.join(ele) for ele in digit_logs]

    #letter_logs.sort(key=lambda x: (x.split()[1:],x.split()[0]))
    print(to_sort + digit_logs)

Reorder(logs)

graph = {
        'A':['B','C'],
        'B':['D','E'],
        'C':['F'],
        'D':[],
        'E':['F'],
        'F':[]
        }
visited = []

def dfs(visited,graph,node):
    if(node not in visited):
        print(node)
        visited.append(node)
        for neighbor in graph[node]:
            dfs(visited,graph,neighbor)
dfs(visited,graph,'A')

carte = [
        [1,0,0,1,0],
        [1,0,1,0,0],
        [0,0,1,0,1],
        [1,0,1,0,1],
        [1,0,1,1,1]
        ]

def NumberRiver(carte):
    rows = len(carte)
    cols = len(carte[0])
    visited = []
    res = 0

    def dfs(r,c):
        if((r,c) in visited):
            return
        visited.append((r,c))
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        for dr, dc in directions:
            nr = dr + r
            nc = dc + c
            if(nr in range(rows) and nc in range(cols) and carte[nr][nc]==1):
                dfs(nr,nc)

    for r in range(rows):
        for c in range(cols):
            if(carte[r][c]==1 and ((r,c) not in visited)):
                dfs(r,c)
                res+=1
    return(res)

print("Number of Islands:", NumberRiver(carte))

def uniquePath(m,n):
    #Creer matrice de zéro de taille m,n
    matrice = [[0 for i in range(n)] for j in range(m)]
    for i in range(m):
        matrice[i][0] = 1
    for j in range(n):
        matrice[0][j] = 1
    for  i in range(1,m):
        for j in range(1,n):
            matrice[i][j] = matrice[i-1][j] + matrice[i][j-1]
    print("Number of paths:",matrice[m-1][n-1]) 

uniquePath(2,3)

def Reorganize(word):
    dic = {}
    organized = ""
    last_char = " "
    for letter in word:
        if(letter not in dic.keys()):
            dic[letter] = 1
        else:
            dic[letter] += 1
    
    while(True):
        total = 0
        for cle,valeur in dic.items():
            res = 0  
            m = max(dic,key=dic.get)
            if(m != cle and m != last_char and valeur > 0):
                organized+=m
                dic[m]-=1
                last_char = m
                res+=1
            if(cle != last_char and valeur>0):
                organized+=cle
                dic[cle] -= 1
                last_char = cle
                res+=1
        for val in dic.values():
            total += val
        if(total == 0):
            return(organized)
        elif(total != 0 and res == 0):
            return("")

word = "vvvlo"
print(Reorganize(word))

print("lala")