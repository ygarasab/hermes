def desenha(a,b, px, py):
    res = []
    res.append([px+a,py+b])
    res.append([px-a,py+b])
    res.append([px+a,py-b])
    res.append([px-a,py-b])
    res.append([px+b,py+a])
    res.append([px-b,py+a])
    res.append([px+b,py-a])
    res.append([px-b,py-a])

    return res

def render_circle(center, radius):
    
    points = []
    a,b = center
    r = 20

    x = 0
    y = radius
    p = 1-radius


    points += desenha(x,y,a,b)

    while x < y:

        x += 1

        if p < 0:
            p += 2*x + 3

        else:
            y-=1
            p += 2*x - 2*y + 5

        points += desenha(x,y,a,b)

    return points

