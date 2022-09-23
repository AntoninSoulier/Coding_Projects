from msilib.schema import Directory
from threading import stack_size
from Segment import Segment
from TwoDPoint import TwoDPoint
from Polygon import Polygon
import tkinter as tk

pointA = TwoDPoint(0,0)
pointB = TwoDPoint(0,5)
pointC = TwoDPoint(1,3)

segment1 = Segment(pointA, pointB)
segment2 = Segment(pointA, pointC)

#Function orientation

def orientation(segment1, segment2):
    res = 0
    x1 = segment1.get_B().get_x() - segment1.get_A().get_x()
    y1 = segment1.get_B().get_y() - segment1.get_A().get_y()
    x2 = segment2.get_B().get_x() - segment2.get_A().get_x()
    y2 = segment2.get_B().get_y() - segment2.get_A().get_y()
    #determinant
    det = x1*y2 - x2*y1 
    
    if(det>0):
        res = 1
    return res
    
def orientation_point(arete, point):
    res = 0
    x1 = arete.get_A().get_x() - point.get_x()
    y1 = arete.get_A().get_y() - point.get_y()
    
    x2 = arete.get_B().get_x() - point.get_x()
    y2 = arete.get_B().get_y() - point.get_y()

    det = x1*y2 - x2*y1
    if(det>0):
        res = 1
    return res

liste_points = []
liste_segment = []
liste_inside = []

#Fonction qui creer les points entré par l'utilisateur
def clique(event):
    X = event.x
    Y = event.y
    r = 5
    surface.create_rectangle(X-r,Y-r,X+r,Y+r,outline = 'black', fill = 'black')
    point = TwoDPoint(X,Y)
    if(len(liste_points) != 0):
        value = liste_points[-1]
        surface.create_line(value.get_x(), value.get_y(), X, Y, width = 2)
    liste_points.append(point)
    
def point(event):
    X = event.x
    Y = event.y
    r = 5
    surface.create_oval(X-r,Y-r,X+r,Y+r, outline = 'black', fill='black')
    point = TwoDPoint(X,Y)
    liste_inside.append(point)
    isInside()
    
#Création des segments à partir des points
def Create_Segment():

    surface.create_line(liste_points[0].get_x(), liste_points[0].get_y(), liste_points[-1].get_x(), liste_points[-1].get_y())
    for i in range(len(liste_points)):
        if(i != len(liste_points) - 1):
            segment = Segment(liste_points[i], liste_points[i+1])
            liste_segment.append(segment)
        else:
            segment = Segment(liste_points[i], liste_points[0])
            liste_segment.append(segment)

def isConvex():

    convexe = True
    if(len(liste_segment) == 0):
        print("Segment non crées!")
    else:
        for i in range(len(liste_segment)):
            if(i != len(liste_segment)-1):
                if(orientation(liste_segment[i], liste_segment[i+1])==0):
                    convexe = False
            else:
                if(orientation(liste_segment[i],liste_segment[0])==0):
                    convexe = False
        print("\nConvexe: " + str(convexe))
        
    if(convexe==True):
        #Methode pour recupérer la valeur du point avec le clic droit
        surface.bind('<Button-3>', point)
        surface.pack(padx = 5, pady = 5)

def isInside():
    res = 0
    for segment in  liste_segment:
        if(orientation_point(segment, liste_inside[-1]) == 1):
            res += 1
    if((res == len(liste_segment)) or (res==0)):
        print("Le point est à l'intérieur du polygone.")
    else:
        print("Le point est à l'exterieur du polygone.")

#Dimension fenêtre
LARGEUR = 480
HAUTEUR = 320

#Création de la fenêtre
geo_app = tk.Tk()
geo_app.title("Application géometrique")

#Création d'une zone graphique
surface = tk.Canvas(geo_app, width=LARGEUR, height=HAUTEUR, bg="white")
surface.pack(padx = 5, pady = 5)

#Méthode bind permet de lier le clique gauche à la fonction clique
surface.bind('<Button-1>', clique)
surface.pack(padx = 5, pady = 5)

#Permet de valider l'input des points
tk.Button(geo_app, text = 'Valider les points', command = Create_Segment).pack(side='left')

#Permet de checker la convexité du polygone
tk.Button(geo_app, text = 'Convex', command = isConvex).pack(side='left')

