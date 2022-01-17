class DataBase:
    def __init__(self, name="DataBase"):
        
        self.version = "Akkacij 1.0 12.01.2022"
        self.name = name
        self.file_name = "DATABASE DATA/{}.database".format(self.name)
        file = open(self.file_name, 'a')
        file.close()

    # --------------------- Write List Of Values ----------------------#
    def write(self, data):
        with open(self.file_name, 'a') as file:
            for d in data:
                file.write(d)
            file.write("\n")
    
    # --------------------- Read All Lines ----------------------#
    def read(self):
        lines = list()
        with open(self.file_name, 'r') as file:
            for line in file:
                lines.append(line)
            return lines

    # --------------------- Read First Line from File ----------------------#
    def read_first(self):
        with open(self.file_name, 'r') as file:
            lines = file.readlines()
            return lines[0]

    # --------------------- Read Last Line from File ----------------------#
    def read_last(self):
        with open(self.file_name, 'r') as file:
            lines = file.readlines()
            return lines[-1]

    # --------------------- Read Line from File With Number ----------------------#
    def read_line_with_number(self, number_line):
        with open(self.file_name, 'r') as file:
            lines = file.readlines()
            return lines[number_line]
        