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

# Accumulate: Max and custom module
nums4 = (12, 23, 13 ,14, 11)
logger.info(f"Example of Accumulate with MAX: {list(accumulate(nums4, max))}")

# Accumulate: With custom method

# nums5 = [130, 230, 234, 340, 450, 990, 900]
# logger.info(f"Examples of custom method (30% of each value): {list(accumulate(nums5, lambda x, y = 0.3: x*y))}")

nums5 = [130, 230, 100, 234, 340, 450, 990, 99, 900]
logger.info(f"Examples of Accumulate with min function: {list(accumulate(nums5, min))}")

# Accumulate: Exampels with intial value to accumulate.
savings = [120, 100, 190, 1000, 13]
print(f"Example of accumulate with initial value: {list(accumulate(savings, initial=1000))}")

nums6 = [140, 12, 13, 11, 9]
print(f"Sum with initial value: {list(accumulate(nums6, initial=10))}")

#groupby: Method
from itertools import groupby

words = ['Cat', 'Bat', 'Salt', 'Beautiful', 'Alfaaz']
words.sort(key=lambda x:x[0])

# print(words)
grouped_words = groupby(words, key=lambda y:y[0])

for letters, group in grouped_words:
    print(f"Wrod groups: {letters}: {list(group)}")

#Question 2
words2 = ['Alpha', 'Gama', 'Omega', 'Sitcom', 'Wazeer', 'Baloon']
words2.sort(key=lambda x:x[0])

for letters, groups in groupby(words2, key=lambda y:y[0]):
    print(f"Letters {letters}: {list(groups)}")

#Question 3

data = ['word', 'Wife', 'Apple', 'alpha', 'Mango', 'Montage']

grouped = groupby(data, key=lambda x: x[0].upper())
# print(list(grouped))
for letters, group in grouped:
    print(f"{letters}: {list(group)}")

#Question 4:
data_Dict = [
    {"Hostel":'B', 'Name':'Kalki', 'State':'Maharshtra'},
    {"Hostel":'A', 'Name':'Shehzadi', 'State':'Kashmir'}, 
    {"Hostel":'B', 'Name':'Kumud', 'State':'Delhi'}, 
    {"Hostel":'A', 'Name':'Vadkadni', 'State':'Karnataka'}
    ]
sorted_Data = sorted(data_Dict, key=lambda x:x['Hostel'])

grouped_data = groupby(sorted_Data, key=lambda x:x['Hostel'])
for letter, group in grouped_data:
    print(f"{letter}: {list(group)}")


# Question 6: Group people by city

people = [
    {"City":'New York', 'Name':'Kalki', 'State':'Maharshtra'},
    {"City":'LA', 'Name':'Shehzadi', 'State':'Kashmir'}, 
    {"City":'New York', 'Name':'Kumud', 'State':'Delhi'}, 
    {"City":'New York', 'Name':'Vadkadni', 'State':'Karnataka'},
    {"City":'Manchester', 'Name':'Jhon', 'State':'Karnataka'}
]

sorted_Data = sorted(people, key=lambda x:x.get('City'))
grouped_data = groupby(sorted_Data, key=lambda x:x.get('City'))

for city, group in grouped_data:
    print(f'{city}: ', end="")
    for person in group:
        print(f'{person.get("Name")}',end=",")
    print('')

#starmap - the unpacker - it unpacks the list/tuple to a function
from itertools import starmap
import operator

coords = [[1, 2, 3], [3, 4, 3], [10, 12, 3], [1, 14, 3]]
def add_coords(x, y, z):
    return x+y+z

result = starmap(add_coords, coords)
print(f"Starmap result: {list(result)}")

#unpack of tuple
data10 = [(12, 3, 1), (12, 13, 14), (110, 19, 19)]
def prod(x, y, z):
    return x*y*z

result1 = list(starmap(prod, data10))
print(f"{result1}")


#examples of accumulate

from itertools import accumulate

savings = [100, 10000, 203303, 102290.12, 1000]
total_saving = list(accumulate(savings))

print(f'Balance of your account is: Rs {total_saving[(len(total_saving)-1)]}')

#compress: the selector - it uses a selector iterable that passes only the true value
from itertools import compress 

selecter = [1, 0, 1, 0, 1, 1, 0]
list1 = ["Apple", "mango", "Banana", "Pineapple", "Mudapple"]

result = list(compress(list1, selecter))
print(result)

#filterfalse: it passes only the values for which the predicate is false

from itertools import filterfalse

number = [100, 200, 300, 400]
result = list(filterfalse(lambda x: x>100, number))

print(result)

data = ['alpha', None, 'Gama', "Theeta", None]
result2 = list(filterfalse(lambda y: y is None, data))

print(result2)


# dropwhile: it will skip the data until the condition is true
from itertools import dropwhile

data2 = [1, 2, 3, 4, 5, 6, 7]
result3 = list(dropwhile(lambda x: x < 3, data2))

print(result3)

prices = [120, 134, 156, 150 , 155, 170, 180]
final_items = list(dropwhile(lambda r: r < 160, prices))

print(final_items)

data4 = ["Mango", "Lichi", "Banana", "Kiwi", "Orange"]
data4.sort(key=lambda x: x[0])

result5 = groupby(data4, key=lambda r: r[0])

for letters, group in result5:
    print(f"{letters}: {list(group)}")

from itertools import zip_longest

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c', 'd']

print(f'Zipped: {list(zip_longest(list1, list2, fillvalue="*"))}')

list3 = ['a', 'b', 'c']
list4 = [(12, 13), (12, 15), (99, 10)]

print(f"Zipped2: {list(zip_longest(list3, list4, fillvalue=None))}")