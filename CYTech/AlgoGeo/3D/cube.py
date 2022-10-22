from Vector4 import vec4
from mat4 import mat4
from math import *
import pygame

pygame.init()
WINDOW_SIZE = 800
window = pygame.display.set_mode( (WINDOW_SIZE,WINDOW_SIZE))
clock = pygame.time.Clock()

cube_points = [n for n in range(8)]
triangle_points = [n for n in range(4)]

#Points du cube
cube_points[0] = vec4(0,0,0,1)
cube_points[1] = vec4(1,0,0,1)
cube_points[2] = vec4(1,1,0,1)
cube_points[3] = vec4(0,1,0,1)
cube_points[4] = vec4(0,0,1,1)
cube_points[5] = vec4(1,0,1,1)
cube_points[6] = vec4(1,1,1,1)
cube_points[7] = vec4(0,1,1,1)

#Points du triangle
triangle_points[0] = vec4(0,0,0,1)
triangle_points[1] = vec4(1,0,0,1)
triangle_points[2] = vec4(0.5,1,0,1)
triangle_points[3] = vec4(0.5,0.5,1,1)

viewport_matrix = mat4(
                       vec4(800/2,0,0,0),
                       vec4(0,800/2,0,0),
                       vec4(0,0,(0.75-0.25)/2,0),
                       vec4(800/4,800/4,1/2,1)
                       )

ortographic_projection_matrix = mat4(
                                    vec4(2/10,0,0,0),
                                    vec4(0,2/10,0,0),
                                    vec4(0,0,-2/(0.75-0.25),0),
                                    vec4(-30/10,-30/10,-(0.75+0.25)/0.75-0.25,1)
                                    )

perspective_projection_matrix = mat4(
                                    vec4(2*0.25/10,0,0,0),
                                    vec4(0,2*0.25/10,0,0),
                                    vec4(30/10,30/10,(0.75+0.25)/0.25-0.75,-1),
                                    vec4(0,0,2*0.75*0.25/0.25-0.75,0)
                                    )

angle_x = angle_y = angle_z = 0.0
tx = ty = tz = 0.0
sc = 1.0
res = 1
teta = 0
carre = False
triangle = False

