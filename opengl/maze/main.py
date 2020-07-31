from OpenGL.GL import *
from OpenGL.GLU import *

import pygame
import os

from pygame.locals import *
from maze.MeshRenderer import ChairMesh

os.environ["SDL_VIDEO_CENTERED"]='1'





def main():
    pygame.init()
    display = (1500, 1080)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(80, (display[0]/display[1]), 0.1, 40.0)
    glTranslatef(0.0, 0.0, -20)
    glRotatef(100, -10, 0, -10)


def controls():
    keys = pygame.key.get_pressed()
    axis = True
    speed = 10
    if keys[pygame.K_LEFT]:
        glRotatef(speed, 0, axis, 0)
    if keys[pygame.K_RIGHT]:
        glRotatef(speed, 0, -axis, 0)
    if keys[pygame.K_UP]:
        glRotatef(speed, axis, 0, 0)
    if keys[pygame.K_DOWN]:
        glRotatef(speed, -axis, 0, 0)


main()
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    controls()


    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    ChairMesh()
    pygame.display.flip()
    pygame.time.wait(10)
pygame.quit()
quit()
