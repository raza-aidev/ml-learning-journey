""" Python has 2 Identity operators
    1. is
    2. is not
 
 The identity operators are used to identify if 2 variables are reffering to the same
 object in the memory locations. 
 
 Note: this operator does not comoare value like '==' operator """

print("-----------------------")
print("Identity operator example with numeric values: ") 

a = 10
b = 10
print(a is b)

# verifying the bigger number
a = 1000
b = 1000

print(a is b)

print("-----------------------")
print("Identity operator example with sequence values: ") 

l1 = [10, 20]
l2 = [10, 20]
l3 = l1

print(l1 is l2) # false: because list is mutable and store in diffrent location in memory although the values inside the lists are same.
print(l2 is l3)  # false: because list is mutable and store in diffrent location in memory although the values inside the lists are same. 
print(l1 is l3)  # True: Because l1 and l3 variables(symbolic representation) are reffering to the same object type in the memoy location.

