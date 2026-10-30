from collections import namedtuple

Points = namedtuple("Points", ['x', 'y', 'z'])
p1 = Points(12, 13, 14)
print(p1)

print(p1._fields)

Coordinates = namedtuple("Coordinates", ["x", "y", "z"])
c1 = Coordinates(12, 13, 15)

print(c1)
print(c1._fields)

new_cord = [12, 56, 89]
c2 = Coordinates._make(new_cord)

print(c2)

print(c2._asdict())
print(f'Getting value like a dictionary: {c2._asdict().values()}')

a, b, c = c2._asdict().values()
print(a, b, c)

result = a+b+c
print(result)