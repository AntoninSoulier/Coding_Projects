#Coding Questions

from collections import Counter
import heapq
import math

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

def NumberIsland(carte):
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

print("Number of Islands:", NumberIsland(carte))

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
            
            if(m != cle and m != last_char and dic[m] > 0):
                organized+=m
                dic[m]-=1
                last_char = m
                res+=1
            if(cle != last_char and valeur>0):
                organized+=cle
                dic[cle] -= 1
                last_char = cle
                res+=1

            """print(organized)
            print(cle)
            for k,v in dic.items():
                print(k,v)
            print("")"""

        for val in dic.values():
            total += val
        if(total == 0):
            return(organized)
        elif(total != 0 and res == 0):
            return("")

word = "kkkkzrkatkwpkkkktrq"
print(Reorganize(word))

def Longest(s):
    if(len(s)==0):
        return(0)
    elif(s == " " or len(s) == 1):
        return(1)
    else:
        dic = {}
        for i in range(len(s)):
            for j in range(i+1,len(s)):
                sub_word = []
                for k in range(i,j+1):
                    if(s[k] not in sub_word):
                        sub_word.append(s[k])
                    else:
                        break
                    dic[(i,j)] = len(sub_word)

        m = max(dic,key=dic.get, default=0)
        return(dic[m])

word = "abcabcbb"
print("Longest word:",Longest(word))

def Alien(words,order):
    res = True
    for i in range(len(words)-1):
        word1 = words[i]
        word2 = words[i+1]
        j=0
        c = False
        while(j<len(word1) and j<len(word2) and word1[j] == word2[j]):
            j+=1
            #check if we are in the case of a prefix: [hello,he]
            if(len(word1)-1<j or len(word2)-1<j):
                if(len(word1)>len(word2)):
                    long = word1
                    small = word2
                else:
                    long = word2
                    small = word1
                if(words.index(long)<words.index(small)):
                    return(False)
                else:
                    c = True
        
        if(c == False and order.index(word1[j]) > order.index(word2[j])):
            res = False
    return(res)

words = ["hello","leetcode"]
order = "hlabcdefgijkmnopqrstuvwxyz"
print("Ordered:",Alien(words,order))


def isDifferent(lst):
    tmp_lst = []
    for element in lst:
        if(element not in tmp_lst):
            tmp_lst.append(element)
        else:
            return(False)
    return(True)

def maxProducts(lst):
    res = []
    if(len(lst)<3):
        return(0)
    elif(len(lst) == 3):
        if(isDifferent(lst)):
            return(sum(lst))
        else:
            return(0)
    else:
        for i in range(len(lst)-2):
            tmp = []
            for j in range(i,i+3):
                tmp.append(lst[j])
            if(isDifferent(tmp)):
                m = sum(tmp)
                res.append(m)
        return(max(res))

sales = [0,1,3,3,5,6]
print(maxProducts(sales))

def FirstUnique(s):
    dic = {}
    for i in range(len(s)):
        if(s[i] in dic):
            dic[s[i]] += 1
        else:
            dic[s[i]] = 1
    for key,val in dic.items():
        if(val == 1):
            return(s.index(key))
    return(-1)

s = "loveleetcode"
print(FirstUnique(s))

def ispow2(n):
    if(n == 1):
        return(True)
    else:
        g = 2
        while(g<=n):
            if(n == g):
                return(True)
            g *= 2
        return(False)

#print(ispow2(64))

def Origin(moves):
    i=0
    j=0
    for ope in moves:
        if(ope=="L"):
            i-=1
        elif(ope=="R"):
            i+=1
        elif(ope=="U"):
            j-=1
        elif(ope=="D"):
            j+=1
    return(i==0 and j==0)

operation = "LL"
print(Origin(operation))

def MissingNumber(nums):
    i = 0
    while(True):
        if(i not in nums):
            return(i)
        i+=1
lst = [9,6,4,2,3,5,7,0,1]
print(MissingNumber(lst))

def MaxBaloons(str):
    if(str == "balon" or str == "ballon" or str == "baloon"):
        return(0)
    else:
        word = "balloon"
        dic = {}
        s = True
        t = 0
        for char in str:
            if(char not in dic):
                dic[char] = 1
            else:
                dic[char] += 1
        while(s == True):  
            res = 0 
            for key in dic.keys():
                if(key in word):
                    if(key == "l" or key=="o"):
                        dic[key]-=2
                        res+=1
                        if(dic[key]==0):
                            s=False
                    else:
                        dic[key]-=1
                        res+=1
                        if(dic[key] == 0):
                            s = False

            if(res == 5):
                t+=1
            else:
                s = False
        return(t)

