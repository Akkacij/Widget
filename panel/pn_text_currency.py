from panel.pn_text import PanelText
from statuses.st_parser.st_parsing import StatusParsing
from statuses.st_changes.st_changes import StatusChanges
from datetime import datetime, timedelta


class PanelTextCurrency(PanelText):
    def __init__(self, win, parser, database, name="BlockTextCurrency"):
        super().__init__(win=win, name=name)
        self.pn_version = "Akkacij 1.0 12.01.2022"
        
        self.pn_parser = parser
        self.pn_database = database
        
        self.pn_status_parsing = StatusParsing(self.pn_canvas,
                                               x=self.pn_status_fields_positions[0]['x'],
                                               y=self.pn_status_fields_positions[0]['y'])
        self.pn_status_changes = StatusChanges(self.pn_canvas,
                                               x=self.pn_status_fields_positions[1]['x'],
                                               y=self.pn_status_fields_positions[1]['y'])
        
    def pn_update_canvas(self):
        date_log = self.pn_database.db_read_date_log((datetime.now() - timedelta(hours=2)).date())
        date_log_last = self.pn_database.db_read_date_log((datetime.now() - timedelta(days=1)).date())
        if date_log is False:
            self.pn_status_changes.update_status('changes_off')  #
            self.pn_status_changes.difference = 0
            self.pn_text_1 = self.pn_status_changes.difference  # Вывод значения
            
            self.pn_status_parsing.update_status('parsing_on')  #  Изменить состояние статуса на "Парсер работает"
            parser_log = self.pn_parser.par_return_log() #  Парсинг и возврат значения из парсера
            if parser_log is not False:
                parser_value = parser_log['VFR']
                self.pn_database.db_write_log(parser_log['DFR'], parser_value)  #  Запись запарсеного значения в базу
                self.pn_text_2 = "1 {0}: {1} BYR".format(self.pn_parser.par_name.split('.')[0], parser_value)  #  Вывод значения
            else:
                self.pn_status_parsing.update_status('parsing_off')  # Изменить состояние статуса на "Парсер работает"
        else:
            if date_log_last is False:
                self.pn_status_changes.update_status('changes_off')  #
                self.pn_status_changes.difference = 0
                self.pn_text_1 = str(self.pn_status_changes.difference)[0:7]
            else:
                self.pn_status_changes.difference = date_log['value'] - date_log_last['value']
                if self.pn_status_changes.difference > 0:
                    self.pn_text_1 = str(self.pn_status_changes.difference)[0:7]
                    self.pn_status_changes.update_status('changes_up')
                elif self.pn_status_changes.difference < 0:
                    self.pn_status_changes.update_status('changes_down')
                    self.pn_text_1 = str(self.pn_status_changes.difference)[0:7]
                else:
                    self.pn_status_changes.update_status('default')
                    self.pn_text_1 = str(self.pn_status_changes.difference)[0:7]
                
            self.pn_text_2 = "1 {0}: {1} BYR".format(self.pn_parser.par_name.split('.')[0],
                                                  date_log['value'])  # Вывод значения
            self.pn_status_parsing.update_status('default')  # Изменить состояние статуса на "Парсер отработал"
        super(PanelTextCurrency, self).pn_update_canvas()  #  Обновить санвас
        
