from datetime import datetime, timedelta

from panel.mainpanel.panel150x70 import Panel150x70


class PanelTimeTo(Panel150x70):
    def __init__(self, win, name="BlockTimeTo", cycle=False, message=list(), finish_message=list(), autonext=False,
                 year=None,
                 month=None,
                 day=None,
                 hour=None,
                 minute=None,
                 second=None,
                 d_year=0,
                 d_month=0,
                 d_day=0,
                 d_hour=0,
                 d_minute=0,
                 d_second=0):
        super().__init__(win, name=name)
        self.pn_version = "Akkacij 1.0 12.01.2022"

        self.pn_finish = False  # Отслеживаемая дата уже прошла?
        self.pn_finish_alarm = 0  # кол-во отработаных тактов после завершения таймера
        self.pn_alarm = 0  # кол-во отработаных тактов таймера
        
        self.pn_cycle = cycle
        self.pn_message = list() + message
        self.pn_finish_message = list() + finish_message
        self.pn_n_message_step = 0
        self.pn_autonext = autonext

        now = datetime.now()
        self.pn_year = year if year != None else now.year
        self.pn_month = month if month != None else now.month
        self.pn_day = day if day != None else now.day
        self.pn_hour = hour if hour != None else now.hour
        self.pn_minute = minute if minute != None else now.minute
        self.pn_second = second if second != None else now.second
        
        if cycle == True:
            self.pn_d_year = d_year
            self.pn_d_month = d_month
            self.pn_d_day = d_day
            self.pn_d_hour = d_hour
            self.pn_d_minute = d_minute
            self.pn_d_second = d_second
        
        self.pn_todatetime = datetime(self.pn_year, self.pn_month, self.pn_day,
                                      self.pn_hour, self.pn_minute, self.pn_second)  #  Отслеживаемая дата
        self.pn_text = ""
        # self.update_todatetime(False)
        self.pn_finish_message.append(self.pn_todatetime)
        self.pn_message.append(self.pn_text)
            
        self.pn_time = self.pn_canvas.create_text(42+30, 5.5+15, text="{}".format(0), font=("c", 8))
        # anchor = "nw"
    
    def pn_text_time(self):
        self.pn_message.remove(self.pn_text)
        delta = self.pn_todatetime - datetime.now()
        year = delta.days // 365 if delta.days // 365 > 0 else 0
        month = (delta.days // 30) - (year * 12) if (delta.days // 30) - (year * 12) > 0 else 0
        day = delta.days - (month * 30) if delta.days - (month * 30) > 0 else 0
        hour = delta.seconds // 3600
        minute = (delta.seconds // 60) - (hour * 60)
        second = delta.seconds - (hour * 3600) - (minute * 60)
        text = "{0}-{1}-{2} {3}:{4}:{5}".format(year, month, day, hour, minute, second)
        self.pn_text = text
        self.pn_message.append(self.pn_text)
     
    def pn_inc_n_message_step(self):
        if self.pn_finish == True:
            self.pn_finish_alarm += 1
            self.pn_alarm = 0
            if self.pn_n_message_step == len(self.pn_finish_message) - 1:
                self.pn_n_message_step = 0
            else:
                self.pn_n_message_step += 1
        else:
            self.pn_finish_alarm = 0
            self.pn_alarm += 1
            if self.pn_n_message_step == len(self.pn_message) - 1:
                self.pn_n_message_step = 0
            else:
                self.pn_n_message_step += 1
        
    def pn_mouse_event(self, event):
        if self.pn_finish == True:
            if self.pn_cycle == True:
                if self.pn_autonext == False:
                    self.pn_update_todatetime()
      
    def pn_update_todatetime(self):
        self.pn_finish_message.remove(self.pn_todatetime)
        if self.pn_d_month != 0 or self.pn_d_year != 0:
            if self.pn_d_month > 12:
                self.pn_d_year += self.pn_d_month // 12
                self.pn_d_month = self.pn_d_month - ((self.pn_d_month // 12) * 12)
            print(self.pn_year, self.pn_d_year)
            delta = (datetime(self.pn_year + self.pn_d_year,
                              self.pn_month + self.pn_d_month,
                              self.pn_day,
                              self.pn_hour,
                              self.pn_minute,
                              self.pn_second) -
                     self.pn_todatetime)
            self.pn_todatetime += timedelta(days=delta.days)
        if self.pn_d_day != 0:
            self.pn_todatetime += timedelta(days=self.pn_d_day)
        if self.pn_d_hour != 0:
            self.pn_todatetime += timedelta(hours=self.pn_d_hour)
        if self.pn_d_minute != 0:
            self.pn_todatetime += timedelta(minutes=self.pn_d_minute)
        if self.pn_d_second != 0:
            self.pn_todatetime += timedelta(seconds=self.pn_d_second)
            
        self.pn_year = self.pn_todatetime.year
        self.pn_month = self.pn_todatetime.month
        self.pn_day = self.pn_todatetime.day
        self.pn_hour = self.pn_todatetime.hour
        self.pn_minute = self.pn_todatetime.minute
        self.pn_second = self.pn_todatetime.second

        self.pn_n_message_step = 0
        self.pn_finish = False
        
        if self.pn_todatetime < datetime.now():
            self.pn_update_todatetime()

        self.pn_finish_message.append(self.pn_todatetime)

    def pn_update_canvas(self):
        self.pn_inc_n_message_step()
        if self.pn_finish == True:
            self.pn_canvas.itemconfigure(self.pn_time, text="{}".format(self.pn_finish_message[self.pn_n_message_step]))
            if self.pn_cycle == True and self.pn_autonext == True and self.pn_finish_alarm == 5:
                self.pn_update_todatetime()
        elif self.pn_todatetime > datetime.now():
            self.pn_text_time()
            self.pn_canvas.itemconfigure(self.pn_time, text="{}".format(self.pn_message[self.pn_n_message_step]))
        else:
            self.pn_n_message_step = 0
            self.pn_finish = True

    def pn_update_frame(self):
        if self.pn_finish == True:
            if self.pn_cycle == True:
                self.pn_frame.configure(background="yellow")
            else:
                self.pn_frame.configure(background="red")
        else:
            self.pn_frame.configure(background='#d9d9d9')
        