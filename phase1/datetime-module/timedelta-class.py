from datetime import datetime,  timedelta

import logging

logger = logging.getLogger("timedelta-class")
logger.setLevel(logging.DEBUG)

console = logging.StreamHandler()
console.setLevel(logging.DEBUG)

logger.addHandler(console)

today = datetime.today()

doom_release = datetime(2026, 12, 16, 7, 00)

doomsday_counter = doom_release - today
logger.info(f"Dooms day will be released in {doomsday_counter.days} days, {doomsday_counter.seconds//3600} hours and {doomsday_counter.seconds//60}")