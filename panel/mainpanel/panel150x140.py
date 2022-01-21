from panel.mainpanel.panel import Panel


class Panel150x140(Panel):
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
        self.pn_version = "Akkacij 1.0 12.01.2022"

        self.pn_init_status_fields_positions(16)
        