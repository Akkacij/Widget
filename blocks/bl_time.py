import datetime

from blocks.mainblocks.block150x70 import Block150x70


class BlockTime(Block150x70):
    def __init__(self, win):
        super().__init__(win, name='BlockTime')
        self.version = "Akkacij 1.0 12.01.2022"
        x_s = 42
        y_s = 5.5
        self.time = self.canvas.create_text(x_s+35,
                                            y_s+15,
                                            text="NIME")
        
    def update_canvas(self):
        dtime = datetime.datetime.now()
        self.canvas.itemconfigure(self.time, text="{0}:{1}:{2}".format(dtime.hour,
                                                                       dtime.minute,
                                                                       dtime.second))
        