"""
Create Square all numbers

numbers = [2, 4, 6, 8, 10]

"""
numbers = [2, 4, 6, 8, 10]
squares = list(map(lambda num: num**2, numbers))

print(squares)


"""
Question 2 - Convert to Uppercase
names = ["raza", "john", "alex", "maria"]
"""

names = ["raza", "jhon", "alex", "maria"]

def to_upper(*names):
    
    for name in names:
        return str(name.upper())
    

upper_case = list(map(to_upper, names))

print(upper_case)

"""
words = ["Python", "Java", "C++", "JavaScript"]
Question 3 - Find Length of Every Word
"""
words = ["Python", "Java", "C++", "JavaScript"]
def find_length(*words):
    for word in words:
        return len(word)

word_length = list(map(find_length, words))

print(word_length)


"""
Add 18% GST to every price.
prices = [100, 250, 500, 1000]
"""
prices = [100, 250, 500, 1000]

GST = list(map(lambda num: (num*0.18)+num, prices))

print(GST)

"""
Convert Celsius to Fahrenheit
celsius = (temps * 9/5)+32
temps = [0, 10, 20, 30, 40]

"""
temps = [0, 10, 20, 30, 40]
temps_celsius = list(map(lambda temp: (temp*9/5)+32 , temps))

print(temps_celsius)

"""

Question 18
qty = [2,4,3]

price = [100,200,50]

Calculate total price of every item.

Output

[200,800,150]

"""

qty = [2,4,3]

price = [100,200,50]

def get_sum(*prices):
    
    result = 0
    for price in prices:
        result = price[0] + price[1]
        return result

consolidated = zip(qty, price)


sum_of_prices = list(map(get_sum, consolidated))

print(sum_of_prices)


"""
Question 19
first = ["Raza","John"]

last = ["Khan","Doe"]

Output

['Raza Khan','John Doe']
"""

first = ["Raza","John"]

last = ["Khan","Doe"]

def form_names(*names):
    full_name = ""
    for name in names:
        full_name = name[0] + " " + name[1]
        return full_name

names = zip(first, last)

full_names = list(map(form_names, names))

print(full_names)

"""
Question 20
subjects = ["Math","Science","English"]

marks = [90,85,95]

Output

{
'Math':90,
'Science':85,
'English':95
}
"""

subjects = ["Math","Science","English"]

marks = [90,85,95]

dict_1 = dict(zip(subjects, marks))


print(dict_1)


"""
employees = [
("John",50000),
("Alex",60000),
("Maria",45000)
]

Increase every salary by 10%.
"""

employees = [
("John",50000),
("Alex",60000),
("Maria",45000)
]

def sal_increament(*sals):
    new_sal = 0
    for sal in sals:
        new_sal = sal[1] + (0.1 * sal[1])
        return (sal[0], new_sal)

new_salary_details = list(map(sal_increament, employees))
print(new_salary_details)

"""
Question 22 - Eligible Voters
people = [
("John",15),
("Alex",22),
("Maria",18),
("Raza",25)
]

Return only eligible voters (age ≥ 18).
"""
people = [
("John",15),
("Alex",22),
("Maria",18),
("Raza",25)
]

def eligible_voters(*voters): # we receive (('Jhon', 15),) which is tuple of tuple, eache elemnt is send in a tuple only
    for voter in voters: 
        if voter[1] >= 18:
            return voters

new_voter_list = list(filter(eligible_voters, people))
print(new_voter_list)


"""
marks = [91,82,76,64,50]

Convert marks into grades.

90+ → A
80+ → B
70+ → C
60+ → D
else → F

Output

['A','B','C','D','F']

"""

marks = [91,82,76,64,50]

def get_grade(mark):
    # print(mark)
    if mark >= 90:
        return "A"
    elif 89 >= mark >= 80:
        return "B"
    elif 79 >= mark >= 70:
        return "C"
    elif 69 >= mark >= 60:
        return "D"
    else:
        return "E"

grades = list(map(get_grade, marks))

print(grades)

"""
Question 24 - Shopping Cart
products = [
("Laptop",50000,2),
("Mouse",500,3),
("Keyboard",1000,2)
]

Calculate total cost of each product.

Expected

[
("Laptop",100000),
("Mouse",1500),
("Keyboard",2000)
]
"""

products = [
("Laptop",50000,2),
("Mouse",500,3),
("Keyboard",1000,2)
]

def total_cost(*items):
    net_amount = 0
    for product, cost, quantity in items:
        net_amount = cost * quantity
        return (product, net_amount)

cost_of_each_product = list(map(total_cost, products))
print(cost_of_each_product)


"""
Question 25 - Highest Scoring Student
names = ["John","Alex","Maria","Raza"]

marks = [78,92,85,88]

Using zip(), determine the student with the highest marks.

Expected

Alex 92
"""
names = ["Nisa","John","Alex","Maria","Raza", "Ravi"]

marks = [99,78,92,85,88,56]

score_by_name = list(zip(names, marks))

# print(score_by_name)

max_score = score_by_name[0] #('Jhon', 78)
max_value = max_score[1]
for i in range(1, len(score_by_name)):
    # print(score_by_name[i][1])
    if max_value >= score_by_name[i][1]:
        continue
    elif max_value < score_by_name[i][1]:
        max_score = score_by_name[i]
        max_value = score_by_name[i][1]
    
print(max_score)

# for value in max_score:
#     print(value, end=",")
