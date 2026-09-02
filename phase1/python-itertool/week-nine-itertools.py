from itertools import islice, count, repeat, cycle
import logging

logger = logging.getLogger("week-nine-itertool")
logger.setLevel(logging.DEBUG)  # DEBUG, INFO, WARNING, ERROR, CRITICAL

console = logging.StreamHandler()
console.setLevel(logging.DEBUG)

logger.addHandler(console)

#Print 1 to 10

list1 = list(islice(count(1, 2), 20)) # count produces infinite range on values, islice is used it to limit.

logger.info(f"Use of Count: {list1}")


list2 = list(islice(repeat("Hello!"), 8))

logger.info(f"Use of repeat: {list2}")

colors = ["red", "Yellow", "Green"]

list3 = list(islice(cycle(colors), 5))

logger.info(f"use of cycle: {list3}")