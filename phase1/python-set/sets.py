set1 = {1, 2, 3, 4}
print("Set: {}".format(set1))

# set can't have duplicate objects

set2 = {1, 2, 1, 4, 5, 6, 2}
print("No Duplicate objects: {}".format(set2))

# Set is mutable, un-ordered, mutable object
# Adding new objects in set

set1.add(84)
print("New Set1: ",set1)

temp_set = {23, "raza", 'r', 1.1}
for i in temp_set:
    set1.add(i)
    
print("New Set1: {}".format(set1))

# temp_set = {23, "raza", 'r', 1.1}
# for obj in temp_set:
#     temp_set.remove(obj)

# temp_set.discard();
print("New temp set: ",temp_set)

#set comprehension 

set1 = {obj**2 for obj in range(14)}
print(f'Set using list comprehension: {set1}')

# nested set comprehension
set2 = {(obj1, obj2) for obj1 in range(5) for obj2 in range(6)}
print(f"nested if else: {set2}")




