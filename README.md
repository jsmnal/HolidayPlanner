## HolidayPlanner task

HolidayPlanner class that calculates how many holiday days a worker needs to use in a certain timespan given as a string input when given Finnish national holidays has been taken into account.

### Understanding the task:
I understood that in this task the idea was to take timespan (written in a commonly used way in Finland e.g. 1.1.2021-1.2.2021) and make the class that can provide the number of holiday days a worker needs if wants to have a holiday during the given time period. As in Finland, the Saturdays were count as a days that consume holiday days whereas Sundays do not. Also the given Finnish national holidays needed to take into account. 

### Resolving process in a nutshell:
I started to resolve the task as following pieces:
    1. The timespan input.
    2. Splitting the time span to beginning and end dates as easier to calculate with them.
    3. Calculating the total number of days in the given timespan.
    4. Adding the requirements/validation criteria of the timespan.
    5. Taking the Sundays off.
    6. Taking the given Finnish national holidays off.
    7. Calculating the number of holiday days needed.
    8. Cleaning and refactoring the code.

I think that it was easier to start to resolve the task with smaller pieces and first to make the code work as wanted and then start to clean and refactor the code. I felt that the task was challenging but not overwhelming even if I used more than two to three hours to the task. So in that I made a compromise as I wanted the code to be readable and clean, not just working. I'm not sure if the timespan was meant to be a non-string type but I thought that the string type would be okey as there were not given restrictions for that given. I think that the challenging thing was to think the best way to handle with datetimes and consider the best solutions to consider the Sundays and national holidays.