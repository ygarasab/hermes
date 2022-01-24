import numpy as np

class Shape:

    def __init__(self, table, color):

        self.vertices = []
        self.points = []
        self.table = table
        self.color = color
        self.n_vertices = 0


    def draw_points(self, points ):

        for x,y in points:
            
            if 0 <= x < self.table.side and 0 <= y < self.table.side:
               
                p = self.table.nodes[x][y]
                self.points.append(p)
                p.fill(self.color)

    def clear(self):

        for p in self.points:

            p.fill('white')

        self.points = []


    def add_vertice(self, point):

        self.vertices.append(point)
        if self.n_vertices and len(self.vertices) == self.n_vertices:
            self.draw()

    def translate(self, x, y):

        self.clear()

        for i in range(len(self.vertices)):

            self.vertices[i] = (
                self.vertices[i][0] + x,
                self.vertices[i][1] + y
                    )

        self.draw()

    def resize(self, anchor, x, y):

        self.clear()
        m,n = anchor

        for i in range(len(self.vertices)):

            a,b = self.vertices[i]
            dx = round((a-m) * (1 + x))
            dy = round((b-n) * (1 + y))

            nx = m + dx
            ny = n + dy

            self.vertices[i] = (nx, ny)

        self.draw()

    def rotate(self, anchor, angle):

        self.clear()
        m,n = anchor
        angle = np.deg2rad(angle)

        for i in range(len(self.vertices)):

            a,b = self.vertices[i]
            x = round((a-m) * np.cos(angle) - (b-n) * np.sin(angle))
            y = round((a-m) * np.sin(angle) + (b-n) * np.cos(angle))

            self.vertices[i] = (x+m,y+n)

        self.draw()
