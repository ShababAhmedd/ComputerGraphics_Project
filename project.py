from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np

def findZone(x0, y0, x1, y1):

    dy = y1-y0
    dx = x1-x0

    if abs(dx) > abs(dy):   # Represents zone 0, 3, 4, 7.
        if dx > 0 and dy > 0:
            #print("FindZone: 0")
            return 0
        elif dx < 0 and dy > 0:
            #print("FindZone: 3")
            return 3
        elif dx < 0 and dy < 0:
            #print("FindZone: 4")
            return 4
        else:
            #print("FindZone: 7")
            return 7

    else:                   # Represents zone 1, 2, 5, 6.
        if dx > 0 and dy > 0:
            #print("FindZone: 1")
            return 1
        elif dx < 0 and dy > 0:
            #print("FindZone: 2")
            return 2
        elif dx < 0 and dy < 0:
            #print("FindZone: 5")
            return 5
        else:
            #print("FindZone: 6")
            return 6

def ZoneZeroConversion(zone, x, y):

    if zone == 0:
        #print("Zone Zero Conversion Executed:", x, ",", y)
        return x, y
    elif zone == 1:
        #print("Zone Zero Conversion Executed:", y, ",", x)
        return y, x
    elif zone == 2:
        #print("Zone Zero Conversion Executed:", -y, ",", x)
        return -y, x
    elif zone == 3:
        #print("Zone Zero Conversion Executed:", -x, ",", y)
        return -x, y
    elif zone == 4:
        #print("Zone Zero Conversion Executed:", -x, ",", -y)
        return -x, -y
    elif zone == 5:
        #print("Zone Zero Conversion Executed:", -y, ",", -x)
        return -y, -x
    elif zone == 6:
        #print("Zone Zero Conversion Executed:", -y, ",", x)
        return -y, x
    elif zone == 7:
        #print("Zone Zero Conversion Executed:", x, ",", -y)
        return x, -y

def zero_to_original_zone(zone, x, y):
    if zone == 0:
        #print("Converted to original zone:", x, ",", y)
        return x, y
    if zone == 1:
        #print("Converted to original zone:", y, ",", x)
        return y, x
    if zone == 2:
        #print("Converted to original zone:", -y, ",", -x)
        return -y, -x
    if zone == 3:
        #print("Converted to original zone:", -x, ",", y)
        return -x, y
    if zone == 4:
        #print("Converted to original zone:", -x, ",", -y)
        return -x, -y
    if zone == 5:
        #print("Converted to original zone:", -y, ",", -x)
        return -y, -x
    if zone == 6:
        #print("Converted to original zone:", y, ",", -x)
        return y, -x
    if zone == 7:
        #print("Converted to original zone:", x, ",", -y)
        return x, -y

def MidPointLine(zone, x0, y0, x1, y1):
    dy = y1-y0
    dx = x1-x0
    d_init = 2*dy - dx
    e = 2*dy
    ne = 2*(dy-dx)

    x = x0
    y = y0
    while x <= x1:
        a, b = zero_to_original_zone(zone, x, y)
        draw_points(a, b)
        if d_init <= 0:
            x += 1
            d_init += e
        else:
            x += 1
            y += 1
            d_init += ne

def eight_way_symmetry(x0, y0, x1, y1):
    zone = findZone(x0, y0, x1, y1)
    z0_x0, z0_y0 = ZoneZeroConversion(zone, x0, y0)
    z0_x1, z0_y1 = ZoneZeroConversion(zone, x1, y1)
    MidPointLine(zone, z0_x0, z0_y0, z0_x1, z0_y1)

def BackGroundColour(x):
    if x > 24 or x < 0:
        print("Invalid Time")
    else:
        if x>5 and x<=6:
            glColor3f(0.0, 0.5, 0.74)
            for i in range(600):
                eight_way_symmetry(0, i, 500, i)

        elif x>6 and x<=7:
            glColor3f(0.0, 0.5, 0.72)
            for i in range(600):
                eight_way_symmetry(0, i, 500, i)

        elif x>7 and x<=8:
            glColor3f(0.0, 0.5, 0.7)
            for i in range(600):
                eight_way_symmetry(0, i, 500, i)

        elif x>8 and x<=9:
            glColor3f(0.0, 0.5, 0.8)
            for i in range(600):
                eight_way_symmetry(0, i, 500, i)

        elif x>9 and x<=10:
            glColor3f(0.0, 0.5, 0.9)
            for i in range(600):
                eight_way_symmetry(0, i, 500, i)

        elif x>10 and x<=11:
            glColor3f(0.0, 0.5, 1.0)
            for i in range(600):
                eight_way_symmetry(0, i, 500, i)

        elif x>11 and x<=12:
            glColor3f(0.0, 0.5, 0.9)
            for i in range(600):
                eight_way_symmetry(0, i, 500, i)

        elif x>12 and x<=13:
            glColor3f(0.0, 0.5, 0.8)
            for i in range(600):
                eight_way_symmetry(0, i, 500, i)

        elif x>12 and x<=13:
            glColor3f(0.0, 0.5, 0.7)
            for i in range(600):
                eight_way_symmetry(0, i, 500, i)


        elif x>13 and x<=14:
            glColor3f(0.0, 0.5, 0.72)
            for i in range(600):
                eight_way_symmetry(0, i, 500, i)


        elif x>14 and x<=15:
            glColor3f(0.0, 0.5, 0.74)
            for i in range(600):
                eight_way_symmetry(0, i, 500, i)


        elif x>15 and x<=18:
            glColor3f(0.0, 0.5, 0.76)
            for i in range(600):
                eight_way_symmetry(0, i, 500, i)



        else:
            print("It is night!")








