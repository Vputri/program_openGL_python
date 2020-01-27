from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *
import sys

def gambar():
     gluOrtho2D(-5,5,-5,5)
    
     glBegin(GL_LINE_LOOP)
     
     glColor3d(1,1,1)
     glVertex2d(0,0)
     glVertex2d(1,0)
     glVertex2d(2,0)
     glVertex2d(1,1)
     glVertex2d(2,1)

     
     
     glEnd()
     glFlush()

glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(500, 500)
glutInitWindowPosition(100, 100)
glutCreateWindow("coba")
glutDisplayFunc(gambar)
glutMainLoop()
