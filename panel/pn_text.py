from panel.mainpanel.panel150x70 import Panel150x70


class PanelText(Panel150x70):
    def __init__(self, win, name="BlockText", text1="----", text2="----", text3="----"):
        super().__init__(win=win, name=name)
        self.pn_version = "Akkacij 1.0 12.01.2022"
        x_s = 42
        y_s = 5.5
        self.pn_text_1 = text1
        self.pn_text_field_1 = self.pn_canvas.create_text(x_s + 35,
                                                          y_s,
                                                          text=self.pn_text_1,
                                                          font=("c", 8))
        self.pn_text_2 = text2
        self.pn_text_field_2 = self.pn_canvas.create_text(x_s + 35,
                                                          y_s + 15,
                                                          text=self.pn_text_2,
                                                          font=("c", 8))
        self.pn_text_3 = text3
        self.pn_text_field_3 = self.pn_canvas.create_text(x_s + 35,
                                                          y_s + (15 * 2),
                                                          text=self.pn_text_3,
                                                          font=("c", 8))
    
    def pn_update_canvas(self):
        self.pn_canvas.itemconfigure(self.pn_text_field_1, text=self.pn_text_1)
        self.pn_canvas.itemconfigure(self.pn_text_field_2, text=self.pn_text_2)
        self.pn_canvas.itemconfigure(self.pn_text_field_3, text=self.pn_text_3)
