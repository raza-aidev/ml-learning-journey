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

# import frozenset

# set3 = frozenset({1,2,3.4})
# print(f"Original frozen set: {set3}")

# # set3.add(5)
# set3.remove(3)



#Accessing the set
set4 = set(range(20))
print(f"set4: {set4}")
result = set()
for obj in set4:
    if obj%2 == 0:
        result.add(obj) 

print(f"result: {result}")

#acessing using using methods

set5 = {12, 11, 2, 54}
if set5.issubset(set4):
    print(f"Set 5 is the subset of set4: ")
else:
    print(f"set 5 is not the sub-set of set4:")

#accesing usinh combination iteration

from itertools import combinations
set6 = set(range(5))
list2 = {tup for tup in combinations(set6, 2)}

print("list of combination of tup: ",list2)

# Adding elements in Set

lang1 = {"C", "C#", "Perl", "C++"}
lang2 = {"Python", "Java", "JavaScritp", "C++", "Type-Script"}


# lang2.add(5)


lang2.update({"c-Py"})

print(f"Lang2: {lang2}")

lang3 = lang1 | lang2
print(f"Lang3: {lang3}")


lang4 = lang1.union(lang2)
print(f"Lang4: {lang4}")

#Adding elemenst in python using Set comprehension 
list3 = ["Shell", "Groovey"]

# print(obj)
lang5 = [obj for obj in list3]
print(f"Lang5: {lang5}")

# lang1.remove("Perl")
# print(f"after removing the Perl from lang1: {lang1}")

# lang1.discard("Perl")
# print(f"Removing non-existing 'Perl' object from Set Lang1: {lang1}")

# lang1.pop()
# print(f"Popping element: {lang1}") #pops the arbitatory element from the Set

s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}

s1.difference_update(s2)
print(f"Set 1 difference update of Set 2 is: {s1}")

s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}

result = s1 ^ s2 #We need to store the result in new set
print(f"Set 1 Syemmetric difference of Set 2: {result}")

s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}

result2 = s1.symmetric_difference(s2) # It returns a new set 
print(f"Set 1 symmetric difference of Set 2: {result2}")

s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}

s1.symmetric_difference_update(s2)  # it returns a new set
print(f"Set 1 symmetric difference of Set 2: {s1}")

s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}

s5 = s1.intersection(s2)
print(f"Set 1 intersection set 2: {s5}")

s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}

s3 = s1 - s2
print(f"s1 - s2 = {s3}")

s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}

s4 = s1.intersection_update(s2)
print(f"Intersection Update of s1 and s2: {s1}")