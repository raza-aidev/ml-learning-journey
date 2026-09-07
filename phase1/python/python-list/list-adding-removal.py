list1 = [12, 13, "letters", 'a', 'b', 'c']

print("Original List: {}".format(list1))
list1.append("Love")
print("List aftyer appending: {}".format(list1))

# Append method just add anything by considering an object

list1.append((122, 133))
print(f"New list: {list1}")

print("Newly added part: {}".format(list1[-1]))
list1.extend("ABDUL")
print(f'Extending ABDUL string in exusting list: {list1}') #extending any list will loop through each charactors passed in as aparameters

list2 = []
list2 = list2 + list1

print(f"new list: {list2}")
list2.remove((122,133))
print(f"Remove: {list2}")

list2.insert(7, (122,133))
print(f"Inserting: {list2}")

list2.insert(100, "Sayyed")
print(f"If we add index more than length of the list: {list2}")

list2.insert(-100, "Start")
print(f"If we add index more than length of the list: {list2}")

print(f"Popping Last Item: {list2.pop()}")

print(f"Indexing Popping of items: {list2.pop(3)}")
# print(f"Indexing Popping of items: {list2.pop(300)}")  #out of index error

list3 = list2[:]
list4 = list1[:]
print(f"New List: {list3}")
list3.clear()
print(f"List After clearing: {list3}; getting Empty list")
# del list4
# print(f"list after deleteion: {list4}") # Going to get error
# list_new = []
# while len(list_new) != 10:
#     list_new.append(input("Enter the string:"))
# print(f"Your final list is: {list_new}")
# for data in list_new:
#     print(data, end=" ")

# print()
# count = 0;
# print(reversed(list1))
# list5 = reversed(list1)
# print(list5)
# # for item in list1:
# #     print(item)

# # while count < len(list1):
# #     print(f"Reversed List: {list1[count]}")
# #     count+=1;

print("iterating hrough 2 lists: ")
for item1, item2 in zip(list1, list2):
    print(f"List1 string: {item1} list2 String: {item2}")

list_2d = [[12, 13, 14],["Ask",'your',"manager", "for", "feedback"],['a','b','c','d','e'],[12.3, 13.6,11.6,113.3]]
for _ in list_2d:
    print(f"Printing list: {_}")
    for index, item in enumerate(_):
        print("Item at {}: {}".format(index,item))