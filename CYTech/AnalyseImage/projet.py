import numpy as np
import cv2 as cv
import math
from PIL import Image
from matplotlib import pyplot as plt

im1 = Image.open("CYTech/AnalyseImage/Images/pepper.bmp").convert('L')
im2 = Image.open("CYTech/AnalyseImage/Images/lena.jpg")
extracted_image = Image.new('L',(512,512))

largeur = im1.width
hauteur = im1.height

def DecimalToBinary(n):
    return "{0:08b}".format(int(n))

def BinaryToDecimal(n):
    return int(n,2)

def HideImage():
    for i in range(hauteur):
        for j in range(largeur):
            coordonnee = i,j
            pixel1 = im1.getpixel(coordonnee)
            pixel2 = im2.getpixel(coordonnee)
            res1 = DecimalToBinary(pixel1)
            res2 = DecimalToBinary(pixel2)
            tmp = res1[0:4] + res2[0:4]
            new_pixel = BinaryToDecimal(tmp)
            im1.putpixel((i,j), (new_pixel))

def ExtractImage():
    for i in range(hauteur):
        for j in range(largeur):
            coordonnee = i,j
            pixel = im1.getpixel(coordonnee)
            res = DecimalToBinary(pixel)
            tmp = res[4:8]
            new_pixel = BinaryToDecimal(tmp+"0000")
            extracted_image.putpixel((i,j), (new_pixel))

#Comparer avce formule (EQM) Erreur quadratique moyenne
def Compare(im_init,im_cache):
    np = hauteur*largeur
    res = 0
    max = 0
    for i in range(hauteur):
        for j in range(largeur):
            coordonnee = (i,j)
            val1 = im_init.getpixel(coordonnee)
            if(max<val1):
                max = val1
            val2 = im_cache.getpixel(coordonnee)
            res += math.pow(abs(val2-val1),2)
    return str(round(((res/np)/max)*100,2))  + " %"

def main():

    HideImage()
    ExtractImage()

    im1.show()
    
    #Image secrète Initiale
    im2.show()
    
    #Image cachée obtenue
    extracted_image.show()

    #Histogramme image secrète originale
    histogram_im2 = np.array(im2.getdata())
    plt.hist(histogram_im2.ravel(),256,(0,256))
    plt.show()

    #Histogramme image cachée obtenue
    histogram_extracted_image = np.array(extracted_image.getdata())
    plt.hist(histogram_extracted_image.ravel(),256,(0,256))
    plt.show()

    res = Compare(im2,extracted_image)
    print(res)

main()