while(True):
    
    font = pygame.font.Font('freesansbold.ttf', 15)
    text1 = font.render("Tx = "+str(tx), True, (255,255,255), (0,0,0))
    textRect = text1.get_rect()
    textRect.center = (50, 20)

    clock.tick(60)
    window.fill((0,0,0))
    window.blit(text1,textRect)

    #Roll
    rotation_x = mat4(
                        vec4(1,0,0,0),
                        vec4(0, cos(angle_x), sin(angle_x),0),
                        vec4(0, -sin(angle_x), cos(angle_x),0),
                        vec4(0,0,0,1)
                    )
    #Pitch
    rotation_y = mat4(
                        vec4(cos(angle_y), 0, -sin(angle_y),0),
                        vec4(0, 1, 0, 0),
                        vec4(sin(angle_y), 0, cos(angle_y),0),
                        vec4(0,0,0,1)
                    )
    #Yaw
    rotation_z = mat4(
                        vec4(cos(angle_z), sin(angle_z), 0, 0),
                        vec4(-sin(angle_z), cos(angle_z), 0, 0),
                        vec4(0,0,1,0),
                        vec4(0,0,0,1)
                    )
    
    # Roll * Pitch * Yaw
    Euler_matrix = (rotation_x.mat_mat_mul(rotation_y)).mat_mat_mul(rotation_z)

    scale_matrix = mat4(
                        vec4(sc,0,0,0),
                        vec4(0,sc,0,0),
                        vec4(0,0,sc,0),
                        vec4(0,0,0,1)
                    ) 
    
    translation_matrix = mat4(
                              vec4(1,0,0,0),
                              vec4(0,1,0,0),
                              vec4(0,0,1,0),
                              vec4(tx,ty,tz,1)
                            )
    if(carre == True):
        points = [0 for _ in range(len(cube_points))]
        i=0
        for point in cube_points:
            
            #Model Matrix: Translate - Scale - Rotate | Object Coordinate to World Coordinate
            point_2d = translation_matrix.mat_vec_mul(scale_matrix.mat_vec_mul((rotation_z.mat_vec_mul(rotation_y.mat_vec_mul(rotation_x.mat_vec_mul(point)))))) #point_2d = translation_matrix.mat_mat_mul(scale_matrix).mat_mat_mul(rotation_z).mat_mat_mul(rotation_y).mat_mat_mul(rotation_x).mat_vec_mul(point)

            #View Matrix
            pt = viewport_matrix.mat_vec_mul(point_2d)
            
            #Projection Matrix
            p = ortographic_projection_matrix.mat_vec_mul(pt)
            p.print()

            #Récupération des coordonnées x et y
            x = p.get_x()
            y = p.get_y()
            
            points[i] = (x,y)
            i += 1
            pygame.draw.circle(window, (0,0,255), (x,y), 4) 

        def connect_points(i,j,points):
            pygame.draw.line(window, (255,255,255), (points[i][0], points[i][1]), (points[j][0], points[j][1]))  
        
        #Face1
        connect_points(0,4,points)
        connect_points(4,5,points)
        connect_points(5,0,points)
        connect_points(0,5,points)
        connect_points(5,1,points)
        connect_points(1,0,points)

        #Face2
        connect_points(1,5,points)
        connect_points(5,6,points)
        connect_points(6,1,points)
        connect_points(1,6,points)
        connect_points(6,2,points)
        connect_points(2,1,points)

        #Face3
        connect_points(2,6,points)
        connect_points(6,7,points)
        connect_points(7,2,points)
        connect_points(2,7,points)
        connect_points(7,3,points)
        connect_points(3,2,points)

        #Face4
        connect_points(3,7,points)
        connect_points(7,4,points)
        connect_points(4,3,points)
        connect_points(3,4,points)
        connect_points(4,0,points)
        connect_points(0,3,points)
        
        #Face5
        connect_points(5,4,points)
        connect_points(4,7,points)
        connect_points(7,5,points)
        connect_points(5,7,points)
        connect_points(7,6,points)
        connect_points(6,5,points)

        #Face6
        connect_points(1,0,points)
        connect_points(0,3,points)
        connect_points(3,1,points)
        connect_points(1,3,points)
        connect_points(3,2,points)
        connect_points(2,1,points)

    if(triangle == True):
        points = [0 for _ in range(len(triangle_points))]
        i=0
        for point in triangle_points:

            #Rotate point
            rotate_x = rotation_x.mat_vec_mul(point)
            rotate_y = rotation_y.mat_vec_mul(rotate_x)
            rotate_z = rotation_z.mat_vec_mul(rotate_y)
            
            #Scale point
            scaled_point = scale_matrix.mat_vec_mul(rotate_z)

            #translated point
            translated_point = translation_matrix.mat_vec_mul(scaled_point)

            #print(translated_point.get_x(),"",translated_point.get_y(),"",translated_point.get_z(),"",translated_point.get_w())
            
            #Ortographic projection
            point_2d = translated_point

            #Récupération des coordonnées x et y
            x = (point_2d.get_x() * 100) + WINDOW_SIZE/2
            y = (point_2d.get_y() * 100) + WINDOW_SIZE/2
            points[i] = (x,y)
            i += 1
            pygame.draw.circle(window, (0,0,255), (x,y), 4) 

        def connect_points(i,j,points):
            pygame.draw.line(window, (255,255,255), (points[i][0], points[i][1]), (points[j][0], points[j][1]))  

        connect_points(0,1,points)
        connect_points(1,3,points)
        connect_points(3,0,points)

        connect_points(1,2,points)
        connect_points(2,3,points)
        connect_points(3,1,points)

        connect_points(2,0,points)
        connect_points(0,3,points)
        connect_points(3,2,points)

        connect_points(0,1,points)
        connect_points(1,2,points)
        connect_points(2,0,points)

    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            pygame.quit()
        
        keys = pygame.key.get_pressed()
        if(keys[pygame.K_r]):
            angle_x = angle_y = angle_z = tx = ty = tz = 0
            sc = 1
        if(keys[pygame.K_z]):
            angle_y += 0.05
        if(keys[pygame.K_d]):
            angle_x += 0.05
        if(keys[pygame.K_q]):
            angle_z += 0.05
        if(keys[pygame.K_p]):
            sc += 0.05
        if(keys[pygame.K_m]):
            sc -= 0.05
        if(keys[pygame.K_LEFT]):
            tx -= 0.05
        if(keys[pygame.K_RIGHT]):
            tx += 0.05
        if(keys[pygame.K_UP]):
            ty -= 0.05
        if(keys[pygame.K_DOWN]):
            ty += 0.05
        if(keys[pygame.K_h]):
            teta+=0.1
        if(keys[pygame.K_b]):
            triangle = False
            carre = True
        if(keys[pygame.K_n]):
            carre = False
            triangle = True
            
    pygame.display.update()

