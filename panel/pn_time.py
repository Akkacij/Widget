import datetime

from panel.mainpanel.panel150x70 import Panel150x70


class PanelTime(Panel150x70):
    def __init__(self, win):
        super().__init__(win, name='BlockTime')
        self.pn_version = "Akkacij 1.0 12.01.2022"
        x_s = 42
        y_s = 5.5
        self.pn_time = self.pn_canvas.create_text(x_s+35,
                                                  y_s+15,
                                                  text="NIME")
        
    def pn_update_canvas(self):
        dtime = datetime.datetime.now()
        self.pn_canvas.itemconfigure(self.pn_time, text="{0}:{1}:{2}".format(dtime.hour,
                                                                             dtime.minute,
                                                                             dtime.second))
        