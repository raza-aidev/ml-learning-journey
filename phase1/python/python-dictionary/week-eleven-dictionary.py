import logging

logger = logging.getLogger('week-eleven-dictionary')
logger.setLevel(logging.INFO)

console = logging.StreamHandler()
console.setLevel(logging.INFO)

logger.addHandler(console)

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

d1 = {'age': 14, "name": 'Sarah', 'height': "5 4'"}

logger.info(d1.get('age'))
logger.error(d1.get('NAME')) # DEBUG, INFO, WARNING, ERROR, CRITICAL

logger.error(f"Not present: {d1.get('NAME')}")

# logger.error(f"{d1['occupation']}")


#Adding data in dictionary examples

details = {"Age":15, "Name": "Ali", "Occupation":"10th Std(Studying)", "School_Name": "Trinity School", "Weight":56}

logger.info(f"Original Dict: {details}")

details["Surname"] = "Khan"

logger.info(f"Updated dictionary: {details} ")

# Deletion of data from dictionary

del details["Surname"]
logger.info(details)

# del details["Surname"] # If the keywe are deleting from the dict is not present and we are usinf del keyword for deletion then we will get KeyError
# logger.info(details)

popped_details = details.pop("Age")
logger.info(f"Popped Value: {popped_details}")
logger.info(f"Final details: {details}")

last_item = details.popitem()
logger.info(f"Last Pooped Item: {last_item}")

details.clear()
logger.info(f"Emptyed Dict: {details}")