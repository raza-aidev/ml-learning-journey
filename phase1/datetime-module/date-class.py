# from datetime import datetime, date, time, timedelta, timezone
# import logging

# logger = logging.getLogger("date-class")
# logger.setLevel(logging.DEBUG)

# console = logging.StreamHandler()
# console.setLevel(logging.DEBUG)

# logger.addHandler(console)

# d1 = date(2026, 12, 8)
# logger.info(f"Date: {d1}")

# logger.info(f"Day: {d1.day}")

# logger.info(f"Month: {d1.month}")

# logger.info(f"Year: {d1.year}")


# today = d1.today()
# logger.info(f"Today's date: {today}")

# diff = d1 - today
# logger.info(diff.days)

# weekday = today.weekday()

# match weekday:
#     case 0:
#         logger.info("Monday")
#     case 1:
#         logger.info("Tuesday")
#     case 2:
#         logger.info("Wednesday")
#     case 3:
#         logger.info("Thursday")
#     case 4:
#         logger.info("Friday")
#     case 5:
#         logger.info("Saturday")
#     case 6:
#         logger.info("Sunday")

#Calculate age
from datetime import date, timedelta 
import logging

logger = logging.getLogger("date-class")
logger.setLevel(logging.DEBUG)

console = logging.StreamHandler()
console.setLevel(logging.DEBUG)

logger.addHandler(console)

def get_age(birth_year, birth_month, birth_day):
    birthday = date(birth_year, birth_month, birth_day)
    today = date.today()
    age_in_days = (today - birthday).days
    age_in_years = age_in_days//365
    remaining_days = age_in_days%365  
    return f"{age_in_years} years and {remaining_days} days"


logger.info(f"My age is: {get_age(1998, 9, 25)}")
