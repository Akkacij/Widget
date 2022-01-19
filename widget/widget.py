from tkinter import Tk, Canvas, Frame
from keypad import Keypad
from math import floor


class Widget(Tk):
    def __init__(self, pos=2):
        super().__init__()
        self.wi_version = "Akkacij 1.0 11.01.2022"
        
        self.wi_width = 302
        self.wi_height = 172
        self.wi_edit_width = 300
        self.wi_edit_height = 150
        if pos == 1:
            self.wi_x = 72
            self.wi_y = 0
        elif pos == 2:
            self.wi_x = 72
            self.wi_y = self.winfo_screenheight() - self.wi_height
        elif pos == 3:
            self.wi_x = self.winfo_screenwidth() - self.wi_width
            self.wi_y = 0
        elif pos == 4:
            self.wi_x = self.winfo_screenwidth() - self.wi_width
            self.wi_y = self.winfo_screenheight() - self.wi_height
        elif pos == 5:
            self.wi_x = floor((self.winfo_screenwidth()/2) - (self.wi_width/2))
            self.wi_y = floor((self.winfo_screenheight()/2) - (self.wi_height/2))

        self.title("MyWidget")

        # self["bg"] = "white"
        self.minsize(self.wi_width, self.wi_height)
        # self.overrideredirect(True)
        # self.resizable(width=False, height=False)

        # self.attributes("-topmost", True)
        # self.attributes("-topmost", False)
        # window.wm_attributes("-alpha", 0.95)
        # update_widget_inf(window)
        # window.overrideredirect(False)
        # self.state('iconic')
        self.geometry("{0}x{1}+{2}+{3}".format(self.wi_width,
                                               self.wi_height,
                                               self.wi_x,
                                               self.wi_y))
        blocks_width = 150
        block_height = 70
        self.wi_position = [{'x': 1, 'y': 1, 'busy': False},
                         {'x': 1, 'y': 1 + block_height, 'busy': False},
                         {'x': 1 + blocks_width, 'y': 1, 'busy': False},
                         {'x': 1 + blocks_width, 'y': 1 + block_height, 'busy': False}]
        
        self.wi_block_list = []

        self.wi_canvas = Canvas(self, width=self.wi_width+5, height=self.wi_height+5)
        self.wi_canvas.create_rectangle(0, 0, self.wi_width + 5, self.wi_height + 5,
                                        fill="gray",
                                        outline="black",
                                        width=1)
        self.wi_canvas.create_rectangle(0, 0, self.wi_width+1, self.wi_height+1,
                                        fill="#d9d9d9",
                                        outline="black",
                                        width=1)
        # self.wi_canvas.pack()
        self.wi_canvas.place(x=0, y=0)

        self.wi_keypad = Keypad(self)
    
    def wi_add_panel(self, panel, in_widget=False):
        if panel not in self.wi_block_list:
            self.wi_block_list.append(panel)
            if in_widget is True:
                self.wi_show_panel_in_widget(panel)

    def wi_show_panel_in_widget(self, pn, pos=-1):
        if pos == -1:
            for tpos in self.wi_position:
                if tpos['busy'] is False:
                    if pn.pn_get_size() == (150, 70):
                        pn.pn_x = tpos['x']
                        pn.pn_y = tpos['y']
                        pn.pn_update_place()
                        tpos['busy'] = True
                        return 1
                    elif pn.pn_get_size() == (300, 70):
                        return 0

    def wi_alarm(self):
        if len(self.wi_block_list) > 0:
            for bl in self.wi_block_list:
                bl.pn_update_block()
        self.after(500, self.wi_alarm)

    def wi_exchange_size_of_window(self):
        if self.winfo_width() == self.wi_width and self.winfo_height() == self.wi_height:
            self.attributes('-zoomed', True)
        else:
            self.attributes('-zoomed', False)
        print("Widget: width=", self.winfo_width(), " height= ", self.winfo_height())
