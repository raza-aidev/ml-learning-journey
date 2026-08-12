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


# add(12,"12")

"""
Question 2 — Invalid Integer

Write a program that asks the user to enter an integer.

If the user enters:

abc

the program should display:

Invalid input. Please enter a number.

Hint: Which exception does int("abc") generate?
"""

def get_data():
    try:
        num = int(input("Enter the number: "))
    except ValueError as er:
        print(f"Exception has occurred: {er}")
    else:
        print(f"The entered number {num}")
    finally:
        print("Process has been completed.")

# get_data()

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

def get_numbers(index):
    try:
        print(numbers[index])
    except IndexError as er:
        print(f"Exception occurred: {er}")

# get_numbers(12)

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



try:
    student = {
        "name" : "Raza",
        "Age" : 33,
        "city" : "Pune"
    }

    # key = input("Enter the Key: ")
    # print(student[key])

except KeyError as er:
    print(f"Exception occurred: KeyError: Key {er} not found in {student}")

"""
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

def division2():
    try:
        a = int(input("Enter value of a: "))
        b = int(input("Enter value of b: "))

        result = a/b

    except ValueError as er:
        print("Please enter numaric value.")

    except ZeroDivisionError as er:
        print(f"Value of b is {b}. Please enter valid value.")

    else:
        print(f"Result: {result}")
    finally:
        print("Process Completed.")

# division2()


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




"""
Question 7 — Specific vs Generic Exception

Create a program that has:

try:
    ...
except ValueError:
    ...
except ZeroDivisionError:
    ...
except Exception as e:
    ...

Create different scenarios that trigger each exception.

Think about:

Why should you put:

except Exception as e:

after the specific exceptions?
"""

def calculate():
    try:
        num1 = int(input("Enter 1st number: "))
        num2 = int(input("Enter 2nd Number: "))

        # count += 1

        result = num1 / num2
        prit("Hello")
    except ZeroDivisionError as er:
        print(f"Exception occurred: {er}")
    
    except ValueError as er:
        print(f"Exception Occurred: {er}")
    
    except Exception as e:
        print(f"Exception occured (Generic exception): {e}")
    else:
        print(f"{result}")
    finally:
        print("Process completed..")

calculate()

"""
Question 8 — Successful Calculation

Write a program that:

Takes two numbers.
Divides them.
Handles ValueError and ZeroDivisionError.
Uses else to print the result only if no exception occurred.

Expected:

Enter number 1: 20
Enter number 2: 5

Division successful.
Result: 4.0

But:

Enter number 1: 20
Enter number 2: 0

Cannot divide by zero.

The else block should not execute in the second case.
"""