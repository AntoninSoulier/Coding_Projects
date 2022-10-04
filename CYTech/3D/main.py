from lib2to3 import pygram
from Vector3 import vec3
from Vector4 import vec4
from mat4 import mat4
from math import *

v = vec3(3,4,5)
w = vec3(2,1,0)

s = vec4(0,1,1,1)
b = vec4(1,1,1,0)
c = vec4(1,0,1,1)
m = vec4(0,1,0,1)

v1 = vec4(6,1,2,4)
v2 = vec4(8,5,1,0)
v3 = vec4(6,6,7,3)
v4 = vec4(4,3,2,1)

l = vec4(1,3,2,2)

matrice1 = mat4(s,b,c,m)
matrice2 = mat4(v1,v2,v3,v4)

matrice1.print()
print(" ")

matrice1.mat_mat_mul(matrice2).print()

print(" ")
matrice1.inv().print()

#Affichage

import pygame 
WINDOW_SIZE = 800
window = pygame.display.set_mode( (WINDOW_SIZE,WINDOW_SIZE) )
clock = pygame.time.Clock()

projection_matrix = [[1,0,0],
                     [0,1,0],
                     [0,0,0]]

cube_points = [n for n in range(8)]
cube_points[0] = [[-1], [-1], [1]]
cube_points[1] = [[1], [-1], [1]]
cube_points[2] = [[1], [1], [1]]
cube_points[3] = [[-1], [1], [1]]

cube_points[4] = [[-1], [-1], [-1]]
cube_points[5] = [[1], [-1], [-1]]
cube_points[6] = [[1], [1], [-1]]
cube_points[7] = [[-1], [1], [-1]]

def multiply_m(a, b):
    a_rows = len(a)
    a_cols = len(a[0])

    b_rows = len(b)
    b_cols = len(b[0])
    # Dot product matrix dimentions = a_rows x b_cols
    product = [[0 for _ in range(b_cols)] for _ in range(a_rows)]

    if a_cols == b_rows:
        for i in range(a_rows):
            for j in range(b_cols):
                for k in range(b_rows):
                    product[i][j] += a[i][k] * b[k][j]
    else:
        print("INCOMPATIBLE MATRIX SIZES")
    return product  

def connect_points(i,j,points):
    pygame.draw.line(window, (255,255,255), (points[i][0], points[i][1]), (points[j][0], points[j][1]))

scale = 100
angle_x = angle_y = angle_z = 0

while(True):
    clock.tick(60)
    window.fill((0,0,0))
    rotation_x = [[1, 0, 0],
                    [0, cos(angle_x), -sin(angle_x)],
                    [0, sin(angle_x), cos(angle_x)]]

    rotation_y = [[cos(angle_y), 0, sin(angle_y)],
                    [0, 1, 0],
                    [-sin(angle_y), 0, cos(angle_y)]]

    rotation_z = [[cos(angle_z), -sin(angle_z), 0],
                    [sin(angle_z), cos(angle_z), 0],
                    [0, 0, 1]]
    
    points = [0 for _ in range(len(cube_points))]
    i=0
    for point in cube_points:
        
        rotate_x = multiply_m(rotation_x, point)
        rotate_y = multiply_m(rotation_y, rotate_x)
        rotate_z = multiply_m(rotation_z, rotate_y)

        point_2d = multiply_m(projection_matrix,rotate_z)
       
        x = (point_2d[0][0] * scale) + WINDOW_SIZE/2
        y = (point_2d[1][0] * scale) + WINDOW_SIZE/2
        print("[",x,",",y,"]")
        points[i] = (x,y)
        i += 1
        pygame.draw.circle(window, (255,0,0), (x,y), 3) 

    connect_points(0, 1, points)
    connect_points(0, 3, points)
    connect_points(0, 4, points)
    connect_points(1, 2, points)
    connect_points(1, 5, points)
    connect_points(2, 6, points)
    connect_points(2, 3, points)
    connect_points(3, 7, points)
    connect_points(4, 5, points)
    connect_points(4, 7, points)
    connect_points(6, 5, points)
    connect_points(6, 7, points)
        
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            pygame.quit()
        
        keys = pygame.key.get_pressed()
        if(keys[pygame.K_r]):
            angle_x = angle_y = angle_z = 0
        if(keys[pygame.K_z]):
            angle_y += 0.05
        if(keys[pygame.K_d]):
            angle_x += 0.05
        if(keys[pygame.K_q]):
            angle_z += 0.05

    pygame.display.update()
