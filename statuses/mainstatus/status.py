from tkinter import PhotoImage, Canvas


class Status:
    def __init__(self, canvas, name='Status', x=0, y=0):
        self.version = "Akkacij 1.0 12.01.2022"
        self.canvas = canvas
        self.name = name
        self.x = x
        self.y = y
        
        self.state = 'default'
        self.images_of_state_dict = {self.state: PhotoImage(file="statuses/images/default_status.png")}

        self.image = self.canvas.create_image(x, y, image=self.images_of_state_dict[self.state])
        
    def update_status(self, state):
        self.state = state
        self.canvas.itemconfigure(self.image, image=self.images_of_state_dict[self.state])

    # --------------Update Place--------------------------------#
    def update_place(self):
        self.image.place_configure(x=self.x, y=self.y)
        
        
        