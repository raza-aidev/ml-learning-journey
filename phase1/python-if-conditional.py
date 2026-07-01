#--------------Example 1 ---------------
# if (age := int(input("Enter Age: ")) >= 18):
#     print("You are Eligible for Voting.")
# else:
#     print("you are a minor.")

#--------------Example 2 ---------------

# if(age := int(input("Enter Age: ")) and (Have_license := bool(input("Do you have any license? (yes/none)")))):
#     print("You are eligible to drive.")
# else:
#     print("You are a minor")

#-------------Example 3 ---------------
"""
Write a program that asks the user for an integer. 
If the number is perfectly divisible by 2, print "Even". Otherwise, print "Odd".
"""

# if ((num := int(input("Enter number: "))) % 2 == 0):
#     print(f"The number '{num}' you have entered is an Even number")
# else:
#     print(f"the Number '{num}' you have entered is an Odd number")

#-----------example 3----------------------
"""
A cinema charges different ticket prices based on a person's age. 
Write a program that asks for a user's age and determines their ticket price based on these rules

Age under 5: Free
Age 5 to 17: $10
Age 18 to 64: $15
Age 65 or older: $12
"""
# if((Age := int(input("Enter the valid Age: "))) < 5 ):
#     if(Age <= 0):
#         print("Not A Valid Age!")
#     else:
#         print("It's FREE!")
# elif((Age >= 5) and (Age <= 17)):
#     print("Please pay $10 per ticket.")
# elif((Age >= 18) and (Age <= 64)):
#     print("Please Pay $15.")
# else:
#     print("You ll have to pay $12.")


#-------------Example 4 -----------------


"""  Write a program to check if a given year is a leap year. A year is a leap year if it is divisible by 4, 
except for end-of-century years (ending in 00), which must also be divisible by 400."""

# year = int(input("Enter the year: "))

# if(((year%4) == 0) or (((year%400)==0)) and ((year%100) != 0)):
#     print("Year is a leap year.")
# else:
#     print("Year is not a leap year.")

#-------------example 5-----------------
""" oneliner conditional Operation or ternary operator"""

# age = int(input("ENter Age: "))

# status = "Adult" if age >= 18 else "minor"

# print(status)

