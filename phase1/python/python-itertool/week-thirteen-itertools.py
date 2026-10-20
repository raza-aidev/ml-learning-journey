from itertools import count, islice, cycle, repeat, chain, tee, product, permutations, combinations, accumulate
import logging

logger = logging.getLogger("week-thirteen-itertools")
logger.setLevel(logging.DEBUG)

console = logging.StreamHandler();
console.setLevel(logging.DEBUG)

logger.addHandler(console)
# Problem 1: Basic use of count
counter = count(0, 2)
print(f"{list(islice(counter, 10))}")

# Problem 2: use of count. Count is for gererating infinite numbers with specified steps (Gap).

for i in count(0, 1):
    print(f"{i}")
    if i == 10:
        break

## Use of cycle function cycle is for iterables.
list1 = ["Apple", "Mango", "Banana"]
print(f"{list(islice(cycle(list1), 17))}")

## Use of repeate, it repeats the element with stop value.

print(f"{list(repeat(12, 19))}")


#chain (sntax: chain(*iterables))  Helps in conbining the iterables

num1 = [1, 2, 3, 4]
num2 = [12, 13, 14, 15]

print(f"Chained iterables: {list(chain(num1, num2, range(1, 11)))}")

# chain method for flatening 
num1 = [1, 2, 3]
num2 = [1]
num3 = [12, 13, 14]
empt = list(chain(num1, num2, num3))

print(empt)

#islice with counter

print(f"{list(islice(range(0, 20), 0, 20, 2))}")

#tee function

it = [1, 2, 3]
a, b, c = tee(it, 3)
print(list(a), list(b), list(c))

items = [1, 2, 3 , 4]
print(f"Cartision products: {list(product(items, repeat=2))}")
print(f"Permutaions: {list(permutations(items, 2))}")

print(f"{list(combinations(items, 2))}")

#accumulate: with default running SUM

nums_to_Accumulate = [1, 2, 3, 4, 5, 6]
new_list = accumulate(nums_to_Accumulate)
logger.debug(f"{list(new_list)}")

#Accumulate: with max fucntion

new_items = [3, 1, 4, 2, 2, 7, 1, 9, 1]
new_list2 = list(accumulate(new_items, max))
logger.debug(f"Accumulate function with max: {new_list2}")


#Basic examples of accumulate
from itertools import accumulate
import operator

nums = [1, 3, 1, 5, 12]
logger.debug(f"Basic examples of Accumulate: {list(accumulate(nums))}")

#Accumulate examples with operator module (cumulative product)
nums2 = [2, 4, 5, 1, 9, 12]
logger.info(f"Use of Operator in accumulate: {list(accumulate(nums2, operator.mul))}")

# operator.sub
nums3 = [2, 4, 5, 6, 7]
logger.info(f"Use of Operator in Accumulate: {list(accumulate(nums3, operator.sub))}")


