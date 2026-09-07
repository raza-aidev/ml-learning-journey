"""

%Y -> Year in 2024
%y -> year in 23
%m -> month in 01 to 12
%d -> days 
%H  -> Hours 00 to 23
%I -> hours 00 to 12 
%M -> minutes  00 to 59
%S -> seconds 00 to 59
%p -> AM/PM
%A  -> weekdays in full Monday
%a -> weekdays in short WED
%B -> Month name full form August
%b -> month name in short Aug

"""

"""
%Y -> Years in 4 digits 2026
%y -> Years in 2 digits 26
%m -> Months in digit 01 - 12
%B -> months in full form March
%b -> months in short form Mar
%d -> date in digits 1 to 31
%H -> hour in 24 hrs 00 to 23
%I -> Hours 12
%M -> Minutes 0 to 59
%S -> Seconds
%B -> weekdays in fullform
%b -> weekdays short form 
%p -> AM/PM

"""

# from datetime import datetime

# import logging

# logger = logging.getLogger("strftime")
# logger.setLevel(logging.DEBUG)

# console = logging.StreamHandler()
# console.setLevel(logging.DEBUG)

# logger.addHandler(console)

# dt1 = datetime.today()

# logger.info(f"Date and Time: {dt1}")

# logger.info(dt1.strftime("%d-%m-%Y, %H:%M:%S %p"))
# logger.info(f'Date and time: {dt1.strftime("%d %B %Y, %A")}')
# logger.info(f'Date and time: {dt1.strftime("%d %B %Y, %A, %I:%M %p")}')

from datetime import datetime
import logging

logger = logging.getLogger("strftime-class")
logger.setLevel(logging.DEBUG)

console = logging.StreamHandler()
console.setLevel(logging.DEBUG)

logger.addHandler(console)

today = datetime.today()
birth_date = datetime(1998, 9, 25, 1, 30, 50)

# logger.info(birth_date)

has_birth_day_passed = (birth_date.day, birth_date.month) > (today.day, today.month)

actual_age = (today.year - birth_date.year) - (0 if has_birth_day_passed else 1)
logger.info(f"The Age is: {actual_age}") 