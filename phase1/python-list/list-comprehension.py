days = ["Mon", "Tues", "Wed","Thus", "Fri", "Sat", "Sun"]
new_days = [day for day in days]
print(f"New List: {new_days}")

sqr = [num**2 for num in range(10)]
print("Square: ", sqr)

Even = [i for i in range(20) if i%2==0]
print(f"Even: {Even}")

Odd = [f for f in range(20) if f%2!=0]
print("Odd: {}".format(Odd))

evn = [num for num in range(20) if num%2==0 and num>=10]
print(f"evn: {evn}")

evn2 = ["Even" if num%2==0 else "Odd" for num in range(1,31)]
print("evn2: {}".format(evn2))

l1 = [1, 2, 3,4]
l2 = ["Hello", "How", "Are", "You", "?"]

result = [(x,y) for x in l1 for y in l2]
print("Nested list Result: {}".format(result))

res1 = [[1,2], [2,3], [3,4], [4,5]]
res2 = [item for rows in res1 for item in rows]
print(f"Flatening of List of list: {res2}")

res3 = [[x*y for x in range(5)] for y in range(5)]
print("Nested list creation: {}".format(res3))