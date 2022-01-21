from tkinter import PhotoImage

from panel.mainpanel.panel import Panel


class Panel150x70(Panel):
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
        self.pn_version = "Akkacij 1.0 12.01.2022"

        self.pn_init_status_fields_positions(8)
