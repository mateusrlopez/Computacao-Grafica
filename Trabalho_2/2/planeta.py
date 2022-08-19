from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from math import sin, cos, pi
from sys import argv
from png import Reader

alpha = 10.0
beta = 0.0

bg_color = (0.05, 0.05, 0.1, 1)

n = 60
m = 60
radius = 1.5

def s_func(phi):
    return (phi / (2 * pi))

def t_func(theta):
    return ((theta + (pi / 2)) / pi)

def structure(i,j):
    theta = ((pi * i) / (n - 1)) - (pi / 2)
    phi = 2 * pi * j / (m - 1)
    
    x = radius * cos(theta) * cos(phi)
    y = radius * sin(theta)
    z = radius * cos(theta) * sin(phi)
    
    s = s_func(phi)

    t = t_func(theta)
    
    return x,y,z,s,t


texture = []

def load_textures():
    global texture
    texture = glGenTextures(2)

    mapa = Reader(filename='./mapa.png')

    w, h, pixels, metadata = mapa.read_flat()

    if(metadata['alpha']):
        modo = GL_RGBA
    else:
        modo = GL_RGB

    glBindTexture(GL_TEXTURE_2D, texture[0])
    glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
    glTexImage2D(GL_TEXTURE_2D, 0, modo, w, h, 0, modo, GL_UNSIGNED_BYTE, pixels.tolist())
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)


def figure():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)    
    glLoadIdentity()    
    glPushMatrix()
  
    glRotatef(alpha, 0.0, 1.0, 0.0)
    glRotatef(beta, 0.0, 0.0, 1.0)
    glBindTexture(GL_TEXTURE_2D, texture[0])

    for i in range(n):
        glBegin(GL_QUAD_STRIP)

        for j in range(m):
            x, y, z, s, t = structure(i,j)
            glTexCoord2f(s, t)
            glVertex3f(x,y,z)

            x, y, z, s, t = structure(i + 1, j)
            glTexCoord2f(s, t)
            glVertex3f(x,y,z)
        glEnd()

    glPopMatrix()
    glutSwapBuffers()

def draw():
    global alpha
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    figure()
    alpha += 0.3
    glutSwapBuffers()

def timer(i):
    glutPostRedisplay()
    glutTimerFunc(10, timer, 1)

def main():    
    glutInit(argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)

    screen_width = glutGet(GLUT_SCREEN_WIDTH)
    screen_height = glutGet(GLUT_SCREEN_HEIGHT)

    width = round(2 * screen_width / 3)
    height = round(2 * screen_height / 3)

    glutInitWindowSize(width, height)
    glutInitWindowPosition(round((screen_width - width) / 2), round((screen_height - height) / 2))
    glutCreateWindow("Textura - Planeta")
    glutDisplayFunc(draw)

    load_textures()

    glEnable(GL_MULTISAMPLE)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_TEXTURE_2D)

    glClearColor(*bg_color)
    glClearDepth(1.0)
    glDepthFunc(GL_LESS)

    glShadeModel(GL_SMOOTH)
    glMatrixMode(GL_PROJECTION)

    gluPerspective(-35, width / height, 0.1, 100.0)
    glTranslatef(0.0, 0.0, -10)

    glMatrixMode(GL_MODELVIEW)

    glutTimerFunc(5, timer, 1)
    glutMainLoop()

main()