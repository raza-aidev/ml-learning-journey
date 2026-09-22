from itertools import count, islice, cycle, repeat, chain
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

# chain 
use_of_chain = list(chain((1, 2), [3, 4], range(5, 11), {11, 12, 13}))
logger.info(f'Use of chain function: {use_of_chain}')

# islice
list1 = list(islice(range(0, 11), 5))
logger.info(list1)

list2 = list(islice(range(40), 3, 35, 3))
logger.info(list2)