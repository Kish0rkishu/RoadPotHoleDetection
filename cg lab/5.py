import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

display_width = 800
display_height = 600

display  = pygame.display.set_mode((display_width,display_height),DOUBLEBUF|OPENGL)
pygame.display.set_caption("3D Transformation")

glClearColor(0.0,0.0,0.0,1.0)
glEnable(GL_DEPTH_TEST)
glMatrixMode(GL_PROJECTION)
gluPerspective(45,(display_width/display_height),0.1,50.0)
glMatrixMode(GL_MODELVIEW)

vertex = np.array([
    [-1,-1,-1],
    [1,-1,-1],
    [1,1,-1],
    [-1,1,-1],
    [-1,-1,1],
    [1,-1,1],
    [1,1,1],
    [-1,1,1]

],dtype=np.float32)

edges = np.array([
    [0,1],[1,2],[2,3],[3,0],
    [4,5],[5,6],[6,7],[7,4],
    [0,4],[1,5],[2,6],[3,7]
],dtype=np.uint32)

trans_matrix = np.eye(4,dtype=np.float32)
trans_matrix[3,:3] = [0,0,-5]
rota_matrix = np.eye(4,dtype=np.float32)
scal_matrix = np.eye(4,dtype=np.float32)
scal_matrix[0,0]=1.5
scal_matrix[1,1]=1.5
scal_matrix[2,2]=1.5

runnuing = True
angle = 0
while runnuing:
    for event  in pygame.event.get():
        if event.type == pygame.QUIT:
            runnuing = False
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glMultMatrixf(trans_matrix)
    glRotatef(angle,90,0,0)
    glMultMatrixf(rota_matrix)
    glMultMatrixf(scal_matrix)

    glBegin(GL_LINES)
    for edge in edges:
        for vertex_index in edge:
            glVertex3fv(vertex[vertex_index])
    glEnd()

    angle += 1

    pygame.display.flip()
    pygame.time.wait(10)
pygame.quit()