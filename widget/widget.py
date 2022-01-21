from tkinter import Tk, Canvas, Button, Frame, Scrollbar, LEFT, Y, RIGHT, VERTICAL
from widget.keypad import Keypad
from widget.place_first import PlaceFirst
from math import floor


class Widget(Tk):
    def __init__(self, pos=2):
        super().__init__()
        self.wi_version = "Akkacij 2.0 11.01.2022"
        
        self.wi_width = 302
        self.wi_height = 172
        self.wi_max_width = self.winfo_screenwidth() - 72
        self.wi_max_height = self.winfo_screenheight() - 64
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
        else:
            self.wi_x = floor((self.winfo_screenwidth()/2) - (self.wi_width/2))
            self.wi_y = floor((self.winfo_screenheight()/2) - (self.wi_height/2))

        self.title("Wi Akkacij")
        self.minsize(self.wi_width, self.wi_height)
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
        self.wi_buffer_x = -3000
        self.wi_buffer_y = -3000

        self.wi_block_list = []
        self.wi_working_block_list = []

        ###-------------------------------------------------------------------------------------

        self.wi_canvas = Canvas(self, width=self.wi_max_width, height=self.wi_max_height)
        self.wi_canvas.create_rectangle(0, 0, self.wi_width + 5, self.wi_height + 5,
                                        fill="gray",
                                        outline="black",
                                        width=1)
        self.wi_canvas.create_rectangle(0, 0, self.wi_width+1, self.wi_height+1,
                                        fill="#d9d9d9",
                                        outline="black",
                                        width=1)
        self.wi_canvas.create_rectangle(303, 177, 303 + 4, self.wi_max_height,
                                        fill="gray",
                                        outline="black",
                                        width=1)
        self.wi_canvas.create_rectangle(458, 0, 458 + 4, self.wi_max_height,
                                        fill="gray",
                                        outline="black",
                                        width=1)
        self.wi_canvas.place(x=0, y=0)

        self.button_all_block = Button(self, text="All blocks", anchor='w',
                                       command=self.wi_keys_click_on_button_all_blocks)
        self.button_all_block.place(x=1, y=self.wi_height + 7)
        self.button_all_block = Button(self, text="All working blocks", anchor='w',
                                       command=self.wi_keys_click_on_button_all_working_blocks)
        self.button_all_block.place(x=1, y=self.wi_height + 7 + (1 * 31))

        ###-------------------------------------------------------------------------------------
        ###-------------------------------------------------------------------------------------
        # self.wi_frame_information_place = LabelFrame(text="Information_place")
        # self.wi_frame_information_place.place(x=310, y=0)
        # self.wi_frame_information_place_canvas = Canvas(self.wi_frame_information_place,
        #                                                 width=300,
        #                                                 height=140,
        #                                                 background="red")
        # self.wi_frame_information_place_canvas.pack()
        ###-------------------------------------------------------------------------------------
        self.wi_keypad = Keypad(self)
        self.wi_place_first = PlaceFirst(self)

    def wi_keys_click_on_button_all_blocks(self):
        self.wi_place_first.pla_show_block(inf={"mode": "All Blocks", "list": self.wi_block_list})

    def wi_keys_click_on_button_all_working_blocks(self):
        self.wi_place_first.pla_show_block(inf={"mode": "Working Blocks", "list": self.wi_working_block_list})

    def wi_add_block(self, block, in_widget=False):
        if block not in self.wi_working_block_list:
            self.wi_working_block_list.append(block)
            if in_widget is True:
                self.wi_show_panel_in_widget(block)

    def wi_show_panel_in_widget(self, block, pos=-1):
        if pos == -1:
            for tpos in self.wi_position:
                if tpos['busy'] is False:
                    if block.pn_get_size() == (150, 70):
                        block.pn_x = tpos['x']
                        block.pn_y = tpos['y']
                        block.pn_update_place()
                        tpos['busy'] = True
                        return 1
                    elif block.pn_get_size() == (300, 70):
                        return 0

    def wi_alarm(self):
        if len(self.wi_working_block_list) > 0:
            for bl in self.wi_working_block_list:
                bl.pn_update_block()
        self.after(500, self.wi_alarm)

    def wi_exchange_size_of_window(self):
        if self.winfo_width() == self.wi_width and self.winfo_height() == self.wi_height:
            self.attributes('-zoomed', True)
        else:
            self.attributes('-zoomed', False)
        print(self.__class__.__name__, "width=", self.winfo_width(), " height= ", self.winfo_height())
        print(self.__class__.__name__, "screen width=", self.winfo_screenwidth(), " height= ", self.winfo_screenheight())

    def wi_init_wi_block_list(self, block_list):
        self.wi_block_list += block_list
