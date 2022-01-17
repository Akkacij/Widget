from statuses.mainstatus.status import Status
from tkinter import PhotoImage


class StatusParsing(Status):
    def __init__(self, canvas, name='StatusParsing', x=0, y=0):
        super().__init__(canvas=canvas, name=name, x=x, y=y)
        self.version = "Akkacij 1.0 12.01.2022"
        
        #  Parser done
        self.images_of_state_dict['default'] = PhotoImage(file="statuses/st_parser/images/status_parsing.png")
        #  Parser working
        self.images_of_state_dict['parsing_on'] = PhotoImage(file="statuses/st_parser/images/status_parsing_on.png")
        #  Parser error
        self.images_of_state_dict['parsing_off'] = PhotoImage(
            file="statuses/st_parser/images/status_parsing_off.png")
        
        