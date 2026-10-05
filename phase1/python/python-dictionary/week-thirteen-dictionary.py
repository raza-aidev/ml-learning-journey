import logging

logger = logging.getLogger("week-thirteen-dictionary")
logger.setLevel(logging.DEBUG)

console = logging.StreamHandler()
console.setLevel(logging.DEBUG)

logger.addHandler(console)


dict1 = {
    "Age": 12,
    "Height": "6 2'",
    "Weight": "109 kg",
    "Occupation": "B.Tech"
} 

logger.debug(f"Age: {dict1.get('Age')}")

dict1['Age'] = 34

logger.debug(f"Updated Age: {dict1.get('Age')}")

dict1["City"] = 'Pune'

logger.debug(f"Updated Dictionary: {dict1}")

age = dict1.pop("Age")
logger.debug(f"Popped Item 'Age': {age}")

logger.debug(f"The updated Dictionary: {dict1}")

last_item = dict1.popitem()

logger.debug(f"The last item is: {last_item}")

del dict1["Weight"]
logger.debug(f"the updated dictionry: {dict1}")

dict1.clear()

logger.debug(f"The emptied Dictionary: {dict1}")


data = {
    "Name": "Raza",
    "Age": 30,
    "Weight (Kg)": 109,
    "Height (cm)": 114
}

logger.info(f'Is Name present in data: {"Name" in data}')
for key in data:
    logger.info(f"{key}: {data[key]}")


logger.info(f"Age: {data.get('Age')}")
logger.info(f"{list(data.keys())}")
logger.info(f"{list(data.values())}")
logger.info(f"{list(data.items())}")

logger.info(f'state: {data.get("State","Maharshtra")}')


data.update({"State": "Maharashtra"}) 
logger.info(data)

data.update({"Last_name": "S"})

logger.info(f'{data}')



data2 = {
    "Name": "Raza",
    "Age": 30,
    "Weight (Kg)": 109,
    "Height (cm)": 114
}

data.setdefault("Name", "Raza AI")
print(data)
data.setdefault("City", "Pune")
print(data)


dataset = ["apple", 'Banana', 'Kiwi', "Orange", 'Dragonfruit', "Papaya", "Watermelon", "Malta", "Guava", "Pineapple", "chiku"]
sets = {}
for word in dataset:
    sets.setdefault(word[0], []).append(word)

print(sets)

# Separate the students according to classes

student_details = [("Class A", "Navin"), ("Class A", "Pravin"), ("Class C", "Radha"), ("Class B", "Rudra"), ("Class C", "Abhinav"), ("Class A", "Uday"), ("Class B", "Mala"), ("Class C", "Sapna")]

sections_details = {}

for key, value in student_details:
    sections_details.setdefault(key, []).append(value)

print(sections_details)   


diction_of_nums = {x: x**2 for x in range(1, 10)}
print(diction_of_nums)


num_type = {x: ("Even" if x%2 == 0 else "Odd") for x in range(1,20)}
print(f"Dictionary comprehension: {num_type}")
 
num_type_2 = {x: "even" for x in range(1, 20) if x%2==0}
print(num_type_2)

keys = ["Name", "City", "State"]
values = ["Riya", "Kolkata", "Karanakata"]

details = {k : v for k, v in zip(keys, values)}
print(details)