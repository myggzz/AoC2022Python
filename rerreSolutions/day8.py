file_name = "input.txt"
with open(file_name, 'r') as f:
    data = f.read().split('\n')
rows = len(data)
len_row = len(data[0])

def check_surrounding(surrounding_trees, tree):
    if max(list(map(int, surrounding_trees))) >= int(tree):
        return False
    return True

score = 0
for count_row, row in enumerate(data):
    for count_tree, tree in enumerate(row):
        if count_row == 0 or count_row == rows - 1 or count_tree == 0 or count_tree == len_row - 1:
            score += 1
            continue

        trees_right = list(row[count_tree+1:])
        trees_left = list(row[:count_tree])
        trees_up = [y_row[count_tree] for y_row in data[:count_row]]
        trees_down = [y_row[count_tree] for y_row in data[count_row+1:]]

        surrounding_trees = [trees_right, trees_left, trees_up, trees_down]

        for trees in surrounding_trees:
            if check_surrounding(trees, tree):
                score += 1
                break

print(score)