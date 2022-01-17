from blocks.mainblocks.block150x70 import Block150x70


class BlockText(Block150x70):
    def __init__(self, win, name="BlockText", text1="----", text2="----", text3="----"):
        super().__init__(win=win, name=name)
        x_s = 42
        y_s = 5.5
        self.text_1 = text1
        self.text_field_1 = self.canvas.create_text(x_s + 35,
                                                    y_s,
                                                    text=self.text_1,
                                                    font=("c", 8))
        self.text_2 = text2
        self.text_field_2 = self.canvas.create_text(x_s + 35,
                                                    y_s + 15,
                                                    text=self.text_2,
                                                    font=("c", 8))
        self.text_3 = text3
        self.text_field_3 = self.canvas.create_text(x_s + 35,
                                                    y_s + (15 * 2),
                                                    text=self.text_3,
                                                    font=("c", 8))
    
    def update_canvas(self):
        self.canvas.itemconfigure(self.text_field_1, text=self.text_1)
        self.canvas.itemconfigure(self.text_field_2, text=self.text_2)
        self.canvas.itemconfigure(self.text_field_3, text=self.text_3)
