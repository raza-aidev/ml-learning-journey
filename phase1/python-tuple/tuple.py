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