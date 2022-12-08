def parse_box_positions(file_path):
    with open(file_path) as f:
        boxes_input = f.read().split('\n')
        box_array = []
        for i in range(len(boxes_input[0])):
            temp_array = []
            for row in boxes_input:
                if row[i].isalpha():
                    temp_array.append(row[i])
            temp_array.reverse()
            if len(temp_array) != 0:
                box_array.append(temp_array)
        return box_array

def parse_directions(file_path):
    with open(file_path) as f:
        movement_directions = []
        move_input = f.read().split('\n')
        for line in move_input:
            temp = []
            for char in line.split():
                if char.isdigit():
                    temp.append(int(char))
            #Cleanup directions to match the actual index of the list
            temp[1] = temp[1] - 1
            temp[2] = temp[2] - 1
            movement_directions.append(temp)
    return movement_directions

def move_boxes(box_positions, directions):
    for direction in directions:
        for _ in range(direction[0]):
            value = box_positions[direction[1]].pop()
            box_positions[direction[2]].append(value)
    return box_positions

box_positions = parse_box_positions("boxesInput.txt")
directions = parse_directions("moveInput.txt") 
box_positions = move_boxes(box_positions, directions)
for list in box_positions:
    print(list[-1], end="")