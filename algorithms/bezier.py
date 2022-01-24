from . import render_line
def casteljau(points, t):

    res = []
    for p in points:
        if (not len(p) == 2):
            raise InvalidInputError('points is not a list of points(tuples)')
    if (len(points) == 1):
        res.append(points[0])
    else:
        newpoints = []
        for i in range(0, len(points)-1):
            x = (1-t) * points[i][0] + t * points[i+1][0]
            y = (1-t) * points[i][1] + t * points[i+1][1]
            newpoints.append((x, y))
        res += casteljau(newpoints, t)
    return res

def render_curve(points):
    t = 0
    res = []
    while t <=1:
        res += casteljau(points, t)
        t += .05
    res = [(round(i), round(j)) for (i,j) in res]
    
    points = []
    for i in range(1,len(res)):
        
        points += render_line(res[i-1], res[i])

    return points


