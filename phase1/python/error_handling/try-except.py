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

# calculate()

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


"""
Question 12 — Age Validation

Write:

def check_age(age):
    ...

If age is less than 18, raise:

ValueError("Age must be 18 or above")

Otherwise print:

Eligible

Test:

check_age(15)

Expected:

ValueError: Age must be 18 or above
"""

def check_age():
    try:
        age = int(input("Enter the age: "))
        if age >= 18:
            print("Your are eligible for vote!")
        else:
            raise ValueError("Enter the age 18 or above 18")
    except ValueError as er:
        print(f"Exception occurred: {er}")
    finally:
        print("Process Completed!")

# check_age()

"""
Question 13 — Salary Validation

Create:

def set_salary(salary):
    ...

Rules:

Salary cannot be negative.
Salary cannot be zero.
Salary must be numeric.

If salary is invalid, raise an appropriate exception.

Example:

set_salary(-5000)

should raise something like:

ValueError: Salary cannot be negative

"""


def set_salary(salary):
    if type(salary) != int:
        raise ValueError(f"Salary must be Numaric.")
    elif salary > 0:
        return f"You have received salary: {salary}"
    elif salary < 0:
        raise ValueError(f"Salary can't by negative: {salary}")
    elif salary == 0:
        raise ValueError(f"Salary can't be Zero.") 
    else:
        raise SyntaxError(f"Enter Valid salary!")

try:
    # salary = int(input("Enter the salary: "))
    # message = set_salary(salary)
    message = ""
except (ValueError, SyntaxError, Exception) as er:
    print(f"Error: {er}")
else:
    print(message)
finally:
    print("Salary setting attempted.")


# a = 10
# b = 12.4
# print(type(a))
# print(type(b))


"""
Question 14 — Password Validation

Create:

def validate_password(password):
    ...

Rules:

Minimum 8 characters.
Must contain at least one digit.
Must contain at least one uppercase letter.

If validation fails, use raise.

Example:

validate_password("hello")

should raise an exception.

Challenge: Decide whether ValueError or another built-in exception is most appropriate.

"""
password = "Password"
print(password.isalnum())

# class LengthError(Exception):
#     pass

# class NotAlphaNumeric(Exception):
#     pass

# class NoUpperCaseError(Exception):
#     pass

# def validate_password(password):
#     if len(password) >= 8:
#         if password.isalnum():
#             for i in range(len(password)):
#                 if password[i].isupper():
#                     break
#             else:
#                 raise NoUpperCaseError("Password must contain at least one uppercase letter.")
#         else:
#             raise NotAlphaNumeric("Password must contain at least one digit")
#     else:
#         raise LengthError("Password must be greater than 8 character.")

# try:
#     password = input("Enter the password: ")
#     validate_password(password)
# except (LengthError, NotAlphaNumeric, NoUpperCaseError) as er:
#     print(f"Error occurred: {er}")
# else:
#     print("Welcome!!!")
# finally:
#     print("Process Finished!")