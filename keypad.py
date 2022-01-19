from tkinter import Button, PhotoImage


class Keypad:
    def __init__(self, widget):
        self.version = "Akkacij 1.0 12.01.2022"
        self.widget = widget
        self.button_size = 30
        self.x = 2
        self.y = widget.wi_height - self.button_size
        # --------------Button Close---------------------------#
        self.img_button_close = PhotoImage(file="images/button_image/b_close.png")
        self.button_close = Button(widget,
                                   image=self.img_button_close,
                                   command=lambda: self.widget.destroy(),
                                   bg='black',
                                   activebackground="red")
        self.button_close.place(x=self.x + (9 * self.button_size),
                                y=self.y)
        
        # --------------Button Open---------------------------#
        self.img_button_open = PhotoImage(file="images/button_image/b_open.png")
        self.button_open = Button(widget,
                                  image=self.img_button_open,
                                  command=lambda: self.widget.wi_exchange_size_of_window())
        self.button_open.place(x=self.x + (0 * self.button_size),
                               y=self.y)

        # --------------Button RollUp---------------------------#
        self.img_button_rollup = PhotoImage(file="images/button_image/b_rollup.png")
        self.button_rollup = Button(widget,
                                    image=self.img_button_rollup)
        self.button_rollup.place(x=self.x + (8 * self.button_size),
                                 y=self.y)

        # --------------Button Edit---------------------------#
        self.img_button_edit = PhotoImage(file="images/button_image/b_edit.png")
        self.button_edit = Button(widget,
                                  image=self.img_button_edit)
        self.button_edit.place(x=self.x + (7 * self.button_size),
                               y=self.y)


        self.tweight = 24
        # --------------Button Test---------------------------#
        self.it1 = PhotoImage(file="images/button_image/b.png")
        self.t1 = Button(widget,
                         width=self.tweight,
                         height=self.tweight,
                         image=self.it1,
                         bg='black',
                         activebackground="red")
        self.t1.place(x=self.x + (6 * self.button_size),
                      y=self.y)

        # --------------Button Test---------------------------#
        self.it2 = PhotoImage(file="images/button_image/b.png")
        self.t2 = Button(widget,
                         width=self.tweight,
                         height=self.tweight,
                         image=self.it2,
                         bg='black',
                         activebackground="red")
        self.t2.place(x=self.x + (5 * self.button_size),
                      y=self.y)

        # --------------Button Test---------------------------#
        self.it3 = PhotoImage(file="images/button_image/b.png")
        self.t3 = Button(widget,
                         width=self.tweight,
                         height=self.tweight,
                         image=self.it3,
                         bg='black',
                         activebackground="red")
        self.t3.place(x=self.x + (4 * self.button_size),
                      y=self.y)

        # --------------Button Test---------------------------#
        self.it4 = PhotoImage(file="images/button_image/b.png")
        self.t4 = Button(widget,
                         width=self.tweight,
                         height=self.tweight,
                         image=self.it4,
                         bg='black',
                         activebackground="red")
        self.t4.place(x=self.x + (3 * self.button_size),
                      y=self.y)

        # --------------Button Test---------------------------#
        self.it5 = PhotoImage(file="images/button_image/b.png")
        self.t5 = Button(widget,
                         width=self.tweight,
                         height=self.tweight,
                         image=self.it5,
                         bg='black',
                         activebackground="red")
        self.t5.place(x=self.x + (2 * self.button_size),
                      y=self.y)

        # --------------Button Test---------------------------#
        self.it6 = PhotoImage(file="images/button_image/b.png")
        self.t6 = Button(widget,
                         width=self.tweight,
                         height=self.tweight,
                         image=self.it6,
                         bg='black',
                         activebackground="red")
        self.t6.place(x=self.x + (1 * self.button_size),
                      y=self.y)
