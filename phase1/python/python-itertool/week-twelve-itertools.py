from itertools import count, islice, cycle, repeat 
import logging

logger = logging.getLogger("week-twelve-itertools")
logger.setLevel(logging.DEBUG)

console = logging.StreamHandler()
console.setLevel(logging.DEBUG)

logger.addHandler(console)

#count

logger.info(f'Creating list using count: {list(islice(count(0,1), 15))}')

# cycle
color = ['red', 'white', 'blue']
logger.info(f'Use of cycle function: {list(islice(cycle(color), 8))}')

# repeat 
logger.info(f'User of repeat: {list(repeat(12, 15))}')