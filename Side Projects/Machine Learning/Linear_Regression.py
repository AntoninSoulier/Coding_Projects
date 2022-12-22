import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
house_data = pd.read_csv('Side Projects\Machine Learning\Dataset\house.csv')
#print(house_data['loyer'])

house_data = house_data[house_data['loyer']<10000]

x = np.matrix([np.ones(house_data.shape[0]), house_data['surface'].values]).T
y = np.matrix(house_data['loyer']).T

theta = np.linalg.inv(x.T.dot(x)).dot(x.T).dot(y)
print(theta)

plt.xlabel('Surface')
plt.ylabel('Loyer')

plt.plot(house_data['surface'], house_data['loyer'], 'ro', markersize = 4)

#Display between 0 and 250
plt.plot([0,250], [theta.item(0), theta.item(0) + 250 * theta.item(1)], linestyle='--', c='#000000')
plt.show()

#Exemple du sortie du prix du loyer avec en entrée une surface de 35 mètres carrés:
print(theta.item(0) + theta.item(1) * 35)

