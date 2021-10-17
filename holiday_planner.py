from datetime import datetime, date, timedelta

class HolidayPlanner():
    def __init__(self,timespan):
        self.timespan = timespan
        self.national_holidays = [date(2020,1,1), date(2020,1,6), date(2020,4,10), date(2020,4,13), date(2020,5,1), date(2020,5,21), date(2020,6,19), date(2020,12,24), date(2020,12,25), date(2021,1,1), date(2021,1,6), date(2021,4,2), date(2021,4,5), date(2021,5,13), date(2021,6,20), date(2021,12,6), date(2021,12,24)]
        try:
            self.beginning = datetime.strptime(timespan.split("-")[0],'%d.%m.%Y').date()
            self.end = datetime.strptime(timespan.split("-")[1],'%d.%m.%Y').date()
        except:
            print("Error: Please check if the given timespan is appropriate.")
    
    def calculate_days(self):
        try:
            num_of_days = (self.end-self.beginning).days + 1
            return num_of_days
        except:
            print("Error: Please check if the given timespan is appropriate.")
    
    def timespan_is_valid(self):
        try:
            if self.calculate_days() <= 50 and self.end >= self.beginning:
                if self.end.month>=4 and self.beginning.month<=3: ## timespan needs to fit within the Finnish holiday period
                    return False
                else:
                    return True
            else:
                return False
        except:
            print("Error: Please check if the given timespan is appropriate.")
    
    def calculate_sundays(self):
        try:
            num_of_sundays = 0
            self.end = self.end + timedelta(days=1)
            while(self.end > self.beginning):
                self.end = self.end - timedelta(days=1)
                if self.end.isoweekday() == 7:
                    num_of_sundays = num_of_sundays + 1
            return num_of_sundays
        except:
            print("Error: Please check if the given timespan is appropriate.")
    
    ## calculate national holidays that are not on Sundays
    def calculate_national_holidays(self):
        try:
            num_of_national_holidays = 0
            for holiday in self.national_holidays:
                if self.beginning <= holiday <= self.end and holiday.isoweekday() != 7:
                    num_of_national_holidays = num_of_national_holidays + 1
            return num_of_national_holidays
        except:
            print("Error: Please check if the given timespan is appropriate.")

    def holiday_day_consumption(self):
        try:
            if self.timespan_is_valid():
                num_of_holiday_days = self.calculate_days() - self.calculate_national_holidays() - self.calculate_sundays()
                return num_of_holiday_days
            else:
                return("Timespan is not valid")
        except:
            print("Error: Please check if the given timespan is appropriate.")

