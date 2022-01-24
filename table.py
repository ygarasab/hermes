from tkinter import *
from node import *
from algorithms import fill_points
from shapes import *

class Table:

    def __init__(self,window,side,width,height):

        self.window = window

        self.side = side
        self.width = width
        self.height = height

        self.canvas = Canvas(self.window, width = self.width, height = self.height)
        self.canvas.pack(side='left')

        self.node_side = min([self.height,self.width])/side

        self.nodes = []
        self.color = 'red'

        for x in range(side):

            column = []

            for y in range(side):

                column += [Node(x,y,self,self.node_side)]

            self.nodes += [column]
        self.filled_nodes = []

        self.shapes = []
        self.target_shape = None
        self.translate_inputs = []
        self.translating = 0
        self.resizing = 0
        self.resize_params = []
        self.rotating = 0
        self.rotation_angle = 0
        self.drawing_2v_cube = 0
        self.drawing_1v_cube = 0
        self.filling = 0


    def clear(self):
        self.target_shape = None
        for node in self.filled_nodes:
            node.clear()
        self.filled_nodes = []

    def draw_line(self):

        line = Line(self, self.color)
        self.target_shape = line

    def draw_1v_cube(self, s):
        self.drawing_1v_cube = 1
        self.target_shape = Cube(self, self.color, s)

    def draw_2v_cube(self, s):
        self.drawing_2v_cube = 1
        self.target_shape = Cube(self, self.color, s)

    def draw_circle(self):

        circle = Circle(self, self.color)
        self.target_shape = circle

    def draw_poliline(self):

        if self.target_shape is None:
            pll = Poliline(self, self.color)
            self.target_shape = pll
        else:
            self.target_shape.draw()
            self.shapes.append(self.target_shape)
            self.target_shape = None

    def draw_curve(self):

        if self.target_shape is None:
            curve = Curve(self, self.color)
            self.target_shape = curve
        else:
            self.target_shape.draw()
            self.shapes.append(self.target_shape)
            self.target_shape = None

    def trigger(self, x, y):
         
        if self.drawing_2v_cube:
            self.target_shape.draw_two_point((x,y))
            self.drawing_2v_cube = 0
        elif self.drawing_1v_cube:
            self.target_shape.draw_one_point((x,y))
            self.drawing_1v_cube = 0

        elif self.filling:
            self.fill(x,y)
            self.filling = 0

        elif self.rotating:
            self.rotate((x,y))
            self.rotating = 0

        elif self.resizing:
            self.resize((x,y))
            self.resizing = 0

        elif self.translating:
            self.translate_inputs.append((x,y))
            if len(self.translate_inputs) == 2:
                self.translate()
                self.translating = 0
                self.translate_inputs = []

        elif self.target_shape is not None:
            self.target_shape.add_vertice((x,y))
            if len(self.target_shape.vertices) == self.target_shape.n_vertices:
                self.shapes.append(self.target_shape)
                self.target_shape = None

    def draw(self, x,y):

        if x < 0 or y < 0 or x >= self.side or y >= self.side: return 

        pixel = self.nodes[x][y]
        pixel.fill(self.color)

    def start_filling(self):
        self.translating = 0
        self.target_shape = None
        self.resizing = 0
        self.rotating = 0
        self.filling = 1

    def fill(self, x,y ):

        node = self.nodes[x][y]
        points = fill_points(x,y,self.color, self)


    def start_translation(self):
        self.resizing = 0
        self.rotating = 0
        self.target_shape = None
        self.translating = 1

    def start_resize(self, x,y):
        self.translating = 0
        self.target_shape = None
        self.rotating = 0
        self.resizing = 1
        self.resize_params = (x,y)

    def start_rotation(self, angle):
        self.translating = 0
        self.target_shape = None
        self.resizing = 0
        self.rotating = 1
        self.rotation_angle = angle

    def translate(self):
        [(a,b),(c,d)] = self.translate_inputs
        x = c-a
        y = d-b
        target = self.shapes[-1]
        target.translate(x,y)   

    def resize(self, anchor):
        x,y = self.resize_params
        target = self.shapes[-1]
        target.resize(anchor, x,y)
    
    def rotate(self, anchor):
        target = self.shapes[-1]
        target.rotate(anchor, self.rotation_angle)

        
