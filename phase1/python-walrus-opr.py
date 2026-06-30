number = [1, 3, 4, 5]

if (len(number)>3):
    print("length: ", len(number))


print("--------------------")
print("Use of walrus operator.")
if ((num := len(number))>3):
    print("length: ", num)

""" The Walrus operator is use to assign a value to a variable and then immediately use the value 
in an expression.

In Short: Assign first, then immediately use the assigned value.

it is also called as assignment expression operator.
"""



print("-------Example 1-------")

"""
replicate:
age = int(input("Enter Age: "))

if (age >= 18):
    print(f"This person is adult, Age: {age}")
"""

if ((age := int(input("Enter Age: ")))>=18):
    print(f"This person is adult, Age: {age}")
else:
    print(f"This person is not an Adult. Age: {age}") 


"""
replicate:

line = input("Enter text: ")

while(line != 'quit'):
    print(line)
    line = input("Enter text: ")
"""
print("------Example 2-------")

while ((line := input("Enter text: ")) != 'quit'):
    print(line)



print("-----Example 3-------")
print("list comprehension with walrus operator:")

fruites = ["apple", "Banana", "Kiwi"]
result = [ length := (len((for word in fruites:))) > 0 ]