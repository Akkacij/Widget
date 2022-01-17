from blocks.bl_text import BlockText
from statuses.st_parser.st_parsing import StatusParsing
from statuses.st_changes.st_changes import StatusChanges
from datetime import datetime, timedelta


class BlockTextCurrency(BlockText):
    def __init__(self, win, parser, database, name="BlockTextCurrency"):
        super().__init__(win=win, name=name)
        self.version = "Akkacij 1.0 12.01.2022"
        
        self.parser = parser
        self.database = database
        
        self.status_parsing = StatusParsing(self.canvas,
                                            x=self.status_fields_positions[0]['x'],
                                            y=self.status_fields_positions[0]['y'])
        self.status_changes = StatusChanges(self.canvas,
                                            x=self.status_fields_positions[1]['x'],
                                            y=self.status_fields_positions[1]['y'])
        
    def update_canvas(self):
        date_log = self.database.read_date_log((datetime.now() - timedelta(hours=2)).date())
        date_log_last = self.database.read_date_log(datetime.now().date() - timedelta(days=1))
        if date_log is False:
            self.status_changes.update_status('changes_off')  #
            self.status_changes.difference = 0
            self.text_1 = self.status_changes.difference  # Вывод значения
            
            self.status_parsing.update_status('parsing_on')  #  Изменить состояние статуса на "Парсер работает"
            parser_log = self.parser.return_log() #  Парсинг и возврат значения из парсера
            if parser_log is not False:
                parser_value = parser_log['VFR']
                self.database.write_log(parser_log['DFR'], parser_value)  #  Запись запарсеного значения в базу
                self.text_2 = "1 {0}: {1} BYR".format(self.parser.name.split('.')[0], parser_value)  #  Вывод значения
            else:
                self.status_parsing.update_status('parsing_off')  # Изменить состояние статуса на "Парсер работает"
        else:
            if date_log_last is False:
                self.status_changes.update_status('changes_off')  #
                self.status_changes.difference = 0
                self.text_1 = str(self.status_changes.difference)[0:7]
            else:
                self.status_changes.difference = date_log['value'] - date_log_last['value']
                if self.status_changes.difference > 0:
                    self.text_1 = str(self.status_changes.difference)[0:7]
                    self.status_changes.update_status('changes_up')
                elif self.status_changes.difference < 0:
                    self.status_changes.update_status('changes_down')
                    self.text_1 = str(self.status_changes.difference)[0:7]
                else:
                    self.status_changes.update_status('default')
                    self.text_1 = str(self.status_changes.difference)[0:7]
                
            self.text_2 = "1 {0}: {1} BYR".format(self.parser.name.split('.')[0],
                                                  date_log['value'])  # Вывод значения
            self.status_parsing.update_status('default')  # Изменить состояние статуса на "Парсер отработал"
        super(BlockTextCurrency, self).update_canvas()  #  Обновить санвас
        
