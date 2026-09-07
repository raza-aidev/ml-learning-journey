str1 = "Hello Python"

# 1st way to modify string by slicing 
print("===========1st way to modify string by slicing=========")
print("String before modification: ", str1)
str1 = str1[:6] + "Abdul!"
print("String after modification: ", str1)


#2nd way to modify string is converting to list 

str4 = "Word"
str4 = list(str4)
str4.insert(3, "l")
str4 = ''.join(str4)
print("String 4: ",str4)


#3rd way to modify string is by using method 
str5 = "Word"
# str5 = list(str4)
str5 = str5.replace("d", "ld")
# str5 = "".join(str5)
print("with replace method: ", str5)