def building1():
    for i in range(250):
        eight_way_symmetry(0, i, 100, i)
    for i in range(40):
        eight_way_symmetry(40, i, 80, i)

def building1_entry():
    for i in range(60):
        eight_way_symmetry(30, i, 70, i)

def building2():
    for i in range(150):
        eight_way_symmetry(106, i, 300, i)
    #glColor3f(0.6, 0.9, 0.9)

def building2_entry():
    for i in range(40):
        eight_way_symmetry(160, i, 240, i)

def building3():
    for i in range(200):
        eight_way_symmetry(306, i, 350,  i)

def building3_entry():
    for i in range(60):
        eight_way_symmetry(330, i, 380, i)

def building4():
    for i in range(230):
        eight_way_symmetry(350, i, 400, i)

def building5():
    for i in range(280):
        eight_way_symmetry(406, i, 500, i)






def eightWay(x, y, x0, y0):
    draw_points(x + x0, y + y0)
    draw_points(y + x0, x + y0)
    draw_points(y + x0, -x + y0)
    draw_points(x + x0, -y + y0)
    draw_points(-x + x0, -y + y0)
    draw_points(-y + x0, -x + y0)
    draw_points(-y + x0, x + y0)
    draw_points(-x + x0, y + y0)

def midPoint(x0, y0, radius,s):
    d = 1 - radius
    x = 0
    y = radius
    scaling_matrix = np.array([[s, 0], [0, s]])
    values = [x, y]
    column = np.array(values).reshape(-1, 1)
    scalled = np.dot(scaling_matrix, column)
    x=scalled[0]
    y=scalled[1]
    eightWay(x, y, x0, y0)
    while x < y:
        if d >= 0:
            d = d + 2 * x - 2 * y + 5
            x = x + 1
            y = y - 1
        else:
            d = d + 2 * x + 3
            x = x + 1
        eightWay(x, y, x0, y0)

def draw_circle(x, y, radius,s):
    midPoint(x, y, radius,s)

    glutSwapBuffers()

# Based on time this algorithm is plotting the position of the sun at different suitable co-ordinates
# and also slightly changing its colour.
def coordinating_circle(x):
        if x >24 or x < 0:
            print("Invalid Time.")
        else:
            if x > 5 and x <= 6:
                for i in range(25, 0, -1):
                    s=2
                    glColor4f(1.0, 0.5, 0.0, 0.0)
                    draw_circle(0, 300, i,s)

            elif x > 6 and x <= 7:
                for i in range(25, 0, -1):
                    s=1.7
                    glColor4f(1.0, 0.6, 0.0, 0.0)
                    draw_circle(50, 350, i,s)

            elif x > 7 and x <= 8:
                for i in range(25, 0, -1):
                    s=1.4
                    glColor4f(1.0, 0.7, 0.0, 0.0)
                    draw_circle(100, 400, i,s)

            elif x > 8 and x <= 9:
                for i in range(25, 0, -1):
                    s=1.3
                    glColor4f(1.0, 0.8, 0.0, 0.0)
                    draw_circle(150, 450, i,s)

            elif x > 9 and x <= 10:
                for i in range(25, 0, -1):
                    s=1.3
                    glColor4f(1.0, 0.9, 0.0, 0.0)
                    draw_circle(200, 500, i,s)

            elif x > 10 and x <= 11:
                for i in range(25, 0, -1):
                    s=1.3
                    glColor4f(1.0, 1.0, 0.0, 0.0)
                    draw_circle(250, 550, i,s)

            elif x > 11 and x <= 12:
                for i in range(25, 0, -1):
                    s=1.3
                    glColor4f(1.0, 0.9, 0.0, 0.0)
                    draw_circle(300, 550, i,s)

            elif x > 12 and x <= 13:
                for i in range(25, 0, -1):
                    s=1.3
                    glColor4f(1.0, 0.8, 0.0, 0.0)
                    draw_circle(350, 500, i,s)

            elif x > 13 and x <= 14:
                for i in range(25, 0, -1):
                    s=1.4
                    glColor4f(1.0, 0.7, 0.0, 0.0)
                    draw_circle(400, 450, i,s)

            elif x > 14 and x <= 15:
                for i in range(25, 0, -1):
                    s=1.7
                    glColor4f(1.0, 0.6, 0.0, 0.0)
                    draw_circle(450, 400, i,s)

            elif x > 15 and x <= 18:
                for i in range(25, 0, -1):
                    s=2
                    glColor4f(1.0, 0.5, 0.0, 0.0)
                    draw_circle(500, 350, i,s)

            else:
                print("It is night!")






def draw_points(x, y):
    glPointSize(5)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()

def iterate():
    glViewport(0, 0, 500, 600)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 600, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()


def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()

    x = float(input("ENTER THE INPUT IN MILITARY TIME ZONE IN HOUR ONLY!: "))  # Enter the time in hour.
    # This function is colouring the background
    BackGroundColour(x)

    # These functions are drawing the buildings.
    glColor3f(0.7, 0.0, 0.0)
    building1()
    building2()
    building3()
    building4()
    building5()

    # These functions are drawing the entry towards the buildings.
    glColor3f(1.0, 1.0, 1.0)
    building2_entry()
    building1_entry()
    building3_entry()



    # This function will centre the sun based on the user input above.
    coordinating_circle(x)

    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 600)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Project_CSE423_ComputerGraphics")
glutDisplayFunc(showScreen)
glutMainLoop()
