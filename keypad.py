from tkinter import Button, PhotoImage


class Keypad:
    def __init__(self, widget):
        self.version = "Akkacij 1.0 12.01.2022"
        self.widget = widget
        self.button_size = 30
        self.x = 0
        self.y = widget.wi_height - self.button_size
        # --------------Button Close---------------------------#
        self.img_button_close = PhotoImage(file="images/button_image/b_close.png")
        self.button_close = Button(widget,
                                   image=self.img_button_close,
                                   command=lambda: self.widget.destroy(),
                                   bg='black',
                                   activebackground="red")
        self.button_close.place(x=self.x + (9 * self.button_size),
                                y=widget.wi_height - self.button_size)
        
        # --------------Button Open---------------------------#
        self.img_button_open = PhotoImage(file="images/button_image/b_open.png")
        self.button_open = Button(widget,
                                  image=self.img_button_open,
                                  command=lambda: print("Привет, Tkinter!"))
        self.button_open.place(x=self.x + (0 * self.button_size),
                               y=widget.wi_height - self.button_size)

        # --------------Button RollUp---------------------------#
        self.img_button_rollup = PhotoImage(file="images/button_image/b_rollup.png")
        self.button_rollup = Button(widget,
                                    image=self.img_button_rollup)
        self.button_rollup.place(x=self.x + (8 * self.button_size),
                                 y=widget.wi_height - self.button_size)

        # --------------Button Edit---------------------------#
        self.img_button_edit = PhotoImage(file="images/button_image/b_edit.png")
        self.button_edit = Button(widget,
                                  image=self.img_button_edit)
        self.button_edit.place(x=self.x + (7 * self.button_size),
                               y=widget.wi_height - self.button_size)
        