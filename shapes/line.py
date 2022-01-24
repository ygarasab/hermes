from algorithms import render_line
from .shape import Shape

class Line(Shape):


    def __init__(self, table, color):

        super().__init__(table, color)
        self.n_vertices = 2

    def draw(self):

        points = render_line(*self.vertices)
        self.draw_points(points)
