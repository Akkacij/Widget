from block.block import Block


class Alarm(Block):
    def __init__(self, widget, d_time=1000):
        super().__init__()
        self.al_widget = widget
        self.al_delta_time = d_time

    def al_alarm(self):
        self.al_widget.after(self.al_delta_time, self.al_alarm)
        