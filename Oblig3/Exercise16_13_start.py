from tkinter import * # Import tkinter
import math

def whichSide(p1, p2, p3):
    x1, y1, x2, y2, x3, y3 = *p1, *p2, *p3
    o = (y3-y2)*(x2-x1)-(y2-y1)*(x3-x2)
    
    if o < 0:
        return -1
    elif o > 0:
        return 1
    else:
        return 0

def find_left(pList):
    left = pList[0][0]
    for p in range(len(pList)):
        if left >= pList[p][0]:
            left = pList[p][0]
            pLeft = pList[p]
            
    return pLeft

def getConvexHull(points):
    if len(points) <= 2:
        return points

    point_on_hull = find_left(points)

    hull = []
    while True:
        hull.append(point_on_hull)
        next = points[0]

        for point in points:
            side = whichSide(point_on_hull, next, point)
            if next == point_on_hull or side == 1 or \
                (side == 0 and distance(point_on_hull[0],point_on_hull[1],point[0], point[1]) > distance(point_on_hull[0],point_on_hull[1], next[0],next[1])):
                next = point

        point_on_hull = next
        if next == hull[0]:
            break
    return hull

def add(event):
    points.append((event.x, event.y))
    repaint()

def remove(event):
    for (x, y) in points:
        if distance(x, y, event.x, event.y) <= 10:
            points.remove((x, y))
    repaint()

def distance(x, y, x1, y1):
    return ((x - x1) * (x - x1) + (y - y1) * (y - y1)) ** 0.5

def repaint():
    canvas.delete("point")
    if len(points) > 0:
        #
        #
        #
        H = getConvexHull(points) # call GiftWrapping getConvexHull
        #
        #
        #
        canvas.create_polygon(H, fill = "gray", tags = "point")

    for [x, y] in points:
        canvas.create_oval(x - radius, y - radius, x + radius, y + radius, tags = "point")
    
def displayInstructions():
    instructions = ["INSTRUCTIONS", "Add:", "Left Click", "Remove:", "Right Click"]
    x = 20
    y = 20
    canvas.create_rectangle(x, y, x + 160, y + 80)
    canvas.create_text(x + 10 + 40, y + 20, text = instructions[0], justify = CENTER)
    for i in range(1, len(instructions), 2):
        canvas.create_text(x + 10 + 40, y + 20 + (i + 1) * 10, text = instructions[i], justify = RIGHT)
        canvas.create_text(x + 80 + 40, y + 20 + (i + 1) * 10, text = instructions[i + 1], justify = RIGHT)
        

window = Tk() # Create a window
window.title("Convex Hull") # Set title

width = 500
height = 150
radius = 2
canvas = Canvas(window, bg = "white", width = width, height = height)
canvas.pack()

# Create a 2-D list for storing points
points = []

displayInstructions()

canvas.bind("<Button-1>", add)
canvas.bind("<Button-3>", remove)


window.mainloop() # Create an event loop

