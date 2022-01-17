from tkinter import Tk
from keypad import Keypad

widget_inf = {'widget_version': '1.0',
              'widget_width': 303,
              'widget_height': 172,
              'widget_edit_width': 300,
              'widget_edit_height': 150,
              'widget_x': 0,
              'widget_y': 0,

              'widget_button_size': 30,  # pixels of button = 24
              'widget_blocks_indent': 1,

              'blocks_width': 150,
              'block_height': 70,
              'blocks_list': list(),

              'position': [{'x': 0 + 1, 'y': 0 + 1, 'busy': False},
                           {'x': 150 + 1, 'y': 70 + 1, 'busy': False},
                           {'x': 0 + 1, 'y': 0 + 1, 'busy': False},
                           {'x': 150 + 1, 'y': 70 + 1, 'busy': False}]}


class Widget(Tk):
    def __init__(self, pos=2):
        super().__init__()

        self.version = "Akkacij 1.0 11.01.2022"
        
        self.width = 303
        self.height = 172
        self.edit_width = 300
        self.edit_height = 150
        if pos == 1:
            self.x = 72
            self.y = 0
        elif pos == 2:
            self.x = 72
            self.y = self.winfo_screenheight() - self.height
        elif pos == 3:
            self.x = self.winfo_screenwidth() - self.width
            self.y = 0
        elif pos == 4:
            self.x = self.winfo_screenwidth() - self.width
            self.y = self.winfo_screenheight() - self.height
        
        
        self.title("MyWidget")
    
        # window["bg"] = "#2bb620"
        self.overrideredirect(True)
        # window.wm_attributes("-alpha", 0.95)
        # update_widget_inf(window)
        # window.overrideredirect(False)
        # window.state('iconic')
        self.geometry("{0}x{1}+{2}+{3}".format(self.width,
                                               self.height,
                                               self.x,
                                               self.y))
        blocks_width = 150
        block_height = 70
        self.position = [{'x': 0 + 1, 'y': 0 + 1, 'busy': False},
                         {'x': 0 + 1, 'y': block_height + 1, 'busy': False},
                         {'x': blocks_width + 1, 'y': 0 + 1, 'busy': False},
                         {'x': blocks_width + 1, 'y': block_height + 1, 'busy': False}]
        
        self.block_list = []
        
        self.keypad = Keypad(self)
    
    def add_block(self, block, in_widget=False):
        if block not in self.block_list:
            self.block_list.append(block)
            if in_widget is True:
                self.show_block_in_widget(block)

    def show_block_in_widget(self, bl, pos=-1):
        if pos == -1:
            for tpos in self.position:
                if tpos['busy'] is False:
                    if bl.get_size() == (150, 70):
                        bl.x = tpos['x']
                        bl.y = tpos['y']
                        bl.update_place()
                        tpos['busy'] = True
                        return 1
                    elif bl.get_size() == (300, 70):
                        return 0

    def alarm(self):
        if len(self.block_list) > 0:
            for bl in self.block_list:
                bl.update_block()
        # print("ALARM")
        self.after(500, self.alarm)

        