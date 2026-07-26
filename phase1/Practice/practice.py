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

# a , b = int(input("Enter Value of a: ")), int(input("Enter Value of b: "))

# print(a//b)
# print(a/b)


"""
Task
The provided code stub reads an integer, n, from STDIN. For all non-negative integers ,i<n print i2.

Example

"""

# n = int(input("Enter integer number: "))

# for i in range(n):
#     if i > 0:
#         print(i*i)


"""

An extra day is added to the calendar almost every four years as February 29, and the day is called a leap day. It corrects the calendar for the fact that our planet takes approximately 365.25 days to orbit the sun. A leap year contains a leap day.

In the Gregorian calendar, three conditions are used to identify leap years:

The year can be evenly divided by 4, is a leap year, unless:
The year can be evenly divided by 100, it is NOT a leap year, unless:
The year is also evenly divisible by 400. Then it is a leap year.
This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years. Source

Task

Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False.

Note that the code stub provided reads from STDIN and passes arguments to the is_leap function. It is only necessary to complete the is_leap function.

"""

# def is_leap(year):
#     if(year%4 == 0 and year%100 != 0 or year%400 == 0):
#         return True
#     else:
#         return False

# year = int(input("Enter the year: "))

# print(is_leap(year))


"""
The included code stub will read an integer, , from STDIN.

Without using any string methods, try to print the following:


Note that "" represents the consecutive values in between.

"""

n = int(input("Enter the numeber to form entire equesnce: "))

for i in range(n+1):
    if(i>0):
        print(f"{i}", end="")
