"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
"""

numbers = list(range(1, 11))
squares = [num ** 2 for num in numbers]
print(squares)

"""
Problem 6 — Squares

Given:

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Create a list containing the squares of all numbers.

Expected:

[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(f"Squares = {[number ** 2 for number in numbers]}")