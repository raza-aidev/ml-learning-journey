list1 = [12, 13, "letters", 'a', 'b', 'c']

print("Original List: {}".format(list1))
list1.append("Love")
print("List aftyer appending: {}".format(list1))

# Append method just add anything by considering an object

list1.append((122, 133))
print(f"New list: {list1}")

print("Newly added part: {}".format(list1[-1]))