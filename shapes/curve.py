from algorithms import render_curve
from .shape import Shape

class Curve(Shape):


    def draw(self):

        points = render_curve(self.vertices)
        self.draw_points(points)

