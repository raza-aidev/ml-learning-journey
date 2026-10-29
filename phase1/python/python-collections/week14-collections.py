from collections import namedtuple

Points = namedtuple("Points", ['x', 'y', 'z'])
p1 = Points(12, 13, 14)
print(p1)

print(p1._fields)