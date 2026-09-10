from itertools import count, islice

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

counter(0, 1)