with open("input.txt") as f:
    input = f.read().split('\n')

pwd = []
file_system = []

def map_filesystem(input):
    if input.startswith("$ cd .."):
        pwd.pop()
    elif input.startswith("$ cd"):
        name = input.split("$ cd ")[1]
        pwd.append(name)
        file_system.append({"path" : pwd[:], "size": 0})
                    
def add_folder_size(input):
    if input.startswith("$ cd .."):
        pwd.pop()
    elif input.startswith("$ cd"):
        name = input.split("cd ")[1]
        pwd.append(name)
    elif input[0].isdigit():
        for folder in file_system:
            if folder["path"] == pwd:
                folder["size"] += int(input.split(" ")[0])

for line in input:
    map_filesystem(line)

pwd = []
for line in input:
    add_folder_size(line)

#Add the size from children to parentfolders
for folder in file_system:
    for i in range(len(folder["path"])):
        for folder2 in file_system:
            if folder2["path"] == folder["path"][0:i]:
                folder2["size"] += folder["size"]

total = 0
for folder in file_system:
    if folder["size"] <= 100000:
        total += folder["size"]
print(total)


