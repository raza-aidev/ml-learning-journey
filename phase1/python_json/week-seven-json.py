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

# import json
# import logging


# logger = logging.getLogger("week-seven-json")
# logger.setLevel(logging.DEBUG)

# console = logging.StreamHandler()
# logger.setLevel(logging.DEBUG)

# #add handler to logger
# logger.addHandler(console)

# with open('./data.json', 'r') as file:
#     data = json.load(file)

# logger.info(data)

# Example of dump in json file

# import json
# import logging 

# logger = logging.getLogger("week-seven-json")
# logger.setLevel(logging.DEBUG)

# console = logging.StreamHandler()
# console.setLevel(logging.DEBUG)

# logger.addHandler(console)


# shipment_details = {
#     "State": "Gujarat",
#     "City": "Jodhpur",
#     "Area": "Raja Mahal",
#     "Pin": 562262,
#     "House Number": 67,
#     "Contact Details" :{
#         "Email ID": "Tukaram.mathur@gmail.com",
#         "Phone Number": "+91 7282727272",
#         "Alternet Number": "+91 8337873833"
#     },
#     "shipment_mode": "Train",
#     "Date of Booking": "12/05/2026",
#     "Estimated Date of Arrival": "25/05/2026",
#     "Package Number": "REO9878123"
# }

# with open('data.json', 'w') as data:
#     data = json.dump(shipment_details, data, indent = 2)

# import json
# import logging

# logger = logging.getLogger("week-seven-json")
# logger.setLevel(logging.DEBUG)

# console = logging.StreamHandler()
# console.setLevel(logging.DEBUG)

# logger.addHandler(console)

# with open('data.json', 'r') as file:
#     json_data = json.load(file)

# # logger.info(json_data)

# json_data["House Number"] = 68
# json_data["Shipment mode"] = "Airline"
# json_data["Contact Details"]["Alternet Number"] = "+91 8967452300"

# # logger.info(json_data)

# with open("data.json", 'w') as file:
#     json.dump(json_data, file, indent= 4)
#     # logger.info(data)

import json, logging

logger = logging.getLogger("week-seven-json")
logger.setLevel(logging.DEBUG)

console = logging.StreamHandler()
console.setLevel(logging.DEBUG)

logger.addHandler(console)

"""
Question to get the total price of items added in cart
and find the expensive item 
"""
json_str = '''
[
    {"id": 1, "product": "Laptop", "price": 1000},
    {"id": 2, "product": "Mouse", "price": 25},
    {"id": 3, "product": "Keyboard", "price": 75}
]
'''

python_data = json.loads(json_str)
# logger.info(python_data)
total_price = sum([product["price"] for product in python_data if product["price"] > 0])


logger.info(f"Total Price: {total_price}")

# expensive = [price for product in python_data for price["price"] in ]
expensive_item = python_data[0]
max_price = expensive_item["price"]

for i in range(len(python_data)):
    if python_data[i]["price"] > max_price:
        expensive_item = python_data[i]

logger.info(f'Expensive product: {expensive_item["product"]}') 