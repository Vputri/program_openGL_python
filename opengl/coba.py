from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *
import sys

def gambar():
     gluOrtho2D(-1,2,-1,2)
     glBegin(GL_QUAD)
     
     glColor3f(0,1,1.0)
     glVertex2f(1,1)
     glVertex2f(1,0)
     glVertex2f(0,0)
     glVertex2f(0,1)

     glEnd()
     glFlush()

glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(500, 500)
glutInitWindowPosition(100, 100)
glutCreateWindow("coba")
glutDisplayFunc(gambar)
glutMainLoop()
