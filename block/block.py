class Block:
    def __init__(self):
        self.bl_version = "Akkacij 1.0 17.01.2022"
        
        self.bl_inputs = {}
        self.bl_outputs = {}
        
    def bl_init_inputs(self, number_of_inputs):
        for input in range(number_of_inputs):
            self.bl_inputs["input{}".format(input)] = 0
            
    def bl_init_outputs(self, number_of_outputs):
        for output in range(number_of_outputs):
            self.bl_outputs["output{}".format(output)] = 0
        
    def bl_get_number_of_input(self):
        return len(self.bl_inputs)
    
    def bl_get_number_of_putput(self):
        return len(self.bl_outputs)
    
    
    