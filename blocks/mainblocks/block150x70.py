from tkinter import PhotoImage

from blocks.mainblocks.block import Block


class Block150x70(Block):
    """
    Класс стандартного блока, который будет отображаться в виджете
    """
    def __init__(self,
                 win,
                 name='Block150x70',
                 canvas_bg=None):
        super().__init__(win=win,
                         width=150,
                         height=70,
                         name=name,
                         canvas_bg=canvas_bg)
        self.version = "Akkacij 1.0 12.01.2022"

        self.init_status_fields_positions(8)
