from TwoDPoint import TwoDPoint
from Arete import Arete
from Triangle import Triangle

import tkinter as tk
from tkinter import *

import math

def orientation(arete, point):
    res = 0
    x1 = arete.get_point1().get_x() - point.get_x()
    y1 = arete.get_point1().get_y() - point.get_y()
    
    x2 = arete.get_point2().get_x() - point.get_x()
    y2 = arete.get_point2().get_y() - point.get_y()

    det = x1*y2 - x2*y1
    if(det>0):
        res = 1
    return res

liste_point = []
liste_triangle = []
liste_arete = []

def create_points(event):
    X = event.x
    Y = event.y
    r=5
    surface.create_oval(X-r,Y-r,X+r,Y+r, outline = 'black', fill='black')
    point = TwoDPoint(X,Y)
    if(len(liste_point)!=0):
        arete = Arete(liste_point[-1], point)
        liste_arete.append(arete)
        value = liste_point[-1]
        surface.create_line(value.get_x(), value.get_y(), X, Y, width=2)        

    liste_point.append(point)

def isInside(point):
    res = 0
    for arete in  liste_arete:
        if(orientation(arete, point) == 1):
            res += 1
    if((res == len(liste_arete)) or (res==0)):
        return True

def NaiveTriangulation():
    point = liste_point[0]
    for i in range(1,len(liste_point)):
        surface.create_line(point.get_x(), point.get_y(), liste_point[i].get_x(), liste_point[i].get_y())
    for i in range(1,len(liste_point)-1):
        arete1 = Arete(point, liste_point[i])
        arete2 = Arete(liste_point[i], liste_point[i+1])
        arete3 = Arete(liste_point[i+1], point)
        triangle = Triangle(arete1,arete2,arete3)
        liste_triangle.append(triangle)

def FindTriangle(point):
    
    for triangle in liste_triangle:
        liste_arete = []
        arete1 = triangle.get_arete1()
        liste_arete.append(arete1)
        arete2 = triangle.get_arete2()
        liste_arete.append(arete2)
        arete3 = triangle.get_arete3()
        liste_arete.append(arete3)
    
        res = 0
        for arete in liste_arete:
            if(orientation(arete,point) == 1):
                res+=1
        if(res == 3):
            return(triangle)

def InsertPoint(triangle, point):

    arete1 = triangle.get_arete1()
    arete2 = triangle.get_arete2()
    arete3 = triangle.get_arete3()

    surface.create_line(arete1.get_point1().get_x(), arete1.get_point1().get_y(), point.get_x(), point.get_y())
    surface.create_line(arete2.get_point1().get_x(), arete2.get_point1().get_y(), point.get_x(), point.get_y())
    surface.create_line(arete3.get_point1().get_x(), arete3.get_point1().get_y(), point.get_x(), point.get_y())

def last_line():
    surface.create_line(liste_point[-1].get_x(),liste_point[-1].get_y(), liste_point[0].get_x(),liste_point[0].get_y())

def newTriangle(t,p):

    arete1 = t.get_arete1()
    arete2 = Arete(arete1.get_point2(), p)
    arete3 = Arete(p, arete1.get_point1())
    triangle = Triangle(arete1,arete2,arete3)
    liste_triangle.append(triangle)

    arete1 = t.get_arete2()
    arete2 = Arete(arete1.get_point2(), p)
    arete3 = Arete(p, arete1.get_point1())
    triangle = Triangle(arete1,arete2,arete3)
    liste_triangle.append(triangle)

    arete1 = t.get_arete3()
    arete2 = Arete(arete1.get_point2(), p)
    arete3 = Arete(p, arete1.get_point1())
    triangle = Triangle(arete1,arete2,arete3)
    liste_triangle.append(triangle)
    
    i = liste_triangle.index(t)
    del liste_triangle[i]


def Delauney_Test(t,p):
    x1 = t.get_arete1().get_point1().get_x() - p.get_x()
    x2 = t.get_arete1().get_point1().get_y() - p.get_x()
    x3 = t.get_arete2().get_point2().get_x() - p.get_x()

    y1 = t.get_arete1().get_point1().get_y() - p.get_y()
    y2 = t.get_arete1().get_point2().get_y() - p.get_y()
    y3 = t.get_arete2().get_point2().get_y() - p.get_y()

    z1 = math.pow(x1,2) + math.pow(y1,2)
    z2 = math.pow(x2,2) + math.pow(y2,2)
    z3 = math.pow(x3,2) + math.pow(y3,2)

    det = x1*y2*z3 + x2*y3*z1 + y1*z2*x3 - (x3*y2*z1 + x2*y1*z3 + x1*y3*z2)
    if(det>0):
        print("p is inside")
    elif(det<0):
        print("p is outside")

def selectionner_point(event):
    X = event.x
    Y = event.y
    r=3
    p = TwoDPoint(X,Y)

    #Je créer le segment qui relie le dernier point au premier
    arete = Arete(liste_point[-1], liste_point[0])
    liste_arete.append(arete)
    
    if(isInside(p) == True):
        surface.create_oval(X-r,Y-r,X+r,Y+r, outline = 'black', fill='black')
        t = FindTriangle(p)
        InsertPoint(t, p)
        #Delauney_Test(t,p)
        newTriangle(t,p)
   

                                #Interface graphique 
#dimension fenêtre
LARGEUR = 480
HAUTEUR = 320

#Création de la fenêtre
triangle_app = tk.Tk()
triangle_app.title("Application Triangle")

#Création d'une zone graphique
surface = tk.Canvas(triangle_app, width=LARGEUR, height=HAUTEUR, bg="white")
surface.pack(padx = 5, pady = 5)

#Méthode bind permet de lier le clique gauche à la fonction clique
surface.bind('<Button-1>', create_points)
surface.pack(padx = 5, pady = 5)

#Méthode pour valider les points
tk.Button(triangle_app, text = 'Valider Points', command = last_line).pack(side='left')

#Méthode pour effectuer la triangulation naive
tk.Button(triangle_app, text = 'Naive', command = NaiveTriangulation).pack(side='left')

#Methode pour recupérer la valeur du point avec le clic droit
surface.bind('<Button-3>', selectionner_point)
surface.pack(padx = 5, pady = 5)

#Permet de valider l'input et quitter la fenêtre
tk.Button(triangle_app, text = 'Quitter', command = triangle_app.destroy).pack(side='right')

triangle_app.mainloop()




