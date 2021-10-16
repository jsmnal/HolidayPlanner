from datetime import datetime, date

class HolidayPlanner():
    def __init__(self,timespan):
        self.timespan = timespan
        self.beginning = datetime.strptime(timespan.split("-")[0],'%d.%m.%Y').date()
        self.ending = datetime.strptime(timespan.split("-")[1],'%d.%m.%Y').date()

    def calculate_days(self):
        num_of_days = (self.ending-self.beginning).days + 2
        return num_of_days
    
    def calculate_weeks(self):
        num_of_weeks = (((self.ending-self.beginning).days) + 2) / 7
        return num_of_weeks
    
    def timespan_is_valid(self):
        if self.calculate_days() <= 50:
            if self.ending.month>=4 and self.beginning.month<=3:
                return False
            else:
                return True
        else:
            return False
    
    def holidays_spent(self):
        holidays = [date(2020,1,1), date(2020,1,6), date(2020,4,10), date(2020,4,13), date(2020,5,1), date(2020,5,21), date(2020,6,19), date(2020,12,24), date(2020,12,25), date(2021,1,1), date(2021,1,6), date(2021,4,2), date(2021,4,5), date(2021,5,13), date(2021,6,20), date(2021,12,6), date(2021,12,24)]
        if self.timespan_is_valid():
            holidays_needed = self.calculate_weeks() * 6
            for holiday in holidays:
                if self.beginning <= holiday <= self.ending:
                    holidays_need = holidays_needed - 1
                    holidays_needed = holidays_need
            return int(holidays_needed)
        else:
            return("Timespan is not valid")
                

