from datetime import time
import logging

logger = logging.getLogger("time-class")
logger.setLevel(logging.DEBUG)

console = logging.StreamHandler()
console.setLevel(logging.DEBUG)

logger.addHandler(console)

t1 = time(12, 34, 30, 121000)
logger.info(t1)

logger.info(f"Hour: {t1.hour}")
logger.info(f"Min: {t1.minute}")
logger.info(f"Sec: {t1.second}")
logger.info(f"Microsecond: {t1.microsecond}")