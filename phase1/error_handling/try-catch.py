"""
Level 1 — try / except
Question 1 — Handle Division by Zero

Write a program that takes two numbers and divides them.

Handle the situation where the user enters 0 as the denominator.

Example:

Enter numerator: 10
Enter denominator: 0

Cannot divide by zero.
"""

"""
Question 2 — Invalid Integer

Write a program that asks the user to enter an integer.

If the user enters:

abc

the program should display:

Invalid input. Please enter a number.

Hint: Which exception does int("abc") generate?

"""


def division():
    try:
        a = int(input("Enter value of a:"))
        b = int(input("Enter value of b:"))
        result = a/b
        print(f"Division of {a} by {b}:")

    except ZeroDivisionError as er:
        print(f"Error found: {er}")

    except ValueError as er:
        print(er)
        print("Please enter number only!")
    
    else:
        print(result)

    finally:
        print("Process completed")


# division()


"""
Question 3 — List Index

Given:

numbers = [10, 20, 30, 40, 50]

Ask the user for an index and print the corresponding element.

Handle an invalid index.

Example:

Enter index: 10

Index does not exist.
"""

numbers = [10, 20, 30, 40, 50]

def get_value(index):
    try:
        return(numbers[index])
    
    except IndexError as er:
        print(er)
        print(f"Please endter Valid Index.")
    except ValueError as er:
        print(er)
        print("Enter valid integer only.")
    except Exception as er:
        print(er) 
    finally:
        print("Process completed...")

# get_value("12")



"""
Question 4 — Dictionary Key

Given:

student = {
    "name": "Raza",
    "age": 25,
    "city": "Pune"
}

Ask the user for a key.

Handle the situation where the key doesn't exist.

Example:

Enter key: salary

Key not found.

"""

dictionary = {
    "name": "raza",
    "age": 32,
    "height": "7 2'" 
}

def get_details(key):
    try:
        print(dictionary[key])
    except KeyError as er:
        print(er)
        print("NO Key with name {} present in dictionary.".format(key))
    except Exception as er:
        print(er)
    finally:
        print("Process completed")

# get_details("Quali")

"""
Level 2 — Specific Exceptions
Question 5 — Multiple Exceptions

Write a program that does:

a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))

result = a / b

Handle both:

ValueError
ZeroDivisionError

Your program should produce different messages.

For example:

abc

should produce:

Please enter a valid number.

while:

10
0

should produce:

Cannot divide by zero.

"""

def divide():
    try:
        a = int(input("Enter value of a:"))
        b = int(input("Enter value of b:"))
        result = a/b
    except (ValueError, ZeroDivisionError) as er:
        print(f"Exception: {er}. Please make corrections")
    else:
        print(result)
    finally:
        print("Process completed...")

# divide()


print("----Custom class-------")

class InvalidAgeError(Exception):
    pass

def is_eligible(age):
    
    try:
        if age < 18:
            raise InvalidAgeError
    except InvalidAgeError as er:
        print("Exception Occured: Please enter Valid Age.")
    else:
        print(f"Entered Age is: {age}")
    finally:
        print("Process completed...")

# is_eligible(21)


"""

Question 6 — except Exception as e

Write a program that intentionally performs an operation that could fail.

Catch the exception using:

except Exception as e:

Print:

Exception occurred: <actual exception message>

For example:

Exception occurred: division by zero

"""


def add(a, b):
    try:
        result = a + b
    except Exception as e:
        print(f"Exception occured: {e}")
    else:
        return result
    finally:
        print("Process Completed")


add(12,"12")