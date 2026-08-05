import os

print(os.getcwd())
# os.chdir("/home/abdulrazzaque/Road-to-AIDev/ml-learning-journey/phase1/OOP/week-fiv-abstraction.py")    
# print(os.getcwd())

print(os.listdir("."))

# os.mkdir("parent1") 
# print(os.listdir("."))

# dirs = ["folder1", "folder2", "folder3", "folder4"]

# for d in dirs:
#     os.mkdir(f"{d}")

# print(os.listdir("."))

dirs1 = ["folder1", "folder2", "folder3", "folder4"]

dirs = ["folder-a", "folder-b", "folder-c", "folder-d"]

# for e in dirs1:
#     # os.makedirs(f"{d}/child1/inner-child")
#     os.rmdir(f"{e}")

# for d in dirs:
#     # os.makedirs(f"{d}/child1/inner-child")
#     os.removedirs(f"{d}")


print(os.listdir("."))

# for d in dirs:
#     if os.path.exists(f"{d}/child1/inner-child"):
#         os.removedirs(f"{d}/child1/inner-child")

# print(os.listdir())
# os.mkdir("parent2")
if(os.path.exists("test2.txt")):
    os.rename("week-six-os-module.py", "/parent2/week-six-os-module.py")
else:
    os.mkdir("test2.txt")

print(os.listdir("./parent1"))
