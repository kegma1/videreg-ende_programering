def whichSide(p1, p2, p3):
    x1, y1, x2, y2, x3, y3 = *p1, *p2, *p3
    o = (y3-y2)*(x2-x1)-(y2-y1)*(x3-x2)
    
    if o < 0:
        return -1
    elif o > 0:
        return 1
    else:
        return 0

def distance(x, y, x1, y1):
    return ((x - x1) * (x - x1) + (y - y1) * (y - y1)) ** 0.5

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
