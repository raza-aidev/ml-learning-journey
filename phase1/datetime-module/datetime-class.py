from datetime import datetime, timedelta
import logging

logger = logging.getLogger("datetime-class")
logger.setLevel(logging.DEBUG)

console = logging.StreamHandler()
console.setLevel(logging.DEBUG)

logger.addHandler(console)

dt1 = datetime(2026, 9, 25, 12, 30, 13)
logger.info(f"Datetime: {dt1}")

#Methods 

logger.info(f"Date: {dt1.date()}")
logger.info(f"Time: {dt1.time()}")

# Properties
logger.debug(f"Hour: {dt1.hour}")
logger.debug(f"Minute: {dt1.minute}")
logger.debug(f"Seconds: {dt1.second}")
# logger.debug(f"MicroSecond: {dt1.microsecond}")

logger.debug(f"Year: {dt1.year}")
logger.debug(f"Month: {dt1.month}")
logger.debug(f"Day: {dt1.day}")

dt2 = datetime(2025, 2, 24, 13, 30, 50)

diff = dt1 - dt2
logger.info(diff)

diff2 = diff - timedelta(hours = 12, days = 4)
logger.info(diff2)