#1

def front_two_back_two(input_string):
    final_string = " "
    if(len(input_string)<2):
        return(final_string)
    else:
        final_string = input_string[0] + input_string[1] + input_string[-2] + input_string[-1]
        return(final_string)

#print(front_two_back_two("Hello"))

#2

def Celsius_Fahrenheit(K_temperature):
    C_temperature = float(K_temperature) - 273.15
    F_temperature = (float(K_temperature) - 273.15) * 9/5 + 32

    print("The temperature in Celsius is " + str(C_temperature))
    print("The temperature in Fahrenheit is " + str(F_temperature))

#K_temperature = input()
#Celsius_Fahrenheit(K_temperature)

#3

def fourDigits(input_int):
    chain = str(input_int)
    new_list = []
    for i in chain:
        new_list.append(i)
    print("The first number is " + (new_list[0]))
    print("The last number is " + str(new_list[-1]))


#input_int = input()
#fourDigits(input_int)

#4

"""list_length =  input("What's the length of your list? ")
list = []
for i in range(int(list_length)):
    x = int(input("value "+ str(i) + ":"))
    list.append(x)

def min_max_sum(list):
    final_list = []

    min_value = min(list)
    max_value = max(list)
    sum_value = sum(list)

    final_list.extend([min_value, max_value, sum_value])

    return(final_list)   

print(min_max_sum(list))"""

#5

def print_square():
    dictionnary = {}
    for i in range (1,16):
        dictionnary[i] = i*i
    print(dictionnary)

#print_square()


#Question 6
def fib(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return fib(n-1) + fib(n-2)

#print(fib(9))

#Question 7
tuple = ("w",3,"r","e","s","o","u","r","c","e")

def get_element(tuple):
    if(len(tuple)<4):
        print("Not enough elements in the tuple.")
    else:
        new_tuple = (tuple[3],tuple[-4])
    return new_tuple

#print(get_element(tuple))

#Question 8
A = {1,3,4,5}
B = {2,4,6,8}

def set_operation(A, B):
    res = "yes"
    for value in A:
        if(not(value in B)):
            res = "no"
    return res

#print(set_operation(A,B))

#Question 9

my_tuple = [(),(1,2),(2,3),(3,4)]
other_tuple = [(1,2,6),(2,3,-6),(3,4),(2,2,2,2)]

def sum_tuples(my_tuple):
    return_list = []

    for value in my_tuple:
        if(not(value)): #check if tuple is empty
            temp = 0 #if empty temp is 0
        else:
            temp = sum(value)
            return_list.append(temp)

    return(return_list)
   
#print(sum_tuples(other_tuple))

#Question 10

def reverse_string(string):
    reversed_string = ""
    t=len(string)-1 #so that index isn't out of range
    for i in range(len(string)):
        reversed_string+=string[t]
        t=t-1
    return reversed_string

def to_binary_recursion(n):
    return_string = ""
    while(n>0):
        return_string += str(n%2)
        n = int(n/2)
    return(reverse_string(return_string))

#print(to_binary_recursion(10))


import numpy as np
import pandas as pd

print("numpy version: " + np.__version__)
print("pandas version: " + pd.__version__)

a = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a)
print(" ")
print(list(a[np.triu_indices(3)]))