"""
Question 11 - Combine Names and Marks
names = ["Raza","John","Alex"]

marks = [80,92,70]
"""

names = ["Raza","John","Alex"]

marks = [80,92,70]

details = list(zip(names,marks))
# details = dict(zip(names, marks))
print(details)


"""
Question 12 - Create Dictionary

Input

keys = ["name","age","city"]

values = ["Raza",25,"Pune"]

"""
keys = ["name","age","city"]

values = ["Raza",25,"Pune"]

print(f"{dict(zip(keys, values))}")


"""
Question 13 - Sum Two Lists
a = [10,20,30]

b = [1,2,3]

Output

[11,22,33]
"""

a = [10,20,30]

b = [1,2,3]

def sum_of_list(*newlist):

    for nums in newlist:
        result = nums[0] + nums[1]
        return result


newlist= zip(a,b)

listsum = list(map(sum_of_list, newlist))
# listsum = list(map(lambda *newlist : [num[0]+num[1] for num in newlist], newlist))

print(listsum)


"""
Question 14 - Print Student Report
names = ["A","B","C"]

marks = [80,60,90]

Print

A scored 80
B scored 60
C scored 90

"""




