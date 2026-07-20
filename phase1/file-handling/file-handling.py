print("---------writing to the file----------")

with open("./inputfile.txt", 'w') as f1:
    f1.write("Hello World!")

print(f"successfully written to the file {f1}")

input_data = ["Hello World\n", "How are you doing\n", "Hope you are doing well.\n"]

with open("./inputfile.txt", "w") as f2:
    f2.writelines(input_data)

with open('./inputfile.txt', 'r') as f3:
    line = f3.readline()
    while line:
        print(line)
        line = f3.readline()

print("Out of the loop")

with open("./inputfile2.txt", "r") as f7:
    lines = f7.readlines()
    for line in lines:
        print(line,end="")


# with open("./input.txt", r) as file:
#     file