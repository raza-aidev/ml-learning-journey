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