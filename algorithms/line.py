def render_line(a, b):

    points = []

    x1 = a[0]
    y1 = a[1]

    x2 = b[0]
    y2 = b[1]

    m = (y2 - y1) / (x2 - x1 + 1e-5)

    txy = 0
    tx = 0
    ty = 0

    if m > 1 or m < -1:
        x1,x2,y1,y2 = y1,y2,x1,x2
        txy = 1

    if x1 > x2:
        x1,x2 = -x1,-x2
        tx = 1

    if y1 > y2:
        y1,y2 = -y1,-y2
        ty = 1

    x = x1
    y = y1


    m = (y2 - y1) / (x2 - x1 + 1e-5)

    e = (m-1)/2

    points.append([x,y])

    while x < x2:
        if e >= 0:
            y+=1
            e-=1
        x+=1
        e+=m
        points.append([x,y])


    a = []

    if ty:
        for [i,j] in points:
            a.append([i,-j])
        points = a
        a = []

    if tx:
        for [i,j] in points:
            a.append([-i,j])
        points = a
        a = []

    if txy:
        for [i,j] in points:
            a.append([j,i])
        points = a

    return points

def render_poliline(vertices):

    points = []
        
    for i in range(len(vertices)):

        points += render_line(vertices[i-1], vertices[i])

    return points

