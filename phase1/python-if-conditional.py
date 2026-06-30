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
if((Age := int(input("Enter the valid Age: "))) < 5 ):
    if(Age <= 0):
        print("Not A Valid Age!")
    else:
        print("It's FREE!")
elif((Age >= 5) and (Age <= 17)):
    print("Please pay $10 per ticket.")
elif((Age >= 18) and (Age <= 64)):
    print("Please Pay $15.")
else:
    print("You ll have to pay $12.")