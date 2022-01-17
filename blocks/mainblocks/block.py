from math import floor
from tkinter import LabelFrame, Canvas


class Block:
    """
    Класс стандартного блока, который будет отображаться в виджете
    """
    
    def __init__(self,
                 win,
                 x=-300,
                 y=-300,
                 width=150,
                 height=70,
                 name='Block',
                 canvas_bg=None):
        self.version = "Akkacij 1.0 12.01.2022"
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.canvas_bg = canvas_bg
        self.name = name
        
        self.frame = LabelFrame(win, width=self.width, height=self.height, text="{0}".format(self.name))
        self.frame.place(x=self.x, y=self.y)
        
        self.canvas = Canvas(self.frame, width=self.width - 6, height=self.height - 23, bg=self.canvas_bg)
        self.canvas.pack()

        # self.status_fields_dict = dict()
        self.status_fields_positions = list()
        
        self.frame.bind('<Button-1>', self.mouse_event)

    # --------------Update Place--------------------------------#
    def update_place(self):
        self.frame.place_configure(x=self.x, y=self.y)
    
    # --------------Update Canvas--------------------------------#
    def update_canvas(self):
        pass
    
    # --------------Update Frame---------------------------------#
    def update_frame(self):
        pass
    
    # --------------Update Information---------------------------#
    def update_information(self):
        pass
    
    # --------------Update All Block---------------------------#
    def update_block(self):
        self.update_information()
        self.update_frame()
        self.update_canvas()

    # --------------Mouse's Events---------------------------#
    def mouse_event(self, event):
        pass

    def get_size(self):
        return self.width, self.height
    
    # -------------- Init Status Fields Positions ---------------------------#
    def init_status_fields_positions(self, number_fields):
        size = 12
        cx = 12
        cy = 6.4 - 12
        for field in range(1, number_fields + 1):
            if field <= floor(number_fields / 2):
                self.status_fields_positions.append({"x": cx, "y": cy + (size * field)})
            else:
                cx = self.width + 1 - 12
                self.status_fields_positions.append({"x": cx, "y": cy + (size * (field-floor(number_fields/2)))})
            