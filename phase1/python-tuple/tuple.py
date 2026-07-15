tuple1 = (1, 2, "test", True, False, 12.5)
print("Elemenst of tuple: ")
for i in tuple1:
    print(f"{i}: {type(i)}")

print(f"accessing: {tuple1[1]}")

print(f"Accessing: {tuple1[1:2]}")

tuple2 = (34,)

tuple3 = 56,
x = (34)

print(f"type of tuple2: {type(tuple2)}, Type of tuple3: {type(tuple3)}, type of x: {type(x)}")

#Updating tuple by converting to list

tuple1 = list(tuple1)
list2 = [12, 13, 14]

# tuple1 = [tuple1+i for i in list2]
# print("new tuple: ", tuple1)

# tuple1 = tuple(tuple1)
# print("updated tuple: ",tuple1)


tuple2 = (12, 13.5, 'test', "ABD", 'a')
a, b, c, *d = tuple2

print(f"a: {a}, b: {b}, c: {c}, d: {d}")


print("-----------looping through tuple---------")
#using index and for loop
for i in range(len(tuple2)):
    print(f"Index {i}: {tuple2[i]}")

#using while loop
count = 0
print("Looping tuple using while -> ")
while count< len(tuple2):
    print(f"{tuple2[count]}")
    count +=1


t1 = (1, 22, 53, 12)
t2 = (22, 34, 54, 22)
print("Contcatination of 2 tuple to get new tuple: ")
t3 = t1 + t2
print("Adding {} and {} to get: {}".format(t1, t2, t3))

print("[t1, t2]: ", [t1, t2])
# t1 = list(t1)
# t2 = list(t2)
tuple4 = [items for sublist in [t1, t2] for items in sublist]
tuple4 = tuple(tuple4)

print("Adding 2 tuples using list comprehension: {}".format(tuple4))

tuple5 = []
for subtuple in [t1, t2]:
    for item in subtuple:
        tuple5.append(item)

print("Tuple5: ",tuple(tuple5))

#find the unique element and print the tuple
tuple6 = (1, 9, 1, 6, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 2)
unique_tuple = []
for item in tuple6:
    if item not in unique_tuple:
        unique_tuple.append(item)
unique_tuple = tuple(unique_tuple)
print("Unique values in tuple: ", unique_tuple)

t1 = (1,)
t2 = (23, 42)
t3 = t2 + (2,)
print(t3)

sum = 0
for item in tuple6:
    sum += item

print(f"Sum of tuple {tuple6}: {sum}")

import random

tuple7 = ()
for i in range(5):
    x = random.randint(0,100)
    tuple7 += (x,)

print(f"Random 5 values of tuple: {tuple7}")

# tuple8 = ()
# for i in range(5):
#     x = random.randfloat(0.0,99.9)
#     tuple8 += (x,)

# print(f"{tuple8}")
