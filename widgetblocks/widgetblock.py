class WidgetBlock:
    def __init__(self):
        self.version = "Akkacij 1.0 17.01.2022"
        
        self.inputs = {}
        self.outputs = {}
        
    def init_inputs(self, number_of_inputs):
        for input in range(number_of_inputs):
            self.inputs["input{}".format(input)] = 0
            
    def init_outputs(self, number_of_outputs):
        for output in range(number_of_outputs):
            self.outputs["output{}".format(output)] = 0
        
    def get_number_of_input(self):
        return len(self.inputs)
    
    def get_number_of_putput(self):
        return len(self.outputs)
    
    
    