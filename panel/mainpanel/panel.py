from math import floor
from tkinter import Frame, Canvas
from block.block import Block


class Panel(Block):
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
        super().__init__()
        self.pn_version = "Akkacij 1.0 12.01.2022"
        self.pn_x = x
        self.pn_y = y
        self.pn_width = width
        self.pn_height = height
        self.pn_canvas_bg = canvas_bg
        self.pn_name = name

        self.pn_frame = Frame(win, width=self.pn_width, height=self.pn_height, background="red")
        self.pn_frame.place(x=self.pn_x, y=self.pn_x)
        self.pn_canvas = Canvas(self.pn_frame, width=self.pn_width, height=self.pn_height, bg=self.pn_canvas_bg)
        self.pn_canvas.create_rectangle(0.6, 0.6, self.pn_width-0.6, self.pn_height-0.6,
                                        fill="white", outline="black", width=1)
        self.pn_canvas.pack()

        # self.status_fields_dict = dict()
        self.pn_status_fields_positions = list()

        self.pn_frame.bind('<Button-1>', self.pn_mouse_event)

    # --------------Update Place--------------------------------#
    def pn_update_place(self):
        self.pn_frame.place_configure(x=self.pn_x, y=self.pn_y)

    # --------------Update Canvas--------------------------------#
    def pn_update_canvas(self):
        pass

    # --------------Update Frame---------------------------------#
    def pn_update_frame(self):
        pass

    # --------------Update Information---------------------------#
    def pn_update_information(self):
        pass

    # --------------Update All Block---------------------------#
    def pn_update_block(self):
        self.pn_update_information()
        self.pn_update_frame()
        self.pn_update_canvas()

    # --------------Mouse's Events---------------------------#
    def pn_mouse_event(self, event):
        pass

    def pn_get_size(self):
        return self.pn_width, self.pn_height

    # -------------- Init Status Fields Positions ---------------------------#
    def pn_init_status_fields_positions(self, number_fields):
        size = 12
        cx = 8 #  12
        cy = -4 # 6.4 - 12
        for field in range(1, number_fields + 1):
            if field <= floor(number_fields / 2):
                self.pn_status_fields_positions.append({"x": cx, "y": cy + (size * field)})
            else:
                cx = self.pn_width + 1 - 12
                self.pn_status_fields_positions.append({"x": cx, "y": cy + (size * (field - floor(number_fields / 2)))})
