import csv
import numpy as np
import matplotlib.pyplot as plt

with open("Temperature.csv") as fp:
	reader = csv.reader(fp)
	data = [ line for line in reader ]

data = np.array(data)

number_of_rows = len(data)
x = [] # Days of the week
y = [] # Temperature

for i in range(number_of_rows):
    x.append(data[i][0])
    y.append(data[i][1])

y.sort() # sorting temperatures

print(x)
print(y)

#find the min in the list and find which day it corresponds to

min_value = min(y)
index_min_value = y.index(min_value)
day_min_value = x[index_min_value]

#find the max in the list and find which day it corresponds to

max_value = max(y)
index_max_value = y.index(max_value)
day_max_value = x[index_max_value]

#plt options

plt.title("Temperatures in San Diego")
plt.xlabel("Days of the week")
plt.ylabel("Temperature")
plt.ylim(-0.5,6.5)

#plot data

plt.scatter(x,y,c='g')
plt.plot(day_max_value,index_max_value-1,'.', c="r",ms=15) # max temperature
plt.plot(day_min_value,index_min_value,'.', c="b",ms=15) # min temperature
