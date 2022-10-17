from random import randrange
import matplotlib.pyplot as plt
import cv2

"""im = cv2.imread("CYTech/AnalyseImage/Images/pepper.bmp")
vals = im.mean(axis=2).flatten()
b,bins,patches = plt.hist(vals,255)
plt.xlim([0,255])
plt.show()
"""
from PIL import Image
import numpy as np
from scipy import signal as sig

im = Image.open("CYTech/AnalyseImage/Images/pepper.bmp")
pixels = im.load()

"""r,g,b = im.split()
print(r.histogram())"""

largeur = im.width
hauteur = im.height
treshold = randrange(0,255)
print(treshold)
for i in range(hauteur):
    for j in range(largeur):
        coordonnee = i,j
        #print(im.getpixel(coordonnee))

#im.show()
from skimage import data
from skimage import filters
from skimage.color import rgb2gray
from skimage import io
import matplotlib.pyplot as plt

im = io.imread("CYTech/AnalyseImage/Images/pepper.bmp")
gray_im = rgb2gray(im)
plt.figure(figsize=(15,15))
"""io.imshow(gray_im)
io.show()"""

for i in range(10):
    binarized_gray = (gray_im > i*0.1)*1
    plt.subplot(5,2,i+1)
    plt.imshow(binarized_gray, cmap='gray')
plt.tight_layout()