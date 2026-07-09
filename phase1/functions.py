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

# def addition(a,b): 
#     """Positional_arguments"""
#     result = a + b
#     return result

# print(addition(12, 13))

# def mens_bio(age, name):
#     """ keyword type aruments """
#     return f"name is: {name} and Age is: {age}"

# print(mens_bio(name="Kartik", age="28"))

# def multiplication(a, b,/):
#     """ positional-only type"""
#     return a*b

# print("Result of multiplication is: ", multiplication(12,2))

def area_of_rectangle(*, length, breadth, height):
    """ keyword-type only """
    return f"Area of a rectangle: {length*breadth*height}"

# print("Area of a rectangle: ", area_of_rectangle(length=10, breadth=9, height=12))


def add(*nums):
    """ arbitrary Arguments"""
    result = 0
    for num in nums:
        result += num
    
    return f"Result of addition is: {result}"

# print("Result of adding", add(21,12,15,17,10))

def get_total_marks_of_student(name, *marks):
    """ Example of arbitrarry arguments """
    total = 0
    for mark in marks:
        total += mark
    
    return f"Total of {name} is: {total}"

# print(get_total_marks_of_student("Harish", 12, 13, 15,16))
# print(get_total_marks_of_student("Namita", 11, 9, 12.5, 8))

def generate_dic_for(**details):
    return f"The dictionary of requested details: {details}"

# print(generate_dic_for(name="Abdul Razzak", age=27, city="Pune"))
# print(generate_dic_for(Object="Smart Phone", Brand="Apple", Model="I-Phone 17 Pro", Storage="1TB"))

PI = 3.14