dict1 = {'a': 2, 'B':"Harry", 'c':'Qali'}

dict1['a']=3

print(dict1)

dict2 = dict([("As", 2), ("A", "Work"), (4, "12")])
print(dict2)

keys = ["key1", 'key2', "Key3"]
dict3 = dict.fromkeys(keys, 0)
print(dict3)

dict3["key1"] = 1

print(dict3)


d = dict.fromkeys(["k",'l'], [])
print(d)
d['k'].append("3")
print(d)