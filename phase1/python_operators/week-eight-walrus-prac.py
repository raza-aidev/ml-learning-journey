import logging

logger = logging.getLogger("week-eight-walrus-prac")
logger.setLevel(logging.DEBUG)

console = logging.StreamHandler()
console.setLevel(logging.DEBUG)

logger.addHandler(console)

"""
Problem 4 — While loop

Use a while loop and walrus operator to continuously accept numbers.

Stop when the user enters -1.

Example:

Enter number: 10
You entered 10


Enter number: 20
You entered 20


Enter number: 5
You entered 5


Enter number: -1
Program ended
"""

# while (num := int(input("Enter Number: "))) != -1:
#     logger.info(f"The entered number is: {num}")


"""
Problem 5 — Find first long word

Given:

words = ["cat", "dog", "elephant", "fox", "tiger"]

Using the walrus operator, find the first word whose length is greater than 5.

Expected:

elephant
"""

words = ["cat", "dog", "elephant", "fox", "tiger"]

# for index, value in enumerate(words):
#     larg_word = words[0]
#     if value := 

# for i in range(len(words)):
#     larg_word = words[0]
#     if  

# larg_word = [word for word in words if len(word) >= 5]
# print(larg_word)

for i in range(len(words)):
    if len((word := words[i])) > 5:
        print(word)
        break

"""
numbers = [10, 20, 30, 40, 50]
Use the walrus operator to calculate the sum and print:

Sum is greater than 100: 150

if the sum is greater than 100.
"""
 
numbers = [10, 20, 30, 40, 50]

if (sum_of_num := sum(numbers)) >= 100:
    logger.info(f"Sum of Number: {sum_of_num}")


"""
Problem 4 — While loop

Use a while loop and walrus operator to continuously accept numbers.

Stop when the user enters -1.

Example:

Enter number: 10
You entered 10

Enter number: 20
You entered 20

Enter number: 5
You entered 5

Enter number: -1
Program ended

"""

while (num := int(input("Enter the number: "))) != -1:
    logger.info(f"The entered number is: {num}")

