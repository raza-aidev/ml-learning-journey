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

dict1.clear()

logger.debug(f"The emptied Dictionary: {dict1}")