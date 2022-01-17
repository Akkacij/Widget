from statuses.mainstatus.status import Status
from tkinter import PhotoImage


class StatusChanges(Status):
    def __init__(self, canvas, name='StatusChanges', x=0, y=0):
        super().__init__(canvas=canvas, name=name, x=x, y=y)
        
        #  No changes
        self.images_of_state_dict['default'] = PhotoImage(file="statuses/st_changes/images/status_changes.png")
        #  Changes up
        self.images_of_state_dict['changes_up'] = PhotoImage(file="statuses/st_changes/images/status_changes_up.png")
        #  Changes down
        self.images_of_state_dict['changes_down'] = PhotoImage(file="statuses/st_changes/images/status_changes_down.png")
        #  Changes error
        self.images_of_state_dict['changes_off'] = PhotoImage(file="statuses/st_changes/images/status_changes_off.png")
        
        self.difference = 0
