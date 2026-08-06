import os, time

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

modi_time = os.path.getmtime(path)
print(f"Modification time: {time.ctime(modi_time)}")

creation_time = os.path.getctime(path)
print(f"Creation time: {time.ctime(creation_time)}")

access_time = os.path.getatime(path)
print(f"Access time: {time.ctime(access_time)}")

# print(os.environ)

# print(f'{os.getenv(path)}')

print(tuple(os.walk('.')))


txt_files = [f for r, d, files in os.walk(".") for f in files if os.path.isfile(f)]

print("Text files: {}".format(txt_files))

# for root, dirs, files in os.walk("ml-learning-journey"):
#     print(f"Root: {root}")
#     print(f"Directories: {dirs}")
#     print(f"Files: {files}")

print(os.path.isdir("/home/abdulrazzaque/Road-to-AIDev/ml-learning-journey/phase1/os-module/test2.txt"))

# os.mkdir("textfile.txt")
os.mkfifo("textfile1.txt")
print(os.path.isfile("textfile1.txt"))
os.remove("textfile1.txt")