#Permet de quitter la fenêtre
tk.Button(geo_app, text = 'Quitter', command = geo_app.destroy).pack(side='right')

geo_app.mainloop()


#Convex Hull

#Dimension fenêtre
LARGEUR = 300
HAUTEUR = 300

#Création de la fenêtre
geo_app = tk.Tk()
geo_app.title("Convex Hull")

#Création d'une zone graphique
surface = tk.Canvas(geo_app, width=LARGEUR, height=HAUTEUR, bg="white")
surface.pack(padx = 5, pady = 5)

import random 

lst_pts = []
lst_smg = []
lst_smg_hull = []

def CreateRandomPoints():
    for  i in range(10):
        r = 5
        x = random.randint(10,250)
        y = random.randint(10,250)
        p = TwoDPoint(x,y)
        lst_pts.append(p) 
        surface.create_oval(x-r,y-r,x+r,y+r, outline = 'black', fill='black')

def ExtremeEdges():
    for point in lst_pts:
        for points in lst_pts[:lst_pts.index(point)] + lst_pts[lst_pts.index(point)+1:]:
            segment = Segment(point,points)
            lst_smg.append(segment)
    
    for segment in lst_smg:
        res = 0
        for point in lst_pts:
            if(orientation_point(segment,point) == 1):
                res+=1
        if(res == len(lst_pts)-2):
            lst_smg_hull.append(segment)

    for s in lst_smg_hull:
        s.display_segment()
        surface.create_line(s.get_A().get_x(),s.get_A().get_y(),s.get_B().get_x(),s.get_B().get_y())
        
def Jarvis():
    #Point le plus à gauche
    a = min(lst_pts, key=lambda point: point.get_x())
    index = lst_pts.index(a)

    #Selection des points du ConvexHall
    l = index
    res = []
    res.append(a)

    while(True):
        q = (l+1) % len(lst_pts)
        for i in range(len(lst_pts)):
            if(i==l):
                continue
            s = Segment(lst_pts[l],lst_pts[i])
            if(orientation_point(s,lst_pts[q])==1):
                q = i
        l = q
        if(l == index):
            break
        res.append(lst_pts[q])
    
    #Relier les points du ConvexHall par des lignes
    for i in range(len(res)): 
        if(i != len(res)-1):
            surface.create_line(res[i].get_x(),res[i].get_y(),res[i+1].get_x(),res[i+1].get_y())
        else:
            surface.create_line(res[-1].get_x(), res[-1].get_y(), res[0].get_x(), res[0].get_y())

def Graham():
    #Find y smallest coordinate
    p0 = min(lst_pts, key=lambda point: point.get_y())
    index = lst_pts.index(p0)

    lst_pts[0], lst_pts[index] = lst_pts[index], lst_pts[0]
    sorted_polar = sorted(lst_pts[1:], cmp = lambda p1, p2: orientation_point(Segment(p1,p2),p0))

    remove = []
    for i in range(len(sorted_polar) -1):
        s = Segment(sorted_polar[i],sorted_polar[i+1])
        if(orientation_point(s,p0)==0):
            remove.append(i)
    sorted_polar = [i for j, i in enumerate(sorted_polar) if j not in remove]
    
    m = len(sorted_polar)
    if(m<2):
        print("Convex hull is empty")
    else:
        stack = []
        stack_size = 0
        stack.append(lst_pts[0])
        stack.append(sorted_polar[0])
        stack.append(sorted_polar[1])
        stack_size = 3

        for i in range(2,m):
            while(True):
                s = Segment(stack[stack_size-2], stack[stack_size-1])
                if(orientation_point(s,sorted_polar[i])==0):
                    break
                else:
                    stack.pop()
                    stack_size -= 1
            stack.append(sorted_polar[i])
            stack_size += 1

CreateRandomPoints()

#Selectionner la méthode Extreme Edges
tk.Button(geo_app, text = 'Extreme Edges', command = ExtremeEdges).pack(side='left')

#Selectionner la méthode Jarvis
tk.Button(geo_app, text = 'Jarvis', command = Jarvis).pack(side='left')

#Selectionner la méthode Jarvis
tk.Button(geo_app, text = 'Graham', command = Jarvis).pack(side='left')

#Permet de quitter la fenêtre
tk.Button(geo_app, text = 'Quitter', command = geo_app.destroy).pack(side='right')

geo_app.mainloop()
                  

