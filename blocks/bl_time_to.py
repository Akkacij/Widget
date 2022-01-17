from datetime import datetime, timedelta

from blocks.mainblocks.block150x70 import Block150x70


class BlockTimeTo(Block150x70):
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
        self.version = "Akkacij 1.0 12.01.2022"

        self.finish = False  # Отслеживаемая дата уже прошла?
        self.finish_alarm = 0  # кол-во отработаных тактов после завершения таймера
        self.alarm = 0  # кол-во отработаных тактов таймера
        
        self.cycle = cycle
        self.message = list() + message
        self.finish_message = list() + finish_message
        self.n_message_step = 0
        self.autonext = autonext

        now = datetime.now()
        self.year = year if year != None else now.year
        self.month = month if month != None else now.month
        self.day = day if day != None else now.day
        self.hour = hour if hour != None else now.hour
        self.minute = minute if minute != None else now.minute
        self.second = second if second != None else now.second
        
        if cycle == True:
            self.d_year = d_year
            self.d_month = d_month
            self.d_day = d_day
            self.d_hour = d_hour
            self.d_minute = d_minute
            self.d_second = d_second
        
        self.todatetime = datetime(self.year, self.month, self.day,
                                   self.hour, self.minute, self.second)  #  Отслеживаемая дата
        self.text = ""
        # self.update_todatetime(False)
        self.finish_message.append(self.todatetime)
        self.message.append(self.text)
            
        self.time = self.canvas.create_text(42+30, 5.5+15, text="{}".format(0), font=("c", 8))
        # anchor = "nw"
    
    def text_time(self):
        self.message.remove(self.text)
        delta = self.todatetime - datetime.now()
        year = delta.days // 365 if delta.days // 365 > 0 else 0
        month = (delta.days // 30) - (year * 12) if (delta.days // 30) - (year * 12) > 0 else 0
        day = delta.days - (month * 30) if delta.days - (month * 30) > 0 else 0
        hour = delta.seconds // 3600
        minute = (delta.seconds // 60) - (hour * 60)
        second = delta.seconds - (hour * 3600) - (minute * 60)
        text = "{0}-{1}-{2} {3}:{4}:{5}".format(year, month, day, hour, minute, second)
        self.text = text
        self.message.append(self.text)
     
    def inc_n_message_step(self):
        if self.finish == True:
            self.finish_alarm += 1
            self.alarm = 0
            if self.n_message_step == len(self.finish_message) - 1:
                self.n_message_step = 0
            else:
                self.n_message_step += 1
        else:
            self.finish_alarm = 0
            self.alarm += 1
            if self.n_message_step == len(self.message) - 1:
                self.n_message_step = 0
            else:
                self.n_message_step += 1
        
    def mouse_event(self, event):
        if self.finish == True:
            if self.cycle == True:
                if self.autonext == False:
                    self.update_todatetime()
      
    def update_todatetime(self):
        self.finish_message.remove(self.todatetime)
        if self.d_month != 0 or self.d_year != 0:
            if self.d_month > 12:
                self.d_year += self.d_month // 12
                self.d_month = self.d_month - ((self.d_month // 12) * 12)
            print(self.year, self.d_year)
            delta = (datetime(self.year + self.d_year,
                              self.month + self.d_month,
                              self.day,
                              self.hour,
                              self.minute,
                              self.second) -
                     self.todatetime)
            self.todatetime += timedelta(days=delta.days)
        if self.d_day != 0:
            self.todatetime += timedelta(days=self.d_day)
        if self.d_hour != 0:
            self.todatetime += timedelta(hours=self.d_hour)
        if self.d_minute != 0:
            self.todatetime += timedelta(minutes=self.d_minute)
        if self.d_second != 0:
            self.todatetime += timedelta(seconds=self.d_second)
            
        self.year = self.todatetime.year
        self.month = self.todatetime.month
        self.day = self.todatetime.day
        self.hour = self.todatetime.hour
        self.minute = self.todatetime.minute
        self.second = self.todatetime.second

        self.n_message_step = 0
        self.finish = False
        
        if self.todatetime < datetime.now():
            self.update_todatetime()

        self.finish_message.append(self.todatetime)

    def update_canvas(self):
        self.inc_n_message_step()
        if self.finish == True:
            self.canvas.itemconfigure(self.time, text="{}".format(self.finish_message[self.n_message_step]))
            if self.cycle == True and self.autonext == True and self.finish_alarm == 5:
                self.update_todatetime()
        elif self.todatetime > datetime.now():
            self.text_time()
            self.canvas.itemconfigure(self.time, text="{}".format(self.message[self.n_message_step]))
        else:
            self.n_message_step = 0
            self.finish = True

    def update_frame(self):
        if self.finish == True:
            if self.cycle == True:
                self.frame.configure(background="yellow")
            else:
                self.frame.configure(background="red")
        else:
            self.frame.configure(background='#d9d9d9')
        