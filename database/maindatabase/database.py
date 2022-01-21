from block.block import Block


class DataBase(Block):
    def __init__(self, name="DataBase"):
        super().__init__()
        self.db_version = "Akkacij 1.0 12.01.2022"

        self.db_name = name
        self.db_file_name = "DATABASE DATA/{}.database".format(self.db_name)
        file = open(self.db_file_name, 'a')
        file.close()

    # --------------------- Write List Of Values ----------------------#
    def db_write(self, data):
        with open(self.db_file_name, 'a') as file:
            for d in data:
                file.write(d)
            file.write("\n")
    
    # --------------------- Read All Lines ----------------------#
    def db_read(self):
        lines = list()
        with open(self.db_file_name, 'r') as file:
            for line in file:
                lines.append(line)
            return lines

    # --------------------- Read First Line from File ----------------------#
    def db_read_first(self):
        with open(self.db_file_name, 'r') as file:
            lines = file.readlines()
            return lines[0]

    # --------------------- Read Last Line from File ----------------------#
    def db_read_last(self):
        with open(self.db_file_name, 'r') as file:
            lines = file.readlines()
            return lines[-1]

    # --------------------- Read Line from File With Number ----------------------#
    def db_read_line_with_number(self, number_line):
        with open(self.db_file_name, 'r') as file:
            lines = file.readlines()
            return lines[number_line]
        