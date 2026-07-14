list1 = [1, 12, 23, 14, 17, 109]

list1.sort()
print("Printing List after sorting: {}".format(list1))

list1.sort(reverse=True)
print("Reversed list: {}".format(list1))

list2 = ["abhsh", "tatat", "uqu", "r", "aa"]
list2.sort(key=len)
print("Sorting string based on the len: {}".format(list2))

#using callback funtion in the anbove example wthe len() is a callback function
#call-back functions are the function passed as an argument inside an another function is called call back funtion

def last_digit(x):
    return x%10

list3 = [12, 15, 110, 43, 67]
list3.sort(key=last_digit)
print("List sorted based on callback funtion: {}".format(list3))

