from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
import png

window = 0

xrot = 0.0
yrot = 0.0
zrot = 0.0
dx = 1
dy = 1
dz = 1

def LoadTextures():
    global texture
    texture = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture)

    reader = png.Reader(filename = './dado.png')
    w, h, pixels, meta = reader.read_flat()

    glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, w, h, 0, GL_RGB,
                 GL_UNSIGNED_BYTE, pixels.tolist())

    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)

def InitGL(Width, Height):
    LoadTextures()
    glEnable(GL_TEXTURE_2D)
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClearDepth(1.0)
    glDepthFunc(GL_LESS)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(90.0, float(Width)/float(Height), 0.5, 10.0)
    glMatrixMode(GL_MODELVIEW)

def DrawGLScene():
    global xrot, yrot, zrot, dx, dy, dz, texture

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glClearColor(0.5, 0.5, .5, 1.0)
    glTranslatef(0.0, 0.0, -5.0)
    glRotatef(xrot, 1.0, 0.0, 0.0)
    glRotatef(yrot, 0.0, 1.0, 0.0)
    glRotatef(zrot, 0.0, 0.0, 1.0)

    glBindTexture(GL_TEXTURE_2D, texture)
    glBegin(GL_QUADS)

    glTexCoord2f(0.0, 0.0)
    glVertex3f(-1.0, -1.0,  1.0)
    glTexCoord2f(0.0, 1/2)
    glVertex3f(1.0, -1.0,  1.0)
    glTexCoord2f(1/3, 1/2)
    glVertex3f(1.0,  1.0,  1.0)
    glTexCoord2f(1/3, 0.0)
    glVertex3f(-1.0,  1.0,  1.0)

    glTexCoord2f(2/3, 1/2)
    glVertex3f(-1.0, -1.0, -1.0)
    glTexCoord2f(2/3, 1.0)
    glVertex3f(-1.0,  1.0, -1.0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(1.0,  1.0, -1.0)
    glTexCoord2f(1, 1/2)
    glVertex3f(1.0, -1.0, -1.0)

    glTexCoord2f(0.0, 1/2)
    glVertex3f(-1.0,  1.0, -1.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-1.0,  1.0,  1.0)
    glTexCoord2f(1/3, 1.0)
    glVertex3f(1.0,  1.0,  1.0)
    glTexCoord2f(1/3, 1/2)
    glVertex3f(1.0,  1.0, -1.0)

    glTexCoord2f(2/3, 0.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(1.0, -1.0, -1.0)
    glTexCoord2f(1.0, 1/2)
    glVertex3f(1.0, -1.0,  1.0)
    glTexCoord2f(2/3, 1/2)
    glVertex3f(-1.0, -1.0,  1.0)

    glTexCoord2f(2/3, 1.0)
    glVertex3f(1.0, -1.0, -1.0)
    glTexCoord2f(2/3, 1/2)
    glVertex3f(1.0,  1.0, -1.0)
    glTexCoord2f(1/3, 1/2)
    glVertex3f(1.0,  1.0,  1.0)
    glTexCoord2f(1/3, 1.0)
    glVertex3f(1.0, -1.0,  1.0)

    glTexCoord2f(1/3, 1/2)
    glVertex3f(-1.0, -1.0, -1.0)
    glTexCoord2f(1/3, 0.0)
    glVertex3f(-1.0, -1.0,  1.0)
    glTexCoord2f(2/3, 0.0)
    glVertex3f(-1.0,  1.0,  1.0)
    glTexCoord2f(2/3, 1/2)
    glVertex3f(-1.0,  1.0, -1.0)

    glEnd()

    glutSwapBuffers()


def keyPressed(tecla):
    global dx, dy, dz
    
    if tecla == b'x' or tecla == b'X':
        dx = 0.5
        dy = 0
        dz = 0
    elif tecla == b'y' or tecla == b'Y':
        dx = 0
        dy = 0.5
        dz = 0
    elif tecla == b'z' or tecla == b'Z':
        dx = 0
        dy = 0
        dz = 0.5


def teclaEspecialPressionada(tecla, x, y):
    global xrot, yrot, zrot, dx, dy, dz

    if tecla == 100:
        yrot -= dy
    elif tecla == 102:
        yrot += dy
    elif tecla == 101:
        xrot -= dx
    elif tecla == 103:
        xrot += dx


def main():
    global window
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutInitWindowPosition(200, 200)
    window = glutCreateWindow("Textura - Dado")
    glutDisplayFunc(DrawGLScene)
    glutIdleFunc(DrawGLScene)
    glutKeyboardFunc(keyPressed)
    glutSpecialFunc(teclaEspecialPressionada)
    InitGL(800, 600)
    glutMainLoop()

main()