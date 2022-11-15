import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
#import matplotlib.pyplot as plt
import math

def histo(img) :
    # Création de l'histogramme
    plt.hist(img.ravel(),256,[0,256])
    plt.show()


def histoColor(img):
    img = cv2.imread(img)
    color = ('b','g','r')
    # Pour chaque couleur, création de l'histogramme
    for i,col in enumerate(color):
        histr = cv2.calcHist([img],[i],None,[256],[0,256])
        plt.plot(histr,color = col)
        plt.xlim([0,256])
    plt.show()


def MergeGreyImages(initial,secret,result) :
    # Lecture des images
    imgInit = cv2.imread(initial, cv2.IMREAD_GRAYSCALE)
    imgSecret = cv2.imread(secret, cv2.IMREAD_GRAYSCALE)
    
    # Création de l'image résultat
    imgF = np.zeros([len(imgInit), len(imgInit[0])])

    for i in range(len(imgInit)) :
        for j in range(len(imgInit[0])) :
            # On récupère les pixels
            pS = imgInit[i][j]
            pL = imgSecret[i][j]
            #On transforme les pixels en octet
            pS = "{0:08b}".format(pS)
            pL = "{0:08b}".format(pL)
            #On fusionne les bits de poids forts
            pR = int(pS[0:4]+pL[0:4],2)
            imgF[i][j] = pR

    # Création et sauvegarde de l'image
    im_pil = Image.fromarray(imgF)
    im_pil = im_pil.convert('L')
    im_pil.show()
    im_pil.save(result)
    
    histo(imgSecret)
    
    
def MergeColoredImages(initial,secret,result) :
    # Lecture des images
    imgInit = cv2.imread(initial,3)
    b,g,r = cv2.split(imgInit)
    imgInit = cv2.merge([r,g,b])

    imgSecret = cv2.imread(secret)
    b,g,r = cv2.split(imgSecret)
    imgSecret = cv2.merge([r,g,b])

    # Création de l'image résultat
    imgF = np.zeros([len(imgInit), len(imgInit[0]),3])

    for i in range(len(imgInit)) :
        for j in range(len(imgInit[0])) :
            for k in range(3) :
                # On récupère les pixels pour chaque canaux
                pS = imgInit[i][j][k]
                pL = imgSecret[i][j][k]
                # On transforme les pixels en octet
                pS = "{0:08b}".format(pS)
                pL = "{0:08b}".format(pL)
                #On fusionne les bits de poids forts
                pR = int(pS[0:4]+pL[0:4],2)
                imgF[i][j][k] = pR
                
    # Création et sauvegarde de l'image
    im_pil = Image.fromarray(imgF.astype(np.uint8))
    im_pil.show()
    im_pil.save(result)
    
    histoColor(secret)
    
    
    
def SeparateGreyImages(toSeparate,secret) :
    # Lecture des images
    imgR = cv2.imread(toSeparate, cv2.IMREAD_GRAYSCALE)
    imgF = np.zeros([len(imgR), len(imgR[0])])

    for i in range(len(imgR)) :
        for j in range(len(imgR[0])) :
            # On récupère le pixel
            p = imgR[i][j]
            # On le transforme en octet
            p = "{0:08b}".format(p)
            # On récupère le bit de poids faible
            pR = int(p[4:8]+"0000",2)
            imgF[i][j] = pR
            
    # Création et sauvegarde de l'image
    im_pil = Image.fromarray(imgF)
    im_pil = im_pil.convert('L')
    im_pil.show()
    im_pil.save(secret)
    imgF = imgF.astype(np.uint8)
    histo(imgF)
    
    
    
def SeparateColoredImages(toSeparate,secret) :
    # Lecture des images
    imgR = cv2.imread(toSeparate)
    b,g,r = cv2.split(imgR)
    imgR = cv2.merge([r,g,b])

    # Création de l'image résultat
    imgF = np.zeros([len(imgR), len(imgR[0]),3])

    for i in range(len(imgR)) :
        for j in range(len(imgR[0])) :
            for k in range(3) :
                # On récupère le pixel pour chaque canaux
                p = imgR[i][j][k]
                # On transforme le pixel en octet
                p = "{0:08b}".format(p)
                # On fusionne les bits de poids forts
                pR = int(p[4:8]+"0000",2)
                imgF[i][j][k] = pR
            
    # Création et sauvegarde de l'image
    im_pil = Image.fromarray(imgF.astype(np.uint8))
    im_pil.show()
    im_pil.save(secret)
    
    histoColor(secret)
    
def compareTwoGreyImages(name1,name2) :
    # Lecture des images
    img1 = cv2.imread(name1, cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread(name2, cv2.IMREAD_GRAYSCALE)

    res = 0
    # Intensité maximale
    max = np.amax(img1)
    for i in range(len(img1)) :
        for j in range(len(img1[0])) :
            # On récupère les pixels
            p1 = img1[i][j]
            p2 = img2[i][j]
            # On calcule l'erreur de chaque pixel
            er = math.pow(int(p1)-int(p2),2)
            res +=er
    # On divise par le nombre de pixel
    res = res/img1.size
    # On divise par max
    res = res/max
    return str(round(res*100,2))  + " %"
    
    
def compareTwoColoredImages(name1,name2) :
    # Lecture des images
    img1 = cv2.imread(name1)
    b,g,r = cv2.split(img1)
    img1 = cv2.merge([r,g,b])
    
    img2 = cv2.imread(name2)
    b,g,r = cv2.split(img2)
    img2 = cv2.merge([r,g,b])
    
    res = 0
    # Intensité maximale
    max = np.amax(img1)
    for i in range(len(img1)) :
        for j in range(len(img1[0])) :
            er3 = 0
            for k in range(3) :
                # On récupère les pixels
                p1 = img1[i][j][k]
                p2 = img2[i][j][k]
                # On calcule l'erreur de chaque pixel
                er = math.pow(int(p1)-int(p2),2)
                er3 += er
            res +=er3
    # On divise par le nombre de pixel
    res = res/img1.size
    # On divise par max
    res = res/max
    return str(round(res*100,2))  + " %"
            

#Grey Images

initialGrey = "pepper.bmp"
secretGrey = "lena.jpg"
mergedGrey = "mergedGrey.png"

MergeGreyImages(initialGrey,secretGrey,mergedGrey)

extractedGrey = "extractGrey.png"

SeparateGreyImages(mergedGrey,extractedGrey)

EMQRGrey = compareTwoGreyImages(secretGrey,extractedGrey)
print("EQM relative : " + EMQRGrey)

#Colored Images 

initialColor = "pepper.bmp"
secretColor = "clown.bmp"
mergedColor = "mergedColor.png"

MergeColoredImages(initialColor,secretColor,mergedColor)

extractedColor = "extractColor.png"

SeparateColoredImages(mergedColor,extractedColor)

EMQRColor = compareTwoColoredImages(secretColor,extractedColor)
print("EQM relative : " + EMQRColor)