s = "loonbalxballpoon"
print(MaxBaloons(s))

def BestTime(prices):
    res = []
    for i in range(len(prices)):
        for j in range(i+1,len(prices)):
            if(prices[j]-prices[i]>0):
                res.append(prices[j]-prices[i])
  
    if(not res):
        return(0)
    else:
        return(max(res))

prices = [7,6,4,3,1]
print(BestTime(prices))

def RemoveElement(nums,val):
    count = 0
    while(val in nums):
        nums.remove(val)
        count+=1
    l = len(nums)
    for _ in range(count):
        nums.append('_')
    return(l,nums)

nums = [3,2,2,3]
val = 3
print(RemoveElement(nums,val))

def RotateArray(nums,k):
    for i in range(k):
        tmp = nums[-1]
        nums = nums[0:-1]
        nums.insert(0,tmp)
    return nums

def AnotherRotateArray(nums,k):
    for _ in range(k):
        copy = nums.copy()
        for i in range(len(nums)):
            nums[(i+1)%len(nums)] = copy[i]
    return(nums)

nums = [1,2,3,4,5,6,7]
k = 3
print(AnotherRotateArray(nums,k))

def ClimbingStairs(n):
    lst = [x for x in range(n+1)]
    lst[0] = 1
    lst[1] = 1
    for i in range(2,n+1):
        lst[i] = lst[i-1]+lst[i-2]
    return(lst[len(lst)-1])

print("Number of ways to climb the stairs: " + str(ClimbingStairs(5)))

def JewelsStones(jewels,stones):
    res = 0
    dic = {}
    for i in range(len(jewels)):
        dic[jewels[i]] = 1
    for j in range(len(stones)):
        if(stones[j] in dic):
            res +=1
    return(res)

jewels = "aA"
stones = "aAAbbbb"
print("Nombre Bijoux: " + str(JewelsStones(jewels,stones)))

def EmailAdresses(emails):
    dic = {} 
    res = 0
    for  i in range(len(emails)):
        email = emails[i].split("@")
        domain = email[1]
        name = email[0].replace('.','')
        if("+" in name):
            name = name.split("+")
            name = name[0].replace('.','')
        if(name not in dic.keys()):
            dic[name] = []
            dic[name].append(domain)
        elif(name in dic.keys() and domain not in dic[name]):
            dic[name].append(domain)
    for k,v in dic.items():
        res += len(v)
    return(res)

emails =   ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]
print("Nombre de mails envoyés: " + str(EmailAdresses(emails)))

def FloodFill(image,sr,sc,color):
    rows = len(image)
    cols = len(image[0])

    if(sr+1 in range(rows) and image[sr+1][sc] == image[sr][sc]):
        image[sr+1][sc] = color 
    if(sr-1 in range(rows) and image[sr-1][sc] == image[sr][sc]):
        image[sr-1][sc] = color  
    if(sc+1 in range(cols) and image[sr][sc+1] == image[sr][sc]):
        image[sr][sc+1] = color
    if(sc-1 in range(cols) and image[sr][sc-1] == image[sr][sc]):
        image[sr][sc-1] = color 
    return(image)

image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
color = 2
t = FloodFill(image,sr,sc,color)
for i in range(len(t)):
    print(t[i])


def Mostwater(height):
    val = 0
    for i in range(len(height)):
        for j in range(i+1,len(height)):
            tmp = (j-i) * min(height[i],height[j])
            if(tmp>val):val = tmp
    return(val)

height = [1,8,6,2,5,4,8,3,7]
print(Mostwater(height))

def Linked(lists):
    lst = []
    final = []
    while(any(lists)):
        for i in range(len(lists)):
            if(len(lists[i])!=0):
                tmp = lists[i][0]
                del lists[i][0]
                lst.append(tmp)    
        final += lst
        lst.clear()
    final.sort()
    return(final)

lists = [[1,4,5],[1,3,4],[2,6]]
print(Linked(lists))

def GroupedAnagrams(strs):
    fin = []
    while(len(strs)!=0):
        tmp = strs[0]
        del strs[0]
        tmp_lst = []
        tmp_lst.append(tmp)
        if(len(strs)!=0):
            for j in range(len(strs)):
                print(strs[j])
                if(Counter(tmp) == Counter(strs[j])):
                    tmp_lst.append(strs[j])
        for i in range(1,len(tmp_lst)):
            strs.remove(tmp_lst[i])
        fin.append(tmp_lst)
    return(fin)

