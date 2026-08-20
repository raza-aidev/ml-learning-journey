
"""
Problem 1 — Even number

Take a number from the user using the walrus operator.

If the number is even, print:

25 is odd

or

24 is even
"""

# import logging

# #Create logger
# logger = logging.getLogger("week-seven-warus-prac")
# logger.setLevel(logging.DEBUG)

# #create console
# console = logging.StreamHandler()
# console.setLevel(logging.DEBUG)

# #Add console to logger
# logger.addHandler(console)

# if num := int(input("Enter a number: "))%2 == 0:
#     logger.debug(f"Entered number {num} is EVEN.")
# else:
#     logger.debug(f"Entered number {num} is ODD.")

"""
Problem 2 — Password length

Ask the user to enter a password.

Using :=, store the password and check whether its length is at least 8.

Expected behavior:

Enter password: python123
Password is valid
"""
import logging

#Create logger
logger = logging.getLogger("week-seven-walrus-prac")
logger.setLevel(logging.DEBUG)

#Create console handler
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)

#Add console to logger
logger.addHandler(console)


if len(password:=input("Enter the password:")) < 8:
    logger.debug(f"Password should have atleast 8 charactors")
else:
    logger.debug("Welcome!")

       