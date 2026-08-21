import json
import logging

# #create logger
# logger = logging.getLogger("week-seven")
# logger.setLevel(logging.INFO)

# #create handler
# console = logging.StreamHandler()
# console.setLevel(logging.INFO)

# #add handler to logger
# logger.addHandler(console)

# python_string = {
#     "name":"raza",
#     "age":30,
#     "Married":True
#     }

# #converting to JSON string
# json_string = json.dumps(python_string)

# logger.info(type(json_string))
# logger.info(json_string)


# python_dictionary = """{"std_name": "Rakesh", "marks": [55, 78, 89], "class": "10th", "division": "A", "Pass": true}"""

# json_value = json.loads(python_dictionary)
# logger.info(json_value)
# logger.info(type(json_value))

#send data to API

# python_data = {
#     "action":"create-user",
#     "user-details":{
#         "user-name":"Ravi Shastri",
#         "age":"67",
#         "profession":"Cricket Coach",
#         "centuries": 101
#     },
#     "stats": [12, 32, 56]
# }

# #create logger
# logger = logging.getLogger("week-seven-json")
# logger.setLevel(logging.DEBUG)

# #create handler
# console = logging.StreamHandler()
# console.setLevel(logging.DEBUG)

# #add handler to logger
# logger.addHandler(console)

# #Convert python data to JSON (for API)
# json_data=json.dumps(python_data)
# logger.debug(f"the JSON data: {json_data}")

# logger.debug(f"Type of Data: {type(json_data)}")


# import json
# import logging 

# logger = logging.getLogger("week-seven-json")
# logger.setLevel(logging.DEBUG)

# console = logging.StreamHandler()
# console.setLevel(logging.DEBUG)

# logger.addHandler(console)

# python_string = {
#     "Address" : {
#         "Area" : "Mulund",
#         "Pin" : 400452,
#         "City" : "Navi Mumbai",
#         "Apt Name" : "Galaxy Euro"
#     },
#     "Contact" : 9863537121,
#     "Name" : "Radhe Ravi",
#     "Email" : "radhe.ravikishan@gmail.com"
# }

# json_string = json.dumps(python_string, indent = 2)
# logger.debug(json_string)

import json
import logging


logger = logging.getLogger("week-seven-json")
logger.setLevel(logging.DEBUG)

console = logging.StreamHandler()
logger.setLevel(logging.DEBUG)

#add handler to logger
logger.addHandler(console)

with open('./data.json', 'r') as file:
    data = json.load(file)

logger.info(data)
