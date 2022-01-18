class Connector:
    """
    Класс является перемычкой, которая хранит id всех объединенных объектов и передает данные от одних к другим
    каждый раз, когда на входе input 1
    """
    def __init__(self):
        self.conn_version = "Akkacij 1.0 17.01.2022"
        
        self.conn_input_wbl_list = []  #[{'block_id': id, 'number_pin': number_pin}]
        self.conn_output_wbl_list = []  #[{'block_id': id, 'number_pin': number_pin}]
        
    def conn_exchange(self):
        input_inf = 0
        for input in self.conn_input_wbl_list:
            input_inf = input['number_pin']
        for output in self.conn_output_wbl_list:
            # output['block_id']
            pass
