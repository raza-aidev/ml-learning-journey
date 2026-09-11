from itertools import count, islice, repeat, cycle
import logging

counter = list(islice(count(0,15),6))

print(counter)

test = count(0,2)

for i in test:
    print(i)
    if i == 6:
        break

def counter(start, step):
    test = count(start, step)
    for x in test:
        print(x)
        if x == 100:
            break

# counter(0, 1)

repeater = list(repeat("Hello", 4))
print(repeater)

logger = logging.getLogger("week-ten-itertools")
logger.setLevel(logging.INFO)

console = logging.StreamHandler()
console.setLevel(logging.INFO)

logger.addHandler(console)

list1 = ['Hello', 'This', 'Is ', 'Raza']
rep = list(repeat(list1, 6))
logger.info(f"repeat: {rep}")

rep2 = islice(cycle(list), 6)
print(rep1)