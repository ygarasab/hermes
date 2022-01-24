from algorithms import render_circle
from .shape import Shape

class Circle(Shape):

    def __init__(self, table, color):

        super().__init__(table, color)
        self.n_vertices = 2

    def draw(self):

        [(a,b),(c,d)] = self.vertices
        radius = round(((a-c)**2 + (b-d)**2) ** .5)
        points = render_circle((a,b), radius)
        self.draw_points(points)
