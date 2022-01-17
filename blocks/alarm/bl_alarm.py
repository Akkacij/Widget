from widgetblocks.widgetblock import WidgetBlock


class Alarm(WidgetBlock):
    def __init__(self, widget, d_time=1000):
        self.widget = widget
        self.delta_time = d_time
        
        
        
    def alarm(self):
        self.widget.after(self.delta_time, self.alarm)
        