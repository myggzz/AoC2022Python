file_name = "input.txt"
text_file = open(file_name)

data = text_file.read().split('\n\n')
#Remove numbers
crates = data[0]

crates = [row[1::4] for row in crates.splitlines()]

print(crates)
exit()
crates = [i.split('   ') for i in crates]
crates_array = [[] for i in range(9)]
index_to_insert_into = 0

for row in crates:
    for crate_list in row:
        curr_boxes = crate_list.split('] [')
        for box in curr_boxes:

            current_box = box.strip(' ').strip('[').strip(']')
            if current_box != "":
                crates_array[index_to_insert_into].append(current_box)
            index_to_insert_into += 1
    index_to_insert_into = 0


crates_array = [r[::-1] for r in crates_array]

print(crates_array)
print(data[1])

move_arr = []

for counter, row in enumerate(data[1].split('\n')):
    move_arr.append([])
    for word in row.split(' '):
        if word.isnumeric():
            move_arr[counter].append(word)


for commands in move_arr:

    move_amount = int(commands[0])
    move_from = int(commands[1]) - 1
    move_to = int(commands[2]) - 1

    for i in range(move_amount):
        pop_it = len(crates_array[move_from]) - move_amount + i
        print(f'moving {str(move_amount)} from {str(move_from)} to {str(move_to)}')
        crates_array[move_to].append(crates_array[move_from].pop(pop_it))
        print(crates_array)
    print("new command ---")


print(move_arr)

for i in crates_array:
    print(i[-1])
    