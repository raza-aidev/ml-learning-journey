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
# if(os.path.exists("test2.txt")):
#     os.rename("week-six-os-module.py", "/parent2/week-six-os-module.py")
# else:
#     os.mkdir("test2.txt")

# print(os.listdir("./parent1"))

# print(f"{os.getcwd()}")
path = "/home/abdulrazzaque/Road-to-AIDev/ml-learning-journey/phase1/os-module/week-six-os-module.py"
abspath = "test.py"
abspath2 = "test.tft.py"
dumm_path = "C:/group/Blood"
file = "B_Pos.txt"
print(f"{os.path.dirname(path)}")
print(f"{os.path.basename(path)}")
print(f"{os.path.split(path)}")
print(f"{os.path.splitext(path)}")
print(f"{os.path.splitext(abspath)}")
print(f"{os.path.join(dumm_path, file)}")

print(f"{os.path.abspath(path)}")
print(f"{os.path.isabs(dumm_path)}")
print(f"{os.path.isabs(file)}")
print(f"{os.path.isabs(path)}")





