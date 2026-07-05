## simple for loop
# for i in range(0, 20):
#     print(i);

# # right angle pyramid

# for i in range (1, n := int(input("Enter the height of the pyramid: "))):
#     print("*"*i)

# Square of stars
# n = int(input("Enter the size of square: "))
# for i in range(n):
#     for j in range(n):
#         print(f"*", end=" ")  #replace string to print with the expected string
#     print()

#increasing triangle 
# n = int(input("Enter the range: "))

# for i in range(1, n+1):
#     print("*"*i)

#decreasing triangle

# n = int(input("Enter the size of the triangle: "))

# for i in range(n,0, -1):
#     print("*"*i)

# decreasing right angle triangle

# n = int(input("Enter the size of the triandle: "))
# for i in range(n):
#     for j in range(i, n):
#         print("*",end=" ")
#     print()

#  right angle triangle on the right side
"""
  *
 **
***

"""
n = int(input("Enter the size of the triangle: "))

# for i in range(n):
#     for j in range(i,n):
#         print(" ", end="")
#     print("*"*(i+1))

# for i in range(n):
#     for j in range(i, n):
#         print(" ", end=" ")
#     for k in range(i+1):
#         print("*", end=" ")
#     for l in range(i):
#         print("*", end=" ")
#     print()

# for i in range(n):
#     for j in range(i):  # to print empty right angle triangle
#         print(" ", end=" ")
#     for k in range(i, n):  # To print inverse right angle with stars
#         print("*", end=" ")
#     for l in range(n,i+1,-1):  #To print 3rd inverse right angle triangle
#         print("*", end=" ")
#     for m in range(i):   # to print empty right angle triangle
#         print(" ", end=" ")
#     print()

for i in range(n):
    for j in range(n, i, -1):
        print(" ", end =" ")
    for k in range(i):
        print("*", end=" ")
    for l in range(i+1):
        print("*", end=" ")
    for m in range(n,i,-1):
        print(" ", end="")
    print()
for i in range(n):
    for j in range(i):
        print(" ", end=" ");
    for k in range(n,i, -1):
        print("*", end=" ")
    for l in range(n+1,i,-1):
        print("*", end=" ")
    for m in range(i):
        print(" ", end=" ")
    print()