mainString = "LearningML"
a = "ea"
b = 'learn'
c = 'ML'

#----------------------------------------
# Use of 'in' membership operator

print("---------------------------")
print('membership operator "in" list')
print(a, "in", mainString, ": ", a in mainString)
print(b, "in", mainString, ": ", b in mainString)
print(c, "in", mainString, ": ", c in mainString)

# there are 2 types of membership operators "in" and "not in"
# membership operator checks whether the sub string is present in main string
# or you can say that an item is a part list or tuple or a part of any sub-list or sub-tuple of list or tuple included in.


#----------------------------------------
# Use of 'not in' membership operator

print("---------------------------")
print('membership operator "not in" list')
print(a, "not in", mainString, ": ", a not in mainString)
print(b, "not in", mainString, ": ", b not in mainString)
print(c, "not in", mainString, ": ", c not in mainString)


#----------------------------------------
# Use of in and not in operators in list and tuple

list1 = [10, 20 , 30, 12]
l1 = 10; l2 = 20

print("---------------------------")
print("membership operator in list")
print(l1, "in ", list1, " :", l1 in list1)
print([l1,l2], "in ", list1, " :", [l1,l2] in list1)

#here list element can be found using in operator
#However, if you try to check if two successive numbers are present in a list or tuple, 
#the in operator returns False. If the list/tuple contains the successive numbers as a 
#sequence itself, then it returns True. Henece, here we got false as we are trying to search a sequesnce in a list 
#not containing any sequence


tuple1=(10, 20, 30, 40)
t1=10
t2=20

print("---------------------------")
print("membership operator in tuple")
print(t1, "in ", tuple1, " :", t1 in tuple1)
print((t1,l2), "in ", tuple1, " :", (t1,l2) in tuple1)

print("---------------------------")
print("membership operator in tuple where sequence is present in parent sequence")

list1 = [[10, 20] , 30, 12]
print([l1,l2], "in ", list1, " :", [l1,l2] in list1)


print("---------------------------")
print("membership operator in Set")

set1 = {12, 13, 14, 15}
print(12, "in ", set1, ": ", 12 in set1)

set1 = {(12, 13), 14, 15}   # You can't add mutable list in immutable set because set uses hastable in python. 
print((12, 13), "in ", set1, ": ", (12, 13) in set1)

print("---------------------------")
print("membership operator in Dictionary")

# membership operator only finds key in dictionary not the value

dict1 = {"1": 12, "2": 20}
print("'1' a key in ", dict1, ": ", "1" in dict1)
print(20, "a key value in", dict1, ": ", 20 in dict1)