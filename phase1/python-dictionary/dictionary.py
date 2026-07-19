dict1 = {"First Name": "Raza", "Age": 26, "Occupation":"Engineer", "Height":"6 7'", 2: "Numeric key"}

print("Accessing using [] Name: ", dict1["First Name"])
print(f"Accesing data using [] for 2: {dict1[2]}")

dict2 = dict()
if not dict2:
    print("dictionary is empty!")
else:
    print("dictionary has some data!") 

# list1 = (12, 23, "age", "Jamie Lanister")
# str1 = "Valar mugulis"
# dict3 = dict(str1)
# print("{}".f(dict3))

d1 = {("Name", "Age"): "Raza, 26", "Nationality": "Indian", "surname" : "Wangshuk"}
print(f"Dictionary: {d1}")
print(f"Dictionary: {d1[('Name', 'Age')]}")

print(f"Accesing dictionary elements using get() method: {d1.get('Nationality')}")
print(f"Accesiing element if it does not exist: {d1.get('Age','Not Found')}")

print(f"Accesing dictionary using key() method: {d1.keys()}")
print(f"Accessing dicionary using valu() method: {d1.values()}")
print(f'Accesinng dist using items() method: {d1.items()}')

for key, value in d1.items():
    print(f"Kay: {key}, value: {value}")

for key in d1.keys():
    print(f"Key: {key}")