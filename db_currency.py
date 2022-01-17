from database.maindatabase.database import DataBase
from datetime import datetime


class DataBaseCurrency(DataBase):
    def __init__(self, name="DataBaseCurrency"):
        super().__init__(name=name)
        self.value = 0
        
    def write_log(self, date, value):
        if value != self.value:
            # date = datetime.now().date()
            currency_data = [str(date), " ", str(self.name), " ", str(value)]
            super(DataBaseCurrency, self).write(data=currency_data)
            self.value = value

    # --------------------- Read Log Line from File With Date ----------------------#
    def read_date_log(self, date):
        with open(self.file_name, 'r') as file:
            lines = file.readlines()
            for line in lines:
                if line.split(" ")[0] == str(date):
                    date_line = {"date": line.split(" ")[0],
                                 "currency": line.split(" ")[1],
                                 "value": float(line.split(" ")[2].split("\n")[0])}
                    return date_line
            return False
        