strs = ["eat","tea","tan","ate","nat","bat"]
print(GroupedAnagrams(strs))

def ArrayParity(nums):
    even = []
    odd = []
    for element in nums:
        if(element%2==0):
            even.append(element)
        else:
            odd.append(element)
    return(even+odd)

nums = [3,1,2,4]
print(ArrayParity(nums))

"""
class TreeNode:
    def __init__(self,val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(root: Optional[TreeNode]):
    if(root == None):
        return 0
    left = maxDepth(root.left)
    right = maxDepth(root.right)
    return(max(left,right)+1)

root = Optional[TreeNode]
root = [3,9,20,None,None,15,7]
print(maxDepth(root))
"""

def LongestCommonPrefix(strs):
    s = min(strs, key=len)
    prefix = ""
    for i in range(len(s)):
        res = 0
        for j in range(len(strs)):
            if(s[i] == strs[j][i]):
               res += 1
        if(res == len(strs)):
            prefix+=s[i]
        else:
            return(prefix)
    return(prefix) 

strs = ["flower","flow","flight"]
print(LongestCommonPrefix(strs))

def coinChange(coins,amount):
    dp = [x for x in range(amount+1)]
    for i in range(len(dp)):
        dp[i] = amount+1
    dp[0] = 0
    for i in range(amount+1):
        for j in range(len(coins)):
            if(coins[j] <= i):
                dp[i] = min(dp[i], 1 + dp[i - coins[j]])
    if(dp[amount] > amount):
        return(-1)
    else:
        return dp[amount]

coins = [1,2,5]
amount = 11
print(coinChange(coins,amount))

def removeVowels(s):
    vowels = ["a","e","i","o","u"]
    for char in s:
        if(char in vowels):
            s = s.replace(char,'')
    return(s)

s = "leetcodeisacommunityforcoders"
print(removeVowels(s))

def lastStoneWeight(stones):
    while(len(stones)!=1):
        stones.sort()
        x = stones[len(stones)-2]
        y = stones[len(stones)-1]
        if(x == y):
            stones.remove(x)
            stones.remove(y)
        else:
            stones.remove(x)
            stones[len(stones)-1] = y - x
        if(len(stones)==0):
            return(0)
    return(stones[0])

stones = [2,7,4,1,8,1]
print(lastStoneWeight(stones))

def roundFavs(n):
    if(len(str(n))>3 and len(str(n))<=6):
        return(str(n)[0:len(str(n))-3]+","+str(n)[len(str(n))-3]+" k")
    elif(len(str(n))>6 and len(str(n))<=9):    
        return(str(n)[0:len(str(n))-6]+","+str(n)[len(str(n))-6]+" M")
    elif(len(str(n))>9):
        return(str(n)[0:len(str(n))-9]+","+str(n)[len(str(n))-9]+" Md")
        
print(roundFavs(456895))

def sort_diff(t):
    res = []
    for _ in range(len(t)):
        tmp = min(t)
        res.append(tmp)
        t.remove(tmp)
    return res

def sort_same(t):
    while(True):
        test = 0
        for i in range(len(t)-1):
            if(t[i]>t[i+1]):
                tmp=t[i]
                t[i] = t[i+1]
                t[i+1] = tmp
                test+=1
        if(test == 0):
            return(t)

t = [4,8,7,3,5,1]
print(sort_diff(t))
s = [4,8,7,3,5,1]
print(sort_same(s))

def minimumCostConnectStick(sticks):
    cost = 0
    while(True):
        if(len(sticks) == 1):
            return(cost)
        min1_stick = min(sticks)
        sticks.remove(min1_stick)
        min2_stick = min(sticks)
        sticks.append(min1_stick)
        new_stick = min1_stick + min2_stick
        cost += new_stick
        sticks.remove(min1_stick)
        sticks.remove(min2_stick)
        sticks.append(new_stick)
        
sticks = [2,4,3]
print("Minimum cost: " + str(minimumCostConnectStick(sticks)))

def Compress(chars):
    char_dic = {}
    for char in chars:
        if(char not in char_dic):
            char_dic[char] = 1
        else: 
            char_dic[char] += 1
    chars.clear()
    for key,val in char_dic.items():
        if(val == 1):
            chars.append(key)
        elif(val > 9):
            chars.append(key)
            for digit in str(val):
                chars.append(digit)
        else:
            chars.append(key)
            chars.append(str(val))
    return(len(chars))

chars = ["a","a","b","b","c","c","c"]
print(Compress(chars))
