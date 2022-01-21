from tkinter import Frame, Canvas, Scrollbar, VERTICAL, RIGHT, Y, LEFT


class PlaceFirst:
    def __init__(self, wi):
        self.widget = wi


        self.pla_width = 135
        self.pla_height = self.widget.wi_max_height - 20

        self.pla_width_box = 133
        self.pla_height_box = 30
        self.pla_indent_width_box = 0
        self.pla_indent_height_box = 2

        self.inf = {"mode": "List"}

        self.pla_text_list = self.widget.wi_canvas.create_text(325, 10, text="List", anchor="w")

        self.wi_frame = Frame(self.widget, width=self.pla_width, height=self.pla_height)
        self.wi_frame.place(x=308, y=20)

        self.canvas = Canvas(self.wi_frame, width=self.pla_width, height=self.pla_height - 5)
        self.scroll = Scrollbar(self.wi_frame, orient=VERTICAL)
        self.scroll.pack(side=RIGHT, fill=Y)
        self.scroll.config(command=self.canvas.yview)
        self.canvas.config(yscrollcommand=self.scroll.set, scrollregion=(0, 0, 120, (0 * 30) + 5))
        self.canvas.pack(side=LEFT)

        self.canvas.bind('<Button-1>', self.pla_mouse_event)
        self.choosed_block = 0

    def pla_show_block(self, inf={"mode": "List"}):
        self.canvas.delete("all")
        self.inf = inf
        if inf['mode'] == "List":
            self.widget.wi_canvas.itemconfigure(self.pla_text_list, text="{}".format(inf['mode']))
        elif inf['mode'] == "All Blocks":
            self.widget.wi_canvas.itemconfigure(self.pla_text_list, text="{}".format(inf['mode']))
            pos = 0
            for bl in inf['list']:
                self.canvas.create_rectangle(self.pla_indent_width_box,
                                             self.pla_indent_height_box + (self.pla_height_box * pos),
                                             self.pla_width_box,
                                             self.pla_height_box + (self.pla_height_box * pos),
                                             fill="yellow" if self.choosed_block == bl else "gray")
                self.canvas.create_text(5,
                                        (self.pla_height_box * pos) + 5,
                                        text="{}".format(bl.__name__[0:20]),
                                        font=("c", 8),
                                        anchor="nw")
                pos += 1
        elif inf['mode'] == "Working Blocks":
            self.widget.wi_canvas.itemconfigure(self.pla_text_list, text="{}".format(inf['mode']))
            pos = 0
            for bl in inf['list']:
                self.canvas.create_rectangle(self.pla_indent_width_box,
                                             self.pla_indent_height_box + (self.pla_height_box * pos),
                                             self.pla_width_box,
                                             self.pla_height_box + (self.pla_height_box * pos),
                                             fill="yellow" if self.choosed_block == bl else "gray")
                self.canvas.create_text(5,
                                        (self.pla_height_box * pos) + 5,
                                        text="{}".format(bl.__class__.__name__[0:20]),
                                        font=("c", 8),
                                        anchor="nw")
                pos += 1

    def pla_mouse_event(self, event):
        self.choosed_block = 0
        mouse_click_x = event.x
        mouse_click_y = event.y
        number_of_block = (mouse_click_y // self.pla_height_box)
        if self.inf['mode'] != "List" and number_of_block <= len(self.inf['list']) - 1:
            self.choosed_block = self.inf['list'][number_of_block]
        self.pla_show_block(inf=self.inf)
        print(self.__class__.__name__,
              "mouse_click_x=", mouse_click_x,
              "mouse_click_y=", mouse_click_y,
              "number_of_block=", number_of_block,
              "self.choosed_block=", self.choosed_block)
