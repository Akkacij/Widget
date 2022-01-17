from blocks.mainblocks.block import Block


class Block150x140(Block):
    """
    Класс стандартного блока, который будет отображаться в виджете
    """
    def __init__(self,
                 win,
                 x=0,
                 y=0,
                 name='Block150x140',
                 canvas_bg=None):
        super().__init__(win,
                         x=x,
                         y=y,
                         width=150,
                         height=140,
                         name=name,
                         canvas_bg=canvas_bg)
        self.version = "Akkacij 1.0 12.01.2022"

        self.init_status_fields_positions(16)
        