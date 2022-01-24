import sys
sys.setrecursionlimit(90000)

class Node:

    def __init__(self,x,y,table,side):

        self.table = table

        self.x = x
        self.y = y
        self.coords = [x,y]

        self.canvas = table.canvas
        self.side = side

        self.rect = self.canvas.create_rectangle(x*side,y*side,(x+1)*side,(y+1)*side, outline='', tags=f"{x},{y}")
        self.canvas.tag_bind(f"{x},{y}", "<Button-1>", lambda e: table.trigger(x,y))
        self.canvas.itemconfig(self.rect, fill='white')

        self.color = 'white'
        self.neighbors = []

        self.load_neighbors()

    def fill(self,color):

        self.color = color
        self.canvas.itemconfig(self.rect, fill=color)
        for x,y in self.neighbors:
            n = self.table.nodes[x][y]
            n.color = color
            self.canvas.itemconfig(n.rect, fill=color)

    def shallow_fill(self,color):

        self.color = color
        self.canvas.itemconfig(self.rect, fill=color)

    def next(self,direction):

        x,y = [self.coords[i]+direction[i] for i in range(2)]

        return self.table.get(x,y)
    
    def load_neighbors(self):

        if 0 <= self.x < self.table.side and 0 <= self.y+1 < self.table.side:
            self.neighbors += [(self.x, self.y + 1)]
        if 0 <= self.x < self.table.side and 0 <= self.y-1 < self.table.side:
            self.neighbors += [(self.x, self.y - 1)]
        if 0 <= self.x+1 < self.table.side and 0 <= self.y < self.table.side:
            self.neighbors += [(self.x+1, self.y)]
        if 0 <= self.x-1 < self.table.side and 0 <= self.y < self.table.side:
            self.neighbors += [(self.x-1, self.y)]

