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