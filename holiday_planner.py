from datetime import datetime, date, timedelta

class HolidayPlanner():
    def __init__(self,timespan):
        self.timespan = timespan
        self.beginning = datetime.strptime(timespan.split("-")[0],'%d.%m.%Y').date()
        self.ending = datetime.strptime(timespan.split("-")[1],'%d.%m.%Y').date()

    def calculate_days(self):
        num_of_days = (self.ending-self.beginning).days
        return num_of_days
    
    def timespan_is_valid(self):
        if self.calculate_days() <= 50 and self.ending >= self.beginning:
            if self.ending.month>=4 and self.beginning.month<=3:
                return False
            else:
                return True
        else:
            return False
    
    def take_sundays(self):
        num_of_days = 0
        self.ending = self.ending + timedelta(days=1)
        while(self.ending > self.beginning):
            self.ending = self.ending - timedelta(days=1)
            if self.ending.isoweekday() <= 6:
                num_of_days = num_of_days + 1
        return num_of_days
    
    def take_national_holidays(self):
        national_holidays = [date(2020,1,1), date(2020,1,6), date(2020,4,10), date(2020,4,13), date(2020,5,1), date(2020,5,21), date(2020,6,19), date(2020,12,24), date(2020,12,25), date(2021,1,1), date(2021,1,6), date(2021,4,2), date(2021,4,5), date(2021,5,13), date(2021,6,20), date(2021,12,6), date(2021,12,24)]
        holidays_needed = self.take_sundays()
        for holiday in national_holidays:
            if self.beginning <= holiday <= self.ending:
                    holidays_need = holidays_needed - 1
                    holidays_needed = holidays_need
        return int(holidays_needed)

    def holiday_day_consumption(self):
        if self.timespan_is_valid():
            total = self.take_national_holidays()
            return total
        else:
            return("Timespan is not valid")

                

