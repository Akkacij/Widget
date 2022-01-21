from database.maindatabase.database import DataBase


class DataBaseCurrency(DataBase):
    def __init__(self, name="DataBaseCurrency"):
        super().__init__(name=name)
        self.db_version = "Akkacij 1.0 12.01.2022"
        self.db_value = 0
        
    def db_write_log(self, date, value):
        if value != self.db_value:
            # date = datetime.now().date()
            currency_data = [str(date), " ", str(self.db_name), " ", str(value)]
            super(DataBaseCurrency, self).db_write(data=currency_data)
            self.db_value = value

    # --------------------- Read Log Line from File With Date ----------------------#
    def db_read_date_log(self, date):
        with open(self.db_file_name, 'r') as file:
            lines = file.readlines()
            for line in lines:
                if line.split(" ")[0] == str(date):
                    date_line = {"date": line.split(" ")[0],
                                 "currency": line.split(" ")[1],
                                 "value": float(line.split(" ")[2].split("\n")[0])}
                    return date_line
            return False
        