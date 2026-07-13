days = ["Mon", "Tues", "Wed","Thus", "Fri", "Sat", "Sun"]
new_days = [day for day in days]
print(f"New List: {new_days}")

sqr = [num**2 for num in range(10)]
print("Square: ", sqr)

Even = [i for i in range(20) if i%2==0]
print(f"Even: {Even}")

Odd = [f for f in range(20) if f%2!=0]
print("Odd: {}".format(Odd))