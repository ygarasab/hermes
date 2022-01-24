def fill_points(x,y, color, table):
    
    node = table.nodes[x][y]
    if node.color == color: return 
    origin_color = node.color
    node.shallow_fill(color) 
    ss = [ (i,j) for i,j in node.neighbors if table.nodes[i][j].color == origin_color ]

    while len(ss):
        p = ss.pop()
        (i,j) = p
        n = table.nodes[i][j]

        if n.color == origin_color:
            n.shallow_fill(color)
            ss += [ (a,b) for a,b in n.neighbors if table.nodes[a][b].color == origin_color ]
            continue




