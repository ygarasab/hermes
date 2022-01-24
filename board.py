from tkinter import *

class Board:

    def __init__(self, launcher):

        self.launcher = launcher

        self.frame = Frame(launcher.window)

        cell0 = Frame(self.frame)

        Button( 
                cell0,text='Linha', 
                command = launcher.table.draw_line,
                font=('Arial',15), width=100
            ).pack(pady=5)

        Button( 
                cell0,text='Curva', 
                command = launcher.table.draw_curve,
                font=('Arial',15), width=100
            ).pack(pady=5)

        Button( 
                cell0,text='Círculo', 
                command = launcher.table.draw_circle,
                font=('Arial',15), width=100
            ).pack(pady=5)
        
        Button( 
                cell0,text='Polilinha', 
                command = launcher.table.draw_poliline,
                font=('Arial',15), width=100
            ).pack(pady=5)

        Button( 
                cell0,text='Limpar', 
                command = launcher.table.clear,
                font=('Arial',15), width=100
            ).pack(pady=5)
        Button( 
                cell0,text='Preencher', 
                command = launcher.table.start_filling,
                font=('Arial',15), width=100
            ).pack(pady=5)
        
        Button( 
                cell0,text='Transladar', 
                command = launcher.table.start_translation,
                font=('Arial',15), width=100
            ).pack(pady=5)

        cell1 = Frame(cell0)
        res_x = Entry( cell1, width=10)
        res_x.pack(side=LEFT, padx=2)
        res_y = Entry( cell1, width=10)
        res_y.pack(side=RIGHT, padx=2)
        Button( 
                cell0,text='Redimensionar', 
                command = lambda: launcher.table.start_resize(
                    float(res_x.get()), float(res_y.get())
                    ),
                font=('Arial',15), width=100
            ).pack(pady=5)

        cell1.pack(pady=5)

        ang = Entry(cell0)

        Button( 
                cell0,text='Rotacionar', 
                command = lambda: launcher.table.start_rotation(
                    float(ang.get())), font=('Arial',15), width=100
            ).pack(pady=5)
        ang.pack(pady=5)

        cell0.pack(pady=30)
        cs = Entry(cell0)

        cell2 = Frame(cell0)

        Button( 
                cell2,text='Cubo 1', 
                command = lambda: launcher.table.draw_1v_cube(
                    int(cs.get())), font=('Arial',13), width=7
            ).pack(side='left',pady=10)
        Button( 
                cell2,text='Cubo 2', 
                command = lambda: launcher.table.draw_2v_cube(
                    int(cs.get())), font=('Arial',13), width=7
            ).pack(side='right',pady=10)
        cell2.pack(pady=5)
        cs.pack(pady=5)


        self.frame.pack()

    def scoreup(self,value):

        self.score['text'] += value

    def levelup(self):

        self.level['text'] += 1

    def death(self):

        restart = Button(self.frame, text='Restart',font=('Arial',13), command=self.launcher.start)
        restart.pack(side='bottom')

