# def greet(name):
#     print(f"Welcome, {name}")


# greet("Abdul")\

# def add(a,b,c):
#     result = a + b + c
#     return result

# print(add(10,23,10))

# def return_multiple():
#     a = 10; b = 12; c=13
#     return a,b,c

# x,y,z = return_multiple()

# print("x: ", x, "y: ",y, "z: ", z)

# def return_multiple():
#     a = 10; b = 12; c=13
#     return a,b,c
# tuple1 = ()
# tuple1 = return_multiple()

# print("Tuple Value: ", tuple1)

#-------------types of function arguments------------

def addition(a,b): 
    """Positional_arguments"""
    result = a + b
    return result

print(addition(12, 13))

def mens_bio(age, name):
    """ keyword type aruments """
    return f"name is: {name} and Age is: {age}"

print(mens_bio(name="Kartik", age="28"))

def multiplication(a, b,/):
    """ positional-only type"""
    return a*b

print("Result of multiplication is: ", multiplication(12,2))



