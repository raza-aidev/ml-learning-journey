from itertools import count, islice, cycle, repeat

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
