list1 = ["a", 'b', "c", 12, 13.5, "letters", 'you']
str1 = "letters"
print("accesing every thrid element of a list: ", list1[::3])

print(f"Origination list is {list1}")
print(f"reversed list is {list1[::-1]}")
print(f"reversed pf the string {str1} is {str1[::-1]}")

print(f"Let's check original list after revesal: {list1}")


print(f"Accessing indivisual values list1[1]: {list1[1]}")
print(f"negative value accessing: {list1[-4]}")
print(f"Accessing each element using for loop: ")
for items in list1:
    print(f"{items}")

for i in range(len(list1)):
    print(f"Index: {i}, Value: {list1[i]}")


print("-----------example of enumrate----------")
for index, value in enumerate(list1):
    print(f"Index: {index} and Value: {value}")

print("Making copy of a list:")
list_copy1 = list1   # this does not make a copy but the new variable name "Label" is referencing to the list object of list1

print(list_copy1)
list_copy = list1[::]
print(f"Actual copy of a list: {list_copy}")


print("Making changes in the 1st example of list copy and tcheck if it is making any change to original one.")
list_copy1[2]="Hello"
print(f"printing original list: {list1}")
list_copy[1] = "Changed Value"
print(f"{list1}")

list2 = [2, 14, 1, 0, 16]
print(f"{list2}")

list3 = [[1,2,3],['a', 'b', 'c'],[12.45, 'letters', 'build']]
print(f"accessing ")