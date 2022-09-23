#1.1 Line Order

line =  [1, 80, 82]
member_to_check = 7
half = 'second'

def check_member(line, member_to_check, half):
    res = False
    if(member_to_check not in line):
        return("The member with ID " + str(member_to_check) + " not found in line")  
    else:
        size = len(line)
        if(size%2==0 and half=='first'):
            if(member_to_check in line[0:int(size/2)]):
                res = True
        if(size%2==0 and half=='second'):
            if(member_to_check in line[int(size/2):size]):
                res = True
        if(size%2==1 and half=='first'):
            if(member_to_check in line[0:int(len(line)/2)]):
                res = True
        if(size%2==1 and half=='second'):
            if(member_to_check in line[int(len(line)/2):len(line)]):
                res = True
    return res

#test = check_member(line,member_to_check,half)
#print(test)

#1.2 Letter Occurences

lst_of_words = ['welcome', 'to', 'computer', 'science', 'department']
letter = 'e'

def words_with_letter(lst_of_words, letter):
    return_list = []

    for word in lst_of_words:
        if(word[-1] == letter):
            return_list.append(word)

    if (not return_list): #Check if list empty
        print("No words endind with " + letter)
    else:
        return return_list

#print(words_with_letter(lst_of_words,letter))

#1.3 Longest Word

lst_of_words = ['python', 'java', 'algorithms', 'data']

def longest_word_index(lst_of_words):
    index = 0
    size = 0
    res = 0
    for word in lst_of_words:
        if(size<len(word)):
            size = len(word)
            res = index
        index+=1
    return res

#print(longest_word_index(lst_of_words))

#1.4 Operations on Lists
import random
from turtle import clear

from scipy import rand

"""list_length =  input("What's the length of your list? ")
list_of_floats = []
for i in range(int(list_length)):
    x = float(input("value ["+ str(i) + "] = "))
    list_of_floats.append(x)
"""
def operations_on_list(list_of_floats):

    return_list = []
    randomize = random.randint(1,3)
    print("Operation chosen = " + str(randomize))
    match randomize:
        case 1:
            for num in list_of_floats:
                num = num*num
                return_list.append(num)
        case 2:
            for num in list_of_floats:
                num = num/2
                return_list.append(num)
        case 3:
            for num in list_of_floats:
                if(num%2==0):
                    num = 1
                    return_list.append(num)
                else:
                    num = 0
                    return_list.append(num)
    return return_list

#print(operations_on_list(list_of_floats))

def is_prime(num):
    for i in range(2,num):
        if(num%i == 0):
            return(str(num) + " is not a prime number")
    return (str(num) + " is a prime number")

def reverse_list(lst):
    rev_lst = []
    for i in range(len(lst)-1,-1,-1):
        rev_lst.append(lst[i])
    return rev_lst

def compute_length_sum(string_list):
    length_sum = 0
    for string in string_list:
        length_sum+=len(string)
    return length_sum

def count_elements(my_lst):
    count = 0
    for n in my_lst:
        count = count + 1
    return count

def compute_pay(hours, rate):
    if hours < 40:
        pay = hours * rate
    else:
        pay = (40 * rate) + ((hours - 40) * 1.5 * rate)
    return pay

def palindrome(word):
    i = 0
    j = len(word)-1
    res = True
    while(i<j):
        if(word[i] == word[j]):
            i+=1
            j-=1
        else:
            res = False
            break
    return res

def format_number(number):
    res = " "
    i = 1
    if(number[0] == "1" and number[1] == "0"):
        res = number[0]  + ","
    print(res)
    for i in range(1,len(number),3):
        for j in range(3):
            res += "0"
        res+=","
    return res


def find_avg(lst):
    total = 0
    count = 0
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j] % 3 == 0:
                total += lst[i][j]
                count += 1
    return total/count

test = find_avg([[15,3,5],[4,5,6]])

def pyramid_straight(height):
    i = 0
    j = height
    stars = 1
    while(i<height):
        print(" " * int(height-i-1) + "*" * stars)
        stars+=2
        i+=1

def pyramid_reverse(height):
    i = 0
    j = height
    stars = height*2-1
    while(i<j):
        print(" "*i + "*"*stars)
        stars=stars-2
        i+=1

def diamond(size):
    pyramid_straight(size)
    pyramid_reverse(size)

def form(size):
    space = size
    news = 0
    for i in range(size):
        print("")
        print(" "*space*2, end=' ')
        for j in range(size):
            print("*", end=' ')
        if(news<size):
            print(" *"*news, end=' ')
            news+=1
        space-=1

def square(size):
    stars = size
    regular = size
    for i in range(size):
        print("")
        while(stars>0):
            for j in range(size):
                print("*"*regular*2,end=' ')
                print(" *"*stars,end=' ')
                stars-=1
                print("")
    
form(10)
square(10)
diamond(5)

