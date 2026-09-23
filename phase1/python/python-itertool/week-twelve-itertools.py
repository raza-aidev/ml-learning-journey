from itertools import count, islice, cycle, repeat, chain
import itertools
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

numbers = [1, 2, 3, 4, 5]

output = list(itertools.accumulate(numbers, lambda x, y : x * y))
logger.info(output)

rand_list = ['c', 'a', 'k', 'e']
output2 = list(itertools.accumulate(rand_list)) 
logger.debug(output2)

output3 = list(itertools.accumulate("abc", lambda x, y: x*3 + y*2))
logger.debug(output3)

import operator

output4 = list(itertools.accumulate(numbers, operator.mul))
logger.debug(output4)

output5 = list(itertools.accumulate(numbers, operator.add))
logger.debug(output5)

output6 = list(itertools.accumulate(numbers, operator.sub))
logger.debug(output6)

numbers2 = [3, 1, 4, 5, 1, 1, 7, 1]
output7 = list(itertools.accumulate(numbers2, max))
logger.debug(f"max: {output7}")

from functools import reduce

output8 = reduce(lambda x,y: x*y ,numbers2)
logger.debug(output8)