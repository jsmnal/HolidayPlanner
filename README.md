## HolidayPlanner task

HolidayPlanner class that calculates how many holiday days a worker needs to use in a certain timespan given as a string input when given Finnish national holidays has been taken into account.

Example: <br>
planner = HolidayPlanner("10.10.2021-17.10.2021") <br>
planner.holiday_day_consumption()

### Resolving process in a nutshell:
I started to resolve the task as following pieces:
1. The timespan input (written in a commonly used way in Finland e.g. 1.1.2021-1.2.2021)
2. Splitting the time span to beginning and end dates as easier to calculate with them.
3. Calculating the total number of days in the given timespan.
4. Adding the requirements/validation criteria of the timespan (max length 50 days,fit within the holiday period 1.4.-31.3.).
5. Taking the Sundays off as they do not consume holiday days.
6. Taking the given Finnish national holidays off as they do not consume holiday days.
7. Calculating the number of holiday days needed.
8. Error handling and structuring and refactoring the code.

I think that it was easier to start to resolve the task with smaller pieces and first to make the code work as wanted and then start to clean and refactor the code. I felt that the task was challenging but not overwhelming even if I used more than two to three hours to the task. So in that I made a compromise as I wanted the code to be a bit more readable and structured, not just working. I'm not sure if the timespan was meant to be a non-string type but I thought that the string type would be okey as there were not given restrictions for that. I think that the challenging thing was to think the best way to handle with datetimes and consider the best solutions to consider the Sundays and national holidays. Cleaning and refactoring the code also takes time in this point.

### How to improve
I would spend more time for error handling and also would still clean the code. E.g. there may have been calendar-related functions in Python that may have been useful. In addition, I think that in other countries the holiday periods and the rules how holiday days consume (e.g. Saturdays) varies, so I think that would be something to consider in the code (e.g. provide self.holiday_period_beginning/end and self.days_not_consume in def__init__() for functions so that it is just easier to modify them from there and no need to modify the functions). It would be great if the open calendar data, including e.g. national holidays, would have been available and it would have been possible to use that. 