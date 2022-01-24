from algorithms import render_poliline
from .shape import Shape

class Poliline(Shape):


    def draw(self):

        print('drawinsdfn')
        points = render_poliline(self.vertices)
        self.draw_points(points)

