"""
Given an integer, n , perform the following conditional actions:

If n is odd, print Weird
If n is even and in the inclusive range of 2 to 5, print Not Weird
If n is even and in the inclusive range of 6 to 20, print Weird
If n is even and greater than 20, print Not Weird

"""
# n = int(input("Enter Number: "))

# if (n%2 != 0):
#     print("Weird")
# else:
#     if (2 <= n <= 5):
#         print("Not Weird")
#     elif(6 <= n <=20):
#         print("Weird")
#     elif(n > 20):
#         print("Not Weird") 

"""
The provided code stub reads two integers from STDIN, a and b. Add code to print three lines where:

The first line contains the sum of the two numbers.
The second line contains the difference of the two numbers (first - second).
The third line contains the product of the two numbers.

"""

# a, b = int(input("Enter Value of a: ")), int(input("Enter Value of b: "))

# print(a+b)
# print(a-b)
# print(a*b)


"""
The provided code stub reads two integers, a and b, from STDIN.

Add logic to print two lines. The first line should contain the result of integer division, a // b. 
The second line should contain the result of float division, a / b.

No rounding or formatting is necessary.

"""

a , b = int(input("Enter Value of a: ")), int(input("Enter Value of b: "))

print(a//b)
print(a/b)