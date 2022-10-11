from random import randrange
from types import coroutine
from PIL import Image

im = Image.open("Analyse Image/cameraman.png")
pixels = im.load()

largeur = im.width
hauteur = im.height

#Test alternance pixels
for i in range(hauteur):
    for j in range(largeur):
        coordinate = i,j
        print(im.getpixel(coordinate))

#Formule de Harris
for i in range(hauteur):
    for j in range(largeur):
        #Derivée première de I(x,y) en x
        continue

im.show()