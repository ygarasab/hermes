from .shape import Shape
from algorithms import draw_plane, get_damn_point, render_line, get_strained_point, get_damn_point_one

class Cube(Shape):

    def __init__(self, table, color, s):

        super().__init__(table, color)
        self.n_vertices = 0
        self.top_vertice = None
        self.top_vertices = []
        self.bottom_vertices = []
        self.bottom_vertice = None
        self.side = s
        self.anchor = None
        self.one_point = 0

    def draw_one_point(self, base):

        self.one_point = 1
        s  = self.side
        self.anchor = base

        self.bottom_vertices = (base,
                (base[0]-s, base[1]),  get_strained_point(base, s))


        self.top_vertices = ((base[0], base[1]- s),
                (base[0]-s, base[1] - s),  get_strained_point((base[0], base[1]- s), s))


        self.top_vertice = get_damn_point_one(self.top_vertices[1], self.top_vertices[2])

        self.draw()

    def draw_two_point(self, base):
        
        s = self.side
        self.anchor = base
        self.bottom_vertices =  draw_plane(base, s)

        upper_base = ( (base[0]), base[1] - s  )

        self.top_vertices = draw_plane(upper_base, s)

        self.top_vertice = get_damn_point(self.top_vertices[1], self.top_vertices[2])
        self.bottom_vertice = get_damn_point(self.bottom_vertices[1], self.bottom_vertices[2])

        self.draw()

    def draw(self):

        points = []

        if self.one_point or  self.anchor[1] + self.side/2 >= 152:
            points += render_line(self.top_vertice, self.top_vertices[1] )
            points += render_line(self.top_vertice, self.top_vertices[2] )

        points += render_line(self.top_vertices[0], self.top_vertices[2] )
        points += render_line(self.top_vertices[0], self.top_vertices[1] )

        points += render_line(self.bottom_vertices[0], self.bottom_vertices[2] )
        points += render_line(self.bottom_vertices[0], self.bottom_vertices[1] )

        
        if not self.one_point and self.anchor[1] + self.side/2 < 150:
            points += render_line(self.bottom_vertice, self.bottom_vertices[1] )
            points += render_line(self.bottom_vertice, self.bottom_vertices[2] )

        for i in range(3):
            points += render_line(self.bottom_vertices[i], self.top_vertices[i] )

        self.draw_points(points)
