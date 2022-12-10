
file_name = "input.txt"
text_file = open(file_name)

data = text_file.read().split('\n')
data.pop(0)


class Directory:
    def __init__(self, dir_name, file_sizes, parent_dir):
        self.dir_name = dir_name
        self.file_sizes = file_sizes
        self.child_dirs = []
        self.parent_dir = parent_dir
        self.size = 0

    def __str__(self):
        return "Directory name: " + self.dir_name

    def get_size(self):
        return self.size

    def update_size(self, size):
        self.size += size
        if self.parent_dir != "":
            self.parent_dir.update_size(size)

    def get_dir_name(self):
        return self.dir_name

    def get_child_dirs(self):
        return self.child_dirs

    def insert_child_dir(self, child_dir):
        self.child_dirs.append(child_dir)

    def get_parent_dir(self):
        return self.parent_dir

    def get_specific_child(self, child_name):
        for child in self.get_child_dirs():
            if child.get_dir_name() == child_name:
                return child

current_directory = Directory('/', 0, "")
saved_directory = current_directory

for command in data:
    if command[0] != "$":
        if command[:3] == "dir":
            #Add directory to child dir in current directory class
            child_dir = command[4:]
            current_directory.insert_child_dir(Directory(child_dir, 0, current_directory))
        else:
            #Get the size of the file
            file_size = int(command.split(' ')[0])
            current_directory.update_size(file_size)

    else:
        if command[2:4] == "cd":
            if command[5:] == "..":
                #Jump up to parent dir
                current_directory = current_directory.get_parent_dir()
            else:
                #Jump to the specific child node
                next_directory = command[5:]
                current_directory = current_directory.get_specific_child(next_directory)


sizes = []
def get_recursive_size(directory):
    sizes.append(directory.get_size())
    if directory.get_child_dirs():
        for child in directory.get_child_dirs():
            get_recursive_size(child)


get_recursive_size(saved_directory)

sum = 0
for i in sizes:
    if i < 100000:
        sum += i

#Part 1
print(sum)


#-------------#

#Part 2
used = sizes[0]
available = 70000000
needed = 30000000
free = available - used
space_to_clear = needed - free

closest = 100000000

for i in sizes:
    if space_to_clear < i < closest:
        closest = i

print(closest)
