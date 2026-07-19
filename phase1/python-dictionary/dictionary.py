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

print("+++++++++++++++Dictionaru modification+++++++++++")

person = {'name':'Raza', 'city':'Jhalna', 'age':22}
print(f"Person details initially: {person}")

person["age"] = 23
print(f"Latest details of {person['name']}: {person}")

person["Blood Group"] = "T+"
print(f"New details of {person['name']}: {person}")

print('Use of setdefault() funtion:')
person.setdefault('surname','pahadi')

print(f"Details of {person['name']} {person['surname']}: {person}")

print("+++++++++++poping out the keys from dictionary++++++++++++")
popped_value = person.pop('Blood Group')

print(f"The popped out value is: {popped_value} from {person}")

pop_items = person.popitem()
print(f'After doing popitem the dictionary will look like: {person}')

del person["name"]
print(f'using del keyword to delete the specific object from Dictionary: {person}')

print("++++++++++++++++++++++joining dict++++++++++++++++++++")

marks = {"Sattya":89, "Mubin":45, "Ashfaq": 90}
marks2 = {"Ratan":67, "siddhi":44, "Ravi": 99}

combine_marks = marks | marks2
print(f"New marks: {combine_marks}")

marks |= marks2
print(f"Marks: {marks}")

d1 = {'reha':100, 'Rohan':99}
marks.update(d1)
print(f'marks: {marks}')

d3 = {"Rudra":88, "Rishi":90}
new_marks = {**d3, **marks}
print("Combining dicts by unpacking oerator: {}".format(new_marks))

d4 = {"Rohini":77, "Rithru": 55}
latest_reg = marks.setdefault("Rakesh",67)
print(f"Marks: {marks}")