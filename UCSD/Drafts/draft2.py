from random import randint
import numpy as np
import pandas as pd

dictionary = {'First' : 1, 'Second' : 2, 'Third' : 3}
series = pd.Series(dictionary)

#1D array
a = np.array([1,2,3])
#2D array
b = np.array([(1,2,3),(4,5,6)])

#range from 1 to 15
r = np.arange(1,16,1)
print(r)

#print 4 integers random numbers
rand = np.random.randint(10,size=4)
print(rand)

df = pd.DataFrame(np.random.randn(5,4),index = 'A B C D E'.split())
#print(df)
#print(df.info())

def print_triangle(base):
    idx = 0
    for index in range(base):
        print("*" * index)
        idx+=1

print_triangle(10)

abs_more_than_10 = False
# Do not edit the above line. Add your code below
i = 0
nums=[1,2,-5,12]
while(i < len(nums)):
    if(abs(nums[i])>10):
        abs_more_than_10 = True
    i+=1
print(abs_more_than_10)

import seaborn as sns
import matplotlib.pyplot as plt

"""Expenditure_1 = [10, 10, 5, 5]  #in thoudands
Expenditure_2 = [40, 30, 20, 30]
Profits = [3, 2, 2, 3]  #in thousands
plt.plot(Profits,Expenditure_1,Profits,Expenditure_2)
plt.title("Month-Jan to Apr")
plt.suptitle("Company A")
plt.xlabel("Profits")
plt.ylabel("Expenditure")
plt.xlim(0, 5)
plt.ylim(0,40)
plt.show()
"""
plt.plot(5,5,'<', c="blue",ms=30)
plt.plot([1,2,3],[1,2,3],'-^b',ms=20, lw=0.5)
plt.show()