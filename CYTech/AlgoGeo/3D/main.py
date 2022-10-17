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
l.print()
print(" ")
matrice1.mat_vec_mul(l).print()

#Affichage

import pygame 
WINDOW_SIZE = 800
window = pygame.display.set_mode( (WINDOW_SIZE,WINDOW_SIZE) )
clock = pygame.time.Clock()

projection_matrix = mat4(vec4(1,0,0,0),vec4(0,1,0,0),vec4(0,0,1,0),vec4(0,0,0,1))

cube_points = [n for n in range(8)]
cube_points[0] = vec4(-1,-1,1,1)
cube_points[1] = vec4(1,-1,1,1)
cube_points[2] = vec4(1,1,1,1)
cube_points[3] = vec4(-1,1,1,1)

cube_points[4] = vec4(-1,-1,-1,1)
cube_points[5] = vec4(1,-1,-1,1)
cube_points[6] = vec4(1,1,-1,1)
cube_points[7] = vec4(-1,1,-1,1)

print(cube_points)

def multiply_m(a, b):
    a_rows = len(a)
    a_cols = len(a[0])

    b_rows = len(b)
    b_cols = len(b[0])
    product = [[0 for _ in range(b_cols)] for _ in range(a_rows)]

    if a_cols == b_rows:
        for i in range(a_rows):
            for j in range(b_cols):
                for k in range(b_rows):
                    product[i][j] += a[i][k] * b[k][j]
    else:
        print("Taille des matrices incompatibles")
    return product  

def connect_points(i,j,points):
    pygame.draw.line(window, (255,255,255), (points[i][0], points[i][1]), (points[j][0], points[j][1]))

angle_x = angle_y = angle_z = 0
sc = 1
res = 1

while(True):

    clock.tick(60)
    window.fill((0,0,0))

    rotation_x = mat4(vec4(1,0,0,0),vec4(0, cos(angle_x), sin(angle_x),0),vec4(0, -sin(angle_x), cos(angle_x),0),vec4(0,0,0,1))

    rotation_y = mat4(vec4(cos(angle_y), 0, -sin(angle_y),0),vec4(0, 1, 0, 0),vec4(sin(angle_y), 0, cos(angle_y),0),vec4(0,0,0,1))

    rotation_z = mat4(vec4(cos(angle_z), sin(angle_z), 0, 0),vec4(-sin(angle_z), cos(angle_z), 0, 0),vec4(0,0,1,0),vec4(0,0,0,1))
                
    scale_matrix = mat4(vec4(sc,0,0,0),vec4(0,sc,0,0),vec4(0,0,sc,0),vec4(0,0,0,sc)) 
    
    points = [0 for _ in range(len(cube_points))]
    i=0
    for point in cube_points:

        #Rotate point
        rotate_x = rotation_x.mat_vec_mul(point)
        rotate_y = rotation_y.mat_vec_mul(rotate_x)
        rotate_z = rotation_z.mat_vec_mul(rotate_y)
        
        #Scale point
        scaled_point = scale_matrix.mat_vec_mul(rotate_z)

        #Remove coordinate z (create 2d point)
        point_2d = projection_matrix.mat_vec_mul(scaled_point)

        x = (point_2d.get_x() * 100) + WINDOW_SIZE/2
        y = (point_2d.get_y() * 100) + WINDOW_SIZE/2
        points[i] = (x,y)
        i += 1
        pygame.draw.circle(window, (0,0,255), (x,y), 4) 
    
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
        if(keys[pygame.K_p]):
            sc += 0.01
        if(keys[pygame.K_m]):
            sc -= 0.01

    pygame.display.update()
