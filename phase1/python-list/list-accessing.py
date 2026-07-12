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