"""
Match Case id introduced in python 3.1 version. To avoid writing if else ladder.

It is like switch statement. But Python match case is very powerful.

It does follwoing things:
1. Compare Values 
2. Match Patterns
3. Unpack sequence
4. Match dictionaries
5. Match objects
6. Add conditions using guards


"""

#----Example to match Values--------

# value = int(input("Select Case 1 to 3:"))

# match value:
#     case 1:
#         print("It's 1st Case!")
#     case 2:
#         print("It's 2nd Case!")
#     case 3:
#         print("It's 3rd Caes!")
#     case _:
#         print("You have selected invalid case. Hence, it's Default case")


#----Example to match String and to match multiple values using |------------

# weekday = input("Enter the day: ")

# match weekday:
#     case "Monday":
#         print(f"It's {weekday} today! you have meeting to attend.")
#     case "Tuesday":
#         print(f"It's {weekday} today! you have function to attend.")
#     case "Wednesday":
#         print(f"It's {weekday} today! you have 2 meetings to attend.")
#     case "Thursday":
#         print(f"It's {weekday} today! you have shopping to do.")
#     case "Friday":
#         print(f"It's {weekday} today! you have prayer to attend.")
#     case "Saturday" | "Sunday":
#         print(f"It's the WEEKEND.....!")
#     case _:
#         print(f"Please enter the valid day....")


#----Example to match list ------------

# def week_cal(weekdays):
#     match weekdays:
#         case [num, day]:
#             return f"It's {day}, you have {num} things to do."
#         case _:
#             return "wrong call...!"

# print("1st Call", week_cal([3, "monday"]))
# print("2nd Call", week_cal([2, "tuesday"]))
# print("3rd call", week_cal([5, "sunday"]))
# print("4th call", week_cal(123))

#-------------Example of wild card ----------

# def wildcard(Values):
#     match Values:
#         case [name, _]:
#             return f"Values is {name}"

# print(wildcard(["Abdul", 12]))

#-------------Example of unpacking of sequence ----------

# def guests(details):
#     match details:
#         case [hotel, names]:
#             return f"Welcome to hotel {hotel} {names}"
#         case [hotel, *names]:
#             msg = ''
#             for name in names:
#                 msg += f"Welcome to hotel {hotel} {name}\n"
#             return msg


# print(guests(["Sunrise", "Amir"]))
# print(guests(["Grand Shereton", "Akshay", "Mira"]))
# print(guests(["Seabreez", "Jhon Smow", "Arya", "Sansa"]))

#--------Example of unpacking dictionary---------------

# dist = {"name":"Abdul", "age":"28", "time" : "12:32 PM"}

# match dist:
#     case {"name":n, "age":a}:  #this case will get exected as it is available in dict and apears in initial case
#         print(f'Hello {n}, Now you are {a}!')
#     case {"time":t}:
#         print(f"Hello, it's {t}")
#     case _:
#         print(f"default case")


dist = {"name":"Abdul", "age":"28", "time" : "12:32 PM"}

match dist:
    case {"nam":n, "age":a}:
        print(f'Hello {n}, Now you are {a}!')
    case {"time":t}:
        print(f"Hello, it's {t}")
    case _:
        print(f"default case")