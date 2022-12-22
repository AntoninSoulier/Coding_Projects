from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn import neighbors
import numpy as np
import Loader

mnist = Loader.mnist

#mnist = fetch_openml('mnist_784', version=1)
#print(mnist.data.shape)
#print(mnist.target.shape)

sample = np.random.randint(70000,size=5000)
data = mnist.data.iloc[sample]
target = mnist.target.iloc[sample]

xtrain, xtest, ytrain, ytest = train_test_split(data,target, train_size=0.8)
knn = neighbors.KNeighborsClassifier(n_neighbors=3)
knn.fit(xtrain,ytrain)
error = 1-knn.score(xtest,ytest)
print('Error: %f' % error)

errors = []
for k in range(2,15):
    knn = neighbors.KNeighborsClassifier(k)
    errors.append(100*(1-knn.fit(xtrain, ytrain).score(xtest, ytest)))
plt.plot(range(2,15), errors, 'o-')
plt.show()

                                        #Prédiction du classifier justes

# On récupère le classifieur le plus performant
knn = neighbors.KNeighborsClassifier(6)
knn.fit(xtrain, ytrain)

# On récupère les prédictions sur les données test
predicted = knn.predict(xtest)

# On redimensionne les données sous forme d'images
images = xtest.values.reshape((-1,28,28))

# On selectionne un echantillon de 12 images au hasard
select = np.random.randint(images.shape[0], size=12)

# On affiche les images avec la prédiction associée
fig,ax = plt.subplots(3,4)

for index, value in enumerate(select):
    plt.subplot(3,4,index+1)
    plt.axis('off')
    plt.imshow(images[value],cmap=plt.cm.gray_r, interpolation="nearest")
    plt.title("Predicted: {}".format(predicted[value]))

plt.show()

                                        #Prédictions du classifier éronnées

#Récuperation des données mal prédites
misclass = (ytest != predicted)
misclass_images = images[misclass,:,:]
misclass_predicted = predicted[misclass]

#Selection d'un échantillon de ces images
select = np.random.randint(misclass_images.shape[0], size=12)

#Affichage des images et des predictions érronées associées à ces images
for index, value in enumerate(select):
    plt.subplot(3,4,index+1)
    plt.axis('off')
    plt.imshow(misclass_images[value], cmap = plt.cm.gray_r, interpolation = 'nearest')
    plt.title("Predicted: {}".format(misclass_predicted[value]))

plt